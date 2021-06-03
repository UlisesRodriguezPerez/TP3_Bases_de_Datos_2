# import arff
import re
from bs4 import BeautifulSoup 
import bs4                      #pip3 install bs4
from unicodedata import normalize

import json

def leerColeccion(archivo):

    textoTotal =""
    Articulos = []
    with open(archivo, 'r') as contenido:
        for line in contenido:
            textoTotal += line 

    soup = BeautifulSoup(textoTotal,"html.parser")
    
    Clases = dict()

    for articulo in soup.findAll('reuters'):    # Se extraen los datos de cada articulo 
        dicJson = dict()
        TITLE = AUTHOR = DATELINE = BODY = ""

        #if articulo["topics"] == "YES" and articulo.topics.text != '' and articulo.body != None:
        if articulo["topics"] == "YES" and articulo.topics.text != '':# and articulo.body != None:

                #OBTIENE EL CAMPO DATE.
            DATE = articulo.date.string
            DATE_json = json.dumps(DATE)
            dicJson["DATE"] = DATE

                #CARGA TODOS LOS TOPICS QUE ENCUENTRE. 
            listaTopicsD = articulo.topics.find_all("d")
            listaTopicTexto = []
            for topic in listaTopicsD:
                listaTopicTexto.append(topic.string)

            TOPICS = listaTopicTexto
            if TOPICS != []:
                dicJson["TOPICS"] = TOPICS


                #OBTIENE TODOS LOS PLACES QUE ENCUENTRE.
            listaPlacesD = articulo.places.find_all("d")
            listaPlacesTexto = []
            for place in listaPlacesD:
                listaPlacesTexto.append(place.string)

            PLACES = listaPlacesTexto
            if PLACES != []:
                dicJson["PLACES"] = PLACES



                #OBTIENE TODOS LOS PEOPLE QUE ENCUENTRE. People
            listaPeoplesD = articulo.people.find_all("d")
            listaPeoplesTexto = []
            for people in listaPeoplesD:
                listaPeoplesTexto.append(people.string)

            PEOPLES = listaPeoplesTexto
            if PEOPLES != []:
                dicJson["PEOPLE"] = PEOPLES





                #OBTIENE TODOS LOS ORGS QUE ENCUENTRE.
            listaOrgsD = articulo.orgs.find_all("d")
            listaOrgsTexto = []
            for orgs in listaOrgsD:
                listaOrgsTexto.append(orgs.string)

            ORGS = listaOrgsTexto
            if ORGS != []:
                dicJson["ORGS"] = ORGS





                #OBTIENE TODOS LOS EXCHENGES.
            listaExchangesD = articulo.exchanges.find_all("d") 
            listaExchangesTexto = []
            for exchanges in listaExchangesD:
                listaExchangesTexto.append(exchanges.string)
            
            EXCHENGES = listaExchangesTexto
            if EXCHENGES != []:
                dicJson["EXCHENGES"] = EXCHENGES




                #OBTIENDE TODOS LOS COMPANIES QUE ENCUENTRE.
            listaCompaniesD = articulo.companies.find_all("d") 
            listaCompaniesTexto = []
            for companies in listaCompaniesD:
                listaCompaniesTexto.append(companies.string)

            COMPANIES = listaCompaniesTexto
            if COMPANIES != []:
                dicJson["COMPANIES"] = COMPANIES




                #OBTIENE EL CAMPO NEWID
            ID = articulo["newid"]
            dicJson["NEWID"] = ID

            dicText = dict()
                #OBTIENE LOS TITLE, AUTHOR, DATELINE y BODY DE TEXT
            if articulo.title != None:
                TITLE = articulo.title.string
                dicText["TITLE"] = TITLE

            if articulo.author != None:
                AUTHOR = articulo.author.string
                dicText["AUTHOR"] = AUTHOR

            if articulo.dateline != None:
                DATELINE = articulo.dateline.string
                dicText["DATELINE"] = DATELINE

            if articulo.body != None:
                BODY = articulo.body.string
                dicText["BODY"] = BODY


            TEXT = [TITLE, AUTHOR, DATELINE, BODY]
            
            dicJson["TEXT"] = dicText
            # print(ID)

            ####GENERA un JSON POR ARTÍCULO.
            # f = open (r'C:\Users\ulirp\OneDrive - Estudiantes ITCR\Cursos TEC\Primer Semestre 2021\Bases de atos II\Proyectos\TPR3\2021-1 TP3 - Noticias Reuters - MongoDB\Parseo\jsons\dataJson'+ID+'.json','w')
            # json.dump(dicJson, f, indent=4)
            # f.close()
            

                #AGREGAMOS TODOS LOS CAMPOS EN UNA LISTA SEPARADA POR ARTÍCULO.
            Articulos.append(dicJson)


    return Articulos
    
    
# def seleccionar_terminos2(archivo):

# 	L_Documentos = leerColeccion(archivo)


def leerDirectorios():
    articulos = []
    with open("directoriosXml.txt","r") as archivo:
        directoriosXml = archivo.read()
        directoriosXml = directoriosXml.split("\n")

        for dir in directoriosXml:
            articles = leerColeccion(dir)
            articulos += articles
 
        f = open ('jsonMiedo2.json','w')
        # f.write("[")
        for dic in articulos:
            json.dump(dic, f, indent=4)
            # f.write(",")
        # f.write("]")
        f.close()

leerDirectorios()

# seleccionar_terminos2("reut2-001.sgm")
# seleccionar_terminos2("Aprueba.sgm")


