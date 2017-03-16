from bpy.props import *
from .Utils.core import *


class MasterSymmetryMenu(bpy.types.Menu):
    bl_label = "Symmetry Options"
    bl_idname = "view3d.master_symmetry_menu"

    @classmethod
    def poll(self, context):
        if get_mode() in [sculpt, texture_paint]:
            return True
        else:
            return False

    def draw(self, context):
        menu = Menu(self)

        if get_mode() == texture_paint:
            menu.add_item().prop(context.tool_settings.image_paint, "use_symmetry_x", toggle=True)
            menu.add_item().prop(context.tool_settings.image_paint, "use_symmetry_y", toggle=True)
            menu.add_item().prop(context.tool_settings.image_paint, "use_symmetry_z", toggle=True)
        else:

            menu.add_item().menu(SymmetryMenu.bl_idname)
            menu.add_item().menu(SymmetryRadialMenu.bl_idname)
            menu.add_item().prop(context.tool_settings.sculpt, "use_symmetry_feather", toggle=True)


class SymmetryMenu(bpy.types.Menu):
    bl_label = "Symmetry"
    bl_idname = "view3d.symmetry_menu"

    def draw(self, context):
        menu = Menu(self)

        menu.add_item().prop(context.tool_settings.sculpt, "use_symmetry_x", toggle=True)
        menu.add_item().prop(context.tool_settings.sculpt, "use_symmetry_y", toggle=True)
        menu.add_item().prop(context.tool_settings.sculpt, "use_symmetry_z", toggle=True)


class SymmetryRadialMenu(bpy.types.Menu):
    bl_label = "Radial"
    bl_idname = "view3d.symmetry_radial_menu"

    def draw(self, context):
        menu = Menu(self)

        menu.add_item("column").prop(context.tool_settings.sculpt, "radial_symmetry", text="", slider=True)

### ------------ New hotkeys and registration ------------ ###
def register():
    pass

def unregister():
    pass 
if __name__ == "__main__":
    register()
