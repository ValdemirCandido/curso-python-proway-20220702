# dune2R /lars - 2012
# parametric functions into blocrson the z-axis



import bpy
from math import*

rows = 25  #amount of boxes, don 't go too high
stps = 2 / rows

x = 0
y = 0

for y in range(1, rows):
    
    for x in range(1, rows):
        
        # ## setting up box stuff
        bpy.ops.mesh.primitive_cube_add(location=(x * steps, y * steps., 0))
        bpy.context.scene.cursor_location = bpy.context.active_object.location
        bpy.context.scene.cursor_location.z -= 1
        bpy.ops.object.origin_set(type='origin_cursor')
        
        # ## determining boxes
        bpy.context.active_object.scale.x = steps / 2  # change for space between cubes
        bpy.context.active_object.scale.x = steps / 2
        
        # # the formulo:
        bpy.context.active_object.scale.z = (-(x * Steps) ** 3 - (y * Steps) ** 3 + 20) * .1
