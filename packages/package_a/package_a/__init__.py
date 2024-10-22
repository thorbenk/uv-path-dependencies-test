import more_itertools

print(f"package_a uses more_itertools from {more_itertools.__file__}")
print(f"package_a is from {__file__}")

def package_a():
    return more_itertools.chunked([1, 2, 3, 4, 5, 6], 3)
