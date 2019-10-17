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


def strings_2_readable(A, n):
    """modified version for better (mine) understanding"""
    index_of = {x: i for i, x in enumerate(A)}
    s = [A[0]] * n
    final_s = [A[-1]] * n
    while s != final_s:
        yield ''.join(s)
        s = increment_array_of_char(s, A)
    yield ''.join(s)


def increment_array_of_char(array_of_char, A):
    index_of = {x: i for i, x in enumerate(A)}
    n = len(A)
    s = array_of_char
    for i in range(1, n + 1):
        if s[-i] == A[-1]:  # Last letter of alphabet, can not increment
            s[-i] = A[0]
        else:
            s[-i] = A[index_of[s[-i]] + 1]  # Modify to next letter
            return s

    raise Exception("Cannot increment after max reached. Program should not get here")



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
    yield _format_bin(int_s, n)
    while int_s < int_end_result:
        int_s += 1
        yield _format_bin(int_s, n)


def _format_bin(val, n):
    bin_str = bin(val)
    bin_str = bin_str.replace('0b', '')
    return bin_str.zfill(n)


def strings_2_4_7_3(A, n):
    """Exercise 4.7.3 (Medium): The main operation in this algorithm is very similar to a particular arithmetic operation.
    What operation is that? Can you re-implement the algorithm using arithmetic operations? In particular, for the
    binary alphabet given in Exercise 4.7.2, can you implement this algorithm very efficiently using bitwise operations and basic arithmetic?"""
    index_of = {x: i for i, x in enumerate(A)}
    s = [A[0]] * n
    final_array = [A[-1]] * n
    int_s = base_to_int(
        char_to_base_num(s, index_of), len(A)
    )
    int_final = base_to_int(char_to_base_num(final_array, index_of), len(A))
    yield ''.join(s)
    while int_s < int_final:
        int_s += 1
        yield ''.join(base_num_to_char(int_to_base(int_s, len(A)), A)).ljust(len(A), A[0])


def char_to_base_num(array_of_chars, index_of):
    """converts array of chars into number in base system (array of digits)"""
    array_of_digits = []
    for el in array_of_chars:
        array_of_digits.append(index_of[el])
    return array_of_digits


def base_num_to_char(array_of_digits, A):
    """converts number in base system (array of digits) into array of chars"""
    array_of_chars = []
    for el in array_of_digits:
        array_of_chars.append(A[el])
    return array_of_chars


def int_to_base(num, base):
    """converts int into number in base system"""
    max_num = int(math.log(num, base))
    array_of_digits = []
    remainder = num
    for pow in range(max_num, -1, -1):
        full_digit = math.pow(base, pow)
        pos_value = int(remainder // full_digit)
        remainder = remainder % math.pow(base, pow)
        array_of_digits.append(pos_value)
    return array_of_digits


def base_to_int(array_of_digits, base):
    """converts number in base system to int"""
    int_value = 0
    for ind, el in enumerate(array_of_digits):
        pow = len(array_of_digits) - ind - 1
        int_value += el * math.pow(base, pow)
    return int_value


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

    print strings_2_4_7_3.__doc__
    print list(strings_2_4_7_3(['0', '1', '2'], n=3))

    print ",".join(strings_2_readable(['0', '1', '2'], n=3))
