---
---
# Plugin Nagios - Nutanix Disk

1. Script :
2. Nagios integration :

#

### 1. What do we have : <br> 
The script check if the nutanix statement for the disk is OK. He use a API
- $NUTANIX_API "GET" "/PrismGateway/services/rest/v2.0/disks" <br>
if element['disk_status'] != <b> "NORMAL" or str(element['online']) != "True": </b>

### 1. Script requirement <br>

- Python3 with standard library <br>
import requests, json, import sys <br>
- Nagios core or NagiosXI 
- Nutanix API with version 2. <br>
The script need a 4 parameters : $IP $LOGIN $PASSWORD $PORT

### 2. Configure in nagios <br>
- Download the script in your plugin directory (git clone or download).
> /usr/local/nagios/libexec/ ## For example

<br>

- Authorize the owner and groups nagios to launch it <br>
- Authorize the file to be execute
> chown apache:nagios request_nutanix_disk.py <br>
> -rwxr-xr-x apache nagios request_nutanix_disk.py 
<br><br>
> chmod +x request_nutanix_disk.py

Call the nutanix API with request <br>
> ./request_nutanix_disk.py $IP $LOGIN $PASSWORD $PORT <br>
> You can help, with ./request_nutanix_disk.py --help

- Integrate in nagios with a new command and a new services.

![Img ?](https://teknow-conseil.com/img/nagios_nutadisk_command.png) <br>
![Img ?](https://teknow-conseil.com/img/nagios_nutadisk_services.png)




