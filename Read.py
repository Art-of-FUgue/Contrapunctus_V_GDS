import pya
import klayout.db as db



# Load the GDS file
layout = db.Layout()
layout.read("bottom contact.gds")

# Access a specific cell
top_cell = layout.top_cell()
layer_10 = layout.layer(10, 0)
layer_9 = layout.layer(9, 0)
layout.dbu = 1
print(layout.dbu)
# Iterate over all shapes in the cell
for shape in top_cell.each_shape(layer_10):
    if shape.is_polygon():
#        polygon = shape.polygon
        # Do something with the polygon
        print(shape)
