import pya
import klayout.db as db
import numpy as np 
import scipy as sp 

#Global parameters for alignment markers 60*60 crossbars, 1.2cm*1.2cm
alignment_distance = 200
number_of_grids = 30 #has to be even
number_of_crosses = number_of_grids * 10
marker_thickness = 2.5
crossbar_thickness = marker_thickness/2


#Start a file
ly = db.Layout()

#create layers
marker_layer = ly.layer(0, 0)
alignment_layer = ly.layer(63, 0)
layer_9 = ly.layer(9, 0)
layer_10 = ly.layer(10, 0)

# Useful instances
zero = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0), db.DPoint(0, marker_thickness*1),
    db.DPoint(marker_thickness*2, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(marker_thickness*1, marker_thickness*4),
    db.DPoint(marker_thickness*1, marker_thickness*1), db.DPoint(0, marker_thickness*1), db.DPoint(0, marker_thickness*5)
    ])

offset_one = 5 * (marker_thickness/2) - marker_thickness/2
one = db.DPolygon([ 
    db.DPoint(0+offset_one, marker_thickness*5), db.DPoint(marker_thickness*1+offset_one, marker_thickness*5), db.DPoint(marker_thickness*1+offset_one, 0), db.DPoint(0+offset_one, 0), db.DPoint(0+offset_one, marker_thickness*5)
    ])

two = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*2), db.DPoint(marker_thickness*1, marker_thickness*2),
    db.DPoint(marker_thickness*1, marker_thickness*1), db.DPoint(marker_thickness*3, marker_thickness*1), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0), db.DPoint(0, marker_thickness*3),
    db.DPoint(marker_thickness*2, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(0, marker_thickness*4), db.DPoint(0, marker_thickness*5)
    ])

three = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0),
    db.DPoint(0, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*2), db.DPoint(0, marker_thickness*2),
    db.DPoint(0, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(0, marker_thickness*4),
    db.DPoint(0, marker_thickness*5)
    ])

four = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*1, marker_thickness*5), db.DPoint(marker_thickness*1, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*3),
    db.DPoint(marker_thickness*2, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0), db.DPoint(marker_thickness*2, 0),
    db.DPoint(marker_thickness*2, marker_thickness*2), db.DPoint(0, marker_thickness*2), db.DPoint(0, marker_thickness*5)
    ])

five = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*4), db.DPoint(marker_thickness*1, marker_thickness*4),
    db.DPoint(marker_thickness*1, marker_thickness*3), db.DPoint(marker_thickness*3, marker_thickness*3), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0),
    db.DPoint(0, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*2),
    db.DPoint(0, marker_thickness*2), db.DPoint(0, marker_thickness*5),
    ])

six = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*4), db.DPoint(marker_thickness*1, marker_thickness*4),
    db.DPoint(marker_thickness*1, marker_thickness*3), db.DPoint(marker_thickness*3, marker_thickness*3), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0),
    db.DPoint(0, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*2), db.DPoint(marker_thickness*1, marker_thickness*2),
    db.DPoint(marker_thickness*1, marker_thickness*1), db.DPoint(0, marker_thickness*1), db.DPoint(0, marker_thickness*5)
    ])

seven = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0), db.DPoint(marker_thickness*2, 0),
    db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(0, marker_thickness*4)
    ])

eight = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0), db.DPoint(0, 0),
    db.DPoint(0, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*1), db.DPoint(marker_thickness*2, marker_thickness*2),
    db.DPoint(0, marker_thickness*2), db.DPoint(0, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*3),
    db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(0, marker_thickness*4), db.DPoint(0, marker_thickness*5),
    db.DPoint(marker_thickness*1, marker_thickness*5), db.DPoint(marker_thickness*1, marker_thickness*1),
    db.DPoint(0, marker_thickness*1),
    ])

nine = db.DPolygon([ 
    db.DPoint(0, marker_thickness*5), db.DPoint(marker_thickness*3, marker_thickness*5), db.DPoint(marker_thickness*3, 0),
    db.DPoint(marker_thickness*2, 0), db.DPoint(marker_thickness*2, marker_thickness*4), db.DPoint(marker_thickness*1, marker_thickness*4),
    db.DPoint(marker_thickness*1, marker_thickness*3), db.DPoint(marker_thickness*2, marker_thickness*3),
    db.DPoint(marker_thickness*2, marker_thickness*2), db.DPoint(0, marker_thickness*2),
    ])

cross_bar = db.DPolygon([ 
    db.DPoint(-crossbar_thickness*5, 0), db.DPoint(-crossbar_thickness*5, crossbar_thickness*1),
    db.DPoint(-crossbar_thickness*1, crossbar_thickness*1), db.DPoint(-crossbar_thickness*1, crossbar_thickness*5),
    db.DPoint(crossbar_thickness*1, crossbar_thickness*5), db.DPoint(crossbar_thickness*1, crossbar_thickness*1), db.DPoint(crossbar_thickness*5, crossbar_thickness*1),
    db.DPoint(crossbar_thickness*5, -crossbar_thickness*1), db.DPoint(crossbar_thickness*1, -crossbar_thickness*1),
    db.DPoint(crossbar_thickness*1, -crossbar_thickness*5), db.DPoint(-crossbar_thickness*1, -crossbar_thickness*5), db.DPoint(-crossbar_thickness*1, -crossbar_thickness*1),
    db.DPoint(-crossbar_thickness*5, -crossbar_thickness*1), db.DPoint(-crossbar_thickness*5, 0),
    ])

joel_cross = db.DPolygon([
    db.DPoint(15, -15), db.DPoint(90, -15), db.DPoint(90, 15), db.DPoint(15, 15), db.DPoint(15, 90), db.DPoint(-15, 90), db.DPoint(-15, 15),
    db.DPoint(-90, 15), db.DPoint(-90, -15), db.DPoint(-15, -15), db.DPoint(-15, -90), db.DPoint(15, -90), db.DPoint(15, -15)])

#create cells for digits
cell_digits = [] 

cell_zero = ly.create_cell('zero')
cell_zero.shapes(marker_layer).insert(zero)
cell_digits.append(cell_zero)

cell_one = ly.create_cell('one')
cell_one.shapes(marker_layer).insert(one)
cell_digits.append(cell_one)

cell_two = ly.create_cell('two')
cell_two.shapes(marker_layer).insert(two)
cell_digits.append(cell_two)

cell_three = ly.create_cell('three')
cell_three.shapes(marker_layer).insert(three)
cell_digits.append(cell_three)

cell_four = ly.create_cell('four')
cell_four.shapes(marker_layer).insert(four)
cell_digits.append(cell_four)

cell_five = ly.create_cell('five')
cell_five.shapes(marker_layer).insert(five)
cell_digits.append(cell_five)

cell_six = ly.create_cell('six')
cell_six.shapes(marker_layer).insert(six)
cell_digits.append(cell_six)

cell_seven = ly.create_cell('seven')
cell_seven.shapes(marker_layer).insert(seven)
cell_digits.append(cell_seven)

cell_eight = ly.create_cell('eight')
cell_eight.shapes(marker_layer).insert(eight)
cell_digits.append(cell_eight)

cell_nine = ly.create_cell('nine')
cell_nine.shapes(marker_layer).insert(nine)
cell_digits.append(cell_nine)


#create cell for cross
cell_crossbar = ly.create_cell('crossbar')
cell_crossbar.shapes(marker_layer).insert(cross_bar)


#create cross for joel alignment
cell_joel_cross = ly.create_cell('joel_cross')
cell_joel_cross.shapes(layer_10).insert(joel_cross)

#total offset for bottom left grid
offset_x = - alignment_distance * (number_of_crosses/2)
offset_y = - alignment_distance * (number_of_crosses/2)

#create cross bars
top_cell = ly.create_cell("Top")
crossbar_array = db.DCellInstArray(cell_crossbar.cell_index(),
                                     db.DTrans(db.DTrans.R0, offset_x , offset_y),
                                     db.DVector(alignment_distance, 0),
                                     db.DVector(0, alignment_distance),
                                     number_of_crosses,
                                     number_of_crosses)
top_cell.insert(crossbar_array)

#create 10X10 numbers grid as one cell
number_offset_left_x = -11.5
number_offset_left_y = -16.5
number_offset_right_x = 4
number_offset_right_y = -16.5

number_grid = ly.create_cell('number_grid')
for i in range(10):
    for j in range(10):
        left_number = db.DCellInstArray(cell_digits[i].cell_index(),
                                        db.DTrans(db.DTrans.R0, number_offset_left_x + i*alignment_distance, number_offset_left_y + j*alignment_distance)) 
        right_number = db.DCellInstArray(cell_digits[j].cell_index(),
                                        db.DTrans(db.DTrans.R0, number_offset_right_x + i*alignment_distance, number_offset_right_y + j*alignment_distance)) 
        number_grid.insert(left_number)
        number_grid.insert(right_number)

number_grid_array = db.DCellInstArray(number_grid.cell_index(),
                                        db.DTrans(db.DTrans.R0, offset_x , offset_y),
                                        db.DVector(alignment_distance * 10, 0),
                                        db.DVector(0, alignment_distance * 10),
                                        number_of_grids,
                                        number_of_grids)

top_cell.insert(number_grid_array)

#insert big numbers into top_cell
big_number_offset_left_x = -11.5
big_number_offset_left_y = -16.5-20
big_number_offset_right_x = 4
big_number_offset_right_y = -16.5-20
big_number_extra_offset = 30
big_number_grid = ly.create_cell('big_number_grid')
for i in range(number_of_grids):
    for j in range(number_of_grids):
        x_left = i//10
        x_right = i%10
        y_left = j//10
        y_right = j%10
        big_left_number_x = db.DCellInstArray(cell_digits[x_left].cell_index(),
                                        db.DTrans(db.DTrans.R0, big_number_offset_left_x + i*alignment_distance*10, big_number_offset_left_y + j*alignment_distance*10))
        big_right_number_x = db.DCellInstArray(cell_digits[x_right].cell_index(),
                                        db.DTrans(db.DTrans.R0, big_number_offset_right_x + i*alignment_distance*10, big_number_offset_right_y + j*alignment_distance*10)) 
        big_left_number_y = db.DCellInstArray(cell_digits[y_left].cell_index(),
                                        db.DTrans(db.DTrans.R0, big_number_extra_offset+big_number_offset_left_x + i*alignment_distance*10, big_number_offset_left_y + j*alignment_distance*10))
        big_right_number_y = db.DCellInstArray(cell_digits[y_right].cell_index(),
                                        db.DTrans(db.DTrans.R0, big_number_extra_offset+big_number_offset_right_x + i*alignment_distance*10, big_number_offset_right_y + j*alignment_distance*10)) 
        big_number_grid.insert(big_left_number_x)
        big_number_grid.insert(big_right_number_x)
        big_number_grid.insert(big_left_number_y)
        big_number_grid.insert(big_right_number_y)
big_number_grid_array = number_grid_array = db.DCellInstArray(big_number_grid.cell_index(),
                                        db.DTrans(db.DTrans.R0, offset_x , offset_y),
                                        db.DVector(0, 0),
                                        db.DVector(0, 0),
                                        0,
                                        0)
top_cell.insert(big_number_grid_array)

###      create bottom contacts     ###

# Load the bottom contact GDS file
bottom_contact = db.Layout()
bottom_contact.read('bottom contact.gds')
read_cell = bottom_contact.top_cell()
rd_layer_10 = bottom_contact.layer(10,0)
rd_layer_9 = bottom_contact.layer(9,0)
cell_contact_pads = ly.create_cell('contact_pads')
cell_fine_features = ly.create_cell('fine_features')
for shape in read_cell.each_shape(rd_layer_10):
    cell_contact_pads.shapes(layer_10).insert(shape)
for shape in read_cell.each_shape(rd_layer_9):
    cell_fine_features.shapes(layer_9).insert(shape)

position_x = 3
position_y = 3
separation = 4
bottom_contact_distance = separation*10*alignment_distance
number_of_bottom_contact = number_of_grids//separation

contact_pad_array = db.DCellInstArray(cell_contact_pads.cell_index(),
                                        db.DTrans(db.DTrans.R0, offset_x + position_x*alignment_distance, offset_y + position_y*alignment_distance),
                                        db.DVector(bottom_contact_distance, 0),
                                        db.DVector(0, bottom_contact_distance),
                                        number_of_bottom_contact,
                                        number_of_bottom_contact)
fine_features_array = db.DCellInstArray(cell_fine_features.cell_index(),
                                        db.DTrans(db.DTrans.R0, offset_x + position_x*alignment_distance, offset_y + position_y*alignment_distance),
                                        db.DVector(bottom_contact_distance, 0),
                                        db.DVector(0, bottom_contact_distance),
                                        number_of_bottom_contact,
                                        number_of_bottom_contact)
top_cell.insert(contact_pad_array)
top_cell.insert(fine_features_array)


### create joel cross array ###


joel_cross_array = db.DCellInstArray(cell_joel_cross.cell_index(),
                                     db.DTrans(db.DTrans.R0, offset_x + 100 , offset_y -100),
                                     db.DVector(bottom_contact_distance, 0),
                                     db.DVector(0, bottom_contact_distance),
                                     number_of_bottom_contact,
                                     number_of_bottom_contact)
top_cell.insert(joel_cross_array)

### create joel cross index numbers ###


#finale of the composition
ly.write('bottom contact grids with alignment markers.gds')
