import argparse
from gattlib import DiscoveryService
from peaners import Peaner

parser = argparse.ArgumentParser(description='Finds Bluethoot Devices.')
parser.add_argument('-t', action='store_const', const=30, help='Time to wait for devices')
args = parser.parse_args()

print("Discovering devices! Wait {}sec...".format(args.t))

service = DiscoveryService("hci0")
devices = service.discover(args.t)

for address, name in devices.items():
    new_peaner = Peaner(address)
    print("Device: {} \n\t name: {}, address: {}".format(new_peaner.get_name(),
                                                         name,
                                                         address))
print("Done!")
