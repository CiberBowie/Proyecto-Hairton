# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:03:46 2025
Este codigo esta diseñado para la creacion y generacion de los archivos csv como tambien su extraccion y transformacion
Los csv seran generados apartir de un KMZ o un DWG dependiendo, a medida que crezca podemos dar soporte a mas tipos de texto
@author: Noe
"""
from kmz_processor import KMZProcessor

class file_generator:
    #generamos un listado de archivos que puede procesar
    _processors = {
        'kmz':  KMZProcessor
        #'dwg': DWGProcessor
        #'txt': TxtProcessor,
        #'csv': CsvProcessor,
        #'json': JsonProcessor
    }
    @classmethod
    def create_processor(self, filename: str) -> FileProcessor:
    # Extrae la extensión del archivo (case-insensitive)
        extension = filename.split('.')[-1].lower()
        
        if extension not in self._processors:
            raise ValueError(f"Extensión no soportada: {extension}")
            
        return self._processors[extension]()
    #Creacion de metodos para distintos tipos de documentos, para un kmz, dwg, etc
    def to_kmz(self, kmz_path):
        kmz_processor = KMZProcessor(kmz_path)
        data = kmz_processor.parse_coordinates()
        return data
