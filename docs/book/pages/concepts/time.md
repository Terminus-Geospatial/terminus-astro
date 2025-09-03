#  Date and Time Concepts

One aspect of astronomy applications which is different from geospatial work focused on the Earth is the importance of *time*.  This is because many conversions, such as from Earth-Centered, Earth-Fixed to Earth-Centered Inertial or Satellite tracking require knowing a lot of time-based orbital mechanics knowledge.  Equations such as Precession, Nutation, Polar Wobble, and SGP4 all utilize various time formats.

To start, we define two concepts:  ***time scales*** and ***time formats***.

## Time Scales:

This represents the actual *timeframe*, epoch, and underlying science aspects.  For example, we have UTC, TAI, TT, UTC1, and Gregorian timescales.  More on each is given later.

These time scales may have different starting points (aka: Epochs), unique progressions (ex: leap seconds), and other aspects.

## Time Formats:

In order to communicate time, can then use a variety of ***formats***.  A few formats are shown below:

* Seconds since an epoch - Ex: unix-seconds
* ISO 8601 - ex: `2025-08-31T19:21:48Z`
* Language-Specific Objects - ex: Python `datetime.datetime`.
* Gregorian Month, Day, Year
* Modified Julian Date
* Julian Date


---

# Time Scales

## UTC - Coordinated Universal Time

Standard time reference used by clocks and computers.

This time-scale is synchronized useing atomic clocks, similarly to International Atomic Time (TAI)[\#1] but with ***leap-second*** adjustments to account for the alignment of the Earth's rotation about the Sun.

## UT1 - Universal Time 1
Universal Time (UT1) is a timescale directly tied to the rotation of the Earth.  This is less constant than atomic time scales.  While UTC is tied to atomic clocks, then ***adjusted*** to match the general rotation of the Earth, UT1 is directly synchronized to the rotation of the Earth.

UTC and UT1 are expected to be within 1 second of each other.  This is done by adding ***leap seconds*** to UTC, rather than adjust UT1.

This measurement depends on the angle between the position of the Earth and the International Celestial Reference Frame (ICRF).  This angle is known as the ***Earth Rotation Angle*** (ERA).  


# References:

1. https://www.nist.gov/pml/time-and-frequency-division/time-realization/leap-seconds