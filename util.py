# -*- coding: utf-8 -*-
'''
title           :util.py
description     :Utilities for different parts of the project
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6
'''

from __future__ import print_function
import collections,heapq


################## CLASSES #########################################
class Queue:
    '''Queue class

    It is a data structure used by the search algorithm to decide the
    order in which to process the locations.
    Itś just a wrapper around the built-in collections.deque class.

    Attrs:
        elements = It's a deque

    '''
    def __init__(self):
        '''It creates a new empty deque'''
        self.elements = collections.deque()

    def empty(self):
        '''Returns True if the queue is empty and False otherwise'''
        return len(self.elements) == 0

    def put(self, x):
        '''Adds a new element to the queue'''
        self.elements.append(x)

    def get(self):
        '''Gets a new element from the left of the queue'''
        return self.elements.popleft()

class PriorityQueue:
    '''
    Here’s a reasonably fast priority queue that uses binary heaps, but does not support reprioritize.
    To get the right ordering, we’ll use tuples (priority, item).
    When an element is inserted that is already in the queue, we’ll have a duplicate;

    Attrs:
        elements: (List) The different elements of the Queue
    '''
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]



#################################### FUNCTIONS ##################################3
def getInfoMessage(state):
    '''Returns the info message corresponding to an specific state
    :param state: (int) Represents an execution state (STATE_NONE,STATE_STARTING_POINT,STATE_GOAL_POINT)
    :return: (String) Info message
    '''
    if(state==STATE_NONE):
        return" Press 'w' and click on the grid to add or remove a wall"
    elif(state == STATE_STARTING_POINT): #Waiting user to add starting point in the grid
        return "Click anywhere on the grid to add a starting point"
    elif (state == STATE_GOAL_POINT): #Waiting user to add goal point in the grid
        return "Click anywhere on the grid to add a goal point."


def getSecondaryInfoMessage(state):
    '''Returns the info message corresponding to an specific state
    :param state: (int) Represents an execution state (STATE_NONE,STATE_STARTING_POINT,STATE_GOAL_POINT)
    :return: (String) Info message
    '''
    if (state == STATE_NONE):
        return " Click on the grid to change the cost of a location. Click Play button to start animation."
    elif (state == STATE_STARTING_POINT):  # Waiting user to add starting point in the grid
        return ""
    elif (state == STATE_GOAL_POINT):  # Waiting user to add goal point in the grid
        return ""



def getColorTerrain(cost):
    if(cost <= 2):
        return (14,112,45)
    elif(2<cost<=4):
        return (87,233,119)
    elif(4<cost<=7):
        return (243,255,67)
    elif(cost>7):
        return (99,84,3)

################## CONSTANTS ###################################
WIDTH = 640
HEIGHT = 480
BOTTOM_BAR_HEIGHT = 210

COLOR_START_POINT=(255,0,0)
COLOR_GOAL_POINT=(112,14,107)
COLOR_WALL=(50,50,50)
COLOR_WHITE=(255,255,255)

STATE_NONE=0
STATE_STARTING_POINT=1
STATE_GOAL_POINT=2

BUTTON_PLAY=0
BUTTON_START_POINT=1
BUTTON_GOAL_POINT=2
BUTTON_RESET=3
BUTTON_BFS = 4
BUTTON_DIJKSTRA=5
BUTTON_ASTAR=6

ALG_NAMES=["Breadth First Search Algorithm","Dijkstra Search Algorithm"]