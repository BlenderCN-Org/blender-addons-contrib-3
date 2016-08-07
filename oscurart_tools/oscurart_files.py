# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy
from bpy.types import Operator


# ---------------------RELOAD IMAGES------------------

class reloadImages(Operator):
    bl_idname = "image.reload_images_osc"
    bl_label = "Reload Images"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        for imgs in bpy.data.images:
            imgs.reload()
        return {'FINISHED'}


# --------------- SYNC MISSING GROUPS -----------------

class reFreshMissingGroups(Operator):
    bl_idname = "file.sync_missing_groups"
    bl_label = "Sync Missing Groups"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        for group in bpy.data.groups:
            if group.library is not None:
                with bpy.data.libraries.load(group.library.filepath, link=True) as (linked, local):
                    local.groups = linked.groups
        return {'FINISHED'}
