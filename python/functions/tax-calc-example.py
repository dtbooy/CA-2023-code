#-------------------Max-line-length-is-72-characters-------------------|

#Declare constants / variables at the top
# TAX_RATE is in ALL CAPS to indicate it is a constant and 
# SHOULD NOT BE CHANGED
TAX_RATE = 0.1 
FLAT_SHIPPING = 10

#Define your functions next
def add_tax(amount):
    total = amount *(1+TAX_RATE)
    return total

def add_shipping(amount):
    return amount + FLAT_SHIPPING

def calc_grand_total(amount):
    return add_tax(add_shipping(amount))

#do your sequencial programming at the bottom

#Main
subtotal = float(input("Subtotal: $")) #input
grand_total = calc_grand_total(subtotal) #processing
print(f"Total: ${grand_total:.2f}") #output


