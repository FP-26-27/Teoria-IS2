from sevici import *
def test_estaciones_bicis_libres(listado: list[Estacion], n:int = 5)->None:
    result = estaciones_bicis_libres(listado)
    print(f"Hay {len(result)} estaciones con {n} o más bicis libres y las {n} primeras son:")
    for i in range(n):
        print(result[i])

if __name__=='__main__':
    listado = lee_datos('data/estaciones.csv', 'utf-8')
    #print(listado[0])
    test_estaciones_bicis_libres(listado)
