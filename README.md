# MPEG2 teletext stream to t42 packet data

## crude scripts to extract teletext data from recorded dvb broadcasts

Use tsp from [TSDuck](https://tsduck.io/) to select only the teletext stream by its PID
`tsp -I file input.ts -P filter --pid [pid] > out.ts`

Then extract Packetised Elementary Stream data
`python ts2pes.py`

Finally extract teletext lines as t42
`python pes2t42.py`

Unused lines are filled with all zeros