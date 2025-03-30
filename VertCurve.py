bl_info = {
    "name": "VertCurve",
    "author": "Robbottom",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),  
    "location": "View3D > VertCurve",  
    "description": "Streamlines Adding A Vertex For Skin Modifier Workflow",
    "warning": "", 
    "wiki_url": "https://linktr.ee/Robbottom",  
    "category": "Add Mesh",
}

import bpy
import bmesh 

class VertCurve(bpy.types.Panel):
    bl_label = "VertCurve"
    bl_idname = "PT_VertPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VertCurve'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add A Vertex", icon='MESH_UVSPHERE')
        row = layout.row()
        row.operator("mesh.primitive_vertex_add")
        row = layout.row()
        row.label(text="Add A Skin Modifier", icon='MOD_SKIN')
        row.operator("object.modifier_add").type = 'SKIN'
        row = layout.row()
        row.label(text="Add Subdivision", icon='MOD_SUBSURF')
        row.operator("object.modifier_add").type = 'SUBSURF'


class ADD_OT_VERTEX(bpy.types.Operator):
    bl_label = "Add A Vertex Curve"
    bl_idname = "mesh.primitive_vertex_add"
    
    def execute(self, context):
        # New mesh object
        mesh = bpy.data.meshes.new(name="NewMesh")
        obj = bpy.data.objects.new("NewObject", mesh)
        
        # Link object to scene
        bpy.context.collection.objects.link(obj)
        
        bm = bmesh.new()
        bm.verts.new((0, 0, 0))
        bm.verts.ensure_lookup_table()
        bm.to_mesh(mesh)
        bm.free()

        return {'FINISHED'}


def register():
    bpy.utils.register_class(VertCurve)
    bpy.utils.register_class(ADD_OT_VERTEX)

def unregister():
    bpy.utils.unregister_class(VertCurve)
    bpy.utils.unregister_class(ADD_OT_VERTEX)

if __name__ == "__main__":
    register()

#Thanks ChatGPT For fixing all of the errors :)