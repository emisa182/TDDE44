#!/usr/bin/env python3

import tkinter
import lab5
import math
LayoutTester = lab5.LayoutTester


def row_layout(squares, frame_height, frame_width):
    """Placera ut fyrkanterna i listan squares i rader.

    Argument:
    squares      -- Lista som innehåller tkinter.Label-objekt
    frame_height -- Höjden (int) på den Frame som fyrkanterna ligger i
    frame_width  -- Bredden (int) på den Frame som fyrkanterna ligger i
    """

    # Slumpa ut positioner för alla fyrkanter utan att de hamnar utanför framen
    for square in squares:

        square_size = square.winfo_width()
        square_amount_x = math.floor(frame_width/square_size)
        x_col = frame_width / (square_amount_x + 1)

        square_amount_y = math.floor(frame_height/square_size)
        y_row = frame_height / (square_amount_y + 1)
        ypos += y_row

        for i in range(square_amount_x)
            xpos += x_col
            square.place(x=xpos, y=ypos)



        # xpos = random.randint(0, frame_width - square_size)
        # ypos = random.randint(0, frame_height - square_size)



if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(row_layout)
