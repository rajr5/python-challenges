class BraceBalancer:
    def __init__(self):
        self.stack = []
        self.brace_pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

    def is_balanced(self, string):
        for char in string:
            if self.__is_opening_brace(char):
                self.__push(char)
            elif self.__is_closing_brace(char):
                is_ok = self.__pop(char)
                if is_ok is False:
                    return False

        if len(self.stack) == 0:
            return True
        else:
            return False

    def __is_opening_brace(self, brace):
        return brace in self.brace_pairs

    def __is_closing_brace(self, brace):
        return brace in self.brace_pairs.values()

    def __push(self, brace):
        self.stack.append(brace)

    def __pop(self, brace):
        if len(self.stack) == 0:
            return False

        last_brace = self.stack.pop()
        if (self.brace_pairs[last_brace] == brace):
            return True
        else:
            return False