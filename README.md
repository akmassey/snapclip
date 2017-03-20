# Dr. Drang’s SnapClip, modified for Alfred

I’ve modified [Dr. Drang’s SnapClip][1] for use with Alfred.  You should start
by reading about [his use with Keyboard Maestro][1].

## Installation

Dr. Drang’s script requires access to four non-standard utilities, all of
which must be installed for this to work properly.

First, download [Pashua][3].  You will also need to install the [Pashua
bindings for python][4].  I’ve installed this in my `~/src/python` folder.

Second, you’ll need [Pillow][5], which can probably just be installed with
`pip install pillow` or similar.

Third, you’ll need Alec Jacobson’s [impbcopy][6].  Dr. Drang is hosting [a
binary that you might be able to just download][7], and I’ve created a
[separate repository with the source code][8].

Fourth, you’ll need [OptiPNG](http://optipng.sourceforge.net/), which is
available on Homebrew with `brew install optipng`.

With those preliminaries out of the way, you’ll also need to install the
Alfred Workflow in this repository.  It has a hard dependency on
`snapclip.py`, which is also in this repository.  If you put everything in a
repository at `~/src/python/snapclip/` then it should “just work.”

## Roadmap

Several things make this script less portable, but the two that stand out are
Pashua and OptiPNG.  Neither is strictly necessary.  Pashua could be replace
by tkinter, which is available by default on most python installs.  OptiPNG
could simply be disabled or only used when present.  These are things I
probably won’t do, but I would be happy to merge.

[1]: http://leancrew.com/all-this/2017/02/screenshots-with-snapclip/
[2]: http://leancrew.com/all-this/2017/02/screenshots-with-snapclip/
[3]: https://www.bluem.net/en/mac/pashua/
[4]: https://github.com/BlueM/Pashua-Binding-Python
[5]: https://python-pillow.org/
[6]: http://www.alecjacobson.com/weblog/?p=3816
[7]: http://leancrew.com/all-this/downloads/impbcopy
[8]: https://github.com/akmassey/impbcopy
