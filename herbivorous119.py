from random import randint, choice, choices
import copy

class CellGenome():

    def createCellName(self):
        return f'herbivorous{randint(0, 1000)}.py'

    def createMembrane(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {items} around
        #determens which {items} can and cant pass

        with open(cellName, 'a') as f:
            f.writelines('''
def getCoordinates(matrix, body):
    for index, line in enumerate(matrix):
        if body in line:
            y_coord = copy.deepcopy(index)
        
        for index, column in enumerate(line):
            if body == column:
                x_coord = copy.deepcopy(index)

    return (y_coord, x_coord)

def neighbors(matrix, body):
    neighb = {}
    coordinates = getCoordinates(matrix, body)

    directions = ['up', 'upRight', 'right', 'downRight', 'down', 'downLeft', 'left', 'upLeft']

    conditions = [coordinates[0] - 1 < 0, coordinates[0] - 1 < 0 or coordinates[1] + 1 >= len(matrix),
                  coordinates[1] + 1 >= len(matrix), coordinates[0] + 1 >= len(matrix) or coordinates[1] + 1 >= len(matrix),
                  coordinates[0] + 1 >= len(matrix), coordinates[0] + 1 >= len(matrix) or coordinates[1] - 1 < 0,
                  coordinates[1] - 1 < 0, coordinates[0] - 1 < 0 or coordinates[1] - 1 < 0]

    neighbors = [matrix[coordinates[0] - 1][coordinates[1]], matrix[coordinates[0] - 1][coordinates[1] + 1 - len(matrix)], 
                 matrix[coordinates[0]][coordinates[1] + 1 - len(matrix)], matrix[coordinates[0] + 1 - len(matrix)][coordinates[1] + 1 - len(matrix)],
                 matrix[coordinates[0] + 1 - len(matrix)][coordinates[1]], matrix[coordinates[0] + 1 - len(matrix)][coordinates[1] - 1],
                 matrix[coordinates[0]][coordinates[1] - 1], matrix[coordinates[0] - 1][coordinates[1] - 1]]

    for i in range(8):
        if conditions[i]:
            neighb[directions[i]] = 'none'
        else:
            neighb[directions[i]] = neighbors[i]

    rawFood[0] -= 1
    return neighb

def trespassingLogic(item):
    if item == 'j':
        return 'no'
    if item == '_':
        return 'nothing'
    else:
        return 'eat'
''')

    def createLisosome(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {food} or {pathogene}
        #disassembles {food} or {pathogene} into singular {parts} or {junk}

        with open(cellName, 'a') as f:
            f.writelines('''
def disassembleFood(item):
    alph = [

        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
        'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ',', 
        "'", '"', '[', ']', '=', '+', '-', ':'
    ]
    energyPool[0] -= 0.5

    weights = [76 for x in range(26)] + [3 for x in range(10)] + [20 for x in range(9)]
    jk = ';'
    parts = []
    junk = []
    howManyFood = 40

    if item == 'f':
        parts += choices(alph, weights, k=howManyFood)
    else:
        particles = item.split('/')
        timesFood = int(((int(particles[0][1]) * 100) / (int(particles[0][1]) + int(particles[1][1])) / 100) * howManyFood)
        parts += choices(alph, weights, k=timesFood)
        junk += choices(jk, k=int(particles[1][1]))

    return parts, junk
''')

    def createExocytosisSystem(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {junk}
        #gets rid of a junk

        with open(cellName, 'a') as f:
            f.writelines('''
def getRidOfJunk(junkList):
    energyPool[0] -= len(junkList) * 0.01
    junkList.clear()
''')

    def createGolgiBody(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {parts dictionary}
        #creates {code pices} out of {parts dictionary}
        pass

    def createCytoPlasm(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {code pices}
        #stores all code bits and energy that avaliable inside {pices dictionary} and {energyCito} variable and determines how big cell is

        with open(cellName, 'a') as f:
            f.writelines('''
energyPool = [0]
rawFood = [0]
howBig = 1
energyMax = 15 * howBig
bitsMax = 100 * howBig
homeostasisConsumption = 0.1 * howBig
''')

    def createReplicator(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy} while active
        #depends on: {pices dictionary}
        #replicate if there is enough code bits
        pass


    def createMitochondrion(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy}
        #depends on: {parts dictionary}
        #creates {energy} out of parts and returns an integer

        with open(cellName, 'a') as f:
            f.writelines('''
def createEnergy(partsList):
    partsList.remove(choice(partsList))
    energyPool[0] += 5

    return partsList
''')

    def createMovingEngine(self, cellName):
        #need ?? {code pices} and ?? {energy} to build
        #consumes ?? {energy}
        #depends on: {energy}
        #moves organism around in cost of energy

        with open(cellName, 'a') as f:
            f.writelines('''
def upMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1]] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix):
        raise IndexError('Cant move down! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1]] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'    

def leftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[1] - 1 < 0:
        raise IndexError('Cant move left! It is the end of the world!')

    matrix[coordinates[0]][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def rightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move right! It is the end of the world!')

    matrix[coordinates[0]][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_' 

def upLeftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0 or coordinates[1] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def upRightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0 or coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downRightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix) or coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downLeftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix) or coordinates[1] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'
''')

    def replicateGenome(self, newCellName):
        with open('herbivorousMother.py', 'r', encoding='UTF-8') as mother:
            with open(newCellName, 'w', encoding='UTF-8') as newCell:
                for line in mother:
                    if line.startswith('init'):
                        continue
                    newCell.write(line)

    def __init__(self):
        #creates a cell
        name = CellGenome.createCellName(self)
        CellGenome.replicateGenome(self, name)
        CellGenome.createCytoPlasm(self, name)
        CellGenome.createMembrane(self, name)
        CellGenome.createMovingEngine(self, name)
        CellGenome.createLisosome(self, name)
        CellGenome.createGolgiBody(self, name)
        CellGenome.createMitochondrion(self, name)
        CellGenome.createReplicator(self, name)

energyPool = [0]
rawFood = [0]
digestedFood = []
junk = []

def getCoordinates(matrix, body):
    for index, line in enumerate(matrix):
        if body in line:
            y_coord = copy.deepcopy(index)
        
        for index, column in enumerate(line):
            if body == column:
                x_coord = copy.deepcopy(index)

    return (y_coord, x_coord)

def neighbors(matrix, body):
    neighb = {}
    coordinates = getCoordinates(matrix, body)

    directions = ['up', 'upRight', 'right', 'downRight', 'down', 'downLeft', 'left', 'upLeft']

    conditions = [coordinates[0] - 1 < 0, coordinates[0] - 1 < 0 or coordinates[1] + 1 >= len(matrix),
                  coordinates[1] + 1 >= len(matrix), coordinates[0] + 1 >= len(matrix) or coordinates[1] + 1 >= len(matrix),
                  coordinates[0] + 1 >= len(matrix), coordinates[0] + 1 >= len(matrix) or coordinates[1] - 1 < 0,
                  coordinates[1] - 1 < 0, coordinates[0] - 1 < 0 or coordinates[1] - 1 < 0]

    neighbors = [matrix[coordinates[0] - 1][coordinates[1]], matrix[coordinates[0] - 1][coordinates[1] + 1 - len(matrix)], 
                 matrix[coordinates[0]][coordinates[1] + 1 - len(matrix)], matrix[coordinates[0] + 1 - len(matrix)][coordinates[1] + 1 - len(matrix)],
                 matrix[coordinates[0] + 1 - len(matrix)][coordinates[1]], matrix[coordinates[0] + 1 - len(matrix)][coordinates[1] - 1],
                 matrix[coordinates[0]][coordinates[1] - 1], matrix[coordinates[0] - 1][coordinates[1] - 1]]

    for i in range(8):
        if conditions[i]:
            neighb[directions[i]] = 'none'
        else:
            neighb[directions[i]] = neighbors[i]

    rawFood[0] -= 1
    return neighb

def trespassingLogic(item):
    if item == 'j':
        return 'no'
    if item == '_':
        return 'nothing'
    else:
        return 'eat'

def upMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1]] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix):
        raise IndexError('Cant move down! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1]] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'    

def leftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[1] - 1 < 0:
        raise IndexError('Cant move left! It is the end of the world!')

    matrix[coordinates[0]][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def rightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move right! It is the end of the world!')

    matrix[coordinates[0]][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_' 

def upLeftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0 or coordinates[1] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def upRightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] - 1 < 0 or coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] - 1][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downRightMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix) or coordinates[1] + 1 >= len(matrix):
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1] + 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def downLeftMove(matrix, body):
    coordinates = getCoordinates(matrix, body)

    if coordinates[0] + 1 >= len(matrix) or coordinates[1] - 1 < 0:
        raise IndexError('Cant move up! It is the end of the world!')

    matrix[coordinates[0] + 1][coordinates[1] - 1] = body
    energyPool[0] -= 1
    matrix[coordinates[0]][coordinates[1]] = '_'

def disassembleFood(item, parts, junk):
    alph = [

        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
        'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', 
        "'", '"', '[', ']', '=', '+', '-', ':', '(', ')'
    ]
    energyPool[0] -= 0.5

    weights = [76 for x in range(26)] + [3 for x in range(10)] + [20 for x in range(11)]
    jk = ';'
    howManyFood = 40

    if item == 'f':
        parts += choices(alph, weights, k=howManyFood)
    else:
        particles = item.split('/')
        timesFood = int(((int(particles[0][1]) * 100) / (int(particles[0][1]) + int(particles[1][1])) / 100) * howManyFood)
        parts += choices(alph, weights, k=timesFood)
        junk += choices(jk, k=int(particles[1][1]))


def createEnergy(partsList):
    partsList.remove(choice(partsList))
    energyPool[0] += 5

    return partsList
