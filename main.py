from Product import Product
from CheckoutRegister import CheckoutRegister

print("----- Welcome to FedUni checkout! -----")

def add(l):
    j = 0
    for i in l:
        j+=i
    return j

def main():
    choice = 'n'
    while( choice == 'n'):
    
        #Creating product instances
        product_list = []
        product_name = ["Milk", "Bread", "Eggs", "Apple"]
        barcode = [123, 456, 789, 111, 222]
        price = [2, 1.5, 3, 3.5]
        weight = [2, 1, 2.5, 3]
        i = 0
        for _ in product_name:
            obj = Product(barcode[i], product_name[i], price[i], weight[i])
            product_list.append(obj)
            i += 1

        #Scannig Product
        CheckoutRegister.purchased_product = []
        CheckoutRegister.total_price = []
        CheckoutRegister.total_weight = []
        ch = 'y'
        while(ch == 'y'):
            j = 0
            flag = 0
            b = int(input("Please enter the barcode of your item:"))
            for i in barcode:
                if b == i:
                    print('{} - ${}'.format(product_list[j].name, product_list[j].price))
                    CheckoutRegister.purchased_product.append(product_list[j].name)
                    CheckoutRegister.total_price.append(product_list[j].price)
                    CheckoutRegister.total_weight.append(product_list[j].weight)
                else:
                    flag += 1
                j += 1

            if flag == len(barcode):
                print("This product does not exist in our inventory")
            ch = input("Would you like to scan another product? (Y/N) ")

        #Payment
        payment_due = add(CheckoutRegister.total_price)
        temp_payment_due = payment_due
        print (payment_due)
        price = 0
        amount_received = 0
        while (temp_payment_due > 0) | (temp_payment_due > price):
            prompt = "Payment due: ${} Please enter an amount to pay:".format(temp_payment_due)
            price = CheckoutRegister.accept_payment(prompt)
            temp_payment_due -= price
            amount_received += price

        #Display
        CheckoutRegister.print_receipt(amount_received, payment_due, CheckoutRegister.purchased_product, CheckoutRegister.total_price)

        choice = input("(N)ext customer, or (Q)uit? q ")

if __name__ == "__main__":
    main()



    

