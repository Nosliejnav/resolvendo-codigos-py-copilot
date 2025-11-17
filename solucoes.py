# -*- coding: utf-8 -*-
"""
Soluções para os desafios de programação em Python.
"""

def concatenar_dados():
    """
    1 - Concatenando Dados: Recebe dois dados do usuário e os concatena.
    """
    print("--- Desafio 1: Concatenando Dados ---")
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + dado2
    print(f"Resultado da concatenação: {resultado}\n")

def repetir_textos():
    """
    2 - Repetindo Textos: Repete uma string um número de vezes.
    """
    print("--- Desafio 2: Repetindo Textos ---")
    texto = input("Digite o texto a ser repetido: ")
    try:
        vezes = int(input("Digite o número de repetições: "))
        resultado = texto * vezes
        print(f"Resultado da repetição: {resultado}\n")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para as repetições.\n")

def operacoes_matematicas():
    """
    3 - Operações Matemáticas Simples: Realiza uma soma com dois números.
    """
    print("--- Desafio 3: Operações Matemáticas ---")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é: {soma}\n")
    except ValueError:
        print("Erro: Por favor, digite números válidos.\n")

def verificar_par_impar():
    """
    4 - Verificando Números Pares e Ímpares: Verifica se um número é par ou ímpar.
    """
    print("--- Desafio 4: Verificando Par ou Ímpar ---")
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.\n")
        else:
            print(f"O número {numero} é ÍMPAR.\n")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.\n")

def calcular_media():
    """
    5 - Calculando Média de Notas: Calcula a média de três notas.
    """
    print("--- Desafio 5: Calculando Média ---")
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        media = (nota1 + nota2 + nota3) / 3
        print(f"A média das notas é: {media:.2f}\n")
    except ValueError:
        print("Erro: Por favor, digite notas válidas.\n")

def verificar_palindromo():
    """
    6 - Verificando Palíndromos: Verifica se uma palavra é um palíndromo.
    """
    print("--- Desafio 6: Verificando Palíndromos ---")
    palavra = input("Digite uma palavra: ").strip().lower()
    palavra_invertida = palavra[::-1]
    
    if not palavra:
        print("Nenhuma palavra foi digitada.\n")
        return

    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um palíndromo!\n")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.\n")

def main():
    """
    Função principal para executar todas as soluções.
    """
    concatenar_dados()
    repetir_textos()
    operacoes_matematicas()
    verificar_par_impar()
    calcular_media()
    verificar_palindromo()

if __name__ == "__main__":
    main()
