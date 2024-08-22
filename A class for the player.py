# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:39:12 2024

@author: hp
"""

import random
class Player(object):
    def __init__(self, canvas, color):
        self.color = color
        size = random.randint(1,100)
        x1 = random.randint(100,700)
        y1 = random.randint(100,700)
        x2 = x1+size
        y2 = y1+size
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords)
        canvas.itemconfig(self.piece, fill=color)
        
