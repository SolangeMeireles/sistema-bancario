import functools
from datetime import datetime


def log_transacao(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)

        # Captura a data e hora atual no formato DD-MM-AAAA HH:MM:SS
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Nome da função executada
        nome_funcao = func.__name__.upper()

        # Print do log
        print(f"\n[LOG] [{data_hora}] Função '{nome_funcao}' executada.")

        return resultado

    return envelope