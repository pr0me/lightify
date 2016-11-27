Ambient Lighting with Hue
=========================
Version 1.1

An ambilight approach using Philips Hue Light System and written in Python.

## Notes
The tool was developed and tested on linux distributions. It uses the os.system
function to execute ImageMagick from the command line and thus depends on a
similar setting.

Use argument '-h' for further help, especially concerning screenshot source and
frequency!

## Change Log
* further optimizations, using numpy now, good speedup (level of wanted usability is finally reached)
* ~~shipping with pre-built extension again, Cython is NOT required~~
* changed to pyximport method, ~~Cython needed (trying to find a better way)~~
* added pre-built c-/ cython-files, ~~user is not required to have Cython installed~~
* analysis and calculation functions are now cythonized for a 200% speedup
* split up lightify (main) and calculation parts

## Requirements

* Python 3.5
* Phillips Hue Lights with a connecting Bridge
* dependencies: [phue](https://github.com/studioimaginaire/phue), [ImageMagick](http://www.imagemagick.org/script/binary-releases.php),
    [Pillow Implementation of PIL](https://pypi.python.org/pypi/Pillow/2.8.1) for Py3.X


## Acknowledgements

Thanks to https://github.com/studioimaginaire/phue for the awesome phue
Python-library, and all the other developers of the used, very helpful
libraries.

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips
Electronics N.V., see www.meethue.com for more information. I am in no way
affiliated with the Philips organization.
