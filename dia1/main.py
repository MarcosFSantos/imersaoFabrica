from functions import bhaskara

#Pedindo os valores ao usuário
print("digite o valor de 'a': ")
a = input()
print("digite o valor de 'b': ")
b = input()
print("digite o valor de 'c': ")
c = input()
print("digite o valor de 'delta': ")
delta = input()

#chamando a função que vai calcular o valor de bhaskara
x = bhaskara(a, b, c, delta)

#imprimindo o valor na tela
print(x)