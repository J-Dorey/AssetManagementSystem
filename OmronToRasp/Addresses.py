import yaml

# loads data from config.yaml into a dictionary
def loadConfig(config_location):
    with open(config_location, 'r') as file:
        addresses = yaml.safe_load(file)

    for k, v in addresses.items():
        addresses[k] = bytes(v)

    return(addresses)
