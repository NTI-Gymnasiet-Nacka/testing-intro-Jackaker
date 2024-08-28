# Vokalräkning

def main():
    string=input("")
    i=0
    vokaler="aeiouyåäöAEIOUYÅÄÖ"
    
    for f in string:
        if f in vokaler:
            i+=1

    return print(i)
if __name__ == "__main__":
    main()
