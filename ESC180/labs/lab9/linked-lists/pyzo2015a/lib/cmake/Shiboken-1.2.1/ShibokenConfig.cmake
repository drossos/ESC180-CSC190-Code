if (NOT PYTHON_SUFFIX)
    message(STATUS "Using default python: .cpython-34m")
    SET(PYTHON_SUFFIX .cpython-34m)
endif()
include(/home/almar/pyzo2015a/lib/cmake/Shiboken-1.2.1/ShibokenConfig${PYTHON_SUFFIX}.cmake)