from functools import partial
import itertools as it
import sys
import click

output = open("out.pes", 'wb')

@click.command()
@click.option('-i', '--input', type=click.File('rb'), help='Input file.', required=True)
@click.option('-p', '--pid', type=str, help='PID of teletext stream in hex.', required=True)
def main(pid, input):
    ccount = -1
    
    for packet in iter(partial(input.read, 0xbc), b''):
        if packet[0] != 0x47: # something has gone horribly wrong
            print("packet without sync byte. Aborting")
            sys.exit()
        #TEI = (packet[1] >> 3) & 1
        #PUSI = (packet[1] >> 2) & 1
        #TransportPriority = (packet[1] >> 1) & 1
        PID = ((packet[1] & 0x1F) << 8) | packet[2]
        
        if int(pid, 16) == PID:

            #TSC = (packet[3] >> 6) & 3
            Adaption = (packet[3] >> 4) & 3
            
            if Adaption == 1:
                output.write(packet[4:0xbc])
            elif Adaption == 3:
                output.write(packet[5+packet[4]:0xbc])
            
            Continuity = packet[3] & 0xF
            
            if ccount == -1:
                ccount = Continuity
            else:
                ccount = (ccount + 1) & 0xF
            
            if ccount != Continuity:
                print("packet lost at "+hex(input.tell() - 0xbc))
                return

if __name__ == "__main__":
    main()