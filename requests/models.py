from django.db import models 

class Requests(models.Model): 
    title = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=False, blank=False)

    class Meta:
        abstract = True 
 
    def addRequest(self, about, title):
        try:
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            if(title is None): 
                raise ValueError('O titulo não pode ser vazio')
            self.about = about
            self.title = title
            self.save()
            return True

        except Exception as Ex:
            print( Ex )
            return False
 
    def readRequest(self, id):
        try: 
            if id is None or isinstance(id, float): 
                raise ValueError('É preciso que exista um valor numérico') 
            return self.__class__.objects.filter(pk=id).first()  # retorna None se não achar

        except Exception as Ex:
            print( Ex )
            return None

class RequestsCustomer(Requests): 
    def addRequest(self, about, title):
        '''the client may not know the title for some situation'''
        try: 
            if(title is None or title == ''): 
                title = 'Quero resolver algo: '
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            self.about = about
            self.title = title
            self.save()
            return True

        except Exception as Ex:
            print( Ex )
            return False

    def readRequest(self, id): 
        return super().readRequest(id)
    

class RequestsInternal(Requests): 
    pass 