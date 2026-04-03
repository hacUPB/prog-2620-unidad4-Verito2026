# Lista principal
aeronaves = []    #Creamos una lista vacía en la que se alacenarán todas las aeronaves

contador = 0


# Para registrar una aeronave:
while True:
    
    print(f"\nAeronave {contador + 1}")         #Imprime la palabra aeronave junto al numero de aeronave que se está registrando
    
    #Pedimos la información de la aeronave al usuario
    matricula = input("Por favor ingrese la matricula de la aeronave: ")
    modelo = input("Por favor ingrese el modelo de la aeronave: ")
    horas_vuelo = float(input("Por favor ingrese las horas de vuelo: "))
    
    #La información se almacena en un diccionario llamado aeronave
    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": []      #Se crea una lista vacía para que posteriormente pidamos los datos que se alamacenarán aquí
    }
    
    #Pedimos los datos que se alamacenarán el la lista componentes
    cantidad_componentes = int(input("Número de componentes: "))    #Le pedimos al usuario que ingrese el numero de componentes que desea registrar
    
    for i in range(cantidad_componentes):                           #Bucle for que se repite de acuerdo a la cantidad de componentes que el usuario ingrese
        print(f"\nComponente {i + 1}")
        
        #Pedimos que inrgrese la información de los componentes
        nombre = input("Por favor ingrese el nombre del componente: ")
        horas_uso = float(input("Por favor ingrese las horas de uso del componente: "))
        limite = float(input("Por favor ingrese el límite de horas: "))
        #Esos datos se alacenan en el diccionario componente
        componente = {
            "nombre": nombre,
            "horas_uso": horas_uso,
            "limite": limite
        }
        #Ese diccionario  se almacenará en la lista vacía componentes
        aeronave["componentes"].append(componente)
    
    #Finalmente esa aeronave, con toda su información se almacenará en la lista aerolinea
    aeronaves.append(aeronave)

    #Termina un ciclo entonces se le suma uno
    contador += 1
    
    # Minimo se deben ingresar tres aeronaves, entonces...
    if contador >= 3:
        opcion = input("\n¿Agregar otra aeronave? (si/no): ")
        if opcion == "no":
            break


#Para el reporte..

print("\nREPORTE DE MANTENIMIENTO")

for aeronave in aeronaves:
    print("\nAeronave:", aeronave["matricula"])
    
    for componente in aeronave["componentes"]:
        if componente["horas_uso"] > componente["limite"]:
            print("Mantenimiento:", componente["nombre"])