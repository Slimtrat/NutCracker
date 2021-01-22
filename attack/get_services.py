import sys

import bluetooth

def main(target) :

    if target == "all":
    	target = None

    services = bluetooth.find_service(address=target)

    if len(services) > 0:
    	print("Found {} services on {}.".format(len(services),target))
    else:
    	print("No services found.")

    for svc in services:
    	print("\nService Name:", svc["name"])
    	print("    Host:       ", svc["host"])
    	print("    Description:", svc["description"])
    	print("    Provided By:", svc["provider"])
    	print("    Protocol:   ", svc["protocol"])
    	print("    channel/PSM:", svc["port"])
    	print("    svc classes:", svc["service-classes"])
    	print("    profiles:   ", svc["profiles"])
    	print("    service id: ", svc["service-id"])
    	

