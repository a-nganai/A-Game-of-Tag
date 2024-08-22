# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:11:46 2024

@author: hp
"""

def handle_key(event):
    if event.char == 'w' :
        player1.move("u")
    if event.char == 's' :
        player1.move("d")
    if event.char == 'a' :
        player1.move("l")
    if event.char == 'd' :w
        player1.move("r")
    if event.char == 'i' :
        player2.move("u")
    if event.char == 'k' :
        player2.move("d")
    if event.char == 'j' :
        player2.move("r")
        
window = tkinter.TK()
window.geometry("800x800")
window.title("Tag!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')
player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")
canvas.bind_all('<Key>', handle_key)

        
        
    