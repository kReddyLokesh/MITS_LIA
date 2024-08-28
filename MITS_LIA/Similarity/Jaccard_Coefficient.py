def jaccard_coefficient(str1, str2):
    # Convert strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)

    # Calculate intersection and union of the sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Calculate Jaccard coefficient
    if len(union) == 0:
        return 1.0  # If both sets are empty, we consider them identical

    return len(intersection) / len(union)


def main():
    # Take input from the user
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Calculate and print the Jaccard coefficient
    coefficient = jaccard_coefficient(str1, str2)
    print(f"Jaccard coefficient: {coefficient:.2f}")


if __name__ == "__main__":
    main()