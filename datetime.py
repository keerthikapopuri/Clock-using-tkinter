from tkinter import *
from time import strftime
# creating tkinter window
root = Tk()
root.title('Clock')
root.geometry('400x150')
# This function is used to display the time with date
def time():
	string = strftime("%m-%d-%Y\n%H:%M:%S %p")
	time_now.config(text = string)
	time_now.after(1000, time)

# Styling the label time_now
time_now = Label(root, font = ('times', 40, 'bold'),
			background = 'light grey',
			foreground = 'black')
Label(root, text ='Have a nice day', font ='times 14').pack(side = BOTTOM)
time()
time_now.pack()
mainloop()
