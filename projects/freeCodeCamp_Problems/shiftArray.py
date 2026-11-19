# Shift an array by n positions.
# A positive integer shifts the array to the left.
# A negative integer shifts the array to the right.
# The shift wraps around the array.
#
# Example:
#   [1, 2, 3, 4, 5] with n = 2 -> [3, 4, 5, 1, 2]
#   [1, 2, 3, 4, 5] with n = -2 -> [4, 5, 1, 2, 3]

def shift_array(arr, n):
    # Handle empty arrays safely.
    if not arr:
        return []

    # Normalize the shift so large values wrap correctly.
    # Example: n = 7 on a 5-element list is the same as n = 2.
    shift = n % len(arr)

    # If the shift is 0, the array is unchanged.
    if shift == 0:
        return arr[:]

    # Create a new list to store the rotated values.
    rotated = []

    # A positive shift moves elements left.
    # Convert index i to its new position using wraparound.
    if n > 0:
        for i in range(len(arr)):
            # Old index i moves to new index (i - shift) mod len(arr)
            # This is equivalent to taking the element from the left and
            # placing it at the current index in the rotated array.
            rotated.append(arr[(i + shift) % len(arr)])

    # A negative shift moves elements right.
    else:
        for i in range(len(arr)):
            # Old index i moves to new index (i + shift) mod len(arr)
            # Because shift is negative, this effectively rotates right.
            rotated.append(arr[(i + shift) % len(arr)])

    return rotated