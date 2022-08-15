import numpy as np
import cmath as cm

class NumComplexo:
    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

print('-----Primeiro Numero Complexo-----')
x1 = float(input('Insira a parte real do primeiro número: '))
x2 = float(input('Insira a parte imaginária do primeiro numero: '))
print('-----Segundo Numero Complexo-----')
y1 = float(input('Insira a parte real do segundo número: '))
y2 = float(input('Insira a parte imaginária do segundo numero: '))
print('-----Terceiro Numero Complexo-----')
z1 = float(input('Insira a parte real do terceiro número: '))
z2 = float(input('Insira a parte imaginária do terceiro numero: '))

x = complex(x1, x2)
y = complex(y1, y2)
z = complex(z1, z2)

print ('O resultado da soma dos números digitados é: ')
print (x+y+z)

print ('O resultado da subtração dos números digitados é: ')
print (x-y-z)

print ('O resultado da multiplicação entre os números digitados é: ')
print (x*y*z)

print ('O resultado da divisão entre o números digitados é: ')
print (x/y/z)



    