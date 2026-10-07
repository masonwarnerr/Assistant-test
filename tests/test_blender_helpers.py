import importlib.util
import os
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/fix_blender_addon_layout.py'
ADDON = 'ADDON_PROTOCOL_VERSION = 13\ndef register():\n    pass\ndef unregister():\n    pass\n'

class BlenderLayoutTests(unittest.TestCase):
    def load_helper(self):
        self.assertTrue(SCRIPT.is_file(), 'Missing safe addon layout helper')
        spec = importlib.util.spec_from_file_location('blender_layout_helper', SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_dry_run_preserves_loose_module_and_existing_package(self):
        module = self.load_helper()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as td:
            root = Path(td)
            (root / 'blender_mcp.py').write_text(ADDON)
            (root / 'blender_mcp').mkdir()
            old = root / 'blender_mcp/__init__.py'
            old.write_text('ADDON_PROTOCOL_VERSION = 9\n')
            result = module.normalize_addon(root, apply=False)
            self.assertEqual(result['action'], 'package_loose_module')
            self.assertEqual(result['protocol'], 13)
            self.assertEqual(old.read_text(), 'ADDON_PROTOCOL_VERSION = 9\n')
            self.assertTrue((root / 'blender_mcp.py').exists())
            self.assertFalse((root / '.lloyd-addon-backups').exists())

    def test_apply_backs_up_old_code_and_preserves_other_assets(self):
        module = self.load_helper()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as td:
            root = Path(td)
            (root / 'blender_mcp.py').write_text(ADDON)
            (root / 'blender_mcp').mkdir()
            target = root / 'blender_mcp/__init__.py'
            target.write_text('ADDON_PROTOCOL_VERSION = 9\n')
            asset = root / 'blender_mcp/keep.txt'
            asset.write_text('keep this resource')
            result = module.normalize_addon(root, apply=True)
            self.assertTrue(result['applied'])
            self.assertEqual(target.read_text(), ADDON)
            self.assertFalse((root / 'blender_mcp.py').exists())
            self.assertEqual(Path(result['backup']).read_text(), 'ADDON_PROTOCOL_VERSION = 9\n')
            self.assertEqual(asset.read_text(), 'keep this resource')

    def test_repeated_apply_is_read_only_when_package_is_already_installed(self):
        module = self.load_helper()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as td:
            root = Path(td)
            (root / 'blender_mcp.py').write_text(ADDON)
            module.normalize_addon(root, apply=True)
            target = root / 'blender_mcp/__init__.py'
            before = target.stat().st_mtime_ns
            result = module.normalize_addon(root, apply=True)
            self.assertEqual(result['action'], 'already_packaged')
            self.assertFalse(result['applied'])
            self.assertEqual(target.stat().st_mtime_ns, before)

    def test_refuses_symlinked_package_before_writing(self):
        module = self.load_helper()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as td:
            root = Path(td) / 'addons'
            root.mkdir()
            outside = Path(td) / 'outside'
            outside.mkdir()
            (outside / '__init__.py').write_text('do not change')
            (root / 'blender_mcp').symlink_to(outside, target_is_directory=True)
            (root / 'blender_mcp.py').write_text(ADDON)
            with self.assertRaises(ValueError):
                module.normalize_addon(root, apply=True)
            self.assertEqual((outside / '__init__.py').read_text(), 'do not change')
            self.assertTrue((root / 'blender_mcp.py').exists())

    def test_invalid_source_does_not_replace_existing_code(self):
        module = self.load_helper()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as td:
            root = Path(td)
            source = root / 'blender_mcp.py'
            source.write_text('not_an_addon = True\n')
            (root / 'blender_mcp').mkdir()
            target = root / 'blender_mcp/__init__.py'
            target.write_text(ADDON)
            with self.assertRaises(ValueError):
                module.normalize_addon(root, apply=True)
            self.assertEqual(target.read_text(), ADDON)
            self.assertTrue(source.exists())

class BlenderBridgeTests(unittest.TestCase):
    def test_enable_bridge_saves_preferences_only_with_telemetry_off(self):
        from types import SimpleNamespace as NS
        script = ROOT / 'scripts/enable_blender_bridge.py'
        self.assertTrue(script.is_file(), 'Missing portable bridge enablement helper')
        spec = importlib.util.spec_from_file_location('enable_bridge_helper', script)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        events = []
        addons = {}
        scene = NS(blendermcp_port=0, blendermcp_auto_start_server=False)
        prefs = NS(telemetry_consent=True)
        fake = NS(context=NS(preferences=NS(addons=addons), scene=scene), types=NS(), app=NS(version_string='fixture-version', background=False))
        def enable(module):
            events.append('enable')
            addons[module] = NS(preferences=prefs)
        def start():
            events.append('start')
            fake.types.blendermcp_server = NS(running=True, host='localhost', port=9876)
        def save_preferences():
            events.append('save_userpref')
        def forbidden_project_save():
            raise AssertionError('Project saves are not authorized by connectivity setup')
        fake.ops = NS(preferences=NS(addon_enable=enable), blendermcp=NS(start_server=start), wm=NS(save_userpref=save_preferences, save_mainfile=forbidden_project_save))
        result = module.enable_bridge(fake)
        self.assertEqual(events, ['enable', 'start', 'save_userpref'])
        self.assertFalse(prefs.telemetry_consent)
        self.assertTrue(scene.blendermcp_auto_start_server)
        self.assertTrue(result['server_running'])
        self.assertFalse(result['project_saved'])

if __name__ == '__main__':
    unittest.main()
