#!/usr/bin/env python
#
# Load me some samples homie.
#

import sys
from optparse import OptionParser
import os
import random
import glob

sys.path.append('pympc1000/mpc1000')
import mpc1k

def sample_name(sample_path):
    return sample_path.split('.')[0]

def main():
    """main function for standalone usage"""
    usage = "usage: %prog [options] samples > foo.pgm"
    parser = OptionParser(usage=usage)
    parser.add_option('-r', '--randomize', default=False, action='store_true',
                      help='Randomize sample placement')

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        return 2

    # do stuff
    pgm = mpc1k.Program()
    
    samples = list(glob.iglob(os.path.join(args[0], "*.wav")))
    if options.randomize:
        random.shuffle(samples)

    samples = samples[:64] # handle this more gracefully in the future
    for i, sample in enumerate(samples):
        pgm.pads[i].samples[0].sample_name = os.path.basename(sample_name(sample))

    sys.stdout.write(pgm.data)

if __name__ == '__main__':
    sys.exit(main())
