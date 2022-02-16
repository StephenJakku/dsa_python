from stack import Stack

def is_balanced(input):
    s=Stack()
    for item in input:
        if s.isEmpty():
            s.push(item)
        elif (s.peek()=='{' and item=='}') or (s.peek()=='[' and item==']') or (s.peek()=='(' and item==')'):
            s.pop()
        else:
            s.push(item)
    if s.isEmpty():
        return True
    else:
        return False
    return -1

def main():
    input="[({{[[())]]}}]"
    result=is_balanced(input)
    print(f"Balanced Paranthesis:{result}")

main()