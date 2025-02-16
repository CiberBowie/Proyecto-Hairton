import pandas as pd
from autocad_manager import AutoCADManager
from coordinate_transformer import CoordinateTransformer
from kmz_processor import KMZProcessor

def main():
    kmz_path = 'S119E_SR 534_ODOT_AE ROAD PINS.kmz'
    offset = 100
    text_height = 25
    delta_x = 0#-151.4048 valores delta_propios de S119E_SR 534_ODOT_AE ROAD PINS.kmz
    delta_y = 0#-606918.7301

    # Inicializar componentes que usaremos en el autocad
    autocad = AutoCADManager(offset=offset, text_height=text_height)
    #setemos el ajuste del desfase de esa manera carga con precision
    transformer = CoordinateTransformer(delta_x=delta_x, delta_y=delta_y)
    kmz_processor = KMZProcessor(kmz_path)
    
    # Procesar coordenadas
    data = []
    #usamos el metodo de descomposicion para traer un diccionario con los datos
    placemarks = kmz_processor.parse_coordinates()
    
    for placemark in placemarks:
        #Transformamos los datos guardados en el diccionario
        x, y = transformer.transform(placemark['longitude'], placemark['latitude'])
        autocad.draw_point(x, y, placemark['name'])
        
        # Guardar datos para Excel
        data.append([placemark['name'], x, y])
    
    # Guardar en Excel
    df = pd.DataFrame(data, columns=["Nombre", "X", "Y"])
    df.to_excel('coordenadas_kmz.xlsx', index=False)
    print("Proceso completado. Puntos importados:", len(data))

if __name__ == '__main__':
    main()