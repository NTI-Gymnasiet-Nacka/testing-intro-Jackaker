# Palindrome

def main():
    resultat=False
    string_1=input("")
    string_1=string_1.lower()
    string_2=string_1[::-1]

    if string_1==string_2:
        resultat=True

    return print(resultat)

if __name__ == "__main__":
    main()
