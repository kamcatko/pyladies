#firstcalucations


""""
x = 4*4
y = 128*4
z = 1+1

print(x+y+z)


pi = 3.1415926
strana = 183
polomer = strana
o = 2*pi*polomer
print(pi*polomer**2) 



strana = float(input('Zadej stranu čtverce v centimetrech: '))
print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')



# how many codes will make Willko give Kamchi massagky

massage = int(input('Enter how many codes Kamchi should do:'))
print('When Kamchi makes', massage, 'codes, she will get', massage/2, 'massages from Willko')



strana = int(input('enter square side length in cm: '))
Dobre = strana > 0

if Dobre:
	print('Length of the square with', strana, 'cm is', 4 * strana, 'cm')
	
else:
	print('you just entered a stupid number, dah?!')



cislo = int(input('Zadej číslo, přičtu k němu 3: '))
if cislo == 0:
    print('Jé, to je jednoduché!')
print(cislo, '+ 3 =', cislo + 3)


strana = float(input('Zadej stranu čtverce v centimetrech: '))
okentry = strana > 0
if okentry:
	print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
	print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
	
else:
	print('What do you mean by that?')
	
print('Come back, when you review maths again')



vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('A ze kterépak jsi planety?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: víno, cider, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Návštěvníky z budoucnosti tady nevidíme rádi.')
    


print('Reply only yes or no')
happines = input('Are you happy?')
if happines=='yes':
	happy = True
elif happines=='no':
	happy=False

richloop=input('Are you rich?')
if richloop=='yes':
	rich=True
elif richloop=='no':
	rich=False

if rich and happy:
	print('Wonderful, congrats!')
elif rich:
	print('Try to smile more')
elif happy:
	print('Try to spend less')
else:
	print('Do not worry it will change!')
	
"""
