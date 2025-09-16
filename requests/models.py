from django.db import models 

class Requests(models.Model): 
    title = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=False, blank=False)
 
    def addRequest(self, about, title):
        try:
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            if(title is None or title == ''): 
                title = 'Quero resolver algo: '
            self.about = about
            self.title = title
            self.save()
            return True

        except Exception as Ex:
            print( Ex )
            return False
 
    def readRequest(self, id):
        try: 
            if id is None or isinstance(id, int): 
                raise ValueError('É preciso que exista um valor numérico') 
            return self.__class__.objects.filter(pk=id).first()  # retorna None se não achar

        except Exception as Ex:
            print( Ex )
            return None 

    def updateRequest(self, about, title, id):
        try: 
            if id is None or isinstance(id, int): 
                raise ValueError('É preciso que exista um valor numérico') 
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            if(title is None or title == ''): 
                title = 'Quero resolver algo: '
            
            self.id = id
            return self.__class__.objects.save() 

        except Exception as Ex:
            print( Ex )
            return None 

    def deleteteRequest(self, id):
        try: 
            if id is None or isinstance(id, int): 
                raise ValueError('É preciso que exista um valor numérico') 
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            if(title is None or title == ''): 
                title = 'Quero resolver algo: '
            
            self.id = id
            return self.__class__.objects.delete()  

        except Exception as Ex:
            print( Ex )
            return None 

    @classmethod
    def listRequests(cls):
        try: 
            return cls.objects.all()  
        except Exception as Ex:
            print( Ex )
            return None 