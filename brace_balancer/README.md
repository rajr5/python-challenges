# Brace balancer

The solution is in the `brace_balancer.py` and the runnable example is in `main.py`.

## Approach to the problem

The problem was solved via the BraceBalancer class, it implements a wrapper with a few methods around a list, the list is used as stack.

There is only one public method `is_balanced` which takes a string to check wether the braces are balanced and returns `True`/`False` based on the result. Rest of the methods are private and shouldn't be used by class consumers.

We can add more flexibility to the solution by allowing the class consumer to specify opening/closing pairs instead of hard coded braces but it would only add uneeded complexity to the solution.


## Solution efficiency

The solution is of both O(n) time and space complexity, looking at the code's main loop we can analyze the time complexity relatively easy:

```py
for char in string:                                     # O(n)
            if self.__is_opening_brace(char):           # O(1)
                self.__push(char)                       # O(1)
            elif self.__is_closing_brace(char):         # O(m) and m << n  => O(1)
                is_ok = self.__pop(char)                # O(1)
                if is_ok is False:                      # O(1)
                    return False                        # O(1)
```

### Time complexity

In case the input is balanced we are looping over the whole input and that gives us O(n) complexity for just the loop and going over the loop internals we can argue that they are of O(1) complexity therefore our solution is of O(n) complexity.

For checking the opening braces the time complexity is of O(1), according to the reference below `key in dict` checking is of O(1) time complexity.

Checking for the closing braces `value in dict.values()` is of O(m) complexity (m = len(dict.values)), but since the number of values is very small for large inputs `m << n` we could argue it's O(1). We could optimize closing brace checking by also having a dictionary for closing braces to make the checks O(1), but it would add uneeded complexity to our solution.

Time complexity evaluation based on: https://wiki.python.org/moin/TimeComplexity

### Space complexity

The space complexity in O(n), the worst case is a totally imbalanced input like '((((((((((((((((((((' where the whole input will go onto the stack.


## Unit tests

The solution is pretty straightforward to test so I've added a few tests implemented via Python's unittest framework to make sure the everything works properly.