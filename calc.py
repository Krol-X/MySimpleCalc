line = "" # входная строка
look = 0  # просматриеваемый символ
cur  = '' # текущий символ

def _next(): # string (char)
	global line, look, cur
	look += 1
	if look > len(line):
		cur = ' '
	else:
		cur = line[look-1]
	return cur

# Требуемая (последовательность) символ(ов) -- ')' + для дальнейших and/or/xor
def _require(s): # bool
	for i in range(len(s)):
		if _next() != s[i]:
			return False
	return True

# Проверка на цифру
def isDigit(ch): # bool
	return '0' <= ch and ch <= '9'

# Прототипы:
def expr(): pass
def fun1(): pass
def fun2(): pass

# Реализация для целых чисел
def number(): # int
	global cur
	value = ""
	while isDigit(cur):
		value = value + cur
		_next()
	return int(value)

def fun2(): # int
	global cur
	value = 0
	sign = False
	if _next() == '+': _next()
	if cur     == '-':
		sign = True
		_next()
	while cur == '(' or isDigit(cur):
		if cur == '(':
			value = expr()
			_require(')')
		else:
			value = number()
	return value * (sign and -1 or 1)

def fun1(): # int
	global cur
	value = fun2()
	while cur == '*' or cur == '/':
		value = value * ( cur == '*' and fun1() or (1/fun1()) )
	return value

def expr(): # int
	global cur
	value = fun1()
	while cur == '+' or cur == '-':
		value = value + fun1() * ( cur == '-' and -1 or 1 )
	return value

def main():
	global line, look
	while True:
		line = input()
		if len(line) == 0: break
		look = 0
		print(expr())

if __name__ == "__main__":
	main()