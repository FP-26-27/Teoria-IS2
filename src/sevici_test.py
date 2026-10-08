from sevici import lee_datos

if __name__=='__main__':
    listado = lee_datos('data/estaciones.csv', 'utf-8')
    print(listado[0])
