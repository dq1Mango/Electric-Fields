#I dont need no chatGPT

import tkinter as tk
import math
import time

width = 1200
height = 800
defaultRadius = 10
xPad, yPad = 20, 20
sliderLength = 200

thickness = 1
fieldFill = "black"

charges = []
chargeUpdateIndex = 0
uglyGlobalVarible = -1
firstChargeAdded = False

fieldDensity = 8
precision = 1
maxPrecision = 25

root = tk.Tk()
root.geometry('1240x900')
root.title('Canvas Demo')

label = tk.Label(root, text = "0, 0")
label.pack(padx = 5, pady = 5)

#Helpful testing code:
def motion(event):
    x, y = event.x, event.y
    label.config(text = "X:" + str(x) + ", Y:" + str(y))

root.bind('<Motion>', motion)

def updateCharges(v):
    global charges
    charges[chargeUpdateIndex][2] = int(float(v))
    s.config(label="Magnitude: " + str(charges[chargeUpdateIndex][2]))
    updateCanvas()

def addCharge(event): #what an accurate name
    if str(event.widget) != ".!canvas":
        return
    x, y = event.x, event.y
    if event.state == 8:
        drawPotential(x, y, -1)
    else:
        global charges
        overlapping = False
        for charge in charges:
            if abs(charge[0] - x) <= 2 * defaultRadius and abs(charge[1] - y) <= 2 * defaultRadius:
                overlapping = True
                if abs(charge[0] - x) <= defaultRadius and abs(charge[1] - y) <= defaultRadius:
                    for i in range(len(charges)):
                        if charges[i] == charge:
                            global chargeUpdateIndex
                            chargeUpdateIndex = i
                            s.set(charge[2])
                            s.config(label="Magnitude: " + str(charge[2]))

                            global uglyGlobalVarible
                            uglyGlobalVarible = i
                            global precision
                            precision = 20

                            return

        if overlapping:
            return

        charges += [[x, y, 1 - 2 * int(event.state == 1)]]
        global firstChargeAdded
        if not firstChargeAdded:
            s.config(label="Magnitude: " + str(charges[0][2]))
            firstChargeAdded = True
        updateCanvas()

root.bind('<Button-1>', addCharge)

def moveCharge(event): #another great function name

    if uglyGlobalVarible == -1:
        return

    global charges
    charges[uglyGlobalVarible][0] = event.x
    charges[uglyGlobalVarible][1] = event.y
    updateCanvas()

root.bind("<B1-Motion>", moveCharge)

def stopChargeMoving(event):
    global uglyGlobalVarible
    global precision

    if uglyGlobalVarible == -1:
        if precision != maxPrecision - int(precision_slider.get()) + 1:
            precision = maxPrecision - int(precision_slider.get()) + 1
            updateCanvas()
        return

    uglyGlobalVarible = -1
    precision = maxPrecision - int(precision_slider.get()) + 1
    updateCanvas()

root.bind("<ButtonRelease-1>", stopChargeMoving)

def changeFieldDensity(value):
    global fieldDensity
    fieldDensity = int(value)
    density_slider.config(label="Field Density: " + str(value))
    updateCanvas()

density_slider = tk.Scale(master = root, label='Field Density: 8', from_=4, to=16, orient=tk.HORIZONTAL, length=sliderLength, showvalue=False, command=changeFieldDensity)
density_slider.place(x=xPad, y=yPad)
density_slider.set(fieldDensity)

def deleteCharge(event):

    if str(event.keysym )!= "BackSpace":
        return

    global charges
    global chargeUpdateIndex
    global firstChargeAdded

    charges.remove(charges[chargeUpdateIndex])
    chargeUpdateIndex = len(charges)
    firstChargeAdded = False
    s.config(label = "Dont touch me now ;)")

    updateCanvas()

root.bind("<KeyPress>", deleteCharge)

s = tk.Scale(master=root, label='Dont touch me now ;)', from_=-10, to=10, orient=tk.HORIZONTAL, length=sliderLength, showvalue=False, command=updateCharges)
s.place(x=width / 2 - sliderLength / 2, y=yPad)

def changePrecision(value):
    global precision
    precision = maxPrecision - int(value) + 1
    precision_slider.config(label='Precision: ' + value)
    updateCanvas()

precision_slider = tk.Scale(master=root, label='Precision: 10', from_=1, to=maxPrecision, orient=tk.HORIZONTAL, length=sliderLength, showvalue=False, command=changePrecision)
precision_slider.place(x = width - sliderLength - xPad, y = yPad)
precision_slider.set(maxPrecision)

canvas = tk.Canvas(root, width=width, height=height, bg='grey')
canvas.place(x=xPad, y=yPad + 60)
#canvas.pack(anchor=tk.CENTER, expand=True)


def boringUIThingIHadToCodeMyself(event):

    global precision
    global width
    global height

    if root.winfo_width() - 2 * xPad != width or root.winfo_height() - 60 - 2 * yPad != height:
        precision = 20
        width = event.width - 2 * xPad
        height = event.height - 60 - 2 * yPad
        canvas.config(width = width)
        canvas.config(height = height)
        s.place(x=width / 2 - sliderLength / 2,y=yPad)
        precision_slider.place(x = width - sliderLength, y = yPad) #ur here btw



        updateCanvas()
        #precision = maxPrecision - (precision_slider.get()) + 1
        return

root.bind("<Configure>", boringUIThingIHadToCodeMyself)

def sign(n):
    return 1 if n >= 0 else -1

#def distance(x1, y1, x2, y2):
#    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
def almostEqual(a, b):
    return abs(a - b) < 10e-2

def calcField(x, y):
    fieldX = 0
    fieldY = 0
    for charge in charges:
        fieldX += (x - charge[0]) * charge[2] / ((charge[0] - x) ** 2 + (charge[1] - y) ** 2) ** (3/2)
        fieldY += (y - charge[1]) * charge[2] / ((charge[0] - x) ** 2 + (charge[1] - y) ** 2) ** (3/2)
    return (fieldX, fieldY)

def calcPotential(x, y):
    fieldX = 0
    for charge in charges:
        if x == charge[0] and y == charge[1]: continue
        fieldX += charge[2] / ((charge[0] - x) ** 2 + (charge[1] - y) ** 2) ** (1/2)
        #fieldY += (y - charge[1]) * charge[2] / ((charge[0] - x) ** 2 + (charge[1] - y) ** 2) ** (1/2)
    return fieldX

def unitVector(x):
    length = math.sqrt(x[0] ** 2 + x[1] ** 2)
    if length > 1: #shhhhhh
        return [0, 0]
    return (x[0] / length, x[1] / length)

def drawField(x, y, sign):
    nextX, nextY = x, y
    pastX, pastY = x + 1, y + 1 #so many hacks
    i = 1
    while 0 < x < width and 0 < y < height:
        field = unitVector(calcField(x, y))

        if field == [0, 0]: #also hush hush
            break

        nextX += field[0] * sign * precision
        nextY += field[1] * sign * precision

        if almostEqual(pastX, nextX) and almostEqual(nextY, pastY):
            break

        canvas.create_line((x, y), (nextX, nextY), width = thickness, fill = fieldFill)

        if i >= 100:
            canvas.create_polygon((nextX, nextY), (nextX - 8 * field[0] + 4 * field[1], nextY - 8 * field[1] - 4 * field[0]), (nextX - 8 * field[0] - 4 * field[1], nextY - 8 * field[1] + 4 * field[0]), fill = fieldFill)
            i = 0

        pastX, pastY = x, y
        x, y = nextX, nextY
        i += 1 * precision


def drawPotential(x, y, drawDirection):
    x, y = int(x), int(y)
    nextX, nextY = x, y
    ogCoords = [x, y]
    ogPotential = calcPotential(x, y)
    bestDifference = 100 #holy hacks
    bestCourse = [0, 0]
    for j in range(-1, 2):

        potential = calcPotential(x + drawDirection, y + j)
        if abs(potential - ogPotential) < bestDifference:
            bestDifference = abs(potential - ogPotential)
            bestCourse = [drawDirection, j]

    potential = calcPotential(x, y + drawDirection)
    if abs(potential - ogPotential) < bestDifference:
        bestDifference = abs(potential - ogPotential)
        bestCourse = [0, drawDirection]

    nextX += bestCourse[0]
    nextY += bestCourse[1]
    canvas.create_line((x, y), (nextX, nextY), width = thickness, fill = "white")
    pastX, pastY = x, y
    x, y = nextX, nextY

    while not (x == ogCoords[0] and y == ogCoords[1]):
        if not (0 < x < width and 0 < y < height):
            if drawDirection == -1:
                drawPotential(ogCoords[0], ogCoords[1], 1)
            break

        bestDifference = 100 #holy hacks
        bestCourse = [0, 0]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (j == 0 and i == 0) or (i + x == pastX and j + y == pastY):
                    continue
                potential = calcPotential(x + i, y + j)
                if abs(potential - ogPotential) < bestDifference:
                    bestDifference = abs(potential - ogPotential)
                    bestCourse = [i, j]
        nextX += bestCourse[0]
        nextY += bestCourse[1]
        canvas.create_line((x, y), (nextX, nextY), width = thickness, fill = "white")
        pastX, pastY = x, y

        x, y = nextX, nextY


def drawCharge(charge):
    if charge[2] == 0:
        fill = "black"
    elif charge[2] > 0:
        fill = "red"
    else:
        fill = "blue"

    if chargeUpdateIndex >= len(charges):
        outline = fill #what wonderful control flow
    elif charges[chargeUpdateIndex] == charge:
        outline = "white"
    else:
        outline = fill

    radius = defaultRadius + abs(charge[2])
    canvas.create_oval((charge[0] - radius, charge[1] - radius), (charge[0] + radius, charge[1] + radius), fill=fill, outline=outline)

def updateCanvas():
    canvas.delete("all")
    for charge in charges:
        if charge[2] == 0: continue
        radius = defaultRadius + abs(charge[2])
        for i in range(fieldDensity + abs(charge[2]) - 1):
            drawField(charge[0] + radius * math.cos(2 * math.pi * i / (fieldDensity + abs(charge[2]) - 1)), charge[1] + radius * math.sin(2 * math.pi * i / (fieldDensity + abs(charge[2]) - 1)), sign(charge[2]))

    for charge in charges:
        drawCharge(charge)

updateCanvas()
root.mainloop()
