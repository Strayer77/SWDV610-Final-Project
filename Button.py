from graphics import *

class Button:
    def __init__( self, window, centerPt, width, height, text ):
        #for finding the x boundaries between x values for button
        self.minX = centerPt.getX() - width / 2.0
        self.maxX = centerPt.getX() + width / 2.0
        
        self.minY = centerPt.getY() - height / 2.0
        self.maxY = centerPt.getY() + height / 2.0
        
        #points determined minus width /2 for upperleft and + width /2 for lowerright
        ulPt = Point(self.minX, self.minY)
        lrPt = Point(self.maxX, self.maxY)
        
        self.rect = Rectangle(ulPt, lrPt)
        self.rect.setFill('light gray')
        self.rect.draw( window )
        
        self.text = Text( centerPt, text )
        self.text.draw( window )
        
        self.isEnabled = True
        
    def setEnabled(self):
        self.isEnabled = True
        self.rect.setFill('light gray')
            
    def setDisabled( self ):
        self.isEnabled = False
        self.rect.setFill('dark gray')
        
    def wasClickedIn(self, clickPoint ):
        #only if button is enabled and all these other parameters are met will we say button wasClickedIn
        return self.isEnabled and clickPoint.getX() >= self.minX and clickPoint.getX() <= self.maxX and clickPoint.getY() >= self.minY and clickPoint.getY() <= self.maxY
        
