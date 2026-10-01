from lecturas import *

def test_lecturas_mensuales():
    listado_datos = lectura_mensual("data/monthly_csv.csv")
    print(listado_datos[0])
    #print(media_incrementos(listado_datos))

if __name__=='__main__':
    test_lecturas_mensuales()