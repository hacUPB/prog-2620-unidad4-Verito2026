# Reto final 
## Pseudpcódigo

PSEUDOCODIGO: Sistema de Gestion de Mantenimiento de Flota Aeronautica


    funcion calcular_mantenimiento(horas_uso, limite)
    si horas_uso > limite
        retornar verdadero
    sino
        retornar falso
    fin si

    inicio
    aeronaves = []
    contador = 0

    mientras verdadero
        mostrar: "Aeronave {contador + 1}"
        ingresar matricula
        ingresar modelo
        ingresar horas_vuelo

        aeronave = {
            "matricula"   : matricula,
            "modelo"      : modelo,
            "horas_vuelo" : horas_vuelo,
            "componentes" : []
        }

        ingresar cantidad_componentes

        para i desde 1 hasta cantidad_componentes
            mostrar: "Componente {i}"
            ingresar nombre
            ingresar horas_uso
            ingresar limite

            componente = {
                "nombre"    : nombre,
                "horas_uso" : horas_uso,
                "limite"    : limite
            }

            aeronave["componentes"].agregar(componente)
        fin para

        aeronaves.agregar(aeronave)
        contador = contador + 1

        si contador >= 3
            ingresar opcion: "¿Agregar otra aeronave? (si/no): "
            si opcion == "no"
                break
            fin si
        fin si
    fin mientras

    mostrar: "REPORTE DE MANTENIMIENTO"

    para cada aeronave en aeronaves
        encabezado_impreso = falso
        para cada componente en aeronave["componentes"]
            si calcular_mantenimiento(componente["horas_uso"], componente["limite"])
                si encabezado_impreso == falso
                    mostrar: "Aeronave: {aeronave['matricula']}"
                    encabezado_impreso = verdadero
                fin si
                mostrar: "  Mantenimiento requerido: {componente['nombre']}"
                mostrar: "  Horas de uso: {componente['horas_uso']} / Limite: {componente['limite']}"
            fin si
        fin para
    fin para

    Fin