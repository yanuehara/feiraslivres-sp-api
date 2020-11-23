import unittest
from django.test import TestCase, TransactionTestCase
from rest_framework.test import APIClient
from .views import Feira

# Create your tests here.

class APITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        feira = Feira(
            lat=-46550164.0,
            long=-23558733.0,
            setcens="355030885000091",
            areap="3550308005040",
            coddist="87",
            distrito="VILA FORMOSA",
            codsubpref="26",
            subpref="ARICANDUVA-FORMOSA-CARRAO",
            regiao5="Leste",
            regiao8="Leste 1",
            nome_feira="FEIRA TESTE",
            registro="4041-1",
            logradouro="RUA DOS BOBOS",
            numero="0",
            bairro="VL DOS BOBOS",
            referencia="",
        )
        feira.save()


    def setUp(self):
        # Testing with Django Rest Client

        # User Agent is used by logger
        self.client = APIClient(HTTP_USER_AGENT='DjangoTestUA/1.0')

    def test_list_feiras(self):
        # Issue a GET request.
        response = self.client.get('/feiras/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the database has one mock feira
        self.assertEqual(len(response.json()), 1)
    
    def test_create_feira(self):
        new_feira = {
            "long": -46550164.0,
            "lat": -23558733.0,
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": "87",
            "distrito": "VILA FORMOSA",
            "codsubpref": "26",
            "subpref": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome_feira": "FEIRA TESTE",
            "registro": "4041-1",
            "logradouro": "RUA DOS BOBOS",
            "numero": "0",
            "bairro": "VL DOS BOBOS",
            "referencia": ""
        }
        # POST to endpoint
        response = self.client.post('/feiras/', new_feira)

        # Assert it was created and it has an id
        self.assertContains(response,'id', status_code=201)
    
    def test_feira_details(self):
        # GET feira details
        response = self.client.get('/feira/1/')

        # Check that the response is 200 OK
        self.assertContains(response,"long", status_code=200)
        self.assertContains(response,"lat", status_code=200)
        self.assertContains(response,"setcens", status_code=200)
        self.assertContains(response,"areap", status_code=200)
        self.assertContains(response,"coddist", status_code=200)
        self.assertContains(response,"distrito", status_code=200)
        self.assertContains(response,"codsubpref", status_code=200)
        self.assertContains(response,"subpref", status_code=200)
        self.assertContains(response,"regiao5", status_code=200)
        self.assertContains(response,"regiao8", status_code=200)
        self.assertContains(response,"nome_feira", status_code=200)
        self.assertContains(response,"registro", status_code=200)
        self.assertContains(response,"logradouro", status_code=200)
        self.assertContains(response,"numero", status_code=200)
        self.assertContains(response,"bairro", status_code=200)
        self.assertContains(response,"referencia", status_code=200)
    
    def test_update_feira_details(self):
        # Test update feira details with patch

        # POST to endpoint
        response = self.client.patch('/feira/1/', {"bairro":"TESTE PATCH"})

        self.assertContains(response, 'TESTE PATCH', status_code=200)
    
    def test_update_feira_details_put(self):
        # Test update feira details with put

        feira = {
            "long": -46550164.0,
            "lat": -23558733.0,
            "setcens": "355030885000091",
            "areap": "3550308005040",
            "coddist": "87",
            "distrito": "VILA CURITIBA", # Distrito changed
            "codsubpref": "26",
            "subpref": "ARICANDUVA-FORMOSA-CARRAO",
            "regiao5": "Leste",
            "regiao8": "Leste 1",
            "nome_feira": "FEIRA TESTE",
            "registro": "4041-1",
            "logradouro": "RUA DOS BOBOS",
            "numero": "0",
            "bairro": "VL DOS BOBOS",
            "referencia": ""
        }

        response = self.client.put('/feira/1/', feira)

        self.assertContains(response, "VILA CURITIBA", status_code=200)
    
    def test_remove_feira(self):
        response = self.client.delete('/feira/1/')

        self.assertEqual(response.status_code, 204)
