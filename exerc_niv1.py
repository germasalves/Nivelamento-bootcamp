print('PRIMEIRA ATIVIDADE')

def conte_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

# Alternativa A) usando uma palavra passada via parâmetro da função
print('---------------------------######---------------------------')
print('Letra A')
palavra_parametro = "Cristianismo"
resultado_parametro = conte_vogais(palavra_parametro)
print(f"A palavra/nome '{palavra_parametro}' apresenta {resultado_parametro} vogais.")

# Alternativa B) usando uma palavra recebida via input do usuário
print('---------------------------######---------------------------')
print('Letra B')
palavra_input = input("Digite uma palavra: ")
resultado_input = conte_vogais(palavra_input)
print(f"A palavra/nome '{palavra_input}' possui {resultado_input} vogais.")
