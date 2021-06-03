#!/usr/bin/python
import os

os.getcwdb()
from pathlib import Path

import webbrowser
import os
from bs4 import BeautifulSoup   #pip3 install bs4
from unicodedata import normalize
import requests                 #pip install requests
import urllib.request
import re
import string
import codecs
from timeit import default_timer

import urllib.parse

import bs4



def extraerArchivosHtmDelDirectorio():

    listaDeDirecciones = [] 
    directorio = r"C:\Users\ulirp\OneDrive - Estudiantes ITCR\Cursos TEC\Primer Semestre 2021\Bases de atos II\Proyectos\TPR3\2021-1 TP3 - Noticias Reuters - MongoDB\reuters21578"

    for carpeta, subCarpetas, archivos in os.walk(directorio):

        carpeta = carpeta.replace("[]","\\")


        archivo = open("directoriosXml.txt","w")
        for archivo in archivos:
            direccionDeArchivosHtm = f"{carpeta}" + f"{subCarpetas}" + f"{archivo}"
            direccionDeArchivosHtm = direccionDeArchivosHtm.replace("[]","\\")  #//Linux
            
            listaDeDirecciones.append(direccionDeArchivosHtm)
        
        with open("directoriosXml.txt","w") as file:
            for i in listaDeDirecciones:
                file.write(i)
                file.write("\n")

extraerArchivosHtmDelDirectorio()