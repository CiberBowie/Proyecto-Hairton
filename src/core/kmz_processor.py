import zipfile
import re
from bs4 import BeautifulSoup

class KMZProcessor:
    def __init__(self, kmz_path):
        self.kmz_path = kmz_path
    
    def extract_kml(self):
        with zipfile.ZipFile(self.kmz_path, 'r') as kmz:
            kml_files = [f for f in kmz.namelist() if f.endswith('.kml')]
            if not kml_files:
                raise ValueError("No se encontró archivo KML en el KMZ")
            
            with kmz.open(kml_files[0]) as kml_file:
                kml_content = kml_file.read().decode('utf-8')
        
        return kml_content
    
    def parse_coordinates(self):
        kml_content = self.extract_kml()
        soup = BeautifulSoup(kml_content, 'lxml-xml')
        
        placemarks = []
        for placemark in soup.find_all('Placemark'):
            try:
                name = placemark.find('name').text.strip() if placemark.find('name') else "Sin nombre"
                coords = placemark.find('coordinates').text.strip()
                lon, lat, alt = re.split(r'[,,\s]+', coords)[:3]
                
                placemarks.append({
                    'name': name,
                    'longitude': float(lon),
                    'latitude': float(lat),
                    'altitude': float(alt) if alt else 0.0
                })
            except Exception as e:
                print(f"Error procesando placemark: {str(e)}")
                continue
        
        return placemarks