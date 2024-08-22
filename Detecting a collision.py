# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 01:24:25 2024

@author: hp
"""

def handle_key(event):
    yellow_xy = canvas.bbox(1)
    overlapping = canvas.find_overlapping(
                   yellow_xy[0],yellow_xy[1],yellow_xy[2],yellow_xy[3])
    if 2 in overlapping:
        canvas.create_text(100,100,font=("Arial",20),text="Tag!")