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
    bl_options = {'DEFAULT_CLOSED'}  

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add A Vertex", icon='MESH_UVSPHERE')
        row = layout.row()
        row.operator("mesh.primitive_vertex_add")
        row = layout.row()
        row.label(text="Add A Skin Modifier", icon='MOD_SKIN')
        row.operator("object.modifier_add", text="Add A Skin Modifier").type = 'SKIN'
        row = layout.row()
        row.label(text="Add Subdivision", icon='MOD_SUBSURF')
        row.operator("object.modifier_add", text="Add A SubSurf Modifier").type = 'SUBSURF'


class ADD_OT_VERTEX(bpy.types.Operator):
    bl_label = "Add A Vertex Curve"
    bl_idname = "mesh.primitive_vertex_add"
    
    def execute(self, context):
       
        mesh = bpy.data.meshes.new(name="NewMesh")
        obj = bpy.data.objects.new("NewObject", mesh)
        
     
        bpy.context.collection.objects.link(obj)
        
        bm = bmesh.new()
        bm.verts.new((0, 0, 0))  
        bm.verts.ensure_lookup_table()
        bm.to_mesh(mesh)
        bm.free()

        return {'FINISHED'}

class AddScrewModifier(bpy.types.Panel):
    bl_label = "Screw Modifier"
    bl_idname = "PT_AddScrewModifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VertCurve'
    bl_parent_id = 'PT_VertPanel'
    bl_options = {'DEFAULT_CLOSED'}  

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add a screw modifier", icon='MOD_SCREW')
        row.operator("object.modifier_add", text="Add Screw Modifier").type = 'SCREW'
        
        
        
def register():
    bpy.utils.register_class(VertCurve)
    bpy.utils.register_class(ADD_OT_VERTEX)
    bpy.utils.register_class(AddScrewModifier)

def unregister():
    bpy.utils.unregister_class(VertCurve)
    bpy.utils.unregister_class(ADD_OT_VERTEX)
    bpy.utils.unregister_class(AddScrewModifier)

if __name__ == "__main__":
    register()

#Thanks ChatGPT for fixing errors, and creating the add vertex operator :)