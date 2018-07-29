brace_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def are_braces_balanced(input_string):
    """Checks wether the braces passed in the input string
    are balanced or not and returns True or False respectively.
    """
    if not isinstance(input_string, str):
        raise ValueError("passed parameter should be a string")

    stack = []
    for char in input_string:
        if _is_opening_brace(char):
            _push(stack, char)
        elif _is_closing_brace(char):
            is_matching_brace = _pop(stack, char)
            if not is_matching_brace:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def _is_opening_brace(brace):
    return brace in brace_pairs


def _is_closing_brace(brace):
    return brace in brace_pairs.values()


def _push(stack, brace):
    stack.append(brace)


def _pop(stack, closing_brace):
    if len(stack) == 0:
        return False

    last_brace = stack.pop()
    if (brace_pairs[last_brace] == closing_brace):
        return True
    else:
        return False
