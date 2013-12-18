# Use either this file or main.ipynb -- do not use both! This simplifies
# grading on our end.
#
# Here is an example of single-process code:

print "Hello, world"

# Next, here is an example of multi-process code:

from IPython.parallel import Client

rc = Client()
view = rc.load_balanced_view()

def function():
   import time
   time.sleep(1)

view.map(function, range(10))

# Feel free to modify these as appropriate for each assignment.