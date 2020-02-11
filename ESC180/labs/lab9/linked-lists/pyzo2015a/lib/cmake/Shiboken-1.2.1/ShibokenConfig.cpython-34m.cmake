#  SHIBOKEN_INCLUDE_DIR        - Directories to include to use SHIBOKEN
#  SHIBOKEN_LIBRARY            - Files to link against to use SHIBOKEN
#  SHIBOKEN_BINARY             - Executable name
#  SHIBOKEN_BUILD_TYPE         - Tells if Shiboken was compiled in Release or Debug mode.
#  SHIBOKEN_PYTHON_INTERPRETER - Python interpreter (regular or debug) to be used with the bindings.
#  SHIBOKEN_PYTHON_LIBRARIES   - Python libraries (regular or debug) Shiboken is linked against.

SET(SHIBOKEN_INCLUDE_DIR "/home/almar/pyzo2015a/include/shiboken")
if(MSVC)
    SET(SHIBOKEN_LIBRARY "/home/almar/pyzo2015a/lib/libshiboken.cpython-34m.lib")
elseif(CYGWIN)
    SET(SHIBOKEN_LIBRARY "/home/almar/pyzo2015a/lib/shiboken.cpython-34m")
elseif(WIN32)
    SET(SHIBOKEN_LIBRARY "/home/almar/pyzo2015a/bin/libshiboken.cpython-34m.so")
else()
    SET(SHIBOKEN_LIBRARY "/home/almar/pyzo2015a/lib/libshiboken.cpython-34m.so")
endif()
SET(SHIBOKEN_PYTHON_INCLUDE_DIR "/home/almar/pyzo2015a/include/python3.4m")
SET(SHIBOKEN_PYTHON_INCLUDE_DIR "/home/almar/pyzo2015a/include/python3.4m")
SET(SHIBOKEN_PYTHON_INTERPRETER "/home/almar/pyzo2015a/bin/python3")
SET(SHIBOKEN_PYTHON_LIBRARIES "/home/almar/pyzo2015a/lib/libpython3.4m.so")
SET(SHIBOKEN_PYTHON_SUFFIX ".cpython-34m")
message(STATUS "libshiboken built for Release")


set(SHIBOKEN_BINARY "/home/almar/pyzo2015a/bin/shiboken")
