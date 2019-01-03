import numpy as np 
from time import sleep
import copy

sudoku = [
[8,-1,-1,-1,-1,-1,-1,-1,-1],   #,9,6,2,7,3,4,
[7,2,4,3,8,5,-1,9,6],
[6,9,3,4,1,7,8,5,2],
[4,3,8,5,7,-1,6,2,9],
[9,5,2,8,3,6,4,7,-1],
[1,7,6,2,4,9,3,8,5],
[3,6,9,-1,5,8,2,4,7],
[2,4,7,6,9,3,5,-1,8],
[5,8,-1,7,2,4,9,6,3]
]
sudokuT = copy.deepcopy(sudoku)
sudokuT = dict(enumerate(sudokuT))

#numpy sudoku
sudokuNp = np.array(sudoku)

#squares of sudoku, dictionary

sudokuSquare = [
list(sudokuNp[0:3,0:3].flatten()),
list(sudokuNp[0:3,3:6].flatten()),
list(sudokuNp[0:3,6:9].flatten()),
list(sudokuNp[3:6,0:3].flatten()),
list(sudokuNp[3:6,3:6].flatten()),
list(sudokuNp[3:6,6:9].flatten()),
list(sudokuNp[6:9,0:3].flatten()),
list(sudokuNp[6:9,3:6].flatten()),
list(sudokuNp[6:9,6:9].flatten()),
]


#testo = sudokuNp[0:3,0:3].flatten(),

#testio = testo[0]
#print(testio)

sudokuSquare = dict(enumerate(sudokuSquare))
#for key, value in sudokuSquare.items():
#	print(key, value)


sudokuSquareT = copy.deepcopy(sudokuSquare)







#vertical lines of sudoku
sudokuVert = list(zip(*sudokuNp))
sudokuVert = dict(enumerate(sudokuVert))
#print(sudokuVert)

for x in range(0, 9):
	toAppend = list(sudokuVert[x])
	sudokuVert[x] = toAppend




sudokuVertT = copy.deepcopy(sudokuVert)
#print(sudokuVert)
#print(sudokuT)


#print(sudokuT)
#for key, value in sudokuT.items():
	#print(key, value)

#delete empty spaces from sudoku to see which one is the shortest
a = 0
b = 0
length = 0

for x in range(0, 8):
	while b < 9:
		try:
			sudokuT[b].remove(-1)
			
		except (ValueError, IndexError) as e:
			
			b += 1
			pass
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


#find sudoku line with most filled in squares
l = []
for k in sorted(dictionary, key=lambda k: len(dictionary[k]), reverse=True):       # todo: create var with value being dict key of longest row (of l)
	l.append(k)
	#print(k)

lowest = l[0]

print("horizontal line to fill in first is:")
print(sudoku[lowest])





   

#                        vertical






a = 0
b = 0
length = 0
#print(sudokuVertT)
#print(sudokuVert)
for x in range(0, 8):
	while b < 9:
		try:
			sudokuVertT[b].remove(-1)
			
		except (ValueError, IndexError) as e:
			
			b += 1
			pass
	try:
		length = len(sudokuVertT[a])
		if length > 8:
			#sudokuT[a].clear()
			del sudokuVertT[a]
			
		else:
			a += 1

	except (KeyError, IndexError) as e:
		a += 1

#print(sudokuT)
#print(sudoku)
dictionaryVert = sudokuVertT


#find sudoku line with most filled in squares
l = []
for k in sorted(dictionaryVert, key=lambda k: len(dictionaryVert[k]), reverse=True):
	l.append(k)
	#print(k)
#print(sudokuT)
#for key, value in sudokuT.items():
#	print(key, value)

#prints value longest row
#maxLine = max(sudokuT, key=len)
#print(maxLine)


#prints key of longest row
lowest = l[0]

print("vertical line to fill in first is:")
print(sudokuVert[lowest])









#                 areas





#print(sudokuSquaresT)

#for value in sudokuSquaresT.items():
#	print(value)




a = 0
b = 0
length = 0
for x in range(0, 8):
	while b < 9:
		try:
			sudokuSquareT[b].remove(-1)
			
		except (ValueError, IndexError) as e:
			
			b += 1
			pass
	try:
		length = len(sudokuSquareT[a])
		if length > 8:
			#sudokuT[a].clear()
			del sudokuSquareT[a]
			
		else:
			a += 1

	except (KeyError, IndexError) as e:
		a += 1



dictionarySquare = sudokuSquareT


#find sudoku line with most filled in squares
l = []
for k in sorted(dictionarySquare, key=lambda k: len(dictionarySquare[k]), reverse=True):
	l.append(k)
	
#for key, value in sudokuSquareT.items():
#	print(key, value)

#prints value longest row
#maxLine = max(sudokuT, key=len)
#print(maxLine)


#prints key of longest row
lowest = l[0]


print("square to fill in first is:")
print(sudokuSquare[lowest])