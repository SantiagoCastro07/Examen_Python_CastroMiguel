from funciones import calcular_propina, dividir_total, salir

while True:
    print("=============================================")
    print("=         SIMULADOR DE PROPINA              =")
    print("=============================================")
    print("1. Calcular propina y total a pagar")
    print("2. Calcular total a pagar divido entre varias personas")
    print("3. Salir")
    print("=============================================")

    opcion = int(input("\nPor favor, elige una opción (1-3): \n"))

    if opcion == 1:
        calcular_propina()
    elif opcion == 2:
        dividir_total()
    elif opcion == 3:
        salir()
        break
    else:
        print("Por favor, ingrese valores numéricos válidos.")