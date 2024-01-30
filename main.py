
def validate_float(number: float, minimo_por_caja: int):
    """Validate that the number we get from the user is valid (at least from the perspective of the
    "factura" we would generate)

    Args:
        number (float): The input from the user that (at this point) we know is a number, but we need
        to be equal or greater than one.
        minimo_por_caja (int): The price in market that will be used as the base price to generate the amount in the
        factura.

    Returns:
        True if the number meets the criteria, False otherwise.
    """
    if number >= float(minimo_por_caja):
        return True
    else:
        return False


def jitomatizante(pesos, centavos, diferencia, costo_maximo_caja=469, costo_minimo_caja=180):
    """
    Uses the information from the amount to determine different ways to create the "factura"

    Args:
        pesos (int): from the original amount the integers.
        centavos (float): the remainder if we take away the integer part of the original amount.
        diferencia (int): a local variable that we use when the amount cannot be contained in the max or minimum
        costo_maximo_caja (int): upper limit that we use to bill a single tomato box
        costo_minimo_caja (int): lower limit that we use to bill a single tomato box

    Returns:
        Prints to the output the different scenarios that can be used to bill the amount.
    """
    encontre_respuesta = False
    for valor_caja in range(costo_maximo_caja, costo_minimo_caja, -1):
        if pesos % valor_caja == 0:
            if diferencia > 0:
                print(f"   BINGO!!! \n"
                      f"      Sólo necesitas hacer una factura con los siguientes montos: \n"
                      f"     {int(pesos / valor_caja) - 1} cajas a un costo de ${valor_caja}.00 \n"
                      f"      1 caja  a un costo de ${valor_caja - diferencia + centavos:.2f}")
                encontre_respuesta = True
                continue
            elif centavos == 0.00:
                print(f"   BINGO!!! Sólo necesitas hacer una factura por {int(pesos / valor_caja)} "
                      f"cajas a un costo de ${valor_caja}.00")
                encontre_respuesta = True
            else:
                print(f"   BINGO!!! \n"
                      f"      Sólo necesitas hacer una factura con los siguientes montos: \n"
                      f"     {int(pesos / valor_caja) - 1} cajas a un costo de ${valor_caja}.00 \n"
                      f"      1 caja  a un costo de ${valor_caja + centavos:.2f}")
                encontre_respuesta = True
    if encontre_respuesta is True:
        return
    else:
        diferencia += 1
        pesos += 1
        jitomatizante(pesos, centavos, diferencia)


def separa_pesos_centavos(cantidad: float):
    """Since this is modeling an amount of money, we need to split the complete pesos from the centavos

    Args:
        cantidad (float): This is the original amount that we need to split.

    Returns:
        tuple:
            pesos (int) This is the integer part of the number.
            centavos (float) The decimals and remaining from the original amount.
    """
    centavos = round(cantidad % 1, 2)
    pesos = int(cantidad // 1)
    return pesos, centavos


def main(costo_minimo_por_caja: int = 179):
    while True:
        try:
            cantidad_por_facturar = float(input("¿Cantidad a facturar? : "))
        except ValueError:
            print("Sorry, solo puedo facturar numeros.")
            continue
        else:
            if validate_float(cantidad_por_facturar, costo_minimo_por_caja):
                break
            else:
                print("Sorry, ese no es un numero que podemos facturar.")
                continue
    cantidad_por_facturar = round(cantidad_por_facturar, 2)
    print(f"Entendido, vamos a intentar jitomatizar la cantidad de : ${cantidad_por_facturar:.2f}")
    pesos, centavos = separa_pesos_centavos(cantidad_por_facturar)
    print(f"La factura es por {pesos} pesos con {centavos:.2f} centavos.")
    diferencia = 0
    jitomatizante(pesos, centavos, diferencia, costo_minimo_caja=costo_minimo_por_caja)


if __name__ == "__main__":
    main()
