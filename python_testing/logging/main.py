import logging

# NIVEL DE PRIORIDAD QUE POSEE CADA MENSAJE
# DEBUG = 10 = debug
# INFO = 20 = info
# WARNING = 30 = warning
# ERROR = 40 = error
# CRITICAL = 50 = critical

# Solo se imprimen los mensajes cuyo nivel sea mayor a 30
# Definiendo el formato de los mensajes.

logging.basicConfig(level=logging.INFO,
                    format='%(threadName)s - %(levelname)s - %(asctime)s - Message: %(message)s',
                    datefmt='%Y/%m/%d',

                    # Creacion de un archivo .log
                    filename='codigo.log',
                    filemode='a')


def sumar_dos_numeros(x: int, y: int) -> int:
    """Funcion que suma dos numeros enteros positivos

    Args:
        x (int): primer numero
        y (int): segundo numero

    Returns:
        int: resultado de la suma
    """

    logging.debug('Entramos aqui.')
    z = x + y
    logging.debug('Nos encontramos en esta linea.')

    return z


if __name__ == '__main__':

    logging.debug('Antes del llamado de la funcion.')

    resultado = sumar_dos_numeros(10, 30)
    logging.info(resultado)
