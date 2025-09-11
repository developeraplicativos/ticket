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

        except Exception as Ex:
            print( Ex )

class RequestsCustomer(Requests): 
    def addRequest(self, about, title):
        '''the client may not know the title for some situation'''
        try: 
            if(title is None): 
                title = 'Quero resolver algo'
            if(about is None): 
                raise ValueError('O autor não pode ser vazio')
            self.about = about
            self.title = title
            self.save()

        except Exception as Ex:
            print( Ex )

    

class RequestsInternal(Requests): 
    def addRequest(self, about, title): 
        super().addRequest(about, title) 