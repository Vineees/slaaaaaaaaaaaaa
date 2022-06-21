# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles e apresentar no final a soma dos números.

num1 = int(input('Digite Seu Numero:'))
num2 = int(input('Digite Seu Numero:'))
cal1 = 0
maior = 0

if num1 > num2:
  maior = num1
else:
  maior = num2
  

cal1 = num1 - num2

for x in range (cal1 ,maior):
  print (x)
