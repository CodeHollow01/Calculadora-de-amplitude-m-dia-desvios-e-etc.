import os
import re

os.system("cls")

array = []

def info(array,amplitude,media,desvio,variancia,desvio_padrao):
    os.system("cls")
    print("INFORMAÇÕES:\nConteúdo da listagem: " + str(array) +"\n"+"Amplitude: "+ str(amplitude)+"\n"+"Média: " + str(media)+"\n"+"Desvio Médio: " + str(desvio)+"\n"+"Variância: "+ str(variancia)+"\n"+"Desvio padrão: "+ str(desvio_padrao))



def verify(numbers):
    if not numbers.isdigit():
        os.system("cls")
        print("Você digitou errado, tente novamente!")
        return False
    else:
        return True

def adicionar_numeros():
    while True:
        numbers = input("Digite o números que deseja!(Aperte X para começar o cálculo, D para apagar e C para limpar): ")
        if numbers == "x":
            calculo(array)
            return False
        elif numbers == "d":
            if array:
                array.pop()
                os.system("cls")
                print(array)
            else:
                print("Sua lista está vazia!")
        elif numbers == "c":
            array.clear()
            os.system("cls")
            print(array)
        else:
            if verify(numbers) == True:
                array.append(int(numbers))
                os.system("cls")
                print(array)

def calculo(array):
    if array:
        variancia_list = []
        desvio_list = []
        amplitude = max(array) - min(array)
        media = round(float(sum(array) / (len(array))),2)
        for i in array:
            if media < i:
                x = i - media
            else:
                x = media - i
            desvio_list.append(x)
            variancia_x = x ** 2
            variancia_list.append(variancia_x)
        variancia = round(float(sum(variancia_list) / len(array)),2)
        desvio = round(float(sum(desvio_list) / len(array)),2)
        desvio_padrao = round(float(variancia ** 0.5),3)
        info(array,amplitude,media,desvio,variancia,desvio_padrao)
    else:
        os.system("cls")
        print("Sua lista está vazia!")

adicionar_numeros()