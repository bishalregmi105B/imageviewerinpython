

from tkinter import*
from PIL import Image,ImageTk
import PIL
root = Tk()

image= (Image.open("nepal.png"))
width, height = image.size
root.geometry(f"{width}x{height}")

canvas= Canvas(root, width= width, height= height)
canvas.pack()
resizedimg = image.resize((width,height), Image.ANTIALIAS)
newimg = ImageTk.PhotoImage(resizedimg)

canvas.create_image(10,10, anchor=NW, image=newimg)

root.mainloop()


