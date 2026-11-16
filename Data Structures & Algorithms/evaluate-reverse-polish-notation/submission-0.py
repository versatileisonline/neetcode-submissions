class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        valid_operator = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] in valid_operator:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if tokens[i] == "+":
                    result = first_num + second_num
                elif tokens[i] == "-":
                    result = first_num - second_num
                elif tokens[i] == "*":
                    result = first_num * second_num
                elif tokens[i] == "/":
                    result = int(float(first_num) / second_num)
                stack.append(result)
            else:
                stack.append(tokens[i])

        return int(stack.pop())
                