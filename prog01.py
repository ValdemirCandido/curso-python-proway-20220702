# crie um programa que receba o nome, o peso e a altura de uma pessoa. em seguida, calcula o seu IMC.A altura
# deva ser informer no formato metros.centimentros (exemplo 1.79).  formula do IMC é a seguite: peso / (altura * altura).abs

if __name__ == "__main__":
    
    nome = input("informer o seu nome: ")
    peso = float(input("informer o seu peso: "))
    altura = float(input("informer a sua altura (por exemplo,1.80): "))

    IMC = peso / (altura * altura)
    # IMC = peso / (altura ** 2) # Operator expronenciação
    # Imc = peso / (pow(altura, 2)) # função built-in pow()

    print(f"{nome}, seu IMC é de {IMC:.1f}")
