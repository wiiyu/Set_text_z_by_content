bl_info = {
    "name": "Set Text Z by Content",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Set Text Z by Content",
    "description": "Sets the Z-coordinate of text objects based on their content.",
    "category": "Object",
}

import bpy

# 主功能：根据文字内容设置Z坐标
def set_text_z_based_on_content():
    for obj in bpy.context.scene.objects:
        if obj.type == 'FONT':  # 确保是文字对象
            try:
                z_value = float(obj.data.body)  # 获取文字内容并转为浮点数
                obj.location.z = z_value  # 设置Z坐标
                print(f"设置对象 '{obj.name}' 的Z坐标为 {z_value}")
            except ValueError:
                print(f"对象 '{obj.name}' 的内容 '{obj.data.body}' 不是有效数字，跳过。")

# 创建一个操作类
class OBJECT_OT_set_text_z(bpy.types.Operator):
    """Set Text Z by Content"""
    bl_idname = "object.set_text_z_by_content"
    bl_label = "Set Text Z by Content"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        set_text_z_based_on_content()
        return {'FINISHED'}

# 将操作添加到菜单中
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_set_text_z.bl_idname)

# 注册和注销
def register():
    bpy.utils.register_class(OBJECT_OT_set_text_z)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_set_text_z)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
