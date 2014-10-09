#!/usr/bin/env python2

import sys, getopt
import RPi.GPIO as GPIO
import mido
from mido import MidiFile

# Handle arguements and exceptions

if len(sys.argv) != 2:
    print 'usage: midi2floppy.py <filename>'
    sys.exit(2)
elif sys.argv[1] == '-h' or sys.argv[1] == '--h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
    print 'usage: midi2floppy.py <filename>'
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        pass
except IOError as e:
    print "Unable to open file" #Does not exist OR no read permissions
    sys.exit()

# Create the midifile object so we can work with it

mid = MidiFile(sys.argv[1])

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for message in track:
        print(message)
