def calculando_imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado
 
    
print("Bem-vindo(a) a calculadora de IMC")
print("Para número decimais utilize '.'(ponto) como separador decimal! ")

pesoUsuario = float(input("Digite seu peso(kg): "))
alturaUsuario = float(input("Digite sua altura(m): "))

imcUsuario = calculando_imc(pesoUsuario, alturaUsuario)

print(f"Seu indice de massa corporal é: {imcUsuario:.2f}")