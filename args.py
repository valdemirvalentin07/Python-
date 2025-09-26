def exibir_frase(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados ="\n".join([f"{chave.title()}: {valor}"for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_frase( 
           
" Sexta-feira, 26 de setembro de 2025",
"Confia no senhor de todo coração e não te estribes no teu própio entendimento.",
autor = "Provérbios 3 - 5", )
    