from Stack import Stack

def reverse_list(str_):
    stack = Stack()
    for char in str_:
        stack.push(char)
    reversed = ""
    while not stack.is_empty():
        reversed += stack.pop()
    return reversed

str_ = "We will conquere COVID-19"
print (reverse_list(str_))