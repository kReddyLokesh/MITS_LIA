def hamming_distance(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    # Calculate the number of positions at which the characters differ
    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))

    return distance


def main():
    # Take input from the user
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    try:
        # Calculate and print the Hamming distance
        distance = hamming_distance(str1, str2)
        print(f"The Hamming Distance between the strings 'Data Science' and 'Machine Lear' is : {distance}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

