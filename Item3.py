import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "KDOJMmEEgxR6hsAmFZkHKbPrAHlSOEIu"
locale = "es_ES" 
unit = "k"
while True:
    orig = input("Inicio del viaje desde: ('salida' o 's' para terminar) ")
    if orig == "salida" or orig == "s":
        break
    dest = input("Destino del viaje es : ")
    if dest == "salida" or dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "locale":locale, "unit":unit})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones viaje: " + (orig) + " a " + (dest))
        print("Duración del viaje:   " + (json_data["route"]["formattedTime"]))
        print ("Kilómetros:" + str ("{:.1f}" .format((json_data ["route"] ["distance"]))))
        print("=============================================")
    
        print("Las instrucciones del viaje son :")
        for i in json_data["route"]["legs"][0]["maneuvers"]:
            print(i["narrative"])
        
