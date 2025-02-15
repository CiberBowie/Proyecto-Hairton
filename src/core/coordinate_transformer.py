from pyproj import Transformer

class CoordinateTransformer:
    def __init__(self, delta_x = 0, delta_y = 0):
        self.transformer = Transformer.from_crs("EPSG:4326", "EPSG:3735", always_xy=True)
        self.delta_x = 0
        self.delta_y = 0
    
    def set_deltas(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y
    
    def transform(self, lon, lat):
        x, y = self.transformer.transform(lon, lat)
        return x + self.delta_x, y + self.delta_y