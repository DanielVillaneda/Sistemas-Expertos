def diagnosticar():
    print("=== Diagnostico de fallas en un automovil ===\n")
    arranca = input("¿Arranca el motor? (s/n): ")
    if arranca == "n":
        luces = input("¿las luces del tablero encienden? (s/n): ")
        if luces == "n":
            print("posible causa: batería descargada.")
        elif luces == "s":
            print("Posible causa: fallo en el motor de arranque.")

    elif arranca == "s":
        acelera = input("¿el auto se apaga al celerar (s/n): ")
        if acelera == "s":
            print("Posible causa: problema en el suministro de combustible.")
        else:
            humo = input("¿el auto tiene humo en el escape? (s/n): ")
            if humo == "s":
                color = input("¿de qué color es el humo: negro/blanco")
                if color == "negro":
                    print("posible causa: mezcla rica de combustible.")
                elif color == "blanco":
                    print("posible causa: falla en la junta de la culata")
            elif humo == "n":
                print("falla no detectada")

    print("\n===   Diagnostico de fallas finalizado   ===")

if __name__ == "__main__":
    diagnosticar()