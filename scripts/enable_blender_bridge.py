"""Run inside local Blender via --python; saves preferences, never project files."""
import json


def enable_bridge(bpy_module):
    bpy = bpy_module
    module = 'blender_mcp'
    if module not in bpy.context.preferences.addons:
        bpy.ops.preferences.addon_enable(module=module)
    prefs = bpy.context.preferences.addons[module].preferences
    if hasattr(prefs, 'telemetry_consent'):
        prefs.telemetry_consent = False
    bpy.context.scene.blendermcp_port = 9876
    bpy.context.scene.blendermcp_auto_start_server = True
    bpy.ops.blendermcp.start_server()
    server = getattr(bpy.types, 'blendermcp_server', None)
    bpy.ops.wm.save_userpref()
    return {
        'blender_version': bpy.app.version_string,
        'addon_enabled': module in bpy.context.preferences.addons,
        'server_running': bool(server and server.running),
        'host': getattr(server, 'host', None),
        'port': getattr(server, 'port', None),
        'prompt_scene_telemetry_consent': bool(getattr(prefs, 'telemetry_consent', False)),
        'preferences_saved': True,
        'project_saved': False,
    }


def main():
    from importlib import import_module
    bpy = import_module('bpy')  # Available only in Blender's bundled Python.
    result = enable_bridge(bpy)
    print('LOCAL_BLENDER_BRIDGE ' + json.dumps(result), flush=True)
    if not result['server_running']:
        raise RuntimeError('Bridge did not start; inspect Blender console and port ownership')


if __name__ == '__main__':
    main()
