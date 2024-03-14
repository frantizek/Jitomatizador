from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("Jitomatizador")


def validar_entrada(texto):
    """
    Valida si el texto dado es un número válido.

    Args:
    texto (str): El texto a validar.

    Returns:
    bool: True si el texto es un número válido, False en caso contrario.
    """

    try:
        # Convertir el texto a un número de punto flotante
        float(texto)
        if float(texto) == 0.0:
            return False
    except ValueError:
        # Si no se puede convertir a un número de punto flotante, no es un número válido
        return False

    # Si el texto es una cadena vacía, no es un número válido
    if not texto:
        return False

    # Si el texto contiene letras, no es un número válido
    if any(letra.isalpha() for letra in texto):
        return False

    return True


def separa_pesos_centavos(cantidad: float) -> tuple:
    """Since this is modeling an amount of money, we need to split the complete pesos from the centavos

    Args:
        cantidad (float): This is the original amount that we need to split.

    Returns:
        a tuple of (int, float)

        pesos (int) This is the integer part of the number.

        centavos (float) The decimals and remaining from the original amount.
    """
    centavos = round(cantidad % 1, 2)
    pesos = int(cantidad // 1)
    return pesos, centavos


def jitomatizante(pesos: int, centavos: float, diferencia: int,
                  costo_maximo_caja: int = 280, costo_minimo_caja: int = 101) -> str:
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
    line = "\n"
    for valor_caja in range(costo_maximo_caja, costo_minimo_caja, -1):
        if pesos % valor_caja == 0:
            if diferencia > 0:
                line += (f"\nPuedes hacer una factura con los siguientes montos: \n "
                         f"{int(pesos / valor_caja) - 1} cajas a un costo de ${valor_caja}.00 \n"
                         f"   1 caja  a un costo de ${valor_caja - diferencia + centavos:.2f}\n\n")
                encontre_respuesta = True
                continue
            elif centavos == 0.00:
                line += (f"\nPuedes hacer una factura por {int(pesos / valor_caja)} "
                      f"cajas a un costo de ${valor_caja}.00\n\n")
                encontre_respuesta = True
            else:
                line += (f"\n"
                      f"Puedes hacer una factura con los siguientes montos: \n"
                      f"     {int(pesos / valor_caja) - 1} cajas a un costo de ${valor_caja}.00 \n"
                      f"        1 caja  a un costo de ${valor_caja + centavos:.2f}\n\n")
                encontre_respuesta = True
    if encontre_respuesta is True:
        return str(line)
    else:
        diferencia += 1
        pesos += 1
        return jitomatizante(pesos, centavos, diferencia)


def carga_jitomatizador():

    Output.delete('1.0', END)
    if validar_entrada(inputtxt.get("1.0", "end-1c")):
        cantidad_por_facturar = float(inputtxt.get("1.0", "end-1c"))
        pesos, centavos = separa_pesos_centavos(cantidad_por_facturar)
        TerribleLongAnswer = f"La factura es por {pesos} pesos con {centavos:.2f} centavos."
        diferencia = 0

        Output.insert(END, TerribleLongAnswer + "\n" + str(jitomatizante(pesos, centavos, diferencia)))


l = Label(text="\n¿Cantidad a facturar? \n")

inputtxt = Text(root, height=1,
                width=15, undo=True, wrap=NONE,
                bg="light yellow")

Output = Text(root, height=24,
              width=60,
              bg="white")

Display = Button(root, height=1,
                 width=20,
                 text="Jitomatiza",
                 command=lambda: carga_jitomatizador())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
