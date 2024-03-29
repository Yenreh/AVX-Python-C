import ctypes
import cProfile as profile
import pstats

prof = profile.Profile()

# Load the shared library into ctypes
lib_avx = ctypes.CDLL('./lib_AVX.so')


def scalar_multiply():
    # Define the function prototype to be able to call it with python data types
    vectorScalarMultiply = lib_avx.vectorScalarMultiply
    vectorScalarMultiply.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_double,
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int
    ]

    # Definition of constants and casting to ctypes
    n = 10000000
    vector = (ctypes.c_double * n)(*range(n))
    scalar = ctypes.c_double(2)
    result = (ctypes.c_double * n)()

    # Call the function
    vectorScalarMultiply(vector, scalar, result, ctypes.c_int(n))


# Start profiling
prof.enable()

# Call the function
scalar_multiply()

# End profiling
prof.disable()

stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
