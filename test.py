import modal

stub = modal.Stub("example-get-started")


@stub.function()
def square(x):
    print("This code is running on a remote worker!")
    return x**2


# @stub.local_entrypoint()
def main():
    print("the square is", square.remote(42))

import time

def min_changes_to_make_palindrome(lst):
    i = 0
    j = len(lst) - 1
    changes = 0
    while i <= j:
        if lst[i] != lst[j]:
            changes += 1
        i += 1
        j -= 1
    return changes

@stub.local_entrypoint()
def test():
    test_cases = [
        ([1, 2, 3, 2, 1], 0),
        ([1, 2, 3, 4, 5], 2),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5),
    ]
    for i, (lst, expected) in enumerate(test_cases):
        start_time = time.time()
        assert min_changes_to_make_palindrome(lst) == expected
        print(f"Test case {i+1} passed in {time.time() - start_time} seconds")

if __name__ == "__main__":
    # main()
    test()
