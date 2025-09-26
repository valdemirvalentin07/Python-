def salvar_carros(marca, modelo, ano, placa):
    # Salva carro no banco de dados...
    print(f"Carro inserido com sucesso!\n{marca}/{modelo}/{ano}/{placa}")
    
#salvar_carros("Fiat","Palio",1999,"ABC-1234") #Neste primeiro exemplo pode ocorrer uma mudança dos valores e python vai interpretar do mesmo modo

#salvar_carros(marca = "Fiat",modelo="Palio",ano= 1999, placa="ABC-1234") 

# Se a variavel mudar dentro do def o python não consegue interpretar

salvar_carros(**{"marca": "Fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})