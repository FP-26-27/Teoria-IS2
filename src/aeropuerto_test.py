from aeropuerto import *

if __name__ == '__main__':
    VUELOS = lee_vuelos('data/vuelos.csv')
    #print(VUELOS[0])
    #print(codigo_vuelos_completos(VUELOS))
    print(duracion_vuelos_fecha(VUELOS, date(2007,12,1)))