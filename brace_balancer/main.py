from brace_balancer import are_braces_balanced

if __name__ == '__main__':
    balanced = are_braces_balanced("""
    Python {is an easy to [learn]}, (powerful programming language. It)
    has efficient high­level [(data structures) and a simple but
    effective approach to object­oriented programming]. Python’s elegant
    syntax and dynamic typing, together with its {interpreted nature,
    make it an ideal language (for) scripting and rapid} application
    development in many areas on most platforms.
    """)

    if balanced:
        print("Braces are balanced")
    else:
        print("Braces aren't balanced")