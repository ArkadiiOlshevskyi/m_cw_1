from typing import List

def capitals(word: str) -> List[int]:
    """
    Returns a list containing the indexes of all capital letters in the input string.

    Parameters:
        word (str): The input string.

    Returns:
        List[int]: A list of integer indexes representing the positions of capital letters in the input string.
    """
    return [index for index, letter in enumerate(word) if letter.isupper()]

# Example usage and test case
input_word = 'CodEWaRs'
result = capitals(input_word)
print(result)  # Output: [0, 3, 4, 6]
