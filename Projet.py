# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:22:46 2021

@author: Chloé
"""

from Document import *

import praw

import urllib.request
import xmltodict   


################################## Création du Corpus ##################################

#Importation de la librairie
import praw

#Création d'une liste : docs
corpus=[]

#REDDIT

#On récupère les données sur Reddit (création d'un compte)
#On crée une application sur Reddit et on recupère les codes 
reddit = praw.Reddit(client_id='eKwweulYysI9RA', client_secret='_Xdmw1Ku27yCxdS1iHJZkONGokg', user_agent='ccarrie')

#Alimenter la liste docs avec le texte
texte = reddit.subreddit('Coronavirus').hot(limit=100)
for post in texte :
    txt=post.title + '.' + post.selftext
    
    #On remplace les sauts de ligne par des espaces
    txt=txt.replace('\n',' ')
    
    #Découpage du document en mot 
    mot=txt.split(" ")

    #Occurences des mots
    from collections import Counter
    #print(Counter(mot))
    
    #On ajoute le document au corpus 
    corpus.append(txt)
    

#Graphes 
import networkx as nwork 
G = nwork.Graph()
G.add_nodes_from(mot)
print(G.nodes)







#URLLIB 

Corpus2=[]

#On récupère les données en XML
import urllib
url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10'
data = urllib.request.urlopen(url).read().decode()
#decode() transforme le bytes stream en chaîne de caractère
#print(data)

#Transformer les données XML en dictionnaire
import xmltodict
docs = xmltodict.parse(data)['feed']['entry']
for i in docs:
    txt = i['title']+ ". " + i['summary']
    txt = txt.replace('\n', ' ')
    Corpus2.append(txt)
    
#print("Le corpus2 est ",corpus)


############################ SUR LE CORPUS ET NON SUR CHAQUE DOCUMENT
#Découpage des documents en mot

#On transforme le corpus en chaîne de caractère :
#chaque document est encadré par des ' ' 
str = "''".join(corpus)
#print(str)

#Puis on découpe en mots
decoupage_mot= str.split(" ")
#print(decoupage_mot)

#Occurences des mots
from collections import Counter
#print(Counter(decoupage_mot))

#Nous pouvons voir que les mots les plus courants sont les mots de liaisons

##############################################################################

