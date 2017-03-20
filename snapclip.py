#!/usr/bin/env -S -P/usr/local/bin python
"""A modified version of Dr. Drang's SnapClip:
    http://leancrew.com/all-this/2017/02/screenshots-with-snapclip/"""

import os, sys

lib_path = os.path.abspath(os.path.join(os.environ['HOME'], 'src', 'python', 'Pashua-Binding-Python'))
sys.path.append(lib_path)

import Pashua
import tempfile
from PIL import Image
import subprocess
import shutil
from datetime import datetime

# Local parameters
type = "png"
localdir = os.path.join(os.environ['HOME'], 'Pictures', 'Screenshots')
tf, tfname = tempfile.mkstemp(suffix='.'+type, dir=localdir)
bgcolor = (61, 101, 156)
border = 16
desktop = os.path.join(os.environ['HOME'],  'Desktop')
fname = os.path.join(desktop, datetime.now().strftime("%Y%m%d-%H%M%S." + type))
impbcopy = os.path.join(os.environ['HOME'], 'bin', 'impbcopy')
optipng = os.path.join('/', 'usr', 'local', 'bin', 'optipng')

# Dialog box configuration
conf = '''
# Window properties
*.title = Snapshot

# Border checkbox properties
bd.type = checkbox
bd.label = Background border
bd.x = 10
bd.y = 60

# Save file checkbox properties
sf.type = checkbox
sf.label = Save file to Desktop
sf.x = 10
sf.y = 35

# Default button
db.type = defaultbutton
db.label = Clipboard

# Cancel button
cb.type = cancelbutton
'''

# Capture a portion of the screen and save it to a temporary file.
status = subprocess.call(["screencapture", "-io", "-t", type, tfname])

# Exit if the user canceled the screencapture.
if not status == 0:
  os.remove(tfname)
  sys.exit()

# Open the dialog box and get the input.
dialog = Pashua.run(conf)
if dialog['cb'] == '1':
  os.remove(tfname)
  sys.exit()

# Add a desktop background border if asked for.
snap = Image.open(tfname)
if dialog['bd'] == '1':
  # Make a solid-colored background bigger than the screenshot.
  snapsize = tuple([ x + 2*border for x in snap.size ])
  bg = Image.new('RGB', snapsize, bgcolor)
  bg.paste(snap, (border, border))
  bg.save(tfname)

# Optimize the file.
subprocess.call([optipng, '-quiet', tfname])

# Put the image on the clipboard.
subprocess.call([impbcopy, tfname])

# Save to Desktop if asked for.
if dialog['sf'] == '1':
  shutil.copyfile(tfname, fname)

# Delete the temporary file
os.remove(tfname)
