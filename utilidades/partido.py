def obtenerPartidoPorNumero(partidos, numero):
    if not str.isdigit(str(numero)):
        return None
    for partido in partidos:
        if partido.numero == int(numero):
            return partido
    return None

def obtenerPartidoPorId(partidos, id):
    for partido in partidos:
        if partido.id == id:
            return partido
    return None