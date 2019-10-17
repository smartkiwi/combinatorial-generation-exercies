import math


def strings(A, n):
    """4.2 Basic recursive solution"""
    if n == 0:
        return ['']
    return [s + c for s in strings(A, n - 1) for c in A]


def strings_readable(A, n):
    """4.2 Basic recursive solution (more readable)"""
    if n == 0:
        return ['']
    result = []
    for c in A:
        for s in strings_readable(A, n - 1):
            result.append(s + c)
    return result


global_counter = 0


def strings_exercise_4_4_3(A, n, inner_call=False):
    """Exercise 4.4.3 (Easy): Modify the solution to keep count of how many string concatenations take place.
    Verify that our closed formula for T(n)T(n)T(n) is correct."""
    global global_counter
    if not inner_call:
        global_counter = 0
    if n == 0:
        return ['']
    result = []
    for c in A:
        for s in strings_exercise_4_4_3(A, n - 1, inner_call=True):
            global_counter += 1
            result.append(s + c)
    return result


def strings_exercise_4_4_4(A, n):
    """Exercise 4.4.4 Modify the recursive solution to return a generator instead (i.e., use yield instead of return
    and yield one string at a time instead of returning the whole list)."""
    pass


def t_n(k, n):
    return (math.pow(k, n + 1) - 1) / (k - 1)


if __name__ == "__main__":
    print strings.__doc__
    print strings(['0', '1', '2'], n=2)
    print strings_readable.__doc__
    print strings_readable(['0', '1', '2'], n=2)
    print """Exercise 4.4.1 (Easy): What if k=1k = 1k=1 ? 
    What is the output of the program? What about space and time complexity?"""
    print strings(['0'], n=2)
    print "Space - 1, Complexity 1"
    print strings_exercise_4_4_3.__doc__
    r = strings_exercise_4_4_3(['0', '1', '2'], n=2)
    print r
    print "space: %s" % len(r)
    print "concat counter k=3 n=2 T(n)=%s" % global_counter
    print "T(n)=%s" % t_n(k=3, n=2+1)
    print "k^n=%s" % math.pow(3, 2)
    r = strings_exercise_4_4_3(['0', '1', '2', '3', '4'], n=6)
    print r
    print "space: %s" % len(r)
    print "concat counter k=5 n=5 T(n)=%s" % global_counter
    print "T(n)=%s" % t_n(k=5, n=6+1)
    print "k^n=%s" % math.pow(5, 6)

