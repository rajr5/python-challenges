# Brace balancer

The solution is in `brace_balancer.py` and the runnable example is in `main.py`.

## Approach to the problem

The problem was solved via the are_braces_balanced function, the implementation is based around a list which is used as stack.

There is only one public function `are_braces_balanced` which takes a string to check wether the braces are balanced and returns `True`/`False` based on the result, it also throws a ValueError if anything but a string is passed. Rest of the functions are private and shouldn't be used by module consumers.

We can add more flexibility to the solution by allowing the class consumer to specify opening/closing pairs instead of hard codeding them but it would only add uneeded complexity to the solution.


## Solution efficiency

The solution is of both O(n) time and space complexity, looking at the code's main loop we can analyze the time complexity relatively easy:

```py
for char in input_string:                              # O(n)
        if _is_opening_brace(char):                    # O(1)
            _push(stack, char)                         # O(1)
        elif _is_closing_brace(char):                  # O(m) and since m == 3  => O(1)
            is_matching_brace = _pop(stack, char)      # O(1)
            if not is_matching_brace:                  # O(1)
                return False                           # O(1)

```

### Time complexity

In case the input is balanced we are looping over the whole input and that gives us O(n) complexity for just the loop and going over the loop internals we can see that each line is of O(1) complexity therefore our solution is of O(n) complexity.

For checking the opening braces the time complexity is of O(1), according to the reference below `key in dict` checking is of O(1) time complexity.

Checking for the closing braces `value in dict.values()` is of O(m) complexity (m = len(dict.values)), but since the number of values is 3 it is O(3) => O(1). We could further optimize closing brace checking by also having a dictionary for closing braces, but the speed gains wouldn't be noticeable.

Time complexity evaluation based on: https://wiki.python.org/moin/TimeComplexity

### Space complexity

The space complexity in O(n), the worst case is a totally imbalanced input like '((((((((((((((((((((' where the whole input will go onto the stack.
