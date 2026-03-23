# utils.py semifinal


#capitalize(text)           # "hello" → "Hello" 
def capitalize(text):
    """Return text with the first character capitalized.

    Args:
        text: string to transform.

    Returns:
        str: text with the first character in uppercase.

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return ""

    return text[0].upper() + text[1:]


#truncate(text, max_len=20) # Apgriež un pievieno "..." ja teksts ir garāks par max_len

def truncate(text, max_len=20):
    """Truncate text and add '...' if it exceeds max_len.

    Args:
        text: string to truncate.
        max_len: maximum allowed length before truncation.

    Returns:
        str: original or truncated text.

    Example:
        >>> truncate("Hello world", 5)
        'He...'
        >>> truncate("Short text", 20)
        'Short text'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(max_len, int):
        raise TypeError("max_len must be an integer")
    if max_len < 0:
        raise ValueError("max_len must be >= 0")

    if len(text) <= max_len:
        return text

    if max_len <= 3:
        return "." * max_len

    return text[:max_len - 3] + "..."


#count_words(text)          # Saskaita vārdus tekstā, atgriež skaitu

def count_words(text):
    """Count words in a string.

    Args:
        text: input string.

    Returns:
        int: number of words.

    Example:
        >>> count_words("Hello world")
        2
        >>> count_words(" one   two  three ")
        3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()
    return len(words)


def clamp(num, low=0, high=100):
    """Clamp a number to the given range.

    Args:
        num: number to clamp.
        low: minimum allowed value.
        high: maximum allowed value.

    Returns:
        int or float: clamped value.

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    if not isinstance(num, (int, float)):
        raise TypeError("num must be a number")
    if not isinstance(low, (int, float)):
        raise TypeError("low must be a number")
    if not isinstance(high, (int, float)):
        raise TypeError("high must be a number")
    if low > high:
        raise ValueError("low must be less than or equal to high")

    if num < low:
        return low
    if num > high:
        return high
    return num


def is_prime(num):
    """Check whether a number is prime.

    Args:
        num: integer to check.

    Returns:
        bool: True if num is prime, otherwise False.

    Example:
        >>> is_prime(2)
        True
        >>> is_prime(9)
        False
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer")

    if num < 2:
        return False

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Args:
        n: non-negative integer.

    Returns:
        int: factorial of n.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is negative.

    Example:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1

    for number in range(1, n + 1):
        result *= number

    return result


def total(numbers):
    """Calculate the sum of a list manually using a loop.

    Args:
        numbers: list of numbers.

    Returns:
        int or float: total sum of elements.

    Example:
        >>> total([1, 2, 3, 4])
        10
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    result = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("all elements in numbers must be numeric")
        result += number

    return result


def average(numbers):
    """Calculate the arithmetic mean of a list.

    Args:
        numbers: list of numbers.

    Returns:
        float: average value of the list.

    Raises:
        ValueError: if the list is empty.

    Example:
        >>> average([2, 4, 6])
        4.0
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")

    return total(numbers) / len(numbers)


if __name__ == "__main__":
    print("--- String functions ---")
    print(capitalize("hello"))
    print(truncate("This is a very long sentence for testing.", 18))
    print(count_words("Python is fun to learn"))

    print("\n--- Number functions ---")
    print(clamp(15, 0, 10))
    print(clamp(-3))  # uses default low=0, high=100
    print(is_prime(29))
    print(factorial(5))

    print("\n--- List functions ---")
    print(total([1, 2, 3, 4, 5]))
    print(average([10, 20, 30]))

    print("\n--- Factorial edge cases ---")
    print(factorial(0))
    print(factorial(1))

    try:
        print(factorial(-1))
    except ValueError as error:
        print(f"Error: {error}")