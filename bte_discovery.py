from gattlib import DiscoveryService
from peaners import Peaner

print("Discovering devices! Wait 30sec...")

service = DiscoveryService("hci0")
devices = service.discover(30)

for address, name in devices.items():
    new_peaner = Peaner(address)
    print("Device: {} \n\t name: {}, address: {}".format(new_peaner.get_name,
                                                         name,
                                                         address))
print("Done!")
