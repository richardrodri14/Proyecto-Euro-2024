def obtenerEstadioPorId(equipos, id_equipo):
    for equipo in equipos:
        if equipo.id == id_equipo:
            return equipo
    return None