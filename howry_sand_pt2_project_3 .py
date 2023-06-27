"""
Sand Game - Pt. II
An animation that creates sand, snow, and water that flows where the mouse is pressed or dragged
Floors can be made for the elements to slide off of

Keys:
S - Sand - sand will fall through water, but not snow
W - Snow
R - Rain
Floor - Floor

File Name: howry_sand_pt2_project_3.py
Author: Ken Howry
Date: 23.1.23
Course: COMP 1352
Assignment: Project III
Collaborators: N/A
Internet Source: N/A
"""

from random import randint
import dudraw

#variables
scale = 500
scaled = int((scale+10)/5)

def hello_world() -> list:
    """
    Description of Function: Creates a list of 0's for every pixel in the canvas
    Parameters: None
    Return: None
    """
    #creating canvas
    dudraw.set_canvas_size(scale, scale)
    dudraw.set_x_scale(0, scale)
    dudraw.set_y_scale(0, scale)
    dudraw.clear(dudraw.LIGHT_GRAY)

    #new list
    pixels = []

    #appending zeroes to the list
    for i in range(scaled+1):
        pixel_row = []
        for j in range(scaled+1):
            pixel_row.append(0)
        pixels.append(pixel_row)

    return pixels

def whole_new_world() -> None:
    """
    Description of Function: Clears the canvas and updates colors according to the values in the grid
    Parameters: None
    Return: None
    """
    #clearing canvas
    dudraw.clear_rgb(135, 206, 235)

    #iterating through grid and coloring the pixels according to the number in the grid
    for j in range(int(scaled)-1):
            #0 = empty
            #1 = sand
            #2 = rain
            #3 = floor
            #4 = snow
            for i in range(int(scaled)-1):
                if pixels[i][j] == 1:
                    dudraw.set_pen_color_rgb(194, 178, 128)
                    dudraw.filled_square(5*i, 5*j, 2.5)
                elif pixels[i][j] == 2:
                    dudraw.set_pen_color_rgb(51, 85, 255)
                    dudraw.filled_square(5*i, 5*j, 2.5)
                elif pixels[i][j] == 3:
                    dudraw.set_pen_color_rgb(0, 0, 0)
                    dudraw.filled_square(5*i, 5*j, 2.5)
                elif pixels[i][j] == 4:
                    dudraw.set_pen_color_rgb(255, 255, 255)
                    dudraw.filled_square(5*i, 5*j, 2.5)

def falling_sand() -> None:
    """
    Description of Function: Makes sand fall in stacks. If water is under the sand, the sand sinks.
    Parameters: None
    Return: None
    """

    for j in range(int(scaled)-1):
        #0 = empty
        for i in range(int(scaled)-1):
            # moves pixels down
            if pixels[i][j+1] == 1 and pixels[i][j] == 0:
                pixels[i][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 1 and pixels[i-1][j] == 0:
                pixels[i-1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 1 and pixels[i+1][j] == 0:
                pixels[i+1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 1 and pixels[i][j] == 2:
                sand_saver = pixels[i][j+1]
                pixels[i][j+1] = pixels[i][j]
                pixels[i][j] = sand_saver

def motion_in_the_ocean() -> None:
    """
    Description of Function: Makes water particles flow
    Parameters: None
    Return: None
    """
    
    for j in range(int(scaled)-1):
        #0 = empty
        for i in range(int(scaled)-1):
            # moves pixels down
            if pixels[i][j+1] == 2 and pixels[i][j] == 0:
                pixels[i][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 2 and pixels[i-1][j] == 0:
                pixels[i-1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 2 and pixels[i+1][j] == 0:
                pixels[i+1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

def froze_over() -> None:
    """
    Description of Function: Makes snow particles fall
    Parameters: None
    Return: None
    """
    for j in range(int(scaled)-1):
        #0 = empty
        for i in range(int(scaled)-1):
            # moves pixels down
            if pixels[i][j+1] == 4 and pixels[i][j] == 0:
                pixels[i][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 4 and pixels[i-1][j] == 0:
                pixels[i-1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

            if pixels[i][j+1] == 4 and pixels[i+1][j] == 0:
                pixels[i+1][j] = pixels[i][j+1]
                pixels[i][j+1] = 0

def make_sand() -> None:
    """
    Description of Function: Creates sand pixels that stack where the mouse is pressed or dragged
    Parameters: None
    Return: None
    """
    if key == 's':
        #changes x, y to mouse position
        if dudraw.mouse_dragged():
            x = int(dudraw.mouse_x())
            y = int(dudraw.mouse_y())

            #setting pen color to sand tone
            dudraw.set_pen_color_rgb(194, 178, 128)

            #generate random int to decide if makes a sand piece right under cursor
            num = randint(1,2)
            if num % 2 == 0:
                pixels[int(x/5)][int(y/5)] = 1

            #generates sand pieces randomly around cursor
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 1
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 1
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 1
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 1

        #calling the sand falling function
        falling_sand()

def make_floor() -> None:
    """
    Description of Function: Creates floor pixels where the mouse is pressed or dragged
    Parameters: None
    Return: None
    """
    if key == 'f':
        #changes x, y to mouse position
        if dudraw.mouse_dragged():
            x = int(dudraw.mouse_x())
            y = int(dudraw.mouse_y())

            #setting pen color to black
            dudraw.set_pen_color_rgb(0, 0, 0)

            #generates floor pixels randomly around cursor
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 3
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 3
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 3
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 3

def make_rain() -> None:
    """
    Description of Function: Creates rain pixels that flow where the mouse is pressed or dragged
    Parameters: None
    Return: None
    """
    if key == 'r':
        #changes x, y to mouse position
        if dudraw.mouse_dragged():
            x = int(dudraw.mouse_x())
            y = int(dudraw.mouse_y())

            #setting pen color to water tone
            dudraw.set_pen_color_rgb(51, 85, 255)

            #generate random int to decide if makes water right under cursor
            num = randint(1,2)
            if num % 2 == 0:
                pixels[int(x/5)][int(y/5)] = 2

            #generates water randomly around cursor
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 2
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 2
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 2
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 2

        #calling the rain falling function
        motion_in_the_ocean()

def make_snow() -> None:
    """
    Description of Function: Creates snow pixels that fall where the mouse is pressed or dragged
    Parameters: None
    Return: None
    """
    if key == 'w':
        #changes x, y to mouse position
        if dudraw.mouse_dragged():
            x = int(dudraw.mouse_x())
            y = int(dudraw.mouse_y())

            #setting pen color to water tone
            dudraw.set_pen_color_rgb(255, 255, 255)

            #generate random int to decide if makes water right under cursor
            num = randint(1,2)
            if num % 2 == 0:
                pixels[int(x/5)][int(y/5)] = 4

            #generates water randomly around cursor
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 4
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 4
            pixels[int((x+randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 4
            pixels[int((x-randint(1,2)*5)/5)][int((y+randint(1,2)*5)/5)] = 4

        #calling function to make the snow fall
        froze_over()

# calling the list
pixels = hello_world()

#key for sand
key = 's'

#while not quit (q)
while key != 'q':
    #creation of sand
    if key == 's':
        make_sand()
        whole_new_world()
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_font_size(18)
        dudraw.text(25, 475, "Sand")

    #creation of floor
    if key == 'f':
        make_floor()
        whole_new_world()
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_font_size(18)
        dudraw.text(25, 475, "Floor")
    
    #creation of rain
    if key == 'r':
        make_rain()
        whole_new_world()
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_font_size(18)
        dudraw.text(25, 475, "Water")
    
    #creation of snow
    if key == 'w':
        make_snow()
        whole_new_world()
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.set_font_size(18)
        dudraw.text(25, 475, "Snow")

    # show animation
    dudraw.show(20)

    #changes key when new key typed
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()