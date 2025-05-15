#funciones a usar

def calcular_propina():
 while True: 
    print('''\n\n============================================
=          Cálculo de Propina              =
============================================''')

    try:
        monto_total = float(input("Ingrese el monto total de la cuenta: $ "))
        porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo: 15): % "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

    total_propina = monto_total * (porcentaje_propina / 100)
    total_pagar = monto_total + total_propina

    print("============================================")
    print(f"La propina calculada es: ${total_propina:.2f}")
    print(f"El total a pagar es: ${total_pagar:.2f}")
    print("============================================\n")
    
    continuar = input("¿Deseas calcular nuevamente? (S/N): ")
    if continuar.lower() != "s":
        print("Saliendo...")
        break


def dividir_total():
 while True:
    print('''\n\n============================================
   Dividir Cuenta entre Varias Personas
============================================''')
    
    try:
        monto_total = float(input("\nIngrese el monto total de la cuenta: $ "))
        porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo: 15): % "))
        personas = int(input("Ingrese el número de personas: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return

    total_propina = monto_total * (porcentaje_propina / 100)
    total_pagar = monto_total + total_propina
    monto_persona = total_pagar / personas

    print("\n============================================")
    print(f"La propina calculada es: ${total_propina:.2f}")
    print(f"El total a pagar es: ${total_pagar:.2f}")
    print(f"Monto por persona: ${monto_persona}")
    print("============================================\n")

    continuar = input("¿Deseas calcular nuevamente? (S/N): ")
    if continuar.lower() != "s":
        print("Saliendo...")
        break
    

def salir():
    print('''\n=============================================
 ¡Gracias por usar el Simulador de Propina!
=============================================\n''')