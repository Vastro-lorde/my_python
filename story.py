import sys
from time import sleep
words = '\nIn leadership, you are only as good as the lowest level you’ve mastered. ' \
        '\nSo I just want to remind you that even if you scored highly in one of the higher levels,	' \
        '\nif you scored poorly on a lower level, ' \
        '\nyour leadership is actually on that lower level. ' \
        '\nThat is where you will need to give your attention when working ' \
        '\nwith people to improve your leadership ability.'
for char in words:
    sleep(0.08)
    sys.stdout.write(char)
    sys.stdout.flush()