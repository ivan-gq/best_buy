import products
import store

def print_menu():
    print("\tStore Menu\n\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def make_order(best_buy):
    prods = best_buy.get_all_products()
    order = []
    # Use enumerate for cleaner indexing
    for i, product in enumerate(prods, start=1):
        if product.active:
            print(f"{i}. {product.name}, price: ${product.price}, quantity: {product.quantity}")
    while True:
        menu_choice = input("Select # of product: ")
        if not menu_choice:
            break
        try:
            prod_index = int(menu_choice)
            if not (0 < prod_index < len(prods)+1):
                print("Error: Product number out of range.")
                continue

            selected_product = prods[prod_index - 1]
            quantity = int(input("Enter amount: "))

            if quantity <= 0:
                print("Error: quantity must be greater the zero")
                continue

            if quantity >= selected_product.quantity and selected_product.active:
                quantity = selected_product.quantity
                print("Stock is empty. Adjusting to remaining stock.")
                order.append((selected_product, quantity))
                selected_product.buy(quantity)
                selected_product.deactivate()

            elif selected_product.active:    
                order.append((selected_product, quantity))
                selected_product.buy(quantity)
                print(f"Added {selected_product.name}, quantity: {quantity}")

            else:
                print("Product sold out")            

        except ValueError:
            print("Value Error")
    if order:        
        print("---ORDER SUMMERY---")
        for item, qty in order:
            print(f"Item: {item.name}, Quantity: {qty}")

def main():
    # setup initial stock of inventory
    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                ]
    best_buy = store.Store(product_list)

    while True:
        print_menu()
        try:
            menu_choice = int(input("Please choose a number: "))
            if menu_choice == 1:
                print("------")
                for product in best_buy.get_all_products():
                    product.show()
                print("------")

            elif menu_choice == 2:
                print(best_buy.get_total_quantity())

            elif menu_choice == 3:
                make_order(best_buy)

            elif menu_choice == 4:
                print("bye bye!!!")
                break

            else:
                print("number must be in menu")
        except ValueError:
            print("Value Error: Type a number")

if __name__ == "__main__":
    main()