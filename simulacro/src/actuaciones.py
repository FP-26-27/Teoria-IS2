import csv
from collections import Counter, defaultdict
from datetime import datetime, date
from typing import NamedTuple

Actuacion = NamedTuple("Actuacion",[
    ("id_actuacion",int),
    ("recinto",str),
    ("artista",str),
    ("promotora",str),
    ("fecha_actuacion",date),
    ("asistentes_totales",int),
    ("asistentes_por_zona",dict[str, int]),
    ("teloneros",list[str]),
    ("tasa_ocupacion",float)
])
