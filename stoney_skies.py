# Florian Fruehwirth
# Stoney Skies Alpha
# This version is non-functional and used for the design and development of
# the GUI.
# Last change: 10.08.2019

import tkinter as tk

marker_ID = 1   # For assigning IDs to the markers. Necessary becausue canvas object count starts at
marker_list = []    # The "collection" of all markers.

# <cf> Classes


class Marker:
    # The class for the user-added markers. Take center coordinates. Color
    # will be unnecessary in the future and is only used for development.
    def __init__(self, canvas, xc, yc, color):
        self.radius = 7     # Radius is fixed. Might be an option later.
        self.xc = xc
        self.yc = yc
        self.x1 = xc - self.radius  # Because the oval takes coordinates of the
        # bounding box, that has to be calculates from given center coords.
        self.y1 = yc - self.radius
        self.x2 = xc + self.radius
        self.y2 = yc + self.radius
        self.id = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color, tag='marker')

    def get_coordinates(self):
        # returns the coordinates of a marker as list
        coordinates = (self.xc, self.yc)
        return(coordinates)

# </cf> Classes

# <cf> Functions


def place_marker(event):
    # Funuction to add the marker. Adds it to marker_list.
    global marker_ID
    global marker_list
    marker_list.append(Marker(canvas, event.x, event.y, 'red'))
    print(marker_list)
    marker_ID += 1


def clear_canvas():
    # Function to clear the entire canvas of all markers
    canvas.delete('marker')


# def undo():
    # Undo function deletes the marker itself as well as its object held
    # in the marker_list.
    # canvas.delete(marker_list[-1].id)
    # del marker_list[-1]


def delete_marker(event):
    # Function to delete the current marker under the mouse pointer.
    object_id = (canvas.find_withtag('current')[0])  # object ID under cursor
    canvas.delete(object_id)  # deletes the object under cursor
    del marker_list[object_id-1]  # deletes the relevant marker object


def configure(event):
    canvas.delete("grid")
    w = event.width
    h = event.height
    r = 20
    for x in range(0, r):
        canvas.create_line((w/r)*x, 0, (w/r)*x, h, tag=('grid'))
    for y in range(0, r):
        canvas.create_line(0, (h/r)*y, w, (h/r)*y, tag=('grid'))


def test():
    marker_coordinates = []
    for i in range(0, len(marker_list)):
        marker_coordinates.append(marker_list[i].get_coordinates())

    print(marker_coordinates)
    # Function for testing function. Gets called by button of same name.
    # pass


# </cf> Functions

# <cf> drawing the interface


root_width = 1120   # width of the main window
root_height = 700   # height of the main window

root = tk.Tk()

control = tk.Frame(bg='green')
control.place(relheight=0.9, relwidth=0.18, rely=0.05, relx=0.01)
canvas = tk.Canvas(cursor='crosshair', bd=5, relief='groove')
canvas.bind("<Configure>", configure)
canvas.bind('<Button-1>', place_marker)
canvas.bind('<Button-3>', delete_marker)
canvas.place(relheight=0.90, relwidth=0.75, rely=0.05, relx=0.2)

# b_undo = tk.Button(control, text="Undo", font=30)
# b_undo.pack(pady=5, fill='x')

# b_redo = tk.Button(control, text="Redo", font=30)
# b_redo.pack(pady=5, fill='x')

b_clear = tk.Button(control, text="Clear canvas", font=30, command=clear_canvas)
b_clear.pack(pady=5, fill='x')

b_test = tk.Button(control, text="Test", font=30, command=test)
b_test.pack(pady=5, fill='x')

b_quit = tk.Button(control, text="Quit", font=30, command=root.quit)
b_quit.pack(pady=5, fill='x')

# </cf> drawing the interface

root.geometry(f'{root_width}x{root_height}+100+100')
root.mainloop()
