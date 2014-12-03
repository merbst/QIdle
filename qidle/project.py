"""
This module contains classes and functions to easily access project
properties.
"""
import json
import os


def get_run_configurations(prj_path):
    path = os.path.join(prj_path, '.qidle', 'run_configs.json')
    try:
        with open(path, 'r') as f:
            content = f.read()
    except OSError:
        return []
    else:
        configs = json.loads(content)
        for cfg in configs:
            cfg['script'] = os.path.abspath(
                os.path.join(prj_path, cfg['script']))
            cfg['working_dir'] = os.path.abspath(
                os.path.join(prj_path, cfg['working_dir']))
        return configs


def set_run_configurations(prj_path, configurations):
    path = os.path.join(prj_path, '.qidle', 'run_configs.json')
    for cfg in configurations:
        cfg['script'] = os.path.relpath(cfg['script'], prj_path)
        cfg['working_dir'] = os.path.relpath(cfg['working_dir'], prj_path)
    with open(path, 'w') as f:
        f.write(json.dumps(configurations, indent=4, sort_keys=True))
