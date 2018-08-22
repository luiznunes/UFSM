def codificaMensagem(mensagem, codificacao):
    lista_msg = list(mensagem)
    mensagem = mensagem.lower()
    mapeamento = codificacao.lower()

    for i in range(len(lista_msg)):
        letra = mensagem[i]
        index = alfabeto.lower().find(letra)
        if letra != " ":
            lista_msg[i] = mapeamento[index]

    return ''.join(lista_msg)


alfabeto = "abcdefghijklmnopqrstuvwxyz"
mapeamento = "zyxwvutsrqponmlkjihgfedcba"
mensagem = "meNsagem teStE"

print("Mensagem original: "+mensagem)
mensagem_codificada = codificaMensagem(mensagem, mapeamento)
print("Mensagem codificada: "+mensagem_codificada)
