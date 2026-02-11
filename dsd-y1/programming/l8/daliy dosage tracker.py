# Track total mg of paracetamol given today
total_mg = 0

def record_dose(mg):
    print("Recorded dose:", mg, "mg. Total today:", total_mg, "mg")
    return total_mg + mg

total_mg = record_dose(250)
total_mg = record_dose(250)
print("Final total:", total_mg)
