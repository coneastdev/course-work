import kagglehub

# Download latest version
path = kagglehub.dataset_download("hm-land-registry/uk-housing-prices-paid")

print("Path to dataset files:", path)