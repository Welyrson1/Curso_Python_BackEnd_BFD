def calculate(num_one, num_two, operator):
    match operator:
        case "+":
            result = num_one + num_two
        case "-":
            result = num_one - num_two
        case "*":
            result = num_one * num_two
        case "/":
            result = num_one / num_two
        case "**":
            result = num_one ** num_two
        case "//":
            result = num_one // num_two
        case "%":
            result = num_one % num_two
    return result
def validating_operator(operator):
    operators_list = ["+", "-", "*", "/", "//", "**", "%"]
    if operator in operators_list:
        return True
    else:
        return False
def division_by_zero(operator, num_two):
    if operator in ("/", "//", "%") and num_two == 0:
        return True
    else:
        return False 
    
def even_or_not(number):
    if number%2 == 0:
        answer = "PAR"
    else:
        answer = "ÍMPAR"
    return answer
def positive_or_negative(number):
    if number > 0:
        answer = "POSITIVO"
    elif number < 0:
        answer = "NEGATIVO"
    else:
        answer = "VALOR NULO (0)"
    return answer
def show_menu():
    print("\n--- Calculadora Aritmética ---\n")
    print("Menu:")
    print("0 → Encerrar")
    print("1 → Calcular\n")
def show_option():
    print("Operadores disponíveis:\n"
      "+  → soma\n"
      "-  → subtração\n"
      "*  → multiplicação\n"
      "/  → divisão\n"
      "// → divisão inteira\n"
      "** → potência\n"
      "%  → resto da divisão\n")

while True:
    show_menu()
    option = int(input("O que você deseja fazer? "))

    if option == 0:
        print("ENCERRANDO CALCULADORA...")
        break
    elif option == 1:
        show_option()
        number_one = float(input("Digite o primeiro número: "))
        operator_typed = str(input("Digite o operador: "))
        number_two = float(input("Digite o segundo número: "))

        if validating_operator(operator_typed):
            if division_by_zero(operator_typed, number_two):
                print("IMPOSSÍVEL DIVIDIR POR 0!")
            else:
                result = calculate(number_one, number_two, operator_typed)
                print(f"\nRESULTADO: {number_one} {operator_typed} {number_two}  = {result:.2f}")
                print(f"O número {result:.2f} é {even_or_not(result)} e {positive_or_negative(result)}\n")
        else:
            print("DIGITE UM OPERADOR VÁLIDO!")
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        continue