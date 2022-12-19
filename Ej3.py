def longitud(string):
    return len(string)

def numero_palabra(i):
    if i == 0:
        return ('zero')
    elif i == 1:
        return ('one')
    elif i == 2:
        return ('two')
    elif i == 3:
        return ('three')
    elif i == 4:
        return ('four')
    elif i == 5:
        return ('five')
    elif i == 6:
        return ('six')
    elif i == 7:
        return ('seven')
    elif i == 8:
        return ('eight')
    elif i == 9:
        return ('nine')

def numero(string):
    i=longitud(string)
    for i in range(0,10):
        while i != 4:
            numero_palabra(i)=numero
            return numero
        else:
            return 'four'
    




print(numero('seven'))

if __name__ == "__main__":
    print(numero('seven'))
