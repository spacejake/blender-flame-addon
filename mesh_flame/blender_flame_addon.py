#bl_info = {
#    "name": "Flame Model Tools",
#    "categoty": "Mesh"
#}

import os
import bpy
from bpy.types import Panel, Operator
from bpy_extras.io_utils import ExportHelper

#import sys
#sys.path.append(R'D:\Jake\FaceModels\flame\blender_flame')
from mesh_flame.flame_utils import gen_util

# adding a PropertyGroup helps keep the Scene namespace clean.
# instead of adding 10 properties directly to Scene, you only
# add 1 group, which itself has a dot(.) lookup to get individual
# properties


class FlameProperties(bpy.types.PropertyGroup):
    model_fname = bpy.props.StringProperty(name="",
        description="Choose a directory:",
        default="",
        maxlen=1024,
        subtype='FILE_PATH')
    output_dir = bpy.props.StringProperty(
        name="",
        description="Choose a directory:",
        default="",
        maxlen=1024,
        subtype='DIR_PATH')
    # ...etc ..


# Class for the panel, derived by Panel
class FlameOperator(Operator):
    """Randomly generate a Face from the Flame Model"""
    #Blender Attribs
    bl_idname = "flame.gen_face"
    bl_label = "Flame Operator"

    # Class Attribs
    module_dir = 'D:\\Jake\\FaceModels\\flame\\flame-fitting'

    def execute(self, context):
        #TODO: Check context.scene.flame.model_fname is set?\

        print("Model_loc:" + context.scene.flame.model_fname)
        file_loc = gen_util.gen_all(context.scene.flame.model_fname, context.scene.flame.output_dir)
        cursor = context.scene.cursor_location

        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        obj_object = bpy.context.selected_objects[0]

        # Move to cursor location
        obj_object.location = cursor

        print('Imported name: ', obj_object.name)
        return {'FINISHED'}

'''
class FlameModelSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "flame.model_selector"
    bl_label = "Select File"

    filename_ext = ""

    def execute(self, context):
        fdir = self.properties.filepath
        context.scene.flame.model_fname = fdir
        return{'FINISHED'}


class FlameOutputSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "flame.output_selector"
    bl_label = "Select Dir"

    filename_ext = ""

    def execute(self, context):
        fdir = self.properties.filepath
        if os.path.isfile(fdir):
            print(fdir+" is not a directory, using" + os.path.dirname(fdir))
            fdir = os.path.dirname(fdir)
        context.scene.flame.output_dir = fdir
        return{'FINISHED'}
'''

class FlameToolPanel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Flame Tools'
    bl_context = 'objectmode'
    bl_category = 'Flame'

    # Add UI elements here
    def draw(self, context):
        layout = self.layout
        scn = context.scene

        # ui
        # File diolag for which flame model to load
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(scn.flame, 'model_fname', text='Model')
        #row.operator(FlameModelSelector.bl_idname, icon="FILE_FOLDER", text="")


        row = col.row(align=True)
        row.prop(scn.flame, 'output_dir', text='Output')
        #row.operator(FlameOutputSelector.bl_idname, icon="FILE_FOLDER", text="")

        #col = layout.column()
        #col.label(scn.flame.model_fname)
        #col.operator("wm.remove_file")

        col = layout.column(align=True)
        col.operator(FlameOperator.bl_idname, text='Generate Face')


# Register
def register():
    print("flame:register")
    #bpy.utils.register_module(__name__)
    bpy.types.Scene.flame = bpy.props.PointerProperty(type=FlameProperties)
    #bpy.utils.register_class(FlameToolPanel)
    #bpy.utils.register_class(FlameOperator)
    #bpy.utils.register_class(FlameModelSelector)


# Unregister
def unregister():
    #bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.flame
    #bpy.utils.unregister_class(FlameToolPanel)
    #bpy.utils.unregister_class(FlameOperator)
    #bpy.utils.unregister_class(FlameModelSelector)


# Needed to run script in Text Editor
if __name__ == '__main__':
    register()

