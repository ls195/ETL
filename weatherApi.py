import requests
import stadt as Stadt_klasse
# ETL:                                  Extract Transform Load
# Anlegen einer venv:                   python -m venv venv
# Venv aktivieren:                      venv\Scripts\activate
# request Bibliothek installieren:      python -m pip install requests       https://www.datacamp.com/tutorial/making-http-requests-in-python

# 1. EXTRACT:

base_url = "https://api.weatherapi.com/v1/current.json?key=aBCD="      # hier Key noch auslagern (GOOGLEN wir das gemacht wird)


cities = ["Koeln", "Berlin", "Munich"]

end_url = "&aqi=no"


responses = {}

for city in cities:
    full_url = f"{base_url}{city}{end_url}"
    responses[city] = requests.get(full_url).json()


print(type(responses))  
for city in responses:
    # Die Daten die hier ausgegeben werden sind wichtig für die Tabelle und sollen ggf. in ein Objekt überfürt werden
    print(f"_____________")

    # print(f"Name:\t\t\t\t\t\t{responses[city]['location']['name']}")   
    # print(f"Bundesland:\t\t\t\t\t{responses[city]['location']['region']}") 
    # print(f"Zeit der Angabe:\t\t\t\t{responses[city]['location']['localtime']}")
    # print(f"Temperatur in Abhängigkeit der Zeit:\t\t{responses[city]['current']['temp_c']}")  
    stadt_name = responses[city]['location']['name']
    stadt_name = Stadt_klasse.Stadt(
        responses[city]['location']['name'], 
        responses[city]['location']['region'], 
        responses[city]['location']['localtime'], 
        responses[city]['current']['temp_c']
        )
    
    print(f"Name der Stadt als Klasse: {stadt_name.name}")
    print(f"Bundesland der Stadt als Klasse: {stadt_name.region}")
    print(f"Zeit der Stadt als Klasse: {stadt_name.localtime}")
    print(f"Temperatur der Stadt als Klasse: {stadt_name.temp_c}")

print(f"Insgesamt wurden {Stadt_klasse.Stadt.staedte_insgesammt} Staedte angelegt.")
print("_____________\nEnde")


# TRANSFORM
# jetzt möchten wir die Zeit ändern und zwar ins deutsche Format

from datetime import datetime
date = ""




# LOAD
# Daten in eine neue Datenbank laden
