import os
import importlib

PLUGIN_DIR = "core/plugins"

def load_plugins():
    plugins = {}

    for file in os.listdir(PLUGIN_DIR):
        if file.endswith(".py"):
            name = file[:-3]
            module = importlib.import_module(f"core.plugins.{name}")
            plugins[name] = module

    return plugins
