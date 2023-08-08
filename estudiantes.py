estudiantes =  [
    {
        "Nombre completo": "Juan Perez",
        "Edad": 16,
        "notas": {
            "MAT": 70,
            "FIS": 80,
            "QMC": 90,
            "LAB": 60
        },
        "Asistencia": 85
    },
      {
        "Nombre completo": "Rosa Perez",
        "Edad": 17,
        "notas": {
            "MAT": 40,
            "FIS": 50,
            "QMC": 60,
            "LAB": 100
        },
        "Asistencia": 100
    }
]

def promedio_estudiante(estudiante: dict) -> float:
    flag = 0
    for item in estudiante["notas"].values():
        flag += item 
    return flag / len(estudiante["notas"])  
    
def promedio_estudiante2(estudiante: dict) -> float:
    accum = sum(estudiante["notas"].values())
    return accum / len(estudiante["notas"])

def promedio_curso(lista_estudiantes: list) -> float:
    flag = 0
    for estudiante in lista_estudiantes:
        flag += promedio_estudiante2(estudiante)
    return flag / len(lista_estudiantes)

def promedio_curso2(lista_estudiantes: list) -> float:
    lista_promedios = [promedio_estudiante2(est) for est in lista_estudiantes]
    accum = sum(lista_promedios)
    return accum / len(lista_estudiantes)

print(promedio_estudiante2(estudiantes[0]))
print(promedio_curso(estudiantes))
