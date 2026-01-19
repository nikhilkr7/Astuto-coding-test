def first_stable_character(s: str):
    """
    Return the first character in `s` whose occurrences form one contiguous block,
    and appears at least twice. Otherwise return None.
    """
    n = len(s)
    i = 0

    while i < n:
        ch = s[i]
        j = i

        # Expand the block of contiguous same characters
        while j < n and s[j] == ch:
            j += 1

        # Now block is s[i:j] for character ch
        block_length = j - i

        # Condition 1: must appear at least twice
        if block_length >= 2:
            # Condition 2: must not appear outside this block
            if s.count(ch) == block_length:
                return ch

        i = j

    return None

if __name__ == "__main__":
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
