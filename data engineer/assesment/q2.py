from collections import Counter

animals = ['dog', 'cat', 'cat', 'cat', 'dog', 'dog', 'mouse', 'mouse', 'dog']

def ContainsMouse(data):
    if 'mouse' in data.keys():
        return True
    return False

def CountObject():
    global animals
    counts = Counter(animals)

    return counts

counter = CountObject()  #{'dog': 4, 'cat': 3, 'mouse': 2}
ContainsMouse(counter) #True