#

#  Terminus Astro Libraries
from tmns.astro import time

#  Main Program
def main():

    #  Start primary loop
    okay_to_run = True
    while okay_to_run:

        print( 'Time Converter' )
        print( '--------------' )
        print( '\n' )
        print( 'Select Input Time Scale' )
        print( '1. UTC' )
        print( '2. UT1' )
        print( '3. TAI' )
        print( 'q. Exit app' )
        res = input( ' --> Option: ' )

        if res == '1':
            scale = time.Scale.UTC
        elif res == '2':
            scale = time.Scale.UT1
        elif res == '3':
            scale = time.Scale.TAI
        elif res == 'q':
            okay_to_run = False
        else:
            raise Exception( f'Unsupported Option: {res}' )

