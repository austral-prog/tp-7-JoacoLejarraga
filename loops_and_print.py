colors = ["Red", "Green", "", "White", "Black"]

def enumerate_list(lista):
    index = 0
    
    while index < len(lista):
        if lista[index]:
            word = lista[index]
            lista[index] = f"{index}. {word}"
            index += 1
        else:
            del lista[index]
    return lista



def enumerate_backwards(lista):
    index = 0
    
    while index < len(lista):
        if lista[index]:
            word = lista[index][-1::-1]
            lista[index] = f"{index}. {word}"           
            index += 1
        else:
            del lista[index]
    return lista
