"""Simulación de una Máquina de Galton.

Simula 3,000 canicas que caen por 12 niveles de obstáculos. En cada nivel
la canica se desvía a la izquierda o a la derecha al azar, y al final se
muestra un histograma con la cantidad de canicas por contenedor.
"""

# Módulo estándar para tomar decisiones aleatorias (izquierda/derecha)
import random

# Paquete externo para crear el histograma
import matplotlib.pyplot as plt


def simular_canica(niveles=12):
    """Simula el recorrido de una sola canica a través de los niveles.

    En cada nivel, la canica se desvía a la izquierda o a la derecha
    con la misma probabilidad (50%). El contenedor final es la cantidad
    de veces que la canica se fue a la derecha.

    Args:
        niveles (int, opcional): Número de niveles de obstáculos.
            Por defecto es 12.

    Returns:
        int: Contenedor final donde cae la canica, entre 0 y `niveles`.
    """
    # La canica empieza en el contenedor 0 (extremo izquierdo)
    contenedor = 0

    # Una decisión aleatoria por cada nivel de obstáculos
    for _ in range(niveles):
        # Si va a la derecha, avanza un contenedor; si va a la izquierda, se queda
        if random.choice(["izquierda", "derecha"]) == "derecha":
            contenedor += 1

    # Se devuelve el contenedor final como número entero
    return contenedor


def simular_canicas(cantidad=3000, niveles=12):
    """Simula muchas canicas y guarda el contenedor final de cada una.

    Args:
        cantidad (int, opcional): Número de canicas a simular.
            Por defecto es 3000.
        niveles (int, opcional): Número de niveles de obstáculos.
            Por defecto es 12.

    Returns:
        list[int]: Lista con el contenedor final de cada canica.
    """
    # Lista donde se almacenan los resultados de todas las canicas
    resultados = []

    # Se lanza una canica por cada repetición del ciclo
    for _ in range(cantidad):
        resultados.append(simular_canica(niveles))

    return resultados


def graficar_resultados(datos, niveles=12):
    """Genera un histograma con la cantidad de canicas por contenedor.

    Args:
        datos (list[int]): Lista con el contenedor final de cada canica.
        niveles (int, opcional): Número de niveles usados en la simulación.
            Por defecto es 12.

    Returns:
        None: La función solo muestra el gráfico en pantalla.
    """
    # Una barra por cada contenedor posible (de 0 a `niveles`), centrada en su número
    plt.hist(datos, bins=range(niveles + 2), align="left", edgecolor="black")

    # Elementos de identificación del gráfico
    plt.title("Máquina de Galton: 3,000 canicas")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")

    # Se muestran todos los números de contenedor en el eje X
    plt.xticks(range(niveles + 1))

    # Se guarda una imagen del gráfico (útil para el README) y se muestra
    plt.savefig("histograma.png")
    plt.show()


# Punto de entrada: solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    # 1. Simular las 3,000 canicas
    resultados = simular_canicas()

    # 2. Graficar los resultados
    graficar_resultados(resultados)
