def incomodam(n):
    if n <= 0: return ""
    if n == 1: return "incomodam "
    return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if n <= 0:
        return ""

    if n > 1:
        if n-1 == 1:
            sentenca_1 = "" 
        else:
            sentenca_1 = "\n" + str(n-1) + " elefantes incomodam muita gente"
        sentenca_2 = "\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"
        return elefantes(n-1) + sentenca_1 + sentenca_2
    else:
        return "\nUm elefante incomoda muita gente"

def main():
    n = int(input("digite:"))
    print(elefantes(n))
    #Primeira alteração no script para entender o controle de versionamento - SCM.
main()
