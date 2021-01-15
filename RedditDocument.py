class RedditDocument(Document)
	
	
	def __init__(self,date,title,author,text,url,nb_com):
		self.nb_com = nb_com
		super().__init__(date, title, author, text, url)
		
	def get_author(self):
        return self.author

    def get_title(self):
        return self.title
    
    def get_date(self):
        return self.date
    
    def get_url(self):
        return self.url
        
    def get_text(self):
        return self.text

    def __str__(self):
        return "Titre du document : " + self.title + ", son auteur est : " + self.author + ", il a été commenté "+ self.nb_col + " fois.\n" 
    
    def __repr__(self):
        return self.title
    
    def getType(self):
        pass
        
    def get_nb_com(self):
    	return self.nb_com
