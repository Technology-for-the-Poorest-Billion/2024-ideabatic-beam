import json
def updateJson(constantsFile):
    """
    Loads the JSON file at /constantsFile, returns. If there is no file, makes an empty one.
    """
    try:
        with open(constantsFile, 'r') as f:
            return json.load(f)
    except:
        with open(constantsFile, "w") as f:
            json.dump({}, f)
            return {}
            
        
def dumpJson(constantsFile, constantsJson):
    """
    Dumps the contents of constantsJson into the JSON file at /constantsFile
    """
    with open(constantsFile, 'w') as f:
        json.dump(constantsJson, f)
    

#Uncomment the below, then run the code to update variables.

#constants = updateJson('constants.json')
#constants["Qtotal"] = 868400 # Energy required to melt the ice pack (J)
#constants["area"] = 0.179 # Area over which the heat is lost, relevant to flux calculations (m^2)
#constants["Rth"] = 9.715 # Thermal resistance of cooler (ohms)
#constants["tdelta"] = 5 * 60 # Time between measurements (seconds)
#constants["lastQ"] = 0 # Time between measurements (seconds)
#dumpJson('constants.json', constants)
