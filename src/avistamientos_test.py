from avistamientos import *

if __name__ == '__main__':
    UFOS = lee_avistamientos('data/ovnis.csv')
    #print(UFOS[0])
    #print(UFOS[1])

    forma = 'circle'
    av_mayor_d=avistamiento_mayor_duracion(UFOS, forma)
    print(f"Avistamiento de forma \'{forma}\' de mayor duración: {av_mayor_d}")
        