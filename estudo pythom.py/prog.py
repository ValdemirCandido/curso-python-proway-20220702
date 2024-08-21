# crie um programa que receba um numero inteiro e exiba se ele é par ou ímpar 

if __name__ == "__main__":
    
    numero = int(input("iforme o numero: ")) 
    
    # operador resto da divisão (%)
    if numero % 2 == 0:
        print("0 numero é par.")
        
    else:
        print("o numero e ímpar.")
