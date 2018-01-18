from array_stack import *

# str -> Stack
# Calculates a postfix arithmetic expression
def postfix_calc(string):
    str_list = string.split(" ")
    result_stack = empty_stack()
    op_list = ["+", "-", "*", "/"]

    for val in str_list:
        if val not in op_list:
            result_stack = push(result_stack, val)
        else:
            pop1 = pop(result_stack)
            result_stack = pop1[1]
            pop2 = pop(result_stack)
            result_stack = pop2[1]

            if val == "+":
                result_stack = push(result_stack, float(pop1[0]) + float(pop2[0]))
            elif val == "-":
                result_stack = push(result_stack, float(pop2[0]) - float(pop1[0]))
            elif val == "*":
                result_stack = push(result_stack, float(pop1[0]) * float(pop2[0]))
            else:
                result_stack = push(result_stack, float(pop2[0]) / float(pop1[0]))

    return peek(result_stack)