Ambient Lighting with Hue
=========================

An ambilight approach using Philips Hue Light System and written in Python.

## Requirements

* Python 3.4
* Phillips Hue Lights with a connecting Bridge
* dependencies: [Cython](http//cython.org/), [phue](https://github.com/studioimaginaire/phue), os and sys std libs, [ImageMagick](http://www.imagemagick.org/script/binary-releases.php),
    [Pillow Implementation of PIL](https://pypi.python.org/pypi/Pillow/2.8.1) for Py3.X

## Change Log
* changed to pyximport method, Cython needed (trying to find a better way)
* added pre-built c-/ cython-files, ~~user is not required to have Cython installed~~
* analysis and calculation functions are now cythonized for a 200% speedup
* split up lightify (main) and calculation parts

## Acknowledgements

Thanks to https://github.com/studioimaginaire/phue for the awesome phue
Python-library, and all the other developers of the used, very helpful
libraries.

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips
Electronics N.V., see www.meethue.com for more information. I am in no way
affiliated with the Philips organization.
