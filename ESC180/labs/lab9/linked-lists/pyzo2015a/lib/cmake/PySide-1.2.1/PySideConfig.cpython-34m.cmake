#  PYSIDE_INCLUDE_DIR   - Directories to include to use PySide
#  PYSIDE_LIBRARY       - Files to link against to use PySide
#  PYSIDE_PYTHONPATH    - Path to where the PySide Python module files could be found
#  PYSIDE_TYPESYSTEMS   - Type system files that should be used by other bindings extending PySide

SET(PYSIDE_INCLUDE_DIR "/home/almar/pyzo2015a/include/PySide")
# Platform specific library names
if(MSVC)
    SET(PYSIDE_LIBRARY "/home/almar/pyzo2015a/lib/libpyside.cpython-34m.lib")
elseif(CYGWIN)
    SET(PYSIDE_LIBRARY "/home/almar/pyzo2015a/lib/libpyside.cpython-34m")
elseif(WIN32)
    SET(PYSIDE_LIBRARY "/home/almar/pyzo2015a/bin/libpyside.cpython-34m.so")
else()
    SET(PYSIDE_LIBRARY "/home/almar/pyzo2015a/lib/libpyside.cpython-34m.so")
endif()
SET(PYSIDE_PYTHONPATH "/home/almar/pyzo2015a/lib/python3.4/site-packages")
SET(PYSIDE_TYPESYSTEMS "/home/almar/pyzo2015a/share/PySide/typesystems")
