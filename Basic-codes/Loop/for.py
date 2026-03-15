# for loops = execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc.

import time
import winsound
for x in reversed(range(1, 11)):
    print(x)
    winsound.Beep(1000, 200)
    time.sleep(1)
