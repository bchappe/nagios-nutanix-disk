#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import sys

## host 
## utilisateur
## password
if "--help"  in sys.argv :
    print("Command ./request_nutanix_disk.py $IP $LOGIN $PASSWORD $PORT")
    exit(0)
try:
    host=sys.argv[1] ## Premiere commande
except:
    print("Problem: Missing argument, try ./request_nutanix_disk.py --help ") # Message si erreur
    exit(3)
try:
    user=sys.argv[2]
except:
    print("Problem: Missing argument, try ./request_nutanix_disk.py --help ")
    exit(3)
try:
    password=sys.argv[3]
except:
    print("Problem: Missing argument, try ./request_nutanix_disk.py --help ")
    exit(3)
try:
    port=sys.argv[4]
except:
    print("Problem: Missing argument, try ./request_nutanix_disk.py --help ")
    exit(3)

url = "https://"+user+":"+password+"@"+host+":"+port+"/PrismGateway/services/rest/v2.0/disks"

#print(url)

try:
    response = requests.get(url, verify=False)
except Exception as e:
    print(e)
    print("Connexion error")
    exit(2)


json_data = json.loads(response.text)
output="CRITICAL:Disks have a problem:"
status= 0
for element in json_data["entities"]: ## Tri du json en stockant dans variable le jsondata tableau elements
   # print(" Chemin " + element["mount_path"] + " - Status: " + element["disk_status"] + " - Online:" + str(element["online"]) + " - Cluster: " + element["node_name"])
    
    if element['disk_status'] != "NORMAL" or str(element['online']) != "True": 
        status=2
        output=output + str(element['mount_path']) +" "+ str(element['disk_status']) + " " + str(element['online']) + " " + element["node_name"]  + ", "
    
if status==0:
    output="Status: OK for Nutanix disk"
    print(output)
    exit(status)
else:
    print(output)
    exit(status)

