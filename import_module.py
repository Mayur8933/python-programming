import module as m
m.print_msg()
m.fav_cricketers("Yuvraj Singh","12")

from module import fav_cricketers
fav_cricketers("Virat Kohli","18")

import module
module.fav_cricketers("Rohit Sharma","45")

from module import *
fav_cricketers("MS Dhoni","7")

from module import fav_cricketers as fc
fc("Shikhar Dhawan","25")

