def overlap_coefficient(str1, str2):
    # Convert strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)

    # Calculate intersection of the sets
    intersection = set1.intersection(set2)

    # Find the size of the smaller set
    min_size = min(len(set1), len(set2))

    # Calculate Overlap Coefficient
    if min_size == 0:
        return 1.0  # If both sets are empty, we consider them identical

    return len(intersection) / min_size


def main():
    # Take input from the user
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Calculate and print the overlap coefficient
    coefficient = overlap_coefficient(str1, str2)
    print(f"The Overlap coefficient between the strings 'Data Science' and 'Machine Learning' is : {coefficient:.2f}")


if __name__ == "__main__":
    main()