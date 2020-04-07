#!/usr/bin/env python3

import tkinter
import lab5
import math


def row_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares i rader.

    Argument:
    squares      -- Lista som innehåller tkinter.Label-objekt
    frame_height -- Höjden (int) på den Frame som fyrkanterna ligger i
    frame_width  -- Bredden (int) på den Frame som fyrkanterna ligger i
    """

    ypos = 0
    xpos = 0

    for square in squares:

        square_size = square.winfo_width()

        square_amount_x = math.floor(frame_width/square_size)
        x_col = (frame_width-square_size*square_amount_x)/(square_amount_x+1)

        square_amount_y = math.floor(frame_height/square_size)
        y_row = (frame_height-square_size*square_amount_y)/(square_amount_y+1)

        if (xpos+x_col*square_amount_x + square_size) <
        (frame_width - x_col*square_amount_x - square_size):
            xpos += x_col*square_amount_x + square_size

        else:
            xpos = x_col*square_amount_x + square_size
            ypos += y_row*square_amount_y + square_size

        square.place(x=(xpos), y=(ypos+square_size))


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(row_layout)
