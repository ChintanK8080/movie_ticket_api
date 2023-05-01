# import the necessary libraries
import tkinter as tk

# create the main window
root = tk.Tk()

# set the window title
root.title("My GUI App")

# create a label widget
label = tk.Label(root, text="Hello World!")

# add the label widget to the window
label.pack()

# run the main event loop
root.mainloop()
