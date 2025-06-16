import time
from time import strftime

time_sec = time.time()
time_struct = time.gmtime(time_sec)

print("Seconds since January 1, 1970: {:,.4f}".format(time_sec), " or {:.2e}".format(time_sec))
print(strftime("%d %b %Y", time_struct)) cccccccc4 c c c  c   c