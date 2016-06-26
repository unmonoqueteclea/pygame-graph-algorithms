# -*- coding: utf-8 -*-
'''
title           :algorithms.py
description     :Contains some well-known graph search algorithms
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6

'''
import util,models
import time

def breadth_first_search(pygame,gameGrid):
    '''Implementation of Breadth First Search algorithm with early exit

    The search stops when we reach the goal point
    Source: http://www.redblobgames.com/pathfinding/a-star/implementation.html
    :param pygame (pygame) The current pygame object that we are using
    :param gameGrid: (UImodels/Grid) The grid where we will make the search
    :return: (Dictionary) List of parents of each point in the grid after the search
    '''
    start=gameGrid.startPoint
    frontier = util.Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        gameGrid.paintSquare(current,(255))
        pygame.display.flip()  # Update screen
        time.sleep(0.05)

        if current == gameGrid.goalPoint:
            time.sleep(1)
            break

        for next in gameGrid.grid.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

def breadth_first_reverse_path(start,goal,parents):
    ''' Obtains the path from starting point to the goal point
        after having done Breadth First Search
    :param start: (Tuple) Starting point with the format (x,y)
    :param goal: (Tuple) Goal point with the format (x,y)
    :param parents: (Dictionary)  List of parents of each point in the grid returned by breadth_first_search()
    :return: (List) List containing all the points of the path from start to goal
    '''
    path=[]
    next=parents.get(goal)
    while (next is not None and next is not start):
        path.append(next)
        next=parents.get(next)

    return path


def dijkstra_search(pygame,gameGrid):
    '''Implementation of Breadth First Search algorithm with early exit

    The search stops when we reach the goal point
    Source: http://www.redblobgames.com/pathfinding/a-star/implementation.html
    :param pygame (pygame) The current pygame object that we are using
    :param gameGrid: (UImodels/GridWithWeights) The grid where we will make the search
    :return: (Dictionary) List of parents of each point in the grid after the search
    '''
    start=gameGrid.startPoint

    frontier = models.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == gameGrid.goalPoint:
            break

        for next in gameGrid.grid.neighbors(current):
            new_cost = cost_so_far[current] + gameGrid.grid.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far