TWENTY_FOUR_WEEKS_GESTATION = round((-((40 * 7)/365.25) - ((24 * 7)/365.25)), 9)
TWENTY_FIVE_WEEKS_GESTATION = round((-((40 * 7)/365.25) - ((25 * 7)/365.25)), 9)
FORTY_WEEKS_GESTATION = 0
FORTY_TWO_WEEKS_GESTATION =   round(((42 * 7)/365.25 - ((40 * 7)/365.25)), 9)
THIRTY_SEVEN_WEEKS_GESTATION = round((((37 * 7)-(40 * 7))/365.25), 9)
TERM_PREGNANCY_LENGTH_DAYS = 40 * 7
TERM_LOWER_THRESHOLD_LENGTH_DAYS = 37 * 7
EXTREME_PREMATURITY_THRESHOLD_LENGTH_DAYS = 32 * 7

"""
Debate here: cf issue #51
LMSGrowth, our current gold standard, written in visual basic for Excel by Pan Huiqi and Tim Cole does not 
agree with RCPCHGrowth beyond ~6 decimal places.On reexamining the original LMS Growth code reasons for this are not clear.

The difficulty with floating point numbers is that these constants, which act as cut offs often between references,
 at 16 dp may be more accurate than the ages supplied. For example, calculating decimal ages from 2 dates, where days are
 whole integers, 14 days for example may actually calculate out to 13.999999999999998.

 For this reason, constants have been rounded to 9 dp, ensuring that any cut offs should be respected.
"""

## Indices for thresholds in the references - Where the first in the array is 0
### These are used in sds_calculations but not from here
"""
TWENTY_THREE_WEEKS_GESTATION_INDEX = 0
TWENTY_FIVE_WEEKS_GESTATION_INDEX = 2
FORTY_TWO_WEEKS_GESTATION_INDEX = 19
TWO_WEEKS_INDEX = 20
TWO_YEARS_LYING_INDEX = 55
TWO_YEARS_STANDING_INDEX = 56
FOUR_YEARS_WHO_INDEX = 80
FOUR_YEARS_UK90_INDEX = 81
SEVENTEEN_YEARS_INDEX = 237
EIGHTEEN_YEARS_INDEX = 249
TWENTY_YEARS_INDEX = 273




These are the decimal age constants calculated to 9dp
They represent ages in decimal years for UK-WHO reference 23 weeks to 20 years, including duplicate ages where the 
references overlap.
Ages should be calculated because in the original references the intervals between measurements are fixed:
weekly from 23-42 weeks, weekly and monthly from 2 weeks to 4 years, monthly from 4-20 yrs.
"""
DECIMAL_AGES=[-0.325804244,-0.306639288,-0.287474333,-0.268309377,-0.249144422,-0.229979466,-0.210814511,-0.191649555,-0.1724846,-0.153319644,-0.134154689,-0.114989733,-0.095824778,-0.076659822,-0.057494867,-0.038329911,-0.019164956,0,0.019164956,0.038329911,0.038329911,0.057494867,0.076659822,0.083333333,0.095824778,0.114989733,0.134154689,0.153319644,0.166666667,0.1724846,0.191649555,0.210814511,0.229979466,0.249144422,0.25,0.333333333,0.416666667,0.5,0.583333333,0.666666667,0.75,0.833333333,0.916666667,1.0,1.083333333,1.166666667,1.25,1.333333333,1.416666667,1.5,1.583333333,1.666666667,1.75,1.833333333,1.916666667,2.0,2.0,2.083333333,2.166666667,2.25,2.333333333,2.416666667,2.5,2.583333333,2.666666667,2.75,2.833333333,2.916666667,3.0,3.083333333,3.166666667,3.25,3.333333333,3.416666667,3.5,3.583333333,3.666666667,3.75,3.833333333,3.916666667,4.0,4.0,4.083333333, 4.166666667, 4.25, 4.333333333, 4.416666667, 4.5, 4.583333333, 4.666666667, 4.75, 4.833333333, 4.916666667, 5.0, 5.083333333, 5.166666667, 5.25, 5.333333333, 5.416666667, 5.5, 5.583333333, 5.666666667, 5.75, 5.833333333, 5.916666667, 6.0, 6.083333333, 6.166666667, 6.25, 6.333333333, 6.416666667, 6.5, 6.583333333, 6.666666667, 6.75, 6.833333333, 6.916666667, 7.0, 7.083333333, 7.166666667, 7.25, 7.333333333, 7.416666667, 7.5, 7.583333333, 7.666666667, 7.75, 7.833333333, 7.916666667, 8.0, 8.083333333, 8.166666667, 8.25, 8.333333333, 8.416666667, 8.5, 8.583333333, 8.666666667, 8.75, 8.833333333, 8.916666667, 9.0, 9.083333333, 9.166666667, 9.25, 9.333333333, 9.416666667, 9.5, 9.583333333, 9.666666667, 9.75, 9.833333333, 9.916666667, 10.0, 10.083333333, 10.166666667, 10.25, 10.333333333, 10.416666667, 10.5, 10.583333333, 10.666666667, 10.75, 10.833333333, 10.916666667, 11.0, 11.083333333, 11.166666667, 11.25, 11.333333333, 11.416666667, 11.5, 11.583333333, 11.666666667, 11.75, 11.833333333, 11.916666667, 12.0, 12.083333333, 12.166666667, 12.25, 12.333333333, 12.416666667, 12.5, 12.583333333, 12.666666667, 12.75, 12.833333333, 12.916666667, 13.0, 13.083333333, 13.166666667, 13.25, 13.333333333, 13.416666667, 13.5, 13.583333333, 13.666666667, 13.75, 13.833333333, 13.916666667, 14.0, 14.083333333, 14.166666667, 14.25, 14.333333333, 14.416666667, 14.5, 14.583333333, 14.666666667, 14.75, 14.833333333, 14.916666667, 15.0, 15.083333333, 15.166666667, 15.25, 15.333333333, 15.416666667, 15.5, 15.583333333, 15.666666667, 15.75, 15.833333333, 15.916666667, 16.0, 16.083333333, 16.166666667, 16.25, 16.333333333, 16.416666667, 16.5, 16.583333333, 16.666666667, 16.75, 16.833333333, 16.916666667, 17.0, 17.083333333, 17.166666667, 17.25, 17.333333333, 17.416666667, 17.5, 17.583333333, 17.666666667, 17.75, 17.833333333, 17.916666667, 18.0, 18.083333333, 18.166666667, 18.25, 18.333333333, 18.416666667, 18.5, 18.583333333, 18.666666667, 18.75, 18.833333333, 18.916666667, 19.0, 19.083333333, 19.166666667, 19.25, 19.333333333, 19.416666667, 19.5, 19.583333333, 19.666666667, 19.75, 19.833333333, 19.916666667, 20.0]

"""
These 2 constants, similar to the DECIMAL_AGES, are the time intervals between LMS values. They are not currently used, and have been added to the reference JSON file
INTERVAL_VALUES=[23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,2,3,4,1,5,6,7,8,2,9,10,11,12,13,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,48,49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240]
INTERVAL_TYPES=["weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","weeks","months","weeks","weeks","weeks","weeks","months","weeks","weeks","weeks","weeks","weeks","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months","months"]
"""