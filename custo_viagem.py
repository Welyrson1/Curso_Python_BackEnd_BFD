def calcula_custo_viagem(distancia, consumo, preco_combustivel):
    resultado = (distancia / consumo ) * preco_combustivel
    return resultado

print("\n--- Calculadora de Custo de Viagem ---\n")

distanciaUsuario = float(input("Qual a distância a ser percorrida (km)? "))
consumoUsuario =  float(input("Qual o consumo do seu veículo (km/l)? "))
preco_combustivel_usuario = float(input("Qual o preço do litro do combustível (R$)? "))

if distanciaUsuario <= 0 or consumoUsuario <= 0 or preco_combustivel_usuario <= 0:
    print("Erro: os valores devem ser maiores que zero!")
else:
    custo_total_viagem = calcula_custo_viagem(distanciaUsuario, consumoUsuario, preco_combustivel_usuario)
    print(f"O custo total da viagem de {distanciaUsuario} km é: R${custo_total_viagem:.2f}")
