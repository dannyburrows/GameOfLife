#Conway's game of life
#
#Rules:
#-Any live cell with < 2 neighbors, dies
#-Any live cell with 2 or 3 neighbors lives to next generation
#-Any live cell with > 3 neighbors, dies
#-Any dead cell with = 3 neighbors, becomes live
 
#Get initially alive cells
#Display starting conditions
#Run game
#-Test each cell to determine all 8 neighbors
#-Cell board is array, then from beg to end, check all +- 1 positions
#    -Count how many are alive
#    -Increase count for alive
#    -Return count after all neighbors are checked
#-Determine outcome of cell based on neighbors
#-Change Array (be careful, changing the same array will change of surrounding cells) # 2 arrays, old and new?
#-Pass new array into the main loop

from random import randint
import os, time, copy
import pygame

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

width = 20
height = 20

margin = 5


pygame.init()

size = [630,630]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Conway's Game of Life")

done = False
clock = pygame.time.Clock()

# check for the number of neighbors
def neighbors(x, y, board_to_test):
	
	neighbors = 0
	test = [-1, 0, 1]
	
#this should loop through the board, testing each spot at -1, 0, 1 but kicking out for a cell with an index below 0 or above 5.	
	for i in test:
		for j in test:
			if (i == 0) and (j == 0):
				pass
			elif ((y + j) < 0) or ((y + j) > (25 - 1)):
				pass
			elif ((x + i) < 0) or ((x + i) > (25 - 1)):
				pass
			elif board_to_test[x + i][y + j] == 1:
				neighbors += 1
			else:
				pass
				
	return neighbors
	

#check lives so we can work on the next generation
def evolve(current_gen):
	next_gen = copy.deepcopy(current_gen)
	
	#loop through the list using rows and columns
	for row in range(len(current_gen)):
		for col in range(len(next_gen[row])):
			num_neighbors = neighbors(row, col, current_gen)
		
			#actual test to determine live or die of each cell, based off of neighbors
			if (num_neighbors == 2) and (current_gen[row][col] == 1):
				next_gen[row][col] = 1
			elif num_neighbors == 3:
				next_gen[row][col] = 1
			elif num_neighbors < 2:
				next_gen[row][col] = 0
			else:
				next_gen[row][col] = 0

	#print the next generation
	print_board(next_gen)
	
	return next_gen
	
def print_board(board):	
	for row in range(25):
		for column in range(25):
			color = white
			if board[row][column] == 1:
				color = green
			pygame.draw.rect(screen, color, [(margin+width)*column+margin,(margin+height)*row+margin,width,height])
			
	clock.tick(20)
	
	pygame.display.flip()

current_gen = []

for row in range(25):
	current_gen.append([])
	for column in range(25):
		current_gen[row].append(0)

#print first generation
print_board(current_gen)
done = False

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
		
			column = pos[0] // (width + margin)
			row = pos[1] // (height + margin)
		
			if current_gen[row][column] == 0:
				current_gen[row][column] = 1
			else:
				current_gen[row][column] = 0
				
		if event.type == pygame.KEYDOWN:
			current_gen = evolve(current_gen)
	
	print_board(current_gen)
	clock.tick(40)
	