#!/usr/bin/python
from ipaddress import ip_address
from os import environ
from subprocess import check_output
from dropbox import Dropbox
from dropbox.files import WriteMode

startIP=ip_address(u'80.73.48.0')
for ipCounter in range(0,4096):
    ip = (startIP+ipCounter).__str__()
    print(ip)
    xmlMessage = check_output("nmap -oX - -F -sV "+ip,shell=True)
    # read the dropbox access key from the environment variable DBX_KEY
    dbxAccessKey = environ["DBX_KEY"]
    # connect to dropbox
    dbx=Dropbox(dbxAccessKey)
    # upload scan file
    dbx.files_upload(xmlMessage, "/NewScans/SCAN_"+ip+".xml", WriteMode.overwrite, True, None , True)
