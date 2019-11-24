from functools import partial
import itertools as it
import sys

input = open("out.ts", 'rb')
output = open("out.pes", 'wb')

def main():
    for packet in iter(partial(input.read, 0xbc), b''):
        if packet[0] != 0x47: # something has gone horribly wrong
            print("packet without sync byte. Aborting")
            sys.exit()
        TEI = (packet[1] >> 3) & 1
        PUSI = (packet[1] >> 2) & 1
        TransportPriority = (packet[1] >> 1) & 1
        
        output.write(packet[4:0xbc])

if __name__ == "__main__":
    main()