def isprime(num) -> bool:
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def calcula_valor_caja(cantidad_por_facturar):
    for valor_caja in range(159, 491, 1):
        if cantidad_por_facturar == 0:
            return valor_caja
    return None



def main():
    cantidad = 5435.40+5139.34
    # cantidad_factura = float(input("¿Cantidad a facturar? : "))
    # cantidad_factura = int(4392.44)
    cantidad_factura = int(cantidad)
    # valor_real_factura = float(4392.44)
    valor_real_factura = float(cantidad)

    print(isprime(cantidad))

    encontre_una_solucion = False
    cantidad_por_compensar = 0
    existe_remanente = False

    print(f"Total a facturar {valor_real_factura:.2f} = {cantidad_factura} + {(valor_real_factura-float(cantidad_factura)):.2f} (diferencia de 1 caja) ")

    if (valor_real_factura-float(cantidad_factura)) != 0:   
        existe_remanente = True

    # while encontre_una_solucion == False:

    #     valor_caja =calcula_valor_caja(cantidad_factura)

    #     if  valor_caja != None:
    #         encontre_una_solucion = True
    #     else:
    #         cantidad_por_compensar += 1
    #         cantidad_factura -= 1

    for valor_caja in range(154, 499, 1):
        if cantidad_factura%valor_caja == 0:
            encontre_una_solucion = True
            # Si encontramos las n combinaciones se van a mostrar aqui
            # en el "peor" de los casos y considerando las cantidades puede que sea entre 10
            if existe_remanente:
                print(f" BINGO!!! \nSólo necesitas hacer una factura con los siguientes montos: \n     {int(cantidad_factura/valor_caja)-1} cajas a un costo de ${valor_caja}.00 \n      1 caja  a un costo de ${valor_caja+valor_real_factura-float(cantidad_factura):.2f}")
            else:
                print(f" BINGO!!! Sólo necesitas hacer una factura por {int(cantidad_factura/valor_caja)} cajas a un costo de ${valor_caja}.00")
    # else:
    #     print(f" BINGO!!! \nSólo necesitas hacer una factura con los siguientes montos: \n     {int(cantidad_factura/valor_caja)-1} cajas a un costo de ${valor_caja}.00 \n      1 caja  a un costo de ${(valor_caja+cantidad_por_compensar)+(valor_real_factura-float(cantidad_factura)):.2f}")
                
        

if __name__ == "__main__":
    main()
