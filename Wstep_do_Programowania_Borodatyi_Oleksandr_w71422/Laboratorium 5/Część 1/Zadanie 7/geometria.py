# geometria.py

PI = 3.14159  # Стала PI

def obwod_kola(promien):
    """
    Функція обчислює обвіт кола з заданим радіусом.
    """
    return 2 * PI * promien

def pole_kola(promien):
    """
    Функція обчислює площу кола з заданим радіусом.
    """
    return PI * promien ** 2
