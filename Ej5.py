#poner las dos diagonales en la misma linea
def diagonal3(n):
    for i in range(n):
        print(" "*(n-i-1)+"#"+"_"*i+"_"*i+"#")
    return " "

print(diagonal3(6))

if __name__ == "__main__":
    print(diagonal3(6))