import package_a
print(package_a.__file__)

def main():
    print(list(package_a.package_a()))

if __name__ == "__main__":
    main()
