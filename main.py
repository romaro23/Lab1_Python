    import sys

    print("Hello world")
    name = input("What is your name: \n")
    print(f"Hello, {name}")
    tupleOfTypes = (1, 3.14, 5 + 6j, "name", (1, 2, 3), [4, 5, 6], {7, 8, 9}, {"one": "two"}, range(3), True,
                   frozenset({1, 2, 3}))
    for obj in tupleOfTypes:
        print(f"Size of {obj} ({type(obj)}): {sys.getsizeof(obj)} bytes")