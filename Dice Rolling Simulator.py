
import tkinter
from PIL import Image,ImageTk
import random

#2 Building a top-level widget to make the main window 
# for our application

# main window of application
root=tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')


# 3 Designing the buttons


#Adding label into the frame

BlankLine=tkinter.Label(root,text="")
BlankLine.pack()

# adding label with different font and formatting

HeadingLabel=tkinter.Label(root,text="Hello from DataFlair!",
fg="light green",
bg="dark green",
font="Helvetica 16 bold italic")
HeadingLabel.pack()

#iamges

dice=['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

#simulating the dice with random numbers between 0 to 6

DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))


#construct a label widget for image
ImageLabel=tkinter.Label(root,image=DiceImage)
ImageLabel.image=DiceImage

#packing a widget in the parent widget
ImageLabel.pack(expand=True)


#function activated by button
def rolling_dice():
    DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image=DiceImage
    
    
#adding button and command will use rolling dice function
button=tkinter.Button(root,text='Roll the Dice',fg='blue', command=rolling_dice)

#pack a widget in teh parent widget
button.pack(expand=True)


root.mainloop()