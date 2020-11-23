# Feiras SP API

Djang-REST API based on public data about Sao Paulo City freemarkets (feiras in portuguese)

The project implemented the following endpoints:

* GET /feiras/: Lists all feiras  
    Returns HTTP 200 on success and an array of feira objects  
    This endpoint accepts the distrito, regiao5, nome_feira and bairro as query params with HTML encoded whitespaces
* POST /feiras/: Creates a new feira  
    Returns HTTP 201 on success and the new feira object as a json
* GET /feira/<id>/: Get the details about one feira  
    Returns HTTP 200 on success and the feira objects as a json or 404 if not located
* PUT /feira/<id>/: Updates a feira  
    Returns HTTP 200 on success, 400 if incomplete call or 404 if not located  
    It also returns the updated feira as a json
* PATCH /feira/<id>/: Updates a field in a feira  
    Returns HTTP 200 on success or 404 if not located  
    It also returns the updated feira as a json
* DELETE /feira/<id>/: Deletes a feira  
    Returns HTTP 204 on success or 404 if not located

Feira fields are located in [models.py](feiraapi/models.py).

# How to run

First create a virtual environment with venv and activate it:

```
virtualenv venv
source venv/bin/activate
```


Then install packages from requirements.txt:

```
pip install -r requirements.txt
```

Project is configured to use postgreSQL, please change the databases key in [settings.py](feiraslivres_sp_api/settings.py) according to your config.
You can run a postgreSQL container with the username/password configured in the project with:

```
docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -d postgres -p 5432:5432
```

then

```
docker exec -it some-postgres /bin/bash  
su - postgres  
createdb feiraapi
exit
exit
```
to create the DB.

After the DB is created, generate django migrations with:
```
python manage.py makemigrations
python manage.py migrate
```

Import data running
```
python manage.py importcsv DEINFO_AB_FEIRASLIVRES_2014.csv
```

Finally, run the project with
```
python manage.py runserver
```

# Testing

Tests are located in [tests.py](feiraapi/tests.py). Unit tests use a mock feira in the test database. Tests also check for the existence of the logfile.
Tests can be run with 
```
python manage.py test feiraapi
```
or
```
coverage run --source="." manage.py test feiraapi
coverage report     # To generate textual report in command prompt
coverage html       # To genereate a visual html report
```
to generate coverage reports with coverage.py.


# Logging

The server logs API calls to a file named feiraapi-requests using django's native log system. Every API call is logged using timestamp, origin IP, origin User-Agent, path and content of the API call (for PUT, PATCH and POST requests). Fields are separated using --- (three dashes) and request body is logged in a newline.

# Examples of queries

These examples assume that the data was imported with importcsv command

* GET /feiras/
```json
[{
    "id": 1,
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
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "",
    "bairro": "VL FORMOSA",
    "referencia": "TV RUA PRETORIA"
  },
  {
    "id": 2,
    "long": -46574716.0,
    "lat": -23584852.0,
    "setcens": "355030893000035",
    "areap": "3550308005042",
    "coddist": "95",
    "distrito": "VILA PRUDENTE",
    "codsubpref": "29",
    "subpref": "VILA PRUDENTE",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "nome_feira": "PRACA SANTA HELENA",
    "registro": "4045-2",
    "logradouro": "RUA JOSE DOS REIS",
    "numero": "909",
    "bairro": "VL ZELINA",
    "referencia": "RUA OLIVEIRA GOUVEIA"
  },
  [...]
]
```

* GET /feira/1/
```json
{
  "id": 1,
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
  "nome_feira": "VILA FORMOSA",
  "registro": "4041-0",
  "logradouro": "RUA MARAGOJIPE",
  "numero": "",
  "bairro": "VL FORMOSA",
  "referencia": "TV RUA PRETORIA"
}
```

* GET /feiras/?bairro=VL FORMOSA
```json
[
  {
    "id": 1,
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
    "nome_feira": "VILA FORMOSA",
    "registro": "4041-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "",
    "bairro": "VL FORMOSA",
    "referencia": "TV RUA PRETORIA"
  },
  {
    "id": 362,
    "long": -46534859.0,
    "lat": -23562772.0,
    "setcens": "355030885000038",
    "areap": "3550308005040",
    "coddist": "87",
    "distrito": "VILA FORMOSA",
    "codsubpref": "26",
    "subpref": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "nome_feira": "VILA FORMOSA",
    "registro": "1030-8",
    "logradouro": "AV TRUMAIN C/ HENRIQUE MORIZE",
    "numero": "",
    "bairro": "VL FORMOSA",
    "referencia": "PRACA LIBERIA"
  },
  {
    "id": 443,
    "long": -46536050.0,
    "lat": -23576820.0,
    "setcens": "355030885000058",
    "areap": "3550308005079",
    "coddist": "87",
    "distrito": "VILA FORMOSA",
    "codsubpref": "26",
    "subpref": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "nome_feira": "PRACA MANOEL ARIZA",
    "registro": "7043-2",
    "logradouro": "AV ANTONIO MANOGRASSO",
    "numero": "234",
    "bairro": "VL FORMOSA",
    "referencia": "TV DA AV JOAO XXIII"
  }
]
```

* GET /feiras/?distrito=PERUS
```json
[
  {
    "id": 41,
    "long": -46737785.0,
    "lat": -23407009.0,
    "setcens": "355030861000025",
    "areap": "3550308005242",
    "coddist": "62",
    "distrito": "PERUS",
    "codsubpref": "1",
    "subpref": "PERUS",
    "regiao5": "Norte",
    "regiao8": "Norte 1",
    "nome_feira": "VILA MALVINA",
    "registro": "6123-9",
    "logradouro": "RUA TIBURNO",
    "numero": "",
    "bairro": "VL MALVINA",
    "referencia": ""
  },
  {
    "id": 204,
    "long": -46746981.0,
    "lat": -23400070.0,
    "setcens": "355030861000051",
    "areap": "3550308005242",
    "coddist": "62",
    "distrito": "PERUS",
    "codsubpref": "1",
    "subpref": "PERUS",
    "regiao5": "Norte",
    "regiao8": "Norte 1",
    "nome_feira": "VILA CAIUBA",
    "registro": "5185-3",
    "logradouro": "RUA IRITUIA",
    "numero": "",
    "bairro": "VILA CAIUBA",
    "referencia": "CDHU"
  },
  [...]
```

* GET /feiras/?regiao5=Norte
```json
{
    "id": 7,
    "long": -46701030.0,
    "lat": -23481683.0,
    "setcens": "355030829000059",
    "areap": "3550308005116",
    "coddist": "29",
    "distrito": "FREGUESIA DO O",
    "codsubpref": "3",
    "subpref": "FREGUESIA-BRASILANDIA",
    "regiao5": "Norte",
    "regiao8": "Norte 1",
    "nome_feira": "CRUZ DAS ALMAS",
    "registro": "1040-5",
    "logradouro": "ES DO SABAO",
    "numero": "448",
    "bairro": "CRUZ DAS ALMAS",
    "referencia": "AV ELISIO TEIXEIRA LEITE"
  },
  {
    "id": 13,
    "long": -46569768.0,
    "lat": -23486440.0,
    "setcens": "355030892000021",
    "areap": "3550308005069",
    "coddist": "94",
    "distrito": "VILA MEDEIROS",
    "codsubpref": "7",
    "subpref": "VILA MARIA-VILA GUILHERME",
    "regiao5": "Norte",
    "regiao8": "Norte 2",
    "nome_feira": "COHAB FERNAO DIAS",
    "registro": "1152-5",
    "logradouro": "RUA COMBATE LAGOA BRANCA",
    "numero": "",
    "bairro": "VL SABRINA",
    "referencia": "ALONSO P B AVENTURA DE SOUZA"
  },
  [...]
```
* GET /feiras/?nome_feira=VELEIROS
```json
[
  {
    "id": 375,
    "long": -46711682.0,
    "lat": -23680417.0,
    "setcens": "355030879000004",
    "areap": "3550308005220",
    "coddist": "81",
    "distrito": "SOCORRO",
    "codsubpref": "19",
    "subpref": "CAPELA DO SOCORRO",
    "regiao5": "Sul",
    "regiao8": "Sul 2",
    "nome_feira": "VELEIROS",
    "registro": "3085-6",
    "logradouro": "RUA DAS PAINEIRAS",
    "numero": "",
    "bairro": "VELEIROS",
    "referencia": "RUAS MAR DEL PLATA /PE POLMAN"
  }
]
```