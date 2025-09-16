from django.test import TestCase
from .models import Requests 
from .views import ControllRequest 

class TestClass(TestCase): 
    def test_save_Requests(self):
        req = Requests()
        result = req.addRequest("Preciso de ajuda", None)
        self.assertTrue(result)

    def test_read_Requests(self):
        req = Requests()
        req.addRequest("Preciso de ajuda", None)   
        found = req.readRequest(req.id)  
        self.assertIsNotNone(found)  

class TestControl(TestCase):
    def test_ControllRequest_visualizar(self):
        req = Requests()
        result = req.addRequest("Preciso de ajuda", None)
        
        result = ControllRequest.visualizar()
        print('-controll------------')
        print(result)
        print('-controll------------')
        self.assertIsNotNone(result)  

    def test_ControllRequest_delete(self): 
        req = Requests()
        result = req.addRequest("Preciso de ajuda", None)
        print(result)

        # result = ControllRequest.deleteResquest(1)
        # print('-controll------------')
        # print(result)
        # print('-controll------------')
        # self.assertIsNotNone(result)  
