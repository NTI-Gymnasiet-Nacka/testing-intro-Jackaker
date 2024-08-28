# Medelvärde

def main():
    string = input().split(", ")
    lista=[]

    if len(string)==1:
        return print(string[0])

    else:
        for f in string:
            lista.append(int(f))

        summa=sum(lista)
    
        return print(summa/len(lista))

if __name__ == "__main__":
    main()
