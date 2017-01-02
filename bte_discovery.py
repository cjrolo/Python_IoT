import argparse
from gattlib import DiscoveryService
from peaners import Peaner

parser = argparse.ArgumentParser(description='Finds Bluethoot Devices.')
parser.add_argument('-t', action='store', help='Time to wait for devices', type=int)
args = parser.parse_args()
if not args.t:
    args.t = 30

print("Discovering devices! Wait {}sec...".format(args.t))

service = DiscoveryService("hci0")
devices = service.discover(args.t)

for address, name in devices.items():
    try:
        new_peaner = Peaner(address)
    except:
        print("Unknown device! Address: {}".format(address))
        continue
    print("Device: {} \n\t name: {}, address: {}".format(new_peaner.get_name(),
                                                         name,
                                                         address))
print("Done!")
