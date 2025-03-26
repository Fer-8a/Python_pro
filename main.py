None
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "wey": "Una forma de decirle a un amigo",
            "chido": "Se usa para decir que algo esta bueno o bonito",
            "gacho": "Se usa para decir que algo esta feo o malo",
            "chafa": "Se usa para referirse a algo de mala calidad",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Porfavor ingresa una palabra para buscar")
