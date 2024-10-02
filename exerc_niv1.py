print('PRIMEIRA ATIVIDADE')

def conte_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
    
# Exemplo a) usando uma palavra passada via parâmetro da função
print('Letra A')
palavra_parametro = "Cristianismo"
resultado_parametro = conte_vogais(palavra_parametro)
print(f"A palavra '{palavra_parametro}' tem {resultado_parametro} vogais.")

# Exemplo b) usando uma palavra recebida via input do usuário
print('Letra B')
palavra_input = input("Digite uma palavra: ")
resultado_input = conte_vogais(palavra_input)
print(f"A palavra '{palavra_input}' tem {resultado_input} vogais.")
