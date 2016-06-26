# -*- coding: utf-8 -*-
'''
title           :UImodels.py
description     :Models of different elements shown in the user interface
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6
'''

import pygame
import util,models

class Grid():
    '''
    Draws a squares grid with different type of squares

    Attrs:
        width: (int) Grid width in pixels
        height: (int) Grid height in pixels
        squareSize: (int) Square size in pixels
        lineWidth: (int) Width of grid lines in pixels
        rows: (int) Number of rows
        cols: (int) Number of columns
        screen: (pygame/display) Pygame display where is shown the grid
        grid: (UImodels/Gris) Grid object
        startPoint: (Tuple) Starting point position, with the format (x,y)
        goalPoint: (Tuple) Goal point position, with the format (x,y)
    '''
    def __init__(self,width,height,squareSize,lineWidth,screen):
        '''Initilization of the Grid object
        :param width: (int) Grid width in pixels
        :param height: (int) Grid height in pixels
        :param squareSize: (int) Square size in pixels
        :param lineWidth: (int) Width of grid lines in pixels
        :param screen: (pygame/display) Pygame display where is shown the grid
        '''
        self.width=width
        self.height=height
        self.squareSize=squareSize
        self.lineWidth = lineWidth
        self.rows = height / squareSize
        self.cols = width / squareSize
        self.screen =screen;
        self.grid = None
        self.createGrid()
        self.startPoint = (0,0)
        self.goalPoint = (1,1)

    def createGrid(self):
        '''Initialization of an empry grid'''
        self.grid = models.GridWithWeights(width=self.rows,height=self.cols)

    def getCoordsAtPoint(self,pos):
        '''Returns the grid coordinates of a given position in pixels
        :param pos: (Tuple) Screen position with the format (x,y) in pixels
        :return: (Tuple) Position of the grid with the format (row, column)
        '''
        x=pos[0]
        y=pos[1]
        row = y/self.squareSize
        col = x/self.squareSize
        return (row,col)

    def setObstacle(self,coords):
        ''' Adds an obstacle at a specific position or removes it if there was an obstacle in this position
        :param coords: (Tuple) Position of the grid with the format (row, column)
        :return:
        '''
        if (coords in self.grid.walls):
            self.grid.walls.remove(coords)
        else:
            self.grid.walls.append(coords)

    def removeObstacle(self,coords):
        ''' True if there is an obstacle in this position, false otherwise
        :param coords: (Tuple) Position of the grid with the format (row, column)
        :return: (Bool) Is there an obstacle at this position?
        '''
        if (coords in self.grid.walls):
            self.grid.walls.remove(coords)

    def reset(self):
        '''Resets all the elements of the grid'''
        self.startPoint = (0, 0)
        self.goalPoint = (1, 1)
        self.grid.walls=[]
        self.grid.weights={}

    def setStartingPoint(self,coords):
        ''' Sets the starting point position
         :param coords: (Tuple) Position of the grid with the format (row, column)
         :return:
         '''
        self.startPoint = coords

    def setGoalPoint(self,coords):
        ''' Sets the goal point position
         :param coords: (Tuple) Position of the grid with the format (row, column)
         :return:
         '''
        self.goalPoint = coords

    def neighbors(self,current):
        ''' Return the neighbors of a grid element
         :param coords: (Tuple) Position of the grid with the format (row, column)
         :return:
         '''
        return self.grid.neighbors(current)

    def paintGrid(self):
        '''Paints the grid in the pygame screen'''
        self.screen.fill((0, 0, 0))
        x,y = 0,0
        while y<=self.height:
                #Horizontal lines
                pygame.draw.line(self.screen, (0, 0, 255), (0, y), (self.cols*self.squareSize, y),self.lineWidth)
                y += self.squareSize
        while x<=self.width:
                #Vertical lines
                pygame.draw.line(self.screen, (0, 0, 255), (x, 0), (x, self.rows*self.squareSize),self.lineWidth)
                x += self.squareSize

        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if((i,j) in self.grid.walls):
                    self.paintSquare((i,j),util.COLOR_WALL)
                elif((i,j) == self.startPoint):
                    self.paintSquare( (i,j),util.COLOR_START_POINT)
                elif((i,j) == self.goalPoint):
                    self.paintSquare( (i,j),util.COLOR_GOAL_POINT)
                else:
                    self.paintSquare( (i,j),util.getColorTerrain(self.grid.cost(None,(i,j))))

    def paintSquare(self,coords,color):
        '''Draws a square in the screen'''
        y = coords[0]*self.squareSize
        x = coords[1]*self.squareSize
        point1 =(x+self.lineWidth,y+self.lineWidth)
        point2 = (x+self.lineWidth,y+self.squareSize-self.lineWidth)
        point3 =(x+self.squareSize-self.lineWidth,y+self.squareSize-self.lineWidth)
        point4=(x+self.squareSize-self.lineWidth,y+self.lineWidth)
        points=[point1,point2,point3,point4]
        pygame.draw.polygon(self.screen,color,points)



class Button():
    '''Pygame Button class

    Attrs:
        x: (int) Left button position
        y: (int) Top button position
        text: (string) Text of the button
        color: (Tuple) Background color of the button with the format (R,G,B) with R,G and B from 0 to 255
        colorText: (Tuple) Color of the text with the format (R,G,B) with R,G and B from 0 to 255
        fontSize: (int) Text size
        font: (pygame.font.Font) Text font
        screen (pygame.display) Our main screen object
        rect (pygame.rect) Rect of the text of the button
        id (int) Button identification integer

    '''
    def __init__(self,x,y,screen,text="Button",fontSize=20,buttonId=None):
        '''Initialization of the button
        :param x:  (int) Left button position
        :param y: Top button position
        :param screen: (pygame.display) Our main screen object
        :param text: (string) Text of the button
        :param fontSize: (int) Text size
        :param buttonId: (int) Button identification integer
        '''
        self.x=x
        self.y=y
        self.text=text
        self.color=(100,100,100)
        self.colorText=(0,0,0)
        self.fontSize=fontSize
        self.font=pygame.font.Font('fonts/Roboto-Light.ttf',fontSize)
        self.screen = screen
        self.rect = None
        self.id=buttonId

    def draw(self):
        '''Draws the button in the screen'''
        render = pygame.font.Font.render(self.font,self.text, 1, self.colorText)
        rect = render.get_rect()
        padding=5
        rect.left = self.x+padding
        rect.top = self.y+padding

        point1 = (self.x,self.y)
        point2 =(self.x+rect.width+2*padding,self.y)
        point3 =(self.x+rect.width+2*padding,self.y+rect.height+2*padding)
        point4 =(self.x,self.y+rect.height+2*padding)
        points = [point1,point2,point3,point4]

        self.rect = pygame.draw.polygon(self.screen,self.color,points)
        self.screen.blit(render,rect)

    def isClicked(self,pos):
        '''Detects if button is clicked given a position with the form (x,y)'''
        return self.rect.collidepoint(pos)

class Text():
    '''Pygame Text class

    Attrs:
        x: (int) Left position
        y: (int) Top position
        text: (string) Text
        colorText: (Tuple) Color of the text with the format (R,G,B) with R,G and B from 0 to 255
        fontSize: (int) Text size
        font: (pygame.font.Font) Text font
        screen (pygame.display) Our main screen object
        rect (pygame.rect) Rect of the text
    '''
    def __init__(self,x,y,screen,text="Text",fontSize=30):
        '''Initialization of the text
        :param x: (int) Left position
        :param y: (int) Top position
        :param screen: (pygame.display) Our main screen object
        :param text: (string) Text
        :param fontSize: (int) Text size
        '''
        self.x=x
        self.y=y
        self.text=text
        self.colorText=(0,0,0)
        self.fontSize=fontSize
        self.font=pygame.font.Font('fonts/Roboto-Light.ttf',fontSize)
        self.screen = screen
        self.rect = None

    def draw(self):
        '''Draws the text in the screen'''
        render = pygame.font.Font.render(self.font,self.text, 1, self.colorText)
        rect = render.get_rect()
        rect.left = self.x
        rect.top = self.y

        self.screen.blit(render,rect)

