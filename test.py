




#  to improve, store entry1,2,3, and entryvalue1,2,3 in dictionaryes and the use them with for loops









import numpy as np 
from time import sleep
import copy
from tkinter import *

#inputValue=window.entry1.get("1.0","end-1c")
#print(inputValue)

def first():

	#inputValuet = int(inputValue1)

	#print(inputValue1)

	sudoku = {
	0 : [int(inputValue1),int(inputValue2),int(inputValue3),int(inputValue4),int(inputValue5),int(inputValue6),int(inputValue7),int(inputValue8),int(inputValue9)],   #,9,6,2,7,3,4,
	1 : [int(inputValue10),int(inputValue11),int(inputValue12),int(inputValue13),int(inputValue14),int(inputValue15),int(inputValue16),int(inputValue17),int(inputValue18)],
	2 : [int(inputValue19),int(inputValue20),int(inputValue21),int(inputValue22),int(inputValue23),int(inputValue24),int(inputValue25),int(inputValue26),int(inputValue27)],
	3 : [int(inputValue28),int(inputValue29),int(inputValue30),int(inputValue31),int(inputValue32),int(inputValue33),int(inputValue34),int(inputValue35),int(inputValue36)],
	4 : [int(inputValue37),int(inputValue38),int(inputValue39),int(inputValue40),int(inputValue41),int(inputValue42),int(inputValue43),int(inputValue44),int(inputValue45)],
	5 : [int(inputValue46),int(inputValue47),int(inputValue48),int(inputValue49),int(inputValue50),int(inputValue51),int(inputValue52),int(inputValue53),int(inputValue54)],
	6 : [int(inputValue55),int(inputValue56),int(inputValue57),int(inputValue58),int(inputValue59),int(inputValue60),int(inputValue61),int(inputValue62),int(inputValue63)],
	7 : [int(inputValue64),int(inputValue65),int(inputValue66),int(inputValue67),int(inputValue68),int(inputValue69),int(inputValue70),int(inputValue71),int(inputValue72)],
	8 : [int(inputValue73),int(inputValue74),int(inputValue75),int(inputValue76),int(inputValue77),int(inputValue78),int(inputValue79),int(inputValue80),int(inputValue81)]
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

	#for key, value in sudokuVert.items():
	#	print(value)




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
        

window = Tk()
window.title('My Window')
window.geometry('187x220')
canvas = Canvas()

entry1 = Text(window, height=1, width=2)
entry1.insert(END, "8")
entry2 = Text(window, height=1, width=2)
entry2.insert(END, "1")
entry3 = Text(window, height=1, width=2)
entry3.insert(END, "5")
entry4 = Text(window, height=1, width=2)
entry4.insert(END, "9")
entry5 = Text(window, height=1, width=2)
entry5.insert(END, "6")
entry6 = Text(window, height=1, width=2)
entry6.insert(END, "2")
entry7 = Text(window, height=1, width=2)
entry7.insert(END, "7")
entry8 = Text(window, height=1, width=2)
entry8.insert(END, "3")
entry9 = Text(window, height=1, width=2)
entry9.insert(END, "4")

entry10 = Text(window, height=1, width=2)
entry10.insert(END, "7")
entry11 = Text(window, height=1, width=2)
entry11.insert(END, "2")
entry12 = Text(window, height=1, width=2)
entry12.insert(END, "4")
entry13 = Text(window, height=1, width=2)
entry13.insert(END, "3")
entry14 = Text(window, height=1, width=2)
entry14.insert(END, "8")
entry15 = Text(window, height=1, width=2)
entry15.insert(END, "5")
entry16 = Text(window, height=1, width=2)
entry16.insert(END, "1")
entry17 = Text(window, height=1, width=2)
entry17.insert(END, "9")
entry18 = Text(window, height=1, width=2)
entry18.insert(END, "6")

entry19 = Text(window, height=1, width=2)
entry19.insert(END, "6")
entry20 = Text(window, height=1, width=2)
entry20.insert(END, "9")
entry21 = Text(window, height=1, width=2)
entry21.insert(END, "3")
entry22 = Text(window, height=1, width=2)
entry22.insert(END, "4")
entry23 = Text(window, height=1, width=2)
entry23.insert(END, "1")
entry24 = Text(window, height=1, width=2)
entry24.insert(END, "7")
entry25 = Text(window, height=1, width=2)
entry25.insert(END, "8")
entry26 = Text(window, height=1, width=2)
entry26.insert(END, "5")
entry27 = Text(window, height=1, width=2)
entry27.insert(END, "2")

entry28 = Text(window, height=1, width=2)
entry28.insert(END, "4")
entry29 = Text(window, height=1, width=2)
entry29.insert(END, "3")
entry30 = Text(window, height=1, width=2)
entry30.insert(END, "8")
entry31 = Text(window, height=1, width=2)
entry31.insert(END, "5")
entry32 = Text(window, height=1, width=2)
entry32.insert(END, "7")
entry33 = Text(window, height=1, width=2)
entry33.insert(END, "1")
entry34 = Text(window, height=1, width=2)
entry34.insert(END, "6")
entry35 = Text(window, height=1, width=2)
entry35.insert(END, "2")
entry36 = Text(window, height=1, width=2)
entry36.insert(END, "9")

entry37 = Text(window, height=1, width=2)
entry37.insert(END, "9")
entry38 = Text(window, height=1, width=2)
entry38.insert(END, "5")
entry39 = Text(window, height=1, width=2)
entry39.insert(END, "2")
entry40 = Text(window, height=1, width=2)
entry40.insert(END, "8")
entry41 = Text(window, height=1, width=2)
entry41.insert(END, "3")
entry42 = Text(window, height=1, width=2)
entry42.insert(END, "6")
entry43 = Text(window, height=1, width=2)
entry43.insert(END, "4")
entry44 = Text(window, height=1, width=2)
entry44.insert(END, "7")
entry45 = Text(window, height=1, width=2)
entry45.insert(END, "1")

entry46 = Text(window, height=1, width=2)
entry46.insert(END, "1")
entry47 = Text(window, height=1, width=2)
entry47.insert(END, "7")
entry48 = Text(window, height=1, width=2)
entry48.insert(END, "6")
entry49 = Text(window, height=1, width=2)
entry49.insert(END, "2")
entry50 = Text(window, height=1, width=2)
entry50.insert(END, "4")
entry51 = Text(window, height=1, width=2)
entry51.insert(END, "9")
entry52 = Text(window, height=1, width=2)
entry52.insert(END, "3")
entry53 = Text(window, height=1, width=2)
entry53.insert(END, "8")
entry54 = Text(window, height=1, width=2)
entry54.insert(END, "5")

entry55 = Text(window, height=1, width=2)
entry55.insert(END, "3")
entry56 = Text(window, height=1, width=2)
entry56.insert(END, "6")
entry57 = Text(window, height=1, width=2)
entry57.insert(END, "9")
entry58 = Text(window, height=1, width=2)
entry58.insert(END, "1")
entry59 = Text(window, height=1, width=2)
entry59.insert(END, "5")
entry60 = Text(window, height=1, width=2)
entry60.insert(END, "8")
entry61 = Text(window, height=1, width=2)
entry61.insert(END, "2")
entry62 = Text(window, height=1, width=2)
entry62.insert(END, "4")
entry63 = Text(window, height=1, width=2)
entry63.insert(END, "7")

entry64 = Text(window, height=1, width=2)
entry64.insert(END, "2")
entry65 = Text(window, height=1, width=2)
entry65.insert(END, "4")
entry66 = Text(window, height=1, width=2)
entry66.insert(END, "7")
entry67 = Text(window, height=1, width=2)
entry67.insert(END, "6")
entry68 = Text(window, height=1, width=2)
entry68.insert(END, "9")
entry69 = Text(window, height=1, width=2)
entry69.insert(END, "3")
entry70 = Text(window, height=1, width=2)
entry70.insert(END, "5")
entry71 = Text(window, height=1, width=2)
entry71.insert(END, "1")
entry72 = Text(window, height=1, width=2)
entry72.insert(END, "8")

entry73 = Text(window, height=1, width=2)
entry73.insert(END, "5")
entry74 = Text(window, height=1, width=2)
entry74.insert(END, "8")
entry75 = Text(window, height=1, width=2)
entry75.insert(END, "1")
entry76 = Text(window, height=1, width=2)
entry76.insert(END, "7")
entry77 = Text(window, height=1, width=2)
entry77.insert(END, "2")
entry78 = Text(window, height=1, width=2)
entry78.insert(END, "4")
entry79 = Text(window, height=1, width=2)
entry79.insert(END, "9")
entry80 = Text(window, height=1, width=2)
entry80.insert(END, "6")
entry81 = Text(window, height=1, width=2)
entry81.insert(END, "3")


entry1.pack()
entry1.place(x=1, y=1, in_= window)
entry2.pack()
entry2.place(x=21, y=1, in_= window)
entry3.pack()
entry3.place(x=41, y=1, in_= window)
entry4.pack()
entry4.place(x=64, y=1, in_= window)
entry5.pack()
entry5.place(x=84, y=1, in_= window)
entry6.pack()
entry6.place(x=104, y=1, in_= window)
entry7.pack()
entry7.place(x=127, y=1, in_= window)
entry8.pack()
entry8.place(x=147, y=1, in_= window)
entry9.pack()
entry9.place(x=167, y=1, in_= window)

entry10.pack()
entry10.place(x=1, y=21, in_= window)
entry11.pack()
entry11.place(x=21, y=21, in_= window)
entry12.pack()
entry12.place(x=41, y=21, in_= window)
entry13.pack()
entry13.place(x=64, y=21, in_= window)
entry14.pack()
entry14.place(x=84, y=21, in_= window)
entry15.pack()
entry15.place(x=104, y=21, in_= window)
entry16.pack()
entry16.place(x=127, y=21, in_= window)
entry17.pack()
entry17.place(x=147, y=21, in_= window)
entry18.pack()
entry18.place(x=167, y=21, in_= window)

entry19.pack()
entry19.place(x=1, y=41, in_= window)
entry20.pack()
entry20.place(x=21, y=41, in_= window)
entry21.pack()
entry21.place(x=41, y=41, in_= window)
entry22.pack()
entry22.place(x=64, y=41, in_= window)
entry23.pack()
entry23.place(x=84, y=41, in_= window)
entry24.pack()
entry24.place(x=104, y=41, in_= window)
entry25.pack()
entry25.place(x=127, y=41, in_= window)
entry26.pack()
entry26.place(x=147, y=41, in_= window)
entry27.pack()
entry27.place(x=167, y=41, in_= window)

entry28.pack()
entry28.place(x=1, y=64, in_= window)
entry29.pack()
entry29.place(x=21, y=64, in_= window)
entry30.pack()
entry30.place(x=41, y=64, in_= window)
entry31.pack()
entry31.place(x=64, y=64, in_= window)
entry32.pack()
entry32.place(x=84, y=64, in_= window)
entry33.pack()
entry33.place(x=104, y=64, in_= window)
entry34.pack()
entry34.place(x=127, y=64, in_= window)
entry35.pack()
entry35.place(x=147, y=64, in_= window)
entry36.pack()
entry36.place(x=167, y=64, in_= window)

entry37.pack()
entry37.place(x=1, y=84, in_= window)
entry38.pack()
entry38.place(x=21, y=84, in_= window)
entry39.pack()
entry39.place(x=41, y=84, in_= window)
entry40.pack()
entry40.place(x=64, y=84, in_= window)
entry41.pack()
entry41.place(x=84, y=84, in_= window)
entry42.pack()
entry42.place(x=104, y=84, in_= window)
entry43.pack()
entry43.place(x=127, y=84, in_= window)
entry44.pack()
entry44.place(x=147, y=84, in_= window)
entry45.pack()
entry45.place(x=167, y=84, in_= window)

entry46.pack()
entry46.place(x=1, y=104, in_= window)
entry47.pack()
entry47.place(x=21, y=104, in_= window)
entry48.pack()
entry48.place(x=41, y=104, in_= window)
entry49.pack()
entry49.place(x=64, y=104, in_= window)
entry50.pack()
entry50.place(x=84, y=104, in_= window)
entry51.pack()
entry51.place(x=104, y=104, in_= window)
entry52.pack()
entry52.place(x=127, y=104, in_= window)
entry53.pack()
entry53.place(x=147, y=104, in_= window)
entry54.pack()
entry54.place(x=167, y=104, in_= window)

entry55.pack()
entry55.place(x=1, y=127, in_= window)
entry56.pack()
entry56.place(x=21, y=127, in_= window)
entry57.pack()
entry57.place(x=41, y=127, in_= window)
entry58.pack()
entry58.place(x=64, y=127, in_= window)
entry59.pack()
entry59.place(x=84, y=127, in_= window)
entry60.pack()
entry60.place(x=104, y=127, in_= window)
entry61.pack()
entry61.place(x=127, y=127, in_= window)
entry62.pack()
entry62.place(x=147, y=127, in_= window)
entry63.pack()
entry63.place(x=167, y=127, in_= window)

entry64.pack()
entry64.place(x=1, y=147, in_= window)
entry65.pack()
entry65.place(x=21, y=147, in_= window)
entry66.pack()
entry66.place(x=41, y=147, in_= window)
entry67.pack()
entry67.place(x=64, y=147, in_= window)
entry68.pack()
entry68.place(x=84, y=147, in_= window)
entry69.pack()
entry69.place(x=104, y=147, in_= window)
entry70.pack()
entry70.place(x=127, y=147, in_= window)
entry71.pack()
entry71.place(x=147, y=147, in_= window)
entry72.pack()
entry72.place(x=167, y=147, in_= window)

entry73.pack()
entry73.place(x=1, y=167, in_= window)
entry74.pack()
entry74.place(x=21, y=167, in_= window)
entry75.pack()
entry75.place(x=41, y=167, in_= window)
entry76.pack()
entry76.place(x=64, y=167, in_= window)
entry77.pack()
entry77.place(x=84, y=167, in_= window)
entry78.pack()
entry78.place(x=104, y=167, in_= window)
entry79.pack()
entry79.place(x=127, y=167, in_= window)
entry80.pack()
entry80.place(x=147, y=167, in_= window)
entry81.pack()
entry81.place(x=167, y=167, in_= window)

canvas.pack()
canvas.place(x=0, y=0, in_= window)
canvas.create_rectangle(1, 1, 187, 187, )
canvas.create_rectangle(1, 1, 62, 187, )
canvas.create_rectangle(1, 1, 187, 62, )
canvas.create_rectangle(1, 1, 125, 187, )
canvas.create_rectangle(1, 1, 187, 125, )

array = [
entry1,
entry2,
entry3,
entry4,
entry5,
entry6,
entry7,
entry8,
entry9,
entry10,
entry11,
entry12,
entry13,
entry14,
entry15,
entry16,
entry17,
entry18,
entry19,
entry20,
entry21,
entry22,
entry23,
entry24,
entry25,
entry26,
entry27,
entry28,
entry29,
entry30,
entry31,
entry32,
entry33,
entry34,
entry35,
entry36,
entry37,
entry38,
entry39,
entry40,
entry41,
entry42,
entry43,
entry44,
entry45,
entry46,
entry47,
entry48,
entry49,
entry40,
entry41,
entry42,
entry43,
entry44,
entry45,
entry46,
entry47,
entry48,
entry49,
entry50,
entry51,
entry52,
entry53,
entry54,
entry55,
entry56,
entry57,
entry58,
entry59,
entry60,
entry61,
entry62,
entry63,
entry64,
entry65,
entry66,
entry67,
entry68,
entry69,
entry70,
entry71,
entry72,
entry73,
entry74,
entry75,
entry76,
entry77,
entry78,
entry79,
entry70,
entry71,
entry72,
entry73,
entry74,
entry75,
entry76,
entry77,
entry78,
entry79,
entry80,
entry81
 ]

def calc():
	global inputValue1
	global inputValue2
	global inputValue3
	global inputValue4
	global inputValue5
	global inputValue6
	global inputValue7
	global inputValue8
	global inputValue9
	global inputValue10
	global inputValue11
	global inputValue12
	global inputValue13
	global inputValue14
	global inputValue15
	global inputValue16
	global inputValue17
	global inputValue18
	global inputValue19
	global inputValue20
	global inputValue21
	global inputValue22
	global inputValue23
	global inputValue24
	global inputValue25
	global inputValue26
	global inputValue27
	global inputValue28
	global inputValue29
	global inputValue30
	global inputValue31
	global inputValue32
	global inputValue33
	global inputValue34
	global inputValue35
	global inputValue36
	global inputValue37
	global inputValue38
	global inputValue39
	global inputValue40
	global inputValue41
	global inputValue42
	global inputValue43
	global inputValue44
	global inputValue45
	global inputValue46
	global inputValue47
	global inputValue48
	global inputValue49
	global inputValue50
	global inputValue51
	global inputValue52
	global inputValue53
	global inputValue54
	global inputValue55
	global inputValue56
	global inputValue57
	global inputValue58
	global inputValue59
	global inputValue60
	global inputValue61
	global inputValue62
	global inputValue63
	global inputValue64
	global inputValue65
	global inputValue66
	global inputValue67
	global inputValue68
	global inputValue69
	global inputValue70
	global inputValue71
	global inputValue72
	global inputValue73
	global inputValue74
	global inputValue75
	global inputValue76
	global inputValue77
	global inputValue78
	global inputValue79
	global inputValue80
	global inputValue81
	inputValue1=entry1.get("1.0","end-1c")
	inputValue2=entry2.get("1.0","end-1c")
	inputValue3=entry3.get("1.0","end-1c")
	inputValue4=entry4.get("1.0","end-1c")
	inputValue5=entry5.get("1.0","end-1c")
	inputValue6=entry6.get("1.0","end-1c")
	inputValue7=entry7.get("1.0","end-1c")
	inputValue8=entry8.get("1.0","end-1c")
	inputValue9=entry9.get("1.0","end-1c")

	inputValue10=entry10.get("1.0","end-1c")
	inputValue11=entry11.get("1.0","end-1c")
	inputValue12=entry12.get("1.0","end-1c")
	inputValue13=entry13.get("1.0","end-1c")
	inputValue14=entry14.get("1.0","end-1c")
	inputValue15=entry15.get("1.0","end-1c")
	inputValue16=entry16.get("1.0","end-1c")
	inputValue17=entry17.get("1.0","end-1c")
	inputValue18=entry18.get("1.0","end-1c")

	inputValue19=entry19.get("1.0","end-1c")
	inputValue20=entry20.get("1.0","end-1c")
	inputValue21=entry21.get("1.0","end-1c")
	inputValue22=entry22.get("1.0","end-1c")
	inputValue23=entry23.get("1.0","end-1c")
	inputValue24=entry24.get("1.0","end-1c")
	inputValue25=entry25.get("1.0","end-1c")
	inputValue26=entry26.get("1.0","end-1c")
	inputValue27=entry27.get("1.0","end-1c")

	inputValue28=entry28.get("1.0","end-1c")
	inputValue29=entry29.get("1.0","end-1c")
	inputValue30=entry30.get("1.0","end-1c")
	inputValue31=entry31.get("1.0","end-1c")
	inputValue32=entry32.get("1.0","end-1c")
	inputValue33=entry33.get("1.0","end-1c")
	inputValue34=entry34.get("1.0","end-1c")
	inputValue35=entry35.get("1.0","end-1c")
	inputValue36=entry36.get("1.0","end-1c")

	inputValue37=entry37.get("1.0","end-1c")
	inputValue38=entry38.get("1.0","end-1c")
	inputValue39=entry39.get("1.0","end-1c")
	inputValue40=entry40.get("1.0","end-1c")
	inputValue41=entry41.get("1.0","end-1c")
	inputValue42=entry42.get("1.0","end-1c")
	inputValue43=entry43.get("1.0","end-1c")
	inputValue44=entry44.get("1.0","end-1c")
	inputValue45=entry45.get("1.0","end-1c")

	inputValue46=entry46.get("1.0","end-1c")
	inputValue47=entry47.get("1.0","end-1c")
	inputValue48=entry48.get("1.0","end-1c")
	inputValue49=entry49.get("1.0","end-1c")
	inputValue50=entry50.get("1.0","end-1c")
	inputValue51=entry51.get("1.0","end-1c")
	inputValue52=entry52.get("1.0","end-1c")
	inputValue53=entry53.get("1.0","end-1c")
	inputValue54=entry54.get("1.0","end-1c")

	inputValue55=entry55.get("1.0","end-1c")
	inputValue56=entry56.get("1.0","end-1c")
	inputValue57=entry57.get("1.0","end-1c")
	inputValue58=entry58.get("1.0","end-1c")
	inputValue59=entry59.get("1.0","end-1c")
	inputValue60=entry60.get("1.0","end-1c")
	inputValue61=entry61.get("1.0","end-1c")
	inputValue62=entry62.get("1.0","end-1c")
	inputValue63=entry63.get("1.0","end-1c")

	inputValue64=entry64.get("1.0","end-1c")
	inputValue65=entry65.get("1.0","end-1c")
	inputValue66=entry66.get("1.0","end-1c")
	inputValue67=entry67.get("1.0","end-1c")
	inputValue68=entry68.get("1.0","end-1c")
	inputValue69=entry69.get("1.0","end-1c")
	inputValue70=entry60.get("1.0","end-1c")
	inputValue71=entry71.get("1.0","end-1c")
	inputValue72=entry72.get("1.0","end-1c")

	inputValue73=entry73.get("1.0","end-1c")
	inputValue74=entry74.get("1.0","end-1c")
	inputValue75=entry75.get("1.0","end-1c")
	inputValue76=entry76.get("1.0","end-1c")
	inputValue77=entry77.get("1.0","end-1c")
	inputValue78=entry78.get("1.0","end-1c")
	inputValue79=entry79.get("1.0","end-1c")
	inputValue80=entry80.get("1.0","end-1c")
	inputValue81=entry81.get("1.0","end-1c")
	first()

def retrieve_input():
	for value in array:
		inputValue=value.get("1.0", "end-1c")
		print(inputValue)

button1 = Button(window, text="calc", command=calc)
button1.pack()
button1.place(x=75, y=190	, in_=window)

#inputValue=entry1.get("1.0","end-1c")
#print("inputValue")

window.mainloop()

