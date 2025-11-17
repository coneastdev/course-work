total_patients = 0

def add_patient():
    global total_patients
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)
    return total_patients + 1

total_patients = add_patient()

def view_total():
    print("Total patients:", total_patients)

view_total()