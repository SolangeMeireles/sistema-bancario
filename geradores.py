def gerador_relatorio(transacoes, tipo_transacao=None):
    for transacao in transacoes:
        # Se um tipo específico for informado, filtra; caso contrário, traz todas
        if (
            tipo_transacao is None
            or transacao["tipo"].lower() == tipo_transacao.lower()
        ):
            yield transacao