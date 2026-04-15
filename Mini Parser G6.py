tokens = []
pos = 0

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
        return True
    return False

def S():
    if match("a"):
        if X():
            if match("c"):
                return True
    return False

def X():
    if match("b"):
        if pos < len(tokens) and tokens[pos] == "b":
            return X()
        return True
    return False

def parse(input_str):
    global tokens, pos
    tokens = list(input_str)
    pos = 0
    return S() and pos == len(tokens)

print(parse("abc"))    # True
print(parse("abbc"))   # True
print(parse("abbbc"))  # True
print(parse("ac"))     # False
