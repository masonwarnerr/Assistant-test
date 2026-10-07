#!/usr/bin/env python3
"""Normalize an installed Blender MCP addon without touching other addons."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import uuid


def addon_protocol(data):
    tree = ast.parse(data.decode('utf-8'))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'ADDON_PROTOCOL_VERSION' for t in node.targets):
            value = ast.literal_eval(node.value)
            if isinstance(value, int) and not isinstance(value, bool) and value > 0:
                return value
    raise ValueError('Source is not a versioned Blender MCP addon')


def normalize_addon(addons_dir, apply=False):
    root = Path(addons_dir)
    source = root / 'blender_mcp.py'
    target = root / 'blender_mcp/__init__.py'
    if not root.is_dir():
        raise ValueError('Addons directory must already exist')
    guarded_paths = [root, source, target.parent, target, root / '.lloyd-addon-backups']
    if any(p.is_symlink() for p in guarded_paths):
        raise ValueError('Refusing symlinked addon or backup paths')
    if not source.exists():
        data = target.read_bytes()
        return {
            'action': 'already_packaged',
            'protocol': addon_protocol(data),
            'target': str(target),
            'sha256': hashlib.sha256(data).hexdigest(),
            'applied': False,
        }
    data = source.read_bytes()
    result = {
        'action': 'package_loose_module',
        'protocol': addon_protocol(data),
        'source': str(source),
        'target': str(target),
        'sha256': hashlib.sha256(data).hexdigest(),
        'applied': False,
    }
    if apply:
        if target.exists() and target.read_bytes() != data:
            backup_dir = root / '.lloyd-addon-backups'
            backup_dir.mkdir(exist_ok=True)
            backup = backup_dir / ('blender_mcp-' + uuid.uuid4().hex + '.py')
            backup.write_bytes(target.read_bytes())
            result['backup'] = str(backup)
        target.parent.mkdir(exist_ok=True)
        temp = target.parent / ('.lloyd-init-' + uuid.uuid4().hex + '.tmp')
        try:
            temp.write_bytes(data)
            os.replace(temp, target)
        finally:
            temp.unlink(missing_ok=True)
        if target.read_bytes() != data or source.read_bytes() != data:
            raise RuntimeError('Addon files changed during install; duplicate source was not removed')
        source.unlink()
        result['applied'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--addons-dir', type=Path, required=True)
    parser.add_argument('--apply', action='store_true', help='Apply the plan; default is a read-only dry run')
    args = parser.parse_args()
    print(json.dumps(normalize_addon(args.addons_dir, apply=args.apply), indent=2))


if __name__ == '__main__':
    main()
