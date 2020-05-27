# MPEG2 teletext stream to t42 packet data

## crude scripts to extract teletext data from recorded dvb broadcasts

Extract Packetised Elementary Stream data from transport stream
`python ts2pes.py -i input.ts -p [pid]`

Then extract teletext lines as t42
`python pes2t42.py`

Unused lines are filled with all zeros