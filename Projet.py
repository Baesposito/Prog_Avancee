class Projet():
    
    # initialisation des donnees pour la creation du graphe
    def __init__(self,tab):
        Donnee_Graphe = {}
        inc = 0
        for i in range(len(tab)):
            mot1 = tab[i][inc]
            for j in range(inc+1,len(tab[i])):
                
                mot2 = tab[i][j]
                k1 = mot1+mot2
                k2 = mot2+mot1
                if(not( k1 in Donnee_Graphe.keys() or k2 in Donnee_Graphe.keys() )):
                    Donnee_Graphe[k1] = [mot1,mot2,1]
                elif(k1 in Donnee_Graphe.keys()):
                    Donnee_Graphe[k1][2] += 1
                else:
                    Donnee_Graphe[k2][2] += 1
    	
        self.Donnee_Graphe = Donnee_Graphe # dictionnaire avec la forme expliquee dans le rapport
    
    # Recuperation du dictionnaire pour l'affichage
    def get_coll(self):
        return self.Donnee_Graphe
    
        
