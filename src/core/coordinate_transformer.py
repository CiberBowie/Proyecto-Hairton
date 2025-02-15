from pyproj import Transformer
"""
Codigo necesario para el cambio de formato entre ciudades y aplicacciones, en futuras versiones tendra soporte para varios formatos
*Recordatorio:crear un diccionario con diferentes formatos
"""
class CoordinateTransformer:
    def __init__(self, delta_x = 0, delta_y = 0):
        #Creamos el objeto Transformer y le decimos que queremos que transforme de un tipo a otro 
        self.transformer = Transformer.from_crs("EPSG:4326", "EPSG:3735", always_xy=True)
        self.delta_x = 0
        self.delta_y = 0
        #modifica los atributos del objeto, sin embargo puede que esto cambie en futuras versiones
    def set_deltas(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y
    
    def transform(self, lon, lat):
        x, y = self.transformer.transform(lon, lat)
        return x + self.delta_x, y + self.delta_y