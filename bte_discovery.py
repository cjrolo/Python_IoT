from gattlib import DiscoveryService

print("Discovering devices! Wait 30sec...")

service = DiscoveryService("hci0")
devices = service.discover(30)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))

print("Done!")
