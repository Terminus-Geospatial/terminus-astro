

#  Python Standard Libraries
import math

class Format:
    JD                  = 'jd'
    MJD                 = 'mjd'
    ISO_8601            = 'iso_8601'
    SECONDS_SINCE_EPOCH = 'seconds'

class Scale:
    DELTA = 'delta'
    TAI   = 'tai'
    UT1   = 'ut1'
    UTC   = 'utc'


class Julian_Date:
    def __init__( self, jd1 : float, jd2 : float = 0 ):
        self.jd1 = jd1
        self.jd2 = jd2

    def single(self):
        return self.jd1 + self.jd2


class Time:

    def __init__(self, scale, format ):
        pass

    @staticmethod
    def from_utc( jd_format : tuple = None ):

        #  If Julian specified
        if jd_format is not None:
            return Time( scale  = Scale.UTC,
                         format = Julian_Date( *jd_format ) )
        

