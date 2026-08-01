import functools
from datetime import datetime


# 1. Defina o decorador PRIMEIRO
def log_transacao(func):

    @functools.wraps(func)
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"\n[LOG] [{data_hora}] Função '{func.__name__.upper()}' executada.")
        return resultado

    return envelope


# 2. Agora sim você pode usá-lo nas funções
@log_transacao
def depositar():
    pass