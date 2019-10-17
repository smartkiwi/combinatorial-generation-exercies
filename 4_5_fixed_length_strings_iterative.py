import math


def strings_2(A, n):
    index_of = {x: i for i, x in enumerate(A)}
    s = [A[0]] * n
    while True:
        yield ''.join(s)
        for i in range(1, n + 1):
            if s[-i] == A[-1]:  # Last letter of alphabet, can not increment
                s[-i] = A[0]
            else:
                s[-i] = A[index_of[s[-i]] + 1]  # Modify to next letter
                break
        else:
            break


def strings_2_counter(A, n):
    """Exercise 4.7.1 (Easy): Modify the source code provided to count the number of resets.
    Experimentally verify that our closed form formula for T(n) is correct."""
    reset_counter = 0
    index_of = {x: i for i, x in enumerate(A)}
    s = [A[0]] * n
    while True:
        yield ''.join(s)
        for i in range(1, n + 1):
            if s[-i] == A[-1]:  # Last letter of alphabet, can not increment
                reset_counter += 1
                s[-i] = A[0]
            else:
                s[-i] = A[index_of[s[-i]] + 1]  # Modify to next letter
                break
        else:
            break
    print "reset count: %s" % reset_counter


def strings_2_4_7_2(n):
    """Exercise 4.7.2 (Medium): Assume the alphabet is fixed as A = [0, 1] so you are generating all binary strings
    of a given length. Simplify the code assuming this hard-coded alphabet."""
    s = '0b' + '0' * n
    int_s = int(s, 2)
    end_result = '0b' + '1' * n
    int_end_result = int(end_result, 2)
    yield format_bin(int_s, n)
    while int_s < int_end_result:
        int_s += 1
        yield format_bin(int_s, n)


def format_bin(val, n):
    bin_str = bin(val)
    bin_str = bin_str.replace('0b', '')
    return bin_str.zfill(n)


def t_n(k, n):
    """
    Calculate T(n)
    helper function
    """
    return int((math.pow(k, n) - 1) / (k - 1))


if __name__ == "__main__":
    print ",".join(strings_2(['0', '1', '2'], n=5))
    print strings_2_counter.__doc__
    print "reset counter: "
    r = list(strings_2_counter(['0', '1', '2'], n=5))
    print "k=3 T(n=5)=%s" % t_n(k=3, n=5)

    print "'%s'" % "','".join(strings_2(['0', '1'], n=3))
    print strings_2_4_7_2.__doc__
    print list(strings_2_4_7_2(n=3))
