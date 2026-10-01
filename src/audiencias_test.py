from audiencias import *

def test_audiencias_en_intervalo(listado: list[Audiencia])->None:
    filtrado = audiencias_en_intervalo_cerrado(listado, 0.25, 0.5)
    print("Hay ", len(filtrado), " capítulos de GH en el intervalo [0.25, 0.5]")


if __name__ == "__main__":
    audiencias = lectura_gh("data/GH.csv")
    print("Probando cosas de audiencias")
    test_audiencias_en_intervalo(audiencias)