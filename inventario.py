#Adicionar item, Remover item, Listar inventário, Atualizar inventario e Sair.
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    print("\n🔧 MENU")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar inventário")
    print("4. Atualizar item")
    print("5. Sair\n")
def add_item(dictionary, item, quantity):
    if item in dictionary:
        resposta = input(f"O item '{item}' já está no inventário com quantidade {dictionary[item]}. Deseja atualizar o valor? (s/n): ").lower()
        if resposta == 's':
            dictionary[item] = quantity
            print(f"Item '{item}' atualizado para {quantity}.")
        else:
            print("Atualização cancelada.\n")
    else:
        dictionary[item] = quantity
        print(f"Item '{item}' adicionado com quantidade {quantity}.\n")
def remove_item(dictionary, index):
    for i, (key, _) in enumerate(dictionary.items(), start=1):
        if i == index:
            del dictionary[key]
            print(f"Item '{key}' removido com sucesso!")
            break
def list_inventory(inventory, name):
    if inventory:
        print(f"\n Inventário: {name}")
        for index, (item, quantity) in enumerate(inventory.items(), start=1):
            print(f"{index}. {item} — Quantidade: {quantity}")
    else:
        print("Inventário vazio\n")
def update_inventory(dictionary, index, new_value):
    for i, (key, value) in enumerate(dictionary.items(), start=1):
        if i == index:
            dictionary[key] = new_value
            break

print("--------- Bem vindo ao gerenciador de inventario! ---------")
name_inventory = input("Qual o nome do seu inventário? ")
main_inventory = dict()
while True:
    show_menu()
    try:
        action = int(input("\nO que voce deseja fazer? "))
        if action == 1:
            while True:
                print("Para parar de adicionar itens digite: s")
                item = input("Digite o item: ").capitalize()
                if item == 'S':
                    break
                else:
                    quantity = int(input("Digite a quantidade: "))
                    add_item(main_inventory, item, quantity)
        elif action == 2:
            list_inventory(main_inventory, name_inventory)
            item_index = int(input("\nDigite o número do elemento que voce deseja remover: "))
            if item_index > 0 and item_index <= len(main_inventory):
                remove_item(main_inventory, item_index)
            else:
                print(f"O inventário não possui um valor com indice {item_index}")
        elif action == 3:
            list_inventory(main_inventory, name_inventory)
        elif action == 4:
            list_inventory(main_inventory, name_inventory)
            item_index = int(input("\nDigite o número do elemento que voce deseja atualizar: "))
            if item_index > 0 and item_index <= len(main_inventory):
                new_item_value = int(input("Digite o valor por qual valor voce quer atualizar: "))
                update_inventory(main_inventory, item_index, new_item_value)
            else:
                print(f"O inventário não possui um valor com indice {item_index}")
                continue
        elif action == 5:
            print("\nSaindo do programa...")
            break
        else:
            print("\nDigite apenas os numeros do menu!")
    except ValueError:
        print("\nEsse não é um número válido, digite apenas entre 1 e 5")

    input("\nPressione Enter para continuar...")
    limpar_tela()
        
        

