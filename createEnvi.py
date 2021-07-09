from random import randint, choice, choices

def createMatrix(x):
    '''Creates matrix with x columns and rows, that contains: 'j' - junk, 'f' - food, 'f5/j2' - mix of junk and food, '_' - empty space.
       Args: y - int, x - int.
       Returns: 2D array.
    '''
    return [choices(['f', 'j', '_', f'f{randint(0, 5)}/j{randint(0, 5)}'], weights=[15, 15, 30, 40], k=x) for _ in range(x)]
