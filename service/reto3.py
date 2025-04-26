def min_movimientos(contenedores):
    permutaciones = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0]
    ]
    
    min_movs = float('inf')

    for asignacion in permutaciones:
        movimientos = 0
        for idx_contenedor in range(3):
            tipo_asignado = asignacion[idx_contenedor]
            for tipo in range(3):
                if tipo != tipo_asignado:
                    movimientos += contenedores[idx_contenedor][tipo]
        if movimientos < min_movs:
            min_movs = movimientos

    return min_movs