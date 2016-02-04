def premier(nombre):
    """
    Fonction qui permet de savoir si un nombre saisi au clavier est premier ou non
    """
    if(nombre <2):
        return False
    for i in range(2, nombre):
        if(nombre % i ==0):
            return False
    return True
    
        
if __name__ == '__main__':
    try:
        nombre = int(input())
        print(premier(nombre))
    except ValueError:
        print("Ce n'est pas un nombre entier.  Try again...")