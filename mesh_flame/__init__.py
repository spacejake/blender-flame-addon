bl_info = {
    "name": "Flame Model Tools",
    "author": "Jacob Morton",
    "version": (0, 3, 4),
    "blender": (2, 7, 9),
    "location": "",
    "description": "Tools for the FLAME Model",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"}

if "bpy" in locals():
    import importlib
    importlib.reload(blender_flame_addon)
    importlib.reload(flame_utils)

else:
    from . import blender_flame_addon
    from . import flame_utils


import bpy
from bpy.props import PointerProperty


def register():
    print("__init__:register")
    bpy.utils.register_module(__name__)
    #bpy.types.Scene.flame = bpy.props.PointerProperty(type=blender_flame_addon.FlameProperties)
    blender_flame_addon.register()


def unregister():
    bpy.utils.unregister_module(__name__)
    blender_flame_addon.unregister()
    #del bpy.types.Scene.flame


if __name__ == "__main__":
    register()