Ambient Lighting with Hue
=========================

An ambilight approach using Philips Hue Light System and written in Python.

## Requirements

* Python 3.4
* Phillips Hue Lights with a connecting Bridge
* dependencies: phue, os and sys std libs, Pillow Implementation of PIL for Py3.X

## Change Log
* added pre-built c-/ cython-files, user is not required to have Cython installed
* analysis and calculation functions are now cythonized for a 200% speedup
* split up lightify (main) and calculation parts

## Acknowledgements

Thanks to https://github.com/studioimaginaire/phue for the awesome phue
Python-library, and all the other developers of the used, very helpful
libraries.

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips
Electronics N.V., see www.meethue.com for more information. I am in no way
affiliated with the Philips organization.
