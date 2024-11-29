import json
ficheiro = input()
try:
    with open(ficheiro) as filho:
        texto = json.load(filho)
        print(texto)
except:
    print("Ocorreu um erro!")
finally:
    print("Processo concluido!")