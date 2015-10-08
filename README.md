## python-dds
A ctypes implementation of dds-bridge in Python 3


[dds-bridge](https://github.com/dds-bridge/dds) is a bridge double-dummy solver implemented in C with a little C++.
This port to Python 3 uses ctypes to interact with the shared object or DLL obtained from dds-bridge. It implements all relevant functions.

#### Installation
python-dds requires the .so (linux) or .dll (windows) shared object binary.
In the file dds.py you need to change the path to that file on your system. NOTE I will try to package python-dds and distribute the package together with the python files.

#### Usage
The dds-bridge functions are described in dds.md. In the folder examples I created many files implementing these functions in Python in a low level way. Use these examples if you want a custom program that can perform a certain calculation.
Currently I am implementing more and more functions.

#### Future
My aim is a higher level (set of) class(es) that can be used as a basis for more advanced programs in Python. These classes wil get an API that will be modelled after dds-bridge with easy initializers, methods that perform calculations and getters and setters.

#### License
The dds-bridge source is licensed under the [Apache license](https://www.apache.org/licenses/LICENSE-2.0). For this implementation in Python I am looking at [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html). This license is [compatible](https://www.apache.org/licenses/GPL-compatibility.html) with Apache. You can always contact me if your project needs another license.

#### Further reading
Check out the README in the folder examples. I already mentioned dds.md.
