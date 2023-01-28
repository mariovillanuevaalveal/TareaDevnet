import requests
import json
requests.packages.urllib3.disable_warnings()


url = "https://172.16.1.102/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"
auth =('cisco',"cisco123!")
payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback99",
    "description": "Creada por Python",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "99.99.99.99",
          "netmask": "255.255.255.255"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
 # 'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}
try:
    response = requests.request("PUT", url, headers=headers, data=payload,auth=auth,verify=False)
    print(response.text)
except:
    print ("Hubo un error en la implementación ")