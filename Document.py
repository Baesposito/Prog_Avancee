# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:12:14 2020

@author: Chloé
"""

################################## Déclaration des classes ##################################

#Importation des packages
import datetime as dt

import pickle

#Question 4.3

#CLASSES 

class Corpus():
    
    def __init__(self,name):
        self.name = name
        self.collection = {}
        self.authors = {}
        self.id2doc = {}
        self.id2aut = {}
        self.ndoc = 0
        self.naut = 0
            
    def add_doc(self, doc):
        
        self.collection[self.ndoc] = doc
        self.id2doc[self.ndoc] = doc.get_title()
        self.ndoc += 1
        aut_name = doc.get_author()
        aut = self.get_aut2id(aut_name)
        if aut is not None:
            self.authors[aut].add(doc)
        else:
            self.add_aut(aut_name,doc)
            
    def add_aut(self, aut_name,doc):
        
        aut_temp = Author(aut_name)
        aut_temp.add(doc)
        
        self.authors[self.naut] = aut_temp
        self.id2aut[self.naut] = aut_name
        
        self.naut += 1

    def get_aut2id(self, author_name):
        aut2id = {v: k for k, v in self.id2aut.items()}
        heidi = aut2id.get(author_name)
        return heidi

    def get_doc(self, i):
        return self.collection[i]
    
    def get_coll(self):
        return self.collection

    def __str__(self):
        return "Corpus: " + self.name + ", Number of docs: "+ str(self.ndoc)+ ", Number of authors: "+ str(self.naut)
    
    def __repr__(self):
        return self.name

    def sort_title(self,nreturn=None):
        if nreturn is None:
            nreturn = self.ndoc
        return [self.collection[k] for k, v in sorted(self.collection.items(), key=lambda item: item[1].get_title())][:(nreturn)]

    def sort_date(self,nreturn):
        if nreturn is None:
            nreturn = self.ndoc
        return [self.collection[k] for k, v in sorted(self.collection.items(), key=lambda item: item[1].get_date(), reverse=True)][:(nreturn)]
    
    def save(self,file):
            pickle.dump(self, open(file, "wb" ))
        
       

class Author():
    def __init__(self,name):
        self.name = name
        self.production = {}
        self.ndoc = 0
        
    def add(self, doc):     
        self.production[self.ndoc] = doc
        self.ndoc += 1

    def __str__(self):
        return "Auteur: " + self.name + ", Number of docs: "+ str(self.ndoc)
    def __repr__(self):
        return self.name
    


class Document():
    
    #Constructeur
    def __init__(self, date, title, author, text, url):
        self.date = date
        self.title = title
        self.author = author
        self.text = text
        self.url = url
    
    #Accesseurs / mutateurs 
    
    def get_author(self):
        return self.author

    def get_title(self):
        return self.title
    
    def get_date(self):
        return self.date
    
    def get_source(self):
        return self.source
        
    def get_text(self):
        return self.text

    def __str__(self):
        return "Document " + self.getType() + " : " + self.title
    
    def __repr__(self):
        return self.title
    
    
        
    def getType(self):
        pass
    

###############################################################################"

##   PARTIE 3
##########################################################################

#Question 3.1

class RedditDocument(Document):
    
    #Constructeur qui recupère de la classe mère 
    def __init__(self,nbcommentaire):
        super().__init__()  #On récupère les attributs de la classe mère
        self.nbcommentaire = nbcommentaire
        self.source="Reddit"
            
    #Accesseurs / mutateurs pour les champs spécifiques ici : nbcommentaires
    def get_nbcommentaire(self):
        return self.nbcommentaire
        
    #Question 3.4
    def getType(self):
        return "reddit"
        
    #Affichage de l'objet
    def __str__(self):
        return Document.__str__(self)+ "[" + str(self.nbcommentaire) + "commentaires]"
        
    
#Question 3.2

class ArxivDocument(Document):

    #Constructeur qui récupère les attributs de la classe mère
    def __init__(self,coauteurs):
        Document.__init__(self, date, title, author, text, url)
        self.coauteurs = coauteurs
    
    #Accesseurs / mutateurs
    def get_coauteurs(self):
        if self.coauteurs is None:
            return 0
        return(len(self.coauteurs)-1)
    
    #Pour renvoyer le nombre de coauteurs
    def get_num_coauteurs(self):
        #Si on n'a aucune coauteurs on renvoit 0
        if self.coauteurs is None:
            return(0)
        return(len(self.coauteurs) - 1)
    
    #Pour renvoyer le nom des coauteurs 
    def get_coauteurs(self):
        #Si pas de coauteurs on renvoit une liste vide 
        if self.coauteurs is None:
            return([])
        return(self.coauteurs)
    
    #Question 3.4
    def getType(self):
        return "arxiv"
        
    #Affichage 
    def __str__(self):
        s = Document.__str__(self)
        if self.get_num_coauteurs() > 0:
            return s + " [" + str(self.get_num_coauteurs()) + " co-auteurs]"
        return s

###################################################################################
##                               PARTIE 4 : accès à partir du contenu 
###################################################################################


