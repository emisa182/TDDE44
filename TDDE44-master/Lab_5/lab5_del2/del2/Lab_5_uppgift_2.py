#!/usr/bin/env python3

import lab5


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
        square.place(x=(xpos), y=(ypos))
        if (xpos + 10 + square_size) < (frame_width - 10 - square_size):
            xpos += 10 + square_size
        elif (ypos + square_size) < (frame_height-10 - square_size):
            xpos = 0
            ypos += 10 + square_size
        else:
            break


if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(row_layout)
