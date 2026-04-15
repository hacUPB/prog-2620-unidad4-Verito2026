# Lista principal donde se almacenan todas las aeronaves
Aeronaves = []

# Mensaje inicial del sistema
print(" SISTEMA DE MANTENIMIENTO AERONÁUTICO ")

# Hacemos un bucle infinito para que el menú se repita hasta que el usuario decida salir
while True:
    
    # Mostrar las opciones disponibles al usuario
    print("\n--- MENÚ ---")
    print("1. Registrar aeronave")
    print("2. Registrar componente")
    print("3. Modificar aeronave")
    print("4. Ver reporte de mantenimiento")
    print("5. Salir")  

    # Pedir al usuario que seleccione una opción
    opcion = input("¿Que opción deseas elegir?: ")

    
    # Si el usuario elige 1,registrar una nueva aeronave
    if opcion == "1":
        
        # Solicitamos los datos al usuario
        matricula = input("Por favor ingrese la matricula:")
        modelo = input("Por favor ingrese el modelo:")
        horas_vuelo = float(input("Por favor ingrese las horas de vuelo:"))
        
        # Creamos un diccionario para guardar esta información
        aeronave = {
            "matricula": matricula,
            "modelo": modelo,
            "horas_vuelo": horas_vuelo,
            "componentes": []  # Lista vacía donde se guardarán los componentes
        }

        # Preguntamos cuántos componentes quiere agregar
        num_componentes = int(input("¿Cuántos componentes desea registrar?: "))
        
        # Bucle for para que se repita la cantidad de veces que puso en la anterior pregunta
        for i in range(num_componentes):
            
            # Mostrar número del componente actual
            print("\nComponente", i + 1)

            # Solicitar datos del componente
            nombre = input("Ingrese el nombre del componente")
            horas_uso = float(input("Ingrese las horas de uso"))
            limite = float(input("Ingrese el limite de horas:"))

            # Crear diccionario del componente
            componente = {
                "nombre": nombre,
                "horas_uso": horas_uso,
                "limite": limite
            }

            # Agregar el diccionario del componente a la lista de componentes de la aeronave.
            aeronave["componentes"].append(componente)

        # Agregamos toda la info de la aeronave a la lista principal
        Aeronaves.append(aeronave)

        # Confirmación al usuario
        print("Hemos registrado tu aeronave correctamente")

    # Si el usuario elige 2,registramos un componente
    # Registrar un componente a una aeronave ya existente
    elif opcion == "2":
        
        # Verificar que exista al menos una aeronave
        if len(Aeronaves)==0:
            print("No hay ninguna aeronave registrada")
        else:
            # Pedir matrícula para identificar la aeronave
            matricula = input("Ingrese la matrícula: ")

            # Buscar la aeronave en la lista
            for a in Aeronaves:
                if a["matricula"] == matricula:
                    
                    # Solicitar datos del nuevo componente
                    nombre = input("Nombre del componente: ")
                    horas = float(input("Horas de uso: "))
                    limite = float(input("Límite: "))

                    # Crear el componente
                    comp = {
                        "nombre": nombre,
                        "horas_uso": horas,
                        "limite": limite
                    }

                    # Agregar componente a la aeronave encontrada
                    a["componentes"].append(comp)

                    print("Componente agregado")
                    break  # Termina la búsqueda

            else:
                # Se ejecuta si no se encontró la aeronave
                print("Aeronave no encontrada")

    # Si el usuario elige opción 3
    # Modificar los datos de una aeronave existente
    elif opcion == "3":
        
        # Validar que haya por lo menos una aeronave
        if len(Aeronaves)==0:
            print("No hay ninguna aeronave registrada")
        else:
            # Pedir matrícula de la aeronave a modificar
            matricula = input("Ingrese la matricula de la aeronave que quiere modificar")

            # Buscar la aeronave
            for a in Aeronaves:
                if a["matricula"] == matricula:
                    
                    # Reemplazar datos
                    a["matricula"] = input("Nueva matrícula: ")
                    a["modelo"] = input("Nuevo modelo: ")
                    a["horas_vuelo"] = float(input("Nuevas horas de vuelo: "))

                    print("Aeronave modificada")
                    break

            else:
                print("Lo sentimos, no encontramos esta aeronave")

    # Si el usuario elige la opción 4
    # Mostrar reporte de componentes que necesitan mantenimiento
    elif opcion == "4":
        
        # Validar que existan aeronaves
        if len(Aeronaves) == 0:
            print("No hay aeronaves registradas")
        else:
            print("\nComponentes que necesitan mantenimiento:")

    for aeronave in Aeronaves:
        print("\nAeronave:", aeronave["matricula"])

        for componente in aeronave["componentes"]:
            if componente["horas_uso"] >= componente["limite"]:
                print("Debe hacer mantenimiento a este componente:", componente["nombre"])
                        
           

    # ---------------- OPCIÓN 5 ----------------
    # Salir del programa
            elif opcion == "5":
                print("Saliendo del sistema...")
    break  # Rompe el while y termina el programa

    # ---------------- OPCIÓN INVÁLIDA ----------------
else:
        print("Opción inválida")