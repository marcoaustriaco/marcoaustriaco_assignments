products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    output = products[code]
    return output

def get_property(code,property):
    output = products[code][property]
    return output

def main():
    order = []
    while True:
        code_quantity = input('Please input product code and quantity (Example: cappuccino 1) : ')
        current_order_pair = code_quantity.split()
        current_order = current_order_pair[0]
        if code_quantity != "/":
            order.append(current_order_pair)
            continue
        else:
            break

    #we want the name of the orders w no duplicates
    exclusive = []
    for i in range(len(order)):
        name = order[i][0]
        exclusive.append(name)

    my_set = set(exclusive)
    exclusive = list(my_set)

    exclusive.sort()

    #we filter out orders if they have same name
    orders = []
    for i in exclusive:
        total = 0
        current_name = i
        for j in order:
            test_name = j[0]
            if current_name == test_name:
                quantity = j[1]
                total += int(quantity)
            else:
                continue
        orders.append([current_name,total])

    with open('receipt.txt','w') as f:
        f.write('==\n')
        f.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
        total = 0
        for i in range(len(orders)):
            current_product_code = orders[i][0]
            name = get_product(current_product_code)['name']
            quantity = orders[i][1] 
            price = get_product(current_product_code)['price']*int(quantity)
            total += price
            f.write(current_product_code + '\t\t' + name + '\t\t' + str(quantity) + '\t\t\t' + str(price)+'\n')
        f.write('\nTotal:\t\t\t\t\t\t\t\t\t'+str(total)+'\n')
        f.write('==')


main()
