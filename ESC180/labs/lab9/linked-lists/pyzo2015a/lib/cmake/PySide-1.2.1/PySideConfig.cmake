if (NOT PYTHON_BASENAME)
    message(STATUS "Using default python: .cpython-34m")
    SET(PYTHON_BASENAME .cpython-34m)
endif()
include(/home/almar/pyzo2015a/lib/cmake/PySide-1.2.1/PySideConfig${PYTHON_BASENAME}.cmake)
