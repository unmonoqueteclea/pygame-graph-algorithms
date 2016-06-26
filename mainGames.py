# -*- coding: utf-8 -*-
'''
title           :mainGames.py
description     :Contains the main code of the BFS screen
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6

'''
import algorithms,util,pygame,UImodels
import time


def main(algorithm):
    '''Main function that is executed when the program starts'''
    pygame.init() #Pygame initialization
    state = util.STATE_NONE
    running=True #It will control the main loop of the program
    screen = pygame.display.set_mode((util.WIDTH+3,util.HEIGHT+util.BOTTOM_BAR_HEIGHT)) #pygame screen
    gameGrid = UImodels.Grid(util.WIDTH,util.HEIGHT,squareSize=32,lineWidth=3,screen=screen)

    gameGrid.grid.addWeight((3,3),3)
    gameGrid.grid.addWeight((3, 4), 6)
    gameGrid.grid.addWeight((3, 5), 10)
    #Main loop
    while running:
        gameGrid.paintGrid() #Repaint all the squares of the grid
        #We wont see any change until we repaint the screen
        buttons=createUI(screen,state,algorithm) #Creation of the main UI elements

        ### DETECTION OF EVENTS #######
        event = pygame.event.poll()
        if event.type == pygame.QUIT: #If user clicks the close button
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() #Click absolute position
            isButton = False
            for button in buttons:
                if (button.isClicked(pos)):
                    isButton = True
                    if(button.id is util.BUTTON_PLAY): #If Play button is clicked
                        state=util.STATE_NONE
                        runAlgoritm(pygame,gameGrid,algorithm)
                    elif(button.id is util.BUTTON_START_POINT):
                        state = util.STATE_STARTING_POINT
                    elif(button.id is util.BUTTON_GOAL_POINT):
                        state = util.STATE_GOAL_POINT
                    elif(button.id is util.BUTTON_RESET):
                        state=util.STATE_NONE
                        gameGrid.reset() #Resets all the grid

            if(not isButton): #If the user clicked the grid
                coords=gameGrid.getCoordsAtPoint(pos)
                if(state is util.STATE_NONE):
                    #If we are pressing "w" key
                    if (pygame.key.get_pressed()[pygame.K_w] != 0):
                        gameGrid.setObstacle(coords) #Adds a wall
                    else:
                        gameGrid.grid.nextWeight(coords)
                elif (state is util.STATE_STARTING_POINT):
                    gameGrid.setStartingPoint(coords) #Adds the starting point
                    state=util.STATE_NONE
                elif (state is util.STATE_GOAL_POINT):
                    gameGrid.setGoalPoint(coords) #Adds the goal point
                    state = util.STATE_NONE

        pygame.display.flip()  # Update screen


def showPath(parents,gameGrid):
    '''Shows the path calculated by the BFS algorithm
    :param parents: (Dictionary)  List of parents of each point in the grid returned by breadth_first_search()
    :param gameGrid: (UImodels/Grid) The grid where we will make the search
    :return:
    '''
    path = algorithms.reverse_path(gameGrid.startPoint, gameGrid.goalPoint, parents)
    gameGrid.paintGrid()
    for point in path:
        gameGrid.paintSquare(point, util.COLOR_WHITE)
        pygame.display.flip()  # Update screen
        time.sleep(0.05) #Wait a little bit
    time.sleep(2) #Wait 2 seconds showing the final path

def createUI(screen,state,algorithm):
    '''Creates the buttons and the different texts on the screen
    :param screen: (pygame.display) Our main screen object
    :param state: (int) Current state of the program (NO_STATE,STATE_STARTING_POINT,STATE_GOAL_POINT)
    :return: (List) List with all the buttons in the UI
    '''
    buttons = []

    #Play button
    button1 = UImodels.Button(30, util.HEIGHT + 150, screen, "Play", fontSize=15, buttonId=util.BUTTON_PLAY)
    button1.color = (0, 0, 255)
    button1.colorText = util.COLOR_WHITE
    button1.draw()
    buttons.append(button1)
    #Reset button
    button2 = UImodels.Button(80, util.HEIGHT + 150, screen, "Reset", fontSize=15, buttonId=util.BUTTON_RESET)
    button2.color = (255, 0, 0)
    button2.colorText = util.COLOR_WHITE
    button2.draw()
    buttons.append(button2)
    #Algorithm title
    title = UImodels.Text( util.WIDTH/4,util.HEIGHT+110,screen,util.ALG_NAMES[algorithm],18)
    title.colorText=util.COLOR_WHITE
    title.draw()
    #Console title
    consoleTitle = UImodels.Text(40, util.HEIGHT + 15, screen,"Console", 17)
    consoleTitle.colorText = util.COLOR_WHITE
    consoleTitle.draw()
    #Console text
    info = UImodels.Text(40, util.HEIGHT + 43, screen,util.getInfoMessage(state), 15)
    info.colorText = util.COLOR_WHITE
    info.draw()
    info = UImodels.Text(40, util.HEIGHT + 68, screen,util.getSecondaryInfoMessage(state), 15)
    info.colorText = util.COLOR_WHITE
    info.draw()
    #Console separation line
    pygame.draw.line(screen, (110,110,110), (20, util.HEIGHT+95), (util.WIDTH-20,util.HEIGHT+95),2)
    #Set starting point button
    buttonStartPoint = UImodels.Button(150, util.HEIGHT + 150, screen, "Set starting point", fontSize=15,
                                       buttonId=util.BUTTON_START_POINT)
    buttonStartPoint.color = (255, 0,0)
    buttonStartPoint.colorText = util.COLOR_WHITE
    buttonStartPoint.draw()
    buttons.append(buttonStartPoint)
    #Set finish point button
    buttonFinishPoint = UImodels.Button(280, util.HEIGHT + 150, screen, "Set goal point", fontSize=15,
                                       buttonId=util.BUTTON_GOAL_POINT)
    buttonFinishPoint.color = util.COLOR_GOAL_POINT
    buttonFinishPoint.colorText = util.COLOR_WHITE
    buttonFinishPoint.draw()
    buttons.append(buttonFinishPoint)


    return buttons

def runAlgoritm(pygame,gameGrid,algorithm):
    if(algorithm==0):
        parents = algorithms.breadth_first_search(pygame, gameGrid)
        showPath(parents, gameGrid)  # We show the path calculated by the algorithm
    elif(algorithm==1):
        parents,cost = algorithms.dijkstra_search(pygame, gameGrid)
        showPath(parents, gameGrid)  # We show the path calculated by the algorithm
