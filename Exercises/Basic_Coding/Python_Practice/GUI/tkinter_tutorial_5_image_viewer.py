from tkinter import *
from PIL import ImageTk, Image  
import glob
# from tkmacosx import Button - allows background color and other features not available on macosx
try:
    n = n
except:
    n = 0
# create the root
root = Tk()
root.title('Dummy Program')

# add an icon to the program
ext = '.JPG'
directory = '/Users/anthonyesposito/Pictures/2018/4/'
Image_Files = glob.glob(directory + '*' + ext)
Image_Files.sort()


# root.iconbitmap(directory + filename + '.ico')

# Import and Resize image

images = [[]] * len(Image_Files)
images = [[]] * 5
for i in range(len(images)):
    image = Image.open(Image_Files[i])
    scale = 1000. / (max(image.size))
    image = image.resize((int(float(image.size[0])*scale), int(float(image.size[1])*scale)), Image.ANTIALIAS)
    images[i] = ImageTk.PhotoImage(image)
print(len(images))
len_im_char = len(str(len(images)))

# Button Actions

def Button_Next():
    global n
    global my_label
    n+=1
    if n == len(images):
        n = 0
    print(n, Image_Files[n])
    my_label.grid_forget()
    my_image = images[n]
    my_label = Label(image=my_image)
    my_label.grid(row=1, column=0, columnspan=3)

    status = Label(root, text=( "Image {} of {}".format((n+1), len(images))), padx=30, pady=10, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=2, sticky=E)
    return

def Button_Last():
    global n
    global my_label
    n-=1
    if n < 0:
        n = len(images)-1
    print(n, Image_Files[n])
    my_label.grid_forget()
    my_image = images[n]
    my_label = Label(image=my_image)
    my_label.grid(row=1, column=0, columnspan=3)

    status = Label(root, text=( "Image {} of {}".format((n+1), len(images))), padx=30, pady=10, bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=2, sticky=E)
    return 

# Buttons

quit_button = Button(root, text="Exit Program", padx=50, pady=50, command = root.quit)
quit_button.grid(row=2, column=1)

next_button = Button(root, text="Next>>", padx= 40, pady=40, command=Button_Next)
next_button.grid(row=0, column=2)

last_button = Button(root, text="<<Prev", padx= 40, pady=40, command=Button_Last)
last_button.grid(row=0, column=0)

# Add an Image with Pillow

my_image = images[n]
my_label = Label(image=my_image)
my_label.grid(row=1, column=0, columnspan=3)

status = Label(root, text=( "Image {} of {}".format((n+1), len(images))), padx=30, pady=10, bd=1, relief=SUNKEN, anchor=E)
status.grid(row=3, column=2, sticky=E)

print(n)
# run the root
root.mainloop()