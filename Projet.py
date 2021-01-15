class Projet():
    
    
    def __init__(self):
        self.Donnee_Graphe = {}
    
    def get_coll(self):
        return self.Donnee_Graphe
    
    def combinaison_mot(self,tab):
        inc = 0
        for i in range(len(tab)):
            mot1 = tab[i][inc]
            for j in range(inc+1,len(tab[i])):
                
                mot2 = tab[i][j]
                k1 = mot1+mot2
                k2 = mot2+mot1
                if(not( k1 in self.Donnee_Graphe.keys() or k2 in self.Donnee_Graphe.keys() )):
                    self.Donnee_Graphe[k1] = [mot1,mot2,1]
                elif(k1 in self.Donnee_Graphe.keys()):
                    self.Donnee_Graphe[k1][2] += 1
                else:
                    self.Donnee_Graphe[k2][2] += 1
