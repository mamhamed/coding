class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-', '*', '/'}

        st = []
        for t in tokens:
            if t not in operators:
                st.append(int(t))
            else:
                b, a = st.pop(), st.pop()
                if t == '+':
                    st.append(a + b)
                elif t == '-':
                    st.append(a - b)
                elif t == '*':
                    st.append(a * b)
                elif t == '/':
                    # this might be a bug
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if a*b < 0 and a % b != 0:
                        st.append(a/b+1)
                    else:
                        st.append(a/b)

        return st.pop()

# print Solution().evalRPN(["2", "1", "+", "3", "*"])
# print Solution().evalRPN(["4", "13", "5", "/", "+"])
# print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print Solution().evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])