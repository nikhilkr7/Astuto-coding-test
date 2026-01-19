def compressed_stack_length(lst: list) -> int:
    """
    For each element:
    - If it matches the top of the stack, pop (cancel)
    - Otherwise, push it
    Return final stack size.
    """
    stack = []
    for val in lst:
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)
    return len(stack)


if __name__ == "__main__":
    print(compressed_stack_length([1, 2, 2, 3]))    # Should print: 2
    print(compressed_stack_length([4, 4, 4, 4]))    # Should print: 0
    print(compressed_stack_length([]))              # Should print: 0
