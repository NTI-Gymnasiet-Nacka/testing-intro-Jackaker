# Största skillnad

def main():
    string = input().split(", ")
    lista=[]

    for t in string:
        t=int(t)
    string.sort()

    for t in string:
        lista.append(int(t))

    return print(int(lista[len(lista)-1])-int(lista[0]))

if __name__ == "__main__":
    main()
