#inventory checker, search csv file for inventory
#checks to see if amount on order is valid in inventory
import csv
from graphics import *
from Button import Button

#-------------------------------------------------------------------------------------------------------
#This is where the main graphics window is created.
def userInterface():
    WIDTH = 700
    HEIGHT = 300
    win = GraphWin("Inventory Checker", WIDTH, HEIGHT)
    win.setBackground("light green")
    
    #Title Rectangle
    titleRectPointOne = Point(WIDTH - 650, 25)
    titleRectPointTwo = Point(WIDTH - 50, 75)
    titleRect = Rectangle(titleRectPointOne, titleRectPointTwo)
    titleRect.setFill("white")
    titleRect.setOutline("gray")
    titleRect.setWidth(2)
    titleRect.draw(win)
    
    #Title Text
    TitleText = Text(titleRect.getCenter(), "Inventory Check")
    TitleText.setSize(36)
    TitleText.setStyle("bold")
    TitleText.setTextColor("black")
    TitleText.draw(win)
    
    
    
    return win
    
#-------------------------------------------------------------------------------------------------------
#This is where the Entry Boxes and Results Display Boxes are created
def InputEntryBox(window):
    #seedSourceInput = input("Enter the seed source: ")
    #amountKG = int(input("Enter the amount need in kg: "))
    #Entry Points
    
    #Results Display Box
    ResultsDisplayBox = Entry(Point(445, 166), 55)
    ResultsDisplayBox.setFill("White")
    ResultsDisplayBox.draw(window)
    ResultsDisplayText = Text(ResultsDisplayBox.getAnchor(), "Results:")
    ResultsDisplayText.setSize(13)
    ResultsDisplayText.move(-173, -25)
    ResultsDisplayText.draw(window)
    
    
    #Seed Source Entry
    SeedSourceEntryBox = Entry(Point(130, 130), 20)
    SeedSourceEntryBox.setFill("White")
    SeedSourceEntryBox.draw(window)
    SeedSourceText = Text(SeedSourceEntryBox.getAnchor(), "Enter Seed Source:")
    SeedSourceText.move(-25, -25)
    SeedSourceText.draw(window)
    
    #Amount Needed Entry
    AmountNeededEntryBox = SeedSourceEntryBox.clone()
    AmountNeededEntryBox.move(0, 65)
    AmountNeededEntryBox.draw(window)
    AmountNeededText = Text(AmountNeededEntryBox.getAnchor(), "Enter Amount Needed(KG):")
    AmountNeededText.move(-7, -25)
    AmountNeededText.draw(window)
    
    
    return SeedSourceEntryBox, AmountNeededEntryBox, ResultsDisplayBox

#-------------------------------------------------------------------------------------------------------
#This is the function that opens the CSV file and searches the appropriate
#rows for the entered info, being the alphanumeric seed source and the
#amount needed. If no information is entered, it will say that info
#should be provided, else it will produce a results statement that will tell
#if the amount requested was more than what is in inventory or will tell
#you how much will be left over in inventory for the amount requested

def csvFileReaderSearch(sourceInput, amountInput):
    sourceFound = False
    with open('Inventory_File.csv', 'rt') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        if sourceInput == "" and amountInput == "":  #if no information was entered
            ResultsStatement = "Please enter your information." #prompts you to provide info
            return ResultsStatement
        else: #if information was provided
            for row in reader:
                if sourceInput in row[0]: #searches first row in cvs file, if found -
                    sourceFound = True    #sourcefound equals true
                    if float(amountInput) < float(row[3]):  #then searches row 3 for amount
                        difference = (float(row[3]) - float(amountInput)) #if amount requested less than what is available, takes difference and prints statement below
                        ResultsStatement = "This will leave {0:0.2f} KG of the {1} KG available for {2}.".format(difference, row[3], sourceInput)                
                    else:  #if amount requested was more than whats in inventory, prints the statement below
                        ResultsStatement = "You requested {0} KG and only {1} KG was available for {2}.".format(amountInput, row[3], sourceInput)
                
                    return ResultsStatement
                
        csvFile.close()


#-------------------------------------------------------------------------------------------------------
#this is where we will get info from the user in the entry boxes in the
#graphics window. It then returns the inputs from both entry boxes
def getInput(window, SeedEntry, AmountEntry, ResultsDisplay):
    #Button to press to enter information
    EnterInfoButton = Button(window, Point(95, 230), 50, 25, "Enter")
    FinishedButton = Button(window, Point(150, 230), 50, 25, "Close")
    mouseclick = window.getMouse()
    if FinishedButton.wasClickedIn(mouseclick): #closes window if this button was clicked
        window.close()
    else: #if finished button wasn't clicked, continues on
        while True:
            if EnterInfoButton.wasClickedIn(mouseclick): #Once enterinfo button is pressed, grabs text and returns it to be used later
                SeedSourceInput = SeedEntry.getText()
                AmountInput = AmountEntry.getText()               
                SeedEntry.setText("")
                AmountEntry.setText("")
            
                return SeedSourceInput, AmountInput           

#-------------------------------------------------------------------------------------------------------
#this function is for displaying the results of the csvFileReaderSearch function
#into the results display box
def displayResult(resultsStatement, resultsDisplay):
    resultsDisplay.setText(resultsStatement)
     

#-------------------------------------------------------------------------------------------------------
def main():
        
    graphicWindow = userInterface()
    SeedSourceEntry, AmountNeededEntry, ResultsDisplayBox = InputEntryBox(graphicWindow)
    while True:
        SeedSourceInput, AmountInput = getInput(graphicWindow, SeedSourceEntry, AmountNeededEntry, ResultsDisplayBox)
        resultsStatement = csvFileReaderSearch(SeedSourceInput, AmountInput)
        displayResult(resultsStatement, ResultsDisplayBox)
    
    
main()
    
    