#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#

#  Python Standard Libraries
from collections import namedtuple
import math

#  Constants
SECONDS_PER_DAY    = 86400
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR   = 60
SECONDS_PER_HOUR   = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

HMS = namedtuple('HMS', [ 'hours',
                          'minutes',
                          'seconds' ] )

def day_to_hms( day : float ) -> HMS:
    '''
    Convert a ratio of a day to hour/min/sec format.
    '''

    EPS = 1e-10

    #  Establish the sign value
    sign = 1
    if day < 0:
        sign = -1

    #  Number of seconds
    secs = day * SECONDS_PER_DAY * sign

    #  Round sec
    total_secs = int( 0.5 + secs )

    hr = int( total_secs / SECONDS_PER_HOUR )
    total_secs -= hr * SECONDS_PER_HOUR

    mn = int( total_secs / SECONDS_PER_MINUTE )
    total_secs -= mn * SECONDS_PER_MINUTE

    sc = secs - (secs - total_secs)

    return HMS( hr * sign, mn, sc )

def angle_to_hms( theta : float ) -> HMS:
    '''
    Convert an angle from [0,2pi] to HMS format.
    '''
    return day_to_hms( theta/(2*math.pi) )

