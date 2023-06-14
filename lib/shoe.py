#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = 0):
        self.brand  = brand
        self.size = size
        self.condition = ''

    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            return print("size must be an integer")
        
    def cobble(self):
        self.condition = 'New'
        return print('Your shoe is as good as new!')
    
    # def condition(self):
    #     return print('New!')