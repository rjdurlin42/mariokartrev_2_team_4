from tkinter import *
import time

root = Tk()
#root.iconbitmap("c:/home/Desktop/GUI/icon.ico")
#root.iconbitmap('D:\Tkinter Projects\icon.ico')
root.configure(bg = "#5d23c2")
#( '#4a59ff')
#myLabel_weight = Label(root)
#myLabel_age = Label(root)

size = 15

frame = Frame(root, bg = '#5d23c2')
frame.grid(row = 1, column = 2)


star = Frame(root, bg = '#5d23c2')
star.grid(row = 0, column = 2)

dpad = Frame(root, bg = '#ff0000')
dpad.grid(row = 1, column = 1)

AB_Button = Frame(root, bg = '#ff0000')
AB_Button.grid(row = 1, column = 3)

frameStopCalc = Frame(root, bg = '#ffffff')
frameStopCalc.grid(row = 0, column = 3)

frameStart = Frame(root, bg = '#5d23c2')
frameStart.grid(row = 0, column = 1)

#my_img.show()

starLabel = Label(star, text = "⭐", bg = '#5d23c2', fg = '#f7da00', font= ('Ariel', size+60))
starLabel.grid()

e = Entry(frame, bg = "#7b2eff", fg = "white", font= ('Ariel', size))
e.grid(row = 0, column = 0,columnspan = 3)

#ageVar = " "
#myLabel_age = Label(root, text= ageVar + " yrs")
#myLabel_age.grid(row = 4, column = 2)

#while 1:
#ageVar = getAge()

root.geometry('860x480')


#Function Declarations

#def function():
#    global START
#    if START is None:
#        START = 0

#def function2():
#    global STOP
#    if STOP is None:
#        STOP = 0

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    
    
    time_label.config(text = hour + ":" + minute + ":" + second)
    time_label.after(1000, clock)
#def update():
#   time_label.config(text="New Text")


#time_label.after(5000, update)


def calcMET(startMET, stopMET, weight):
    met = 7
    weight_kg = float(weight)*0.453592  #1 lb is 0.453592 kg
    duration = (stopMET*0.000277778) - (startMET*0.000277778)    #0.000277778
    calories = (duration*60*met*3.5*weight_kg)/200
    caloriesLabel.config(text = str(round(calories, 2)) + " calories")
    
#    testLabelstart = Label(root, text = startMET, fg = "green")
#    testLabelstart.grid()
#    testLabelstop = Label(frame, text = stopMET, fg = "red")
#    testLabelstop.grid()    
    
def startTime():
#myLabel_2.config(text="")
	global start
	hour = time.strftime("%H")
	minute = time.strftime("%M")
	second = time.strftime("%S")
	start = time.time()
	startTimeLabel.config(text= "Start time: " + hour + ":" + minute + ":" + second, bg = 'green', fg = 'white') 
#"Your mario workout session is running!"

#def getAge():
#ageVar = e.get()
#e.delete(0, END)
#myLabel_age.config(text= ageVar + " yrs")

def delete():
   e.delete(0, END)


def getWeight():
	global weightVar
	weightVar = e.get()
	e.delete(0, END)
	myLabel_weight.config(text= "Weight: " + weightVar + " lbs")

def stopTime():
#myLabel.config(text="")
#startVar = myLabel.get() doesn't work
#newLabel = Label(root, text= startVar, fg = 'purple')
#newLabel.grid()
	global stop
	hour = time.strftime("%H")
	minute = time.strftime("%M")
	second = time.strftime("%S")
	stop = time.time()
	myLabel_2.config(text= "Stop time: " + hour + ":" + minute + ":" + second, bg = '#d40813', fg = 'white', font= ('Ariel', size), padx = 60)

def click_num(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


startTimeLabel = Label(frameStart, text= "Start Time: ", bg = '#7b2eff', fg = 'white', font= ('Ariel', size), padx = 60)
startTimeLabel.grid(row = 0, column = 0, sticky = 'nesw', padx = 2)

myLabel_2 = Label(frameStopCalc, text= "Stop time: ", bg = '#7b2eff', fg = 'white', font= ('Ariel', size), padx = 60)
myLabel_2.grid(row = 0, column = 0, sticky = 'nesw', padx = 2)

    
caloriesLabel = Label(frameStopCalc, text = "Calories: - ", bg = '#7b2eff', fg = 'white', font= ('Ariel', size), padx = 60)
caloriesLabel.grid(row = 1, column = 0, sticky = 'nesw', padx = 2)

#myLabel_age = Label(root, text= "-" + " yrs")
#myLabel_age.grid(row = 4, column = 2)

myLabel_weight = Label(frameStart, text= "Weight: -" + " lbs", bg = '#7b2eff', fg = 'white', font= ('Ariel', size), padx = 60)
myLabel_weight.grid(row = 1, column = 0, sticky = 'nesw', padx = 2)

time_label = Label(frameStart, text= "", bg = '#7b2eff', fg = 'white', font= ('Ariel', size), padx = 60)
time_label.grid(row = 2, column = 0, sticky = 'nesw', padx = 2)

#time_label = Label(root, text="")
#time_label.grid(row = 8, column = 2)

#age = getAge() #should I make it a loop

startButton = Button(frameStart, text="[2] START SESSION", command=startTime, bg = "#1ec700",fg = "white", font= ('Ariel', size), padx = 60)
startButton.grid(row = 3, column = 0,sticky = 'nesw', padx = 2)
stopButton = Button(frameStopCalc, text = "[3] STOP SESSION", command=stopTime, bg = "#ff212c",fg = "white", font= ('Ariel', size), padx = 60)    #calcMET(START, stop, 100),
stopButton.grid(row = 2, column = 0,sticky = 'nesw', padx = 2)
calcButton = Button(frameStopCalc, text = "[4] CALCULATE", command=lambda: calcMET(start, stop, weightVar) , bg = "blue",fg = "white", font= ('Ariel', size), padx = 60)    #calcMET(START, stop, 100),
calcButton.grid(row = 3, column = 0, sticky = 'nesw', padx = 2)

#ageButton = Button(frame, text = "Set age", command=getAge, bg = '#7b2eff',fg = 'white', font= ('Ariel', size))
#ageButton.grid(row = 5, column = 0, columnspan = 3, padx = 1,pady = 1, sticky = 'nesw')
weightButton = Button(frame, text = "[1] SET WEIGHT", command=getWeight, bg = '#7b2eff',fg = 'white', font= ('Ariel', size))
weightButton.grid(row = 6, column = 0, columnspan = 3, padx = 1,pady = 1, sticky = 'nesw')

button_7 = Button(frame, text = "7", bg = "#f7da00",fg = "white", command=lambda: click_num(7), font= ('Ariel', size))
button_8 = Button(frame, text = "8", bg = "#f7da00",fg = "white", command=lambda: click_num(8), font= ('Ariel', size))
button_9 = Button(frame, text = "9", bg = "#f7da00",fg = "white", command=lambda: click_num(9), font= ('Ariel', size))

button_4 = Button(frame, text = "4", bg = "#f7da00",fg = "white", command=lambda: click_num(4), font= ('Ariel', size))
button_5 = Button(frame, text = "5", bg = "#f7da00",fg = "white", command=lambda: click_num(5), font= ('Ariel', size))
button_6 = Button(frame, text = "6", bg = "#f7da00",fg = "white", command=lambda: click_num(6), font= ('Ariel', size))

button_1 = Button(frame, text = "1", bg = "#f7da00",fg = "white", command=lambda: click_num(1), font= ('Ariel', size))
button_2 = Button(frame, text = "2", bg = "#f7da00",fg = "white", command=lambda: click_num(2), font= ('Ariel', size))
button_3 = Button(frame, text = "3", bg = "#f7da00",fg = "white", command=lambda: click_num(3), font= ('Ariel', size))

button_0 = Button(frame, text = "0", bg = "#f7da00",fg = "white", command=lambda: click_num(0), font= ('Ariel', size))
button_clr = Button(frame, text = "Delete", command=delete, bg = "#f7da00",fg = "white", font= ('Ariel', size))

button_7.grid(row = 1, column = 0, sticky = 'nesw', padx = 1,pady = 1)
button_8.grid(row = 1, column = 1, sticky = 'nesw', padx = 1,pady = 1)
button_9.grid(row = 1, column = 2, sticky = 'nesw', padx = 1,pady = 1)

button_4.grid(row = 2, column = 0, sticky = 'nesw', padx = 1,pady = 1)
button_5.grid(row = 2, column = 1, sticky = 'nesw', padx = 1,pady = 1)
button_6.grid(row = 2, column = 2, sticky = 'nesw', padx = 1,pady = 1)

button_1.grid(row = 3, column = 0, sticky = 'nesw', padx = 1,pady = 1)
button_2.grid(row = 3, column = 1, sticky = 'nesw', padx = 1,pady = 1)
button_3.grid(row = 3, column = 2, sticky = 'nesw', padx = 1,pady = 1)


button_8 = Button(dpad, text = " ↑ ", bg = "#f7da00",fg = "white", command=lambda: click_num(8), font= ('Ariel', size+8))
button_4 = Button(dpad, text = " ←", bg = "#f7da00",fg = "white", command=lambda: click_num(4), font= ('Ariel', size+8))
button_6 = Button(dpad, text = "→ ", bg = "#f7da00",fg = "white", command=lambda: click_num(6), font= ('Ariel', size+8))
button_2 = Button(dpad, text = " ↓ ", bg = "#f7da00",fg = "white", command=lambda: click_num(2), font= ('Ariel', size+8))

button_8.grid(row = 1, column = 1, sticky = 'nesw', padx = 10,pady = 5)
button_6.grid(row = 2, column = 2, sticky = 'nesw', padx = 10,pady = 5)
button_4.grid(row = 2, column = 0, sticky = 'nesw', padx = 10,pady = 5)
button_2.grid(row = 3, column = 1, sticky = 'nesw', padx = 10,pady = 5)

button_A = Button(AB_Button, text = " A ", bg = "#f7da00",fg = "white", command=lambda: click_num(6), font= ('Ariel', size+8))
button_B = Button(AB_Button, text = " B ", bg = "#f7da00",fg = "white", command=lambda: click_num(2), font= ('Ariel', size+8))
button_A.grid(row = 0, column = 1, sticky = 'nesw', padx = 10,pady = 5)
button_B.grid(row = 1, column = 0, sticky = 'nesw', padx = 10,pady = 5)


button_0.grid(row = 4, column = 0, sticky = 'nesw', padx = 1,pady = 1)
button_clr.grid(row = 4, column = 1, columnspan = 2, sticky = 'nesw', padx = 1,pady = 1) 
#button_1 = Button(root, text = "?", bg = "#f7da00",fg = "white")
#button_2 = Button(root, text = "?", bg = "#f7da00",fg = "white")
#button_3 = Button(root, text = "?", bg = "#f7da00",fg = "white")

#button_1.grid(row = 7, column = 1, padx = 1)
#button_2.grid(row = 7, column = 2, padx = 1)
#button_3.grid(row = 7, column = 3, padx = 1)


#Age = Label(root, text="Enter age: ")
#Weight = Label(win, text= "Enter Weight: ")

#Age.grid(row = 1, column = 5, pady = 2)
#Weight.grid(row = 0, column = 1, pady = 2)
#function()
#function2()
clock()
root.title("Mario Health Meter")
root.mainloop()
