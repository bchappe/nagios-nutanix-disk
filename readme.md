---
---
# Plugin Nagios - Nutanix Disk

The script check if the nutanix statement for the disk is OK. He use a API of Nutanix in version 2.
- $NUTANIX_API "GET" "/PrismGateway/services/rest/v2.0/disks" <br>
Conditions :
if element['disk_status'] != <b> "NORMAL" </b> or str(element<b>['online']) != "True": </b>

### Dependencies <br>

- Python3 with standard library <br>
> import requests <br>
> json <br>
> import sys <br>
- Nagios core or NagiosXI <br>
- Nutanix API with version 2. <br>


### Usage <br>
> request_nutanix_disk.py $IP $LOGIN $PASSWORD $PORT <br>

### Examples <br>
``` 
request_nutanix_disk.py --help
request_nutanix_disk.py 192.168.1.1 api_test mypassword 9443
``` 


### 2. Installation Instructions <br>
- Download the script in your plugin directory (git clone or download).
> /usr/local/nagios/libexec/ ## Your script directory Nagios XI.

<br>

- Authorize the owner and groups nagios to launch it <br>
- Authorize the file to be execute
``` 
chown apache:nagios request_nutanix_disk.py <br>
-rwxr-xr-x apache nagios request_nutanix_disk.py 
chmod +x request_nutanix_disk.py
``` 

Call the nutanix API with request <br>
``` 
 ./request_nutanix_disk.py $IP $LOGIN $PASSWORD $PORT <br>
 ``` 
 You can help, with ./request_nutanix_disk.py --help

- Integrate in nagios with a new command and a new services. <br>
``` 
command[check_nutanix_disk]=/usr/local/nagios/libexec/nutanix.py
```
```
define command {
    command_name    check_nutanix_disk
    command_line    $USER1$/request_nutanix_disk.py $ARG1$ $ARG2$ $ARG3$ $ARG4$
```

![Img ?](https://teknow-conseil.com/img/nagios_nutadisk_command.png) <br>
![Img ?](https://teknow-conseil.com/img/nagios_nutadisk_services.png)
