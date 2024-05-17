def index_of(word, lista):
    index = 0
    while index < len(lista):
        element = lista[index]
        if word == element:
            return index
        else:
            index += 1

    return -1


def index_of_by_index(word, lista, indice):
    index = indice
    new_list = lista[index:]

    while index < len(lista):
        element = lista[index]
        if word == element:
            return index
        else:
            index += 1

    return -1



def index_of_empty(lista):
    index = 0
    while index < len(lista):
        if lista[index]:
            index += 1
        else: 
            return index
    return -1

def put(word, lista):
    for i in range(len(lista)):
        if lista[i] == "":
            lista[i] = word
            return i
    return -1

    

def remove(word, lista):
    count = 0
    for i in range(len(lista)):
        if word == lista[i]:
            count += 1
            lista[i] = ""
    return count
