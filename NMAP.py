#!/usr/bin/python
import subprocess
# import xml.etree.ElementTree as ET
import ipaddress
# call NMAP with the right path

startIP=ipaddress.ip_address(u'80.73.48.15')
for ipCounter in range(0,1):
    ip = (startIP+ipCounter).__str__()
    print(ip)
    xmlMessage = subprocess.check_output("nmap -oX - -F -sV "+ip,shell=True)
    # write the XML Message into a file
    xmlFile = open("SCAN_"+ip+".xml","w")
    xmlFile.write(xmlMessage)
    xmlFile.close()

# parse the XML Message String into a element tree
# treeRoot = ET.fromstring(xmlMessage)
# print(treeRoot)
# for child in treeRoot:
#     print child.tag, child.attrib
# for port in treeRoot.iter('port'):
#     print port.tag, port.attrib

