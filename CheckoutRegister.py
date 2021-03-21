class CheckoutRegister:
    purchased_product = []
    total_price = []
    total_weight = []
    
    def __init__(self):
        pass

    @staticmethod
    def accept_payment(prompt):
        price = float(0.0)
        while True:
            try:
                price = float(input(prompt))

                if price<0.0:
                    print("We don't accept negative money")
                    continue
                break

            except ValueError:
                print('Please enter a valid floating point value.')
        return price

    @staticmethod
    def print_receipt(amount_received, payment_due, purchased_product, total_price):
        print("\n\n----- Final Receipt -----\n")
        i = 0
        for product in purchased_product:
            print("\n{}: ${}".format(purchased_product[i], total_price[i]))
            i += 1
        print("\nTotal amount due: ${}".format(payment_due))
        print("\nAmount received: ${}".format(amount_received))
        if payment_due < amount_received:
            print("\nChange given: ${}".format(amount_received - payment_due))
                
        print("\nThank you for shopping at FedUni!")
        
                
                

    
        
        
