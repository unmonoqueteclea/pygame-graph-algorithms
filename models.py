# -*- coding: utf-8 -*-
'''
title           :models.py
description     :Contains useful model classes to use with IA Algorithms
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7

'''
class SquareGrid:
    '''
    Represents a grid of squares

    Attrs:
        width: (int) An integer that contains the number of squares of each row
        height: (int) An integer that contains the number of squares of each column

    '''
    def __init__(self, width, height):
        '''Inits the grid
        :param width: An integer that contains the number of squares of each row
        :param height: An integer that contains the number of squares of each column

        '''
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        '''Checks if a location is inside the grid (x,y)
        :param id: (Tuple) Location in the grid
        :return: (Boolean) True if the location is inside the grid or False otherwise
        '''
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        '''Checks if we can pass through a location
        :param id: (Tuple) Location in the grid (x,y)
        :return: False if the location is a wall and True otherwise
        '''
        return id not in self.walls

    def neighbors(self, id):
        '''Obtains the neighbors of a location

        It only obtains the neighbors that are passable (not walls)
        :param id:(Tuple) Location in the grid (x,y)
        :return: (List) List of locations (Tuple) with the form (x,y)
        '''
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    '''
        Represents a grid of squares with a cost value for each square.
        It's a kind of SquareGrid

        Attrs:
            From SquareGrid:
                width: (int) An integer that contains the number of squares of each row
                height: (int) An integer that contains the number of squares of each column
            wights: (Dictionary) It has the cost value of different positions

        '''
    def __init__(self, width, height):
        SquareGrid.__init__(self,width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        '''
        Obtains the cost of a location (Or 1 if it is not set)
        :param from_node: (Tuple) Origin location  in the grid (x,y)
        :param to_node: (Tuple) Destination location in the grid(x,y)
        :return: The weight of the destination location (Or 1 if it is not set)
        '''
        return self.weights.get(to_node, 1)

    def addWeight(self,location,weight):
        self.weights[location]=weight

    def nextWeight(self,location):
        currentWeight = self.cost(None,location)
        if (currentWeight <= 2):
            self.weights[location]=3
        elif (2 < currentWeight<= 4):
            self.weights[location]=5
        elif (4 < currentWeight <= 7):
            self.weights[location]=10
        elif (currentWeight > 7):
            self.weights[location]=1