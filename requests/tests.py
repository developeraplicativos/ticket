from django.test import TestCase
from .models import Requests,RequestsCustomer,RequestsInternal

class TestClass(TestCase): 
    def test_save_RequestsCustomer(self):
        req = RequestsCustomer()
        result = req.addRequest("Preciso de ajuda", None)
        self.assertTrue(result)

    def test_read_RequestsCustomer(self):
        req = RequestsCustomer()
        req.addRequest("Preciso de ajuda", None)  
        found = req.readRequest(req.id)  
        self.assertIsNotNone(found) 


    def test_save_RequestsInternal(self):
        tst = RequestsInternal()
        tst.addRequest("Preciso de ajuda", 'teste bem sussedido')
        self.assertEqual(tst.title, 'teste bem sussedido')

 
    def test_read_RequestsInternal(self):
        req = RequestsInternal()
        req.addRequest("Preciso de ajuda", 'Opa')  
        found = req.readRequest(req.id)  
        self.assertIsNotNone(found) 