# File:           wonly047.py
# Author:         Liang Xing Wong
# Student ID:     110240156
# Email ID:       wonly047
# Description:    Assignment 1 - Tic Tac Toe
# Version:        1.53 - Removed global variable
# This is my own work as defined by the University's
# Academic Misconduct policy.

import tic_tac_toe_gui
import tkinter
import random

def display_details():
	print('''File:           wonly047.py
Author:         Liang Xing Wong
Student ID:     110240156
Email ID:       wonly047
This is my own work as defined by the University's
Academic Misconduct policy.''')

def check_win(slots, letter):
	# Win conditions
	win_0 = [0, 1, 2]
	win_1 = [3, 4, 5]
	win_2 = [6, 7, 8]
	win_3 = [0, 3, 6]
	win_4 = [1, 4, 7]
	win_5 = [2, 5, 8]
	win_6 = [0, 4, 8]
	win_7 = [2, 4, 6]
	for i in range(8):
		slots_str = ""
		# Concentrate "slots" strings
		for j in range(3):
			slots_str += slots[vars()["win_" + str(i)][j]]
		if slots_str == letter * 3:
			# Found
			return True
	# Missing
	return False

def display_game(slots):
	# Paddings
	for i in range(9):
		if slots[i] == "":
			slots[i] = " "
	print(slots[0], "|", slots[1], "|", slots[2])
	print(slots[3], "|", slots[4], "|", slots[5])
	print(slots[6], "|", slots[7], "|", slots[8])

def end_game():
	print("\n" + " END GAME ".center(55, "-") + "\n")
	print("That was fun!\n")
	# End game "play again" prompt
	playing = ""
	while playing != "n" and playing != "y":
		playing = input("Play again? [y/n] ")
		print("")
	# "Play again" clean-up
	if playing == "y":
		print("\n" + " START GAME ".center(55, "-") + "\n")
		# Player first
		ttt.player_turn = True
	else:
		# Game stats
		print("\nYou played", games_count, "games!")
		print(" -> Won:   ", ttt.get_wins())
		print(" -> Lost:  ", ttt.get_losses())
		print(" -> Drawn: ", draws_count, "\n")
		# Thanks and details MSG
		print("Thanks for playing! :)\n")
		display_details()
	return playing

def move_computer():
	# Computer moves marker (list) and a switch (boolean)
	computer_move = []
	computer_moved = False
	slots = list(ttt.slots)
	slots_order = list(range(9))
	# 1. Winning move
	for i in slots_order:
		# "Slots" shadow copy tester
		slots_shadow = list(slots)
		# Mark current iteration if blank
		if slots_shadow[i] == "":
			slots_shadow[i] = "O"
			# Does shadow have an "OOO" now?
			if check_win(slots_shadow, "O"):
				computer_move.append(i)
				# Flip switch
				computer_moved = True
	# 2. Blocking move (99% = 1.)
	# Skip when another method has been executed
	if computer_moved == False:
		for i in slots_order:
			slots_shadow = list(slots)
			if slots_shadow[i] == "":
				slots_shadow[i] = "X"
				if check_win(slots_shadow, "X"):
					computer_move.append(i)
					computer_moved = True
	# 3. Cornering move
	if computer_moved == False:
		corners = [0, 2, 6, 8]
		# Randomize order
		random.shuffle(corners)
		for i in corners:
			# Fill blanks
			if slots[i] == "":
				computer_move.append(i)
				computer_moved = True
	# 4. Centering move
	if computer_moved == False and slots[4] == "":
			computer_move.append(4)
			computer_moved = True
	# 5. Filling move
	if computer_moved == False:
		# Randomize order
		random.shuffle(slots_order)
		for i in slots_order:
			# Fill blanks
			if slots[i] == "":
				computer_move.append(i)
				computer_moved = True
	# Marker's first value (int) -> ttt.move_computer()
	ttt.move_computer(computer_move[0])

# Init games & draws counters
games_count = 0
draws_count = 0
display_details()
print("")
# Play prompt
# y or n (case sensitive)
playing = ""
while playing != "n" and playing != "y":
	playing = input("Would you like to play Tic Tac Toe? [y/n] ")

# "n" = skip
if playing == "y":
	# Name prompt
	name = input("Please enter your name: ")
	# Init GUI
	ttt = tic_tac_toe_gui.TicTacToeGUI(name)
	print("\n" + " START GAME ".center(55, "-") + "\n")
	# Player first
	ttt.player_turn = True

# MAIN LOOP
while playing == "y":
	slots = list(ttt.slots)
	# Player loss, counters update
	if check_win(slots, "O"):
		print("--- Computer wins! ---\n")
		display_game(slots)
		games_count += 1
		ttt.increment_losses()
		playing = end_game()
	# Player win, counters update
	elif check_win(slots, "X"):
		print("--- Player wins! ---\n")
		display_game(slots)
		games_count += 1
		ttt.increment_wins()
		playing = end_game()
	else:
		# Count moves left
		moves_left = 0
		for i in range(9):
			if slots[i] == "":
				moves_left += 1
		# No moves left && no win/loss
		if moves_left == 0:
			print("--- Draw! ---\n")
			display_game(slots)
			games_count += 1
			draws_count += 1
			ttt.draw()
			playing = end_game()
	# AI waits for its turn
	if ttt.player_turn == False:
		move_computer()
	# GUI REFRESH --- DO NOT TOUCH ---
	try:
		ttt.main_window.update()
	except (tkinter.TclError, KeyboardInterrupt):
		quit(0)
