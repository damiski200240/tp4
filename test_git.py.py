#%% 1-er qst ecrire une fonction permettant d'afficher le polynome donnée par l'utilisateur sous forme de anXn+....a0X0
def afficher (p) : 
    n = len(p) - 1 #degré de polynome 
    termes = [] #liste pour stocker les coef des polynomes 

    for i in range(n,-1,-1) : #la lecture de la liste se fait du dernier element jusqu'au premeier donc on s'arrete a 0, -1 represente la limite de ce la boucle 
        coef = p[i] 
        if coef !=0:
            if i == 0 : 
                termes.append (f"{coef}")
            elif i == 1 :
                if coef == 1 :
                    termes.append(f"X")
                else : 
                    termes.append(f"{coef} X")
            else : 
                if coef == 1 :
                    termes.append(f"X^{i}")
                else :
                    termes.append(f"{coef} X^{i}")
        
    return "+".join(termes).replace("+ -", "-")

def get_valeur(p, x): 
    n = len (p) - 1
    resultat = 0
    for i in range(n,-1,-1):
        coef = p[i]
        resultat += coef * ( x**i)
    
    return resultat 

def deriver (p) : 
    n = len (p) 
    termes = []
    for i in range(1,n):
        coef = p[i]
        termes.append(coef*i) 
    return termes


p =[1, 1, 1, -1]
print(afficher (p))
print(get_valeur(p,1))
derivee = deriver(p)
print(afficher(derivee))
