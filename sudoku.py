import numpy as np 
from time import sleep
import copy
from window import *
#inputValue=window.entry1.get("1.0","end-1c")
#print(inputValue)

def first():
	#print(inputValue)

	inputValue1 = int(inputValue)

	print(inputValue1)

	sudoku = {
	0 : [inputValue1,0,5,9,6,2,7,3,4],   #,9,6,2,7,3,4,
	1 : [7,2,4,3,8,5,1,9,6],
	2 : [6,9,3,4,1,7,8,5,2],
	3 : [4,3,8,5,7,1,6,2,9],
	4 : [9,5,2,8,3,6,4,7,1],
	5 : [1,7,6,2,4,9,3,8,5],
	6 : [3,6,9,1,5,8,2,4,7],
	7 : [2,4,7,6,9,3,5,1,8],
	8 : [5,8,1,7,2,4,9,6,3]
	}

	sudokuC = copy.deepcopy(sudoku)
	sudokuT = []
	for key, value in sudokuC.items():
	    sudokuT.append(value)




	# sudoku vertical

	sudokuNp = np.array(sudokuT)
	sudokuVertT = list(zip(*sudokuNp))

	for x in range(0, 9):
		toAppend = list(sudokuVertT[x])
		sudokuVertT[x] = toAppend

	sudokuVert = copy.deepcopy(sudokuVertT)
	sudokuVert = dict(enumerate(sudokuVert, 9))

	for key, value in sudokuVert.items():
		print(value)




	# sudoku sqaures

	sudokuSquare = {
	18 : sudokuNp[0:3,0:3],
	19 : sudokuNp[0:3,3:6],
	20 : sudokuNp[0:3,6:9],
	21 : sudokuNp[3:6,0:3],
	22 : sudokuNp[3:6,3:6],
	23 : sudokuNp[3:6,6:9],
	24 : sudokuNp[6:9,0:3],
	25 : sudokuNp[6:9,3:6],
	26 : sudokuNp[6:9,6:9],
	}

	sudokuSquareT = []
	for key, value in sudokuSquare.items():
	    sudokuSquareT.append(list(value.flatten()))

	for x in range(0, len(sudokuVertT)):
		sudokuT.append(sudokuVertT[x])

	for x in range(0, len(sudokuSquareT)):
		sudokuT.append(sudokuSquareT[x])

	sudokuT = dict(enumerate(sudokuT))


	#for key, value in sudokuT.items():
	#	print(key, value)


	a = 0
	b = 0
	length = 0

	#print(sudokuT)

	while b < 27:
			try:
				sudokuT[b].remove(0)
				
			except (ValueError, IndexError) as e:
				
				b += 1
				pass

	for x in range(0, 100):

		try:
			length = len(sudokuT[a])
			if length > 8:
				#sudokuT[a].clear()
				del sudokuT[a]
				
			else:
				a += 1

		except (KeyError, IndexError) as e:
			a += 1
			

	#print(sudokuT)
	#print(sudoku)
	dictionary = sudokuT

	print(sudokuT)
	#find sudoku line with most filled in squares
	l = []
	for k in sorted(dictionary, key=lambda k: len(dictionary[k]), reverse=False):       
		l.append(k)
		#print(k)

	lowest = l[0]
	print(l)


	print("sudoku:")
	for key, value in sudoku.items():
		print(value)

	print("what to fill in first:")
	if lowest < 9:
		print(sudoku[lowest])
	elif lowest > 17:
		print(sudokuSquare[lowest])
	else:
		print(sudokuVert[lowest])