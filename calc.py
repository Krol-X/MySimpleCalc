from traceback import format_exc


def compute(s):
    """Compute a mathematics expression"""
    line = s  # input string (stream)
    look = 0  # looked char (next current char)
    cur = ''  # current char

    def next_():  # string (char)
        """Return next character of the input stream"""
        nonlocal line, look, cur
        look += 1
        if look > len(line):
            cur = '\0'
        else:
            cur = line[look - 1]
        return cur

    def require(s):  # bool
        """Check input stream for the string"""
        for i in range(len(s)):
            if next_() != s[i]:
                return False
        return True

    digits = "0123456789"

    def reqenum(s, _next=False):  # bool
        """Check input stream for the characters"""
        if _next:
            next_()
        for i in range(len(s)):
            if cur == s[i]:
                return True
        return False

    def skip_blank():
        """Skip blank characters from input stream"""
        while cur != '\0' and cur <= ' ':
            next_()

    # def expr(): pass
    # def fun1(): pass
    # def fun2(): pass

    def number():  # int
        """Number recognize function"""
        nonlocal cur
        result = ""
        while cur.isdigit():
            result = result + cur
            next_()
        if cur == '.':
            if result == "":
                result = "0"
            result = result + cur
            assert (reqenum(digits, True))
            while cur.isdigit():
                result = result + cur
                next_()
        return int(result)

    def fun2():  # int
        """Expression level 2"""
        nonlocal cur
        result, sign = 0, False
        next_()
        skip_blank()
        assert (reqenum("(+-" + digits))
        if cur == '+': next_()
        if cur == '-':
            sign = True
            next_()
        skip_blank()
        while cur == '(' or cur.isdigit():
            if cur == '(':
                result = fun0()
                skip_blank()
                require(')')
            else:
                result = number()
            skip_blank()
        return result * (sign and -1 or 1)

    def fun1():  # int
        """Expression level 1"""
        nonlocal cur
        result = fun2()
        skip_blank()
        while cur == '*' or cur == '/':
            result = result * (cur == '*' and fun1() or (1 / fun1()))
        return result

    def fun0():  # int
        """Expression level 0"""
        nonlocal cur
        result = fun1()
        skip_blank()
        while cur == '+' or cur == '-':
            result = result + (cur == '-' and -1 or 1) * fun1()
        return result

    try:
        result = fun0()
        assert (cur == '\0')
    except onException:
        # print(format_exc())
        print(' ' * (look - 1) + '^ there is error')
        return None
    return result


def _main():
    while True:
        line = input()
        if len(line) == 0: break
        result = compute(line)
        if result:
            print(result)


if __name__ == "__main__":
    _main()
