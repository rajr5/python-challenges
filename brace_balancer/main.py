from brace_balancer import BraceBalancer

if __name__ == '__main__':
    bb = BraceBalancer()
    result = bb.is_balanced('(())')
    print (result)
    if result:
        print("Braces are balanced")
    else:
        print("Braces aren't balanced")