
import datetime 

anoAtual = datetime.datetime.now()

name = input("Qual é o seu nome: ")

dataDeNascimento = int(input("Coloque sua data de nascimento: "))

idade = anoAtual.year - dataDeNascimento

print("Olá, {0}!".format(name) + " Você esta com " + str(idade) + " anos")