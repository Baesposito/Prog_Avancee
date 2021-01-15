
################################## Importation et Déclaration des classes ##################################
from Author import Author
from Document import Document
import re
import datetime as dt
from collections import Counter
import pickle
import networkx as nwork 
from Projet import Projet
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
from bokeh.io import output_notebook, show, save
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.io import output_notebook, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8
from bokeh.transform import linear_cmap
from bokeh.models import EdgesAndLinkedNodes, NodesAndLinkedEdges


# classe Corpus
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
        
       
    
    
    

    


import praw

import urllib.request
import xmltodict   

from collections import Counter


################################## Création du Corpus ##################################

corpus = Corpus("Corona")


#Creation du graphe
G = nwork.Graph()
All_words = []


reddit = praw.Reddit(client_id='FKY5VqNh6l0eFQ', client_secret='11u6uVMp-CKUru9Pw66LCktrGlEDaA', user_agent='Reddit')
hot_posts = reddit.subreddit('Coronavirus').hot(limit=100)
for post in hot_posts:
    datet = dt.datetime.fromtimestamp(post.created)
    txt = post.title + ". "+ post.selftext
    txt = txt.replace('\n', ' ')
    txt = txt.replace('\r', ' ')
    
    doc = Document(datet,
                   post.title,
                   post.author_fullname,
                   txt,
                   post.url)
    corpus.add_doc(doc)
    mot=txt.split(" ")
    # on récupère tous les mots du corpus
    All_words = All_words + [mot]

# on enleve les doublons des textes et pas du corpus
for i in range(len(All_words)):
    for j in range(len(All_words[i])):
        All_words[i][j] = All_words[i][j].lower() 
    All_words[i] = list(set(All_words[i]))
    #on enleve aussi l'element vide qui est present dans chaque corpus.
    All_words[i].remove('')


#creation des donnees pour la creation du graphe
Info_Graph = Projet(All_words)

# creation du multi graphe
G = nwork.MultiDiGraph()
# on forme les noeuds
for m in All_words:
    for mot in m:
        if(not(mot in G.nodes())):
            G.add_node(mot, size = 10)

# ici on fait les aretes
Edge_info = Info_Graph.get_coll()

for k in Edge_info.keys():
    G.add_edge(Edge_info[k][0],Edge_info[k][1],Edge_info[k][2],width = 2 * Edge_info[k][2])
    
######## PARTIE GRAPHE    #####################

#Pour afficher le nombre de co-occurences : stockage des valeurs
degree = dict(nwork.degree(G))
nwork.set_node_attributes(G, name='cooccurence', values=degree)

#Titre du grahe
title = 'Graphe des co-occurences des mots '

#Affichage des informations quand on survole le noeud
HOVER_TOOLTIPS = [("Mot", "@index"),("Nombre de fois que le mot est en co-occurence","@cooccurence")]

#Création du plot — set dimensions, toolbar, et titre
plot = figure(tooltips = HOVER_TOOLTIPS, tools="pan,wheel_zoom,save,reset",x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), active_scroll='wheel_zoom', title=title,plot_width=1600, plot_height=900)

#Création d'un graphe
network_graph = from_networkx(G, nwork.spring_layout, scale=10, center=(0, 0))
	
#### Mise en forme du graphe 
network_graph.node_renderer.glyph = Circle(size=10)
#Subrillance des liens et des noeuds
network_graph.selection_policy = NodesAndLinkedEdges()
network_graph.inspection_policy = NodesAndLinkedEdges()


####  Affichage du graphe 

plot.renderers.append(network_graph)

show(plot)

#Pour enregistrer le graphe 
save(plot, filename=f"{title}.html")

#########################################################


