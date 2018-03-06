""""

from math import pi
print(pi)

from math import sin
x = sin (1)
print(x)

print("Jedna plus dva je", 1 + 2)

print('1 + 2', end=' ')
print('=', end=' ')
print(1 + 2, end='!')
print()

print(1, "dvě", False)
print(1, end=" ")
print(2, 3, 4, sep=", ")

3 == int('3') == int(3.0) == int(3.141) == int(3)
8.12 == float('8.12') == float(8.12)
8.0 == float(8) == float('8') == float(8.0)
'3' == str(3) == str('3')
'3.141' == str(3.141) == str('3.141')

print(float(8))
print(int(3.5))
print(str('try'))

from math import sin, cos, tan, sqrt, floor, cei

help(print)
import math
print(math)

from random import randrange
cislo=randrange(0,9)
if cislo==0:
	print('Zero')
elif cislo==1:
	print('One')
else:
	print('Two')


from turtle import *
forward(150)
left(90)
forward(50)
right(60)
forward(50)


from turtle import *
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(110)


forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)

left(20)

forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)



from turtle import *
for i in range(3):
	forward(50)
	left(90)
	forward(50)
	left(90)
	forward(50)
	left(90)
	forward(50)
	left(110)

from turtle import *
for i in range(10):
	forward(30)
	penup()
	forward(5)
	pendown()

from turtle import *
for i in range(4):
	forward(50)
	left(90)
left(1200)
forward(150)
left(90)
forward(10)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(10)
left(90)
forward(110)

left(180)
penup()
forward(150)
pendown()

for i in range(6):
	forward(10)
	penup()
	forward(5)
	pendown()

penup()
right(180)
forward(90)
right(90)
forward(10)
right(90)
pendown()

for i in range(6):
	forward(10)
	penup()
	forward(5)
	pendown()

penup()
right(180)
forward(90)
right(90)
forward(10)
right(90)
pendown()

for i in range(6):
	forward(10)
	penup()
	forward(5)
	pendown()

penup()
right(180)
forward(90)
right(90)
forward(10)
right(90)
pendown()

for i in range(6):
	forward(10)
	penup()
	forward(5)
	pendown()


answer = input('Say Halaaaaous: ')
while answer != 'Halaaaous':
	print('Try again')
	answer = input('Say Halaaaous: ')

from random import randrange

while True:
    print('Číslo je', randrange(10000))
    print('(Počkej, než se počítač unaví...)')
    

from turtle import *
for i in range(4):
	for i in range(6):
		forward(10)
		penup()
		forward(5)
		pendown()

	penup()
	right(180)
	forward(90)
	right(90)
	forward(10)
	right(90)
	pendown()


for i in range(20):  # Vnější cyklus
    for j in range(10):  # Vnitřní cyklus
        print(j * i, end=' ')
        if i <= j:
            break
    print()
    
"""
from random import randrange
summary = 0


while summary <21:
	print('You have', summary, 
	'points')
	answer = input('Do you want a card? ')
	if answer == 'yes':
		card = randrange (2,11)
		summary = summary + card
		print('You drew', card)
	elif answer == 'no':
			break
	else:
		print('You need to answer yes or no')
	
if summary==21:
		print('Congrats, you won!')
elif summary>21:
		print('Game over!, you missed it by only' , summary-21)
		if summary-21>1:
			print('points')
		elif summary-21==1:
				print('point')
else:
	print('You were only missing', 21-summary, 'points!')



