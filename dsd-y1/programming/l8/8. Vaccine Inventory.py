# Clinic vaccine stock (single brand for simplicity)
stock = 50

def dispense(doses):
    print("Dispensed:", doses, "Remaining:", stock)
    return stock - doses

def restock(amount):
    print("Before restock:", stock)
    print("After restock:", stock + amount)
    return stock + amount

stock = dispense(5)
stock = restock(10)
print("End of day stock:", stock)
