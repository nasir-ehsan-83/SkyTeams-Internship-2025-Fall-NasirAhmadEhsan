def largest_smallest(a, b, c):
    largest = a
    if b > largest: largest = b
    if c > largest: largest = c

    smallest = a
    if b < smallest: smallest = b
    if c < smallest: smallest = c

    return largest, smallest
