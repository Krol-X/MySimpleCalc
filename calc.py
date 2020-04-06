from traceback import format_exc

_debug = False
_line = ''  # input string (stream)
_look = 0  # looked char (current next char)
_cur = ''  # _current char


class ParseError(Exception):
    def __init__(self):
        self.text = 'Parse error at %d character in "%s"' % (_look, _line)
        self.n = _look


def next_():  # string (char)
    """Return next character of the input stream"""
    global _line, _look, _cur
    _look += 1
    if _look > len(_line):
        _cur = '\0'
    else:
        _cur = _line[_look - 1]
    return _cur


def require(s):  # bool
    """Check input stream for the string"""
    for i in range(len(s)):
        if next_() != s[i]:
            return False
    return True


_digits = "0123456789"


def reqenum(s, call_next=False):  # bool
    """Check input stream for the characters"""
    global _cur
    if call_next:
        next_()
    for i in range(len(s)):
        if _cur == s[i]:
            return True
    return False


def skip_blank():
    """Skip blank characters from input stream"""
    global _cur
    while _cur != '\0' and _cur <= ' ':
        next_()


def _fun0(): pass


def _fun1(): pass


def _fun2(): pass


def _number():  # int
    """Number recognize function"""
    global _cur
    result = ""
    while _cur.isdigit():
        result = result + _cur
        next_()
    if _cur == '.':
        if result == "":
            result = "0"
        result = result + _cur
        if not reqenum(_digits, True):
            raise ParseError
        while _cur.isdigit():
            result = result + _cur
            next_()
    return int(result)


def _fun2():  # int
    """Expression level 2"""
    global _cur
    result, sign = 0, False
    next_()
    skip_blank()
    if not reqenum("(+-" + _digits):
        raise ParseError
    if _cur == '+':
        next_()
    if _cur == '-':
        sign = True
        next_()
    skip_blank()
    while _cur == '(' or _cur.isdigit():
        if _cur == '(':
            result = _fun0()
            skip_blank()
            require(')')
        else:
            result = _number()
        skip_blank()
    return result * (sign and -1 or 1)


def _fun1():  # int
    """Expression level 1"""
    global _cur
    result = _fun2()
    skip_blank()
    while _cur == '*' or _cur == '/':
        result = result * (_cur == '*' and _fun1() or (1 / _fun1()))
    return result


def _fun0():  # int
    """Expression level 0"""
    global _cur
    result = _fun1()
    skip_blank()
    while _cur == '+' or _cur == '-':
        result = result + (_cur == '-' and -1 or 1) * _fun1()
    return result


def compute(s):
    """Compute a mathematics expression"""
    global _line, _look, _cur
    _line, _look = s, 0
    result = _fun0()
    if _cur != '\0':
        raise ParseError
    return result


###########################################################################
# TEST CODE
###########################################################################

if __name__ == "__main__":
    while True:
        print(">", end='')
        line = input()
        if len(line) == 0: break
        try:
            result = compute(line)
        except ParseError as ex:
            print(' ' * ex.n + "^")
            print(ex.text)
            if _debug:
                print(format_exc())
        except Exception as ex:
            print("Some exception :(")
            print(format_exc())
        else:
            print(result)
        print()
