class JaccardSimilarity:
    """
    A class to calculate the Jaccard coefficient between two strings.

    Attributes:
        str1 (str): The first string for comparison.
        str2 (str): The second string for comparison.

    Methods:
        _bigrams(s):
            Generates bigrams (2-character substrings) from a given string.

        jaccard_coefficient():
            Calculates the Jaccard coefficient between the two strings.
    """

    def __init__(self, str1, str2):
        """
        Initializes the JaccardSimilarity class with two strings.

        Parameters:
            str1 (str): The first string for comparison.
            str2 (str): The second string for comparison.
        """
        self.str1 = str1
        self.str2 = str2

    def _bigrams(self, s):
        """
        Generate bigrams (2-character substrings) from the input string.

        Parameters:
            s (str): The input string to generate bigrams from.

        Returns:
            set: A set of bigrams extracted from the input string.
        """
        return set(s[i:i + 2] for i in range(len(s) - 1))

    def jaccard_coefficient(self):
        """
        Calculate the Jaccard coefficient between the two strings.

        Returns:
            float: The Jaccard coefficient, which is the size of the intersection
            of bigrams divided by the size of the union of bigrams. Returns 1.0 if
            both strings are empty and 0.0 if only one is empty.
        """
        set1 = self._bigrams(self.str1)
        set2 = self._bigrams(self.str2)

        intersection = set1.intersection(set2)
        union = set1.union(set2)

        if not union:  # Handle the case where both sets are empty
            return 1.0 if not set1 and not set2 else 0.0

        return len(intersection) / len(union)


# Example usage
if __name__ == "__main__":
    str1 = "hello"
    str2 = "hell"
    similarity = JaccardSimilarity(str1, str2)
    print(f"Jaccard Coefficient between '{str1}' and '{str2}': {similarity.jaccard_coefficient():.4f}")
