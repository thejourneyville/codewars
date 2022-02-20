def solve(a,b):
    
    if "*" in a:
        if a == "*":
            return True
        else:
            aidx = a.index("*")
            if 0 < aidx < len(a) - 1:
                parts = a.partition("*")
                if len(parts[0]) + len(parts[-1]) <= len(b):
                    return parts[0] in b and parts[-1] == b[-len(parts[-1]):]
                else:
                    return False
            elif aidx == 0:
                return a[1:] == b[-len(a[1:]):]
            elif aidx == len(a) - 1:
                return a[:-1] in b and a[0] == b[0]
    else:
        return a == b