import requests
import json 
# ------------------------------------------

infoip = "IP INFO:\n"
erro = "Error, no requests possible"
info = "Inquery IP Software - v1.0"

# ------------------------------------------

ip = input("What IP? \n> ")
api_ip_info = f"https://ipinfo.io/{ip}/json"
collect = requests.get(api_ip_info)

# ------------------------------------------

    
def  save_to_json(data, filename =f"{ip}_info.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
# ------------------------------------------

if collect.status_code == 200:
    getinfos = collect.json()
    print(infoip)
    print(getinfos)
    save_to_json(getinfos)
else:
    print(erro)
