import kagglehub
import csv 
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("hm-land-registry/uk-housing-prices-paid")

with open(path + "/price_paid_records.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
        
