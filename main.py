# -*- coding: utf-8 -*-
'''
title           :main.py
description     :Contains the main code
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6

'''
import util,pygame,UImodels,mainGames
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,40)


def main():
    '''Main function that is executed when the program starts'''
    running=True #It will control the main loop of the program
    screen = pygame.display.set_mode((600,300)) #pygame screen
    buttons = createUI(screen)  # Creation of the main UI elements
    #Main loop
    while running:

        ### DETECTION OF EVENTS #######
        event = pygame.event.poll()
        if event.type == pygame.QUIT: #If user clicks the close button
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() #Click absolute position
            for button in buttons:
                if (button.isClicked(pos)):
                    running = False
                    if(button.id is util.BUTTON_BFS):
                       mainGames.main(0)
                    elif(button.id is util.BUTTON_DIJKSTRA):
                        mainGames.main(1)

        pygame.display.flip()  # Update screen



def createUI(screen):
    '''Creates the buttons and the different texts on the screen
    :param screen: (pygame.display) Our main screen object
    :return: (List) List with all the buttons in the UI
    '''
    buttons = []

    title = UImodels.Text(160,25,screen,"Algorithms visualizer",30)
    title.colorText=util.COLOR_WHITE
    title.draw()

    credits = UImodels.Text(30, 235, screen, "Created by Pablo Gonzalez Carrizo", 15)
    credits.colorText = util.COLOR_WHITE
    credits.draw()

    status = UImodels.Text(360,140, screen, "Not supported yet", 17)
    status.colorText = (200,40,40)
    status.draw()

    credits2 = UImodels.Text(30, 255, screen, "Email: pgonzalezcarrizo@gmail.com", 15)
    credits2.colorText = util.COLOR_WHITE
    credits2.draw()

    credits3 = UImodels.Text(30, 275, screen, "https://github.com/unmonoqueteclea/Pygame-Graph-Search-Algorithms-Visualizer ", 14)
    credits3.colorText = util.COLOR_WHITE
    credits3.draw()

    button1 = UImodels.Button(100, 100, screen, "Breadth-First Search", fontSize=20, buttonId=util.BUTTON_BFS)
    button1.color = (0, 0, 255)
    button1.colorText = util.COLOR_WHITE
    button1.draw()
    buttons.append(button1)

    button2 = UImodels.Button(125, 170, screen, "Dijkstra Search", fontSize=20, buttonId=util.BUTTON_DIJKSTRA)
    button2.color = (0, 128,0)
    button2.colorText = util.COLOR_WHITE
    button2.draw()
    buttons.append(button2)


    button3 = UImodels.Button(380, 100, screen, "A* Search", fontSize=20, buttonId=util.BUTTON_ASTAR)
    button3.color = (255,0,0)
    button3.colorText = util.COLOR_WHITE
    button3.draw()
    buttons.append(button3)



    return buttons
if __name__ == '__main__':
    pygame.init() #Pygame initialization
    main() #Main function