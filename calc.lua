line  = "" -- входная строка
look  = 1  -- просматриеваемый символ
cur   = '' -- текущий символ

-- Берём следующий символ
function _next() --> char
  look = look + 1
  cur = line:sub(look-1, look-1)
  return cur
end

-- Требуемая (последовательность) символ(ов) -- ')' + для дальнейших and/or/xor
function _require(s) --> boolean
  for i=1, #s do
    if _next() ~= s:sub(i, i) then  return false  end
  end
  return true
end

-- Проверка на цифру
function isDigit(ch) --> boolean
  ch = ch or ''
  return '0' <= ch and ch <= '9'
end

local expr, fun1, fun2 -- прототипы

-- Реализация для целых чисел
function number() --> number
  local value = ""
  while isDigit(cur) do
    value = value .. cur
    _next()
  end
  return tonumber(value)
end

fun2 = function() --> number
  local value, sign = 0
  if _next() == '+' then  _next()  end
  if cur     == '-' then  sign = true; _next()  end
  while cur == '(' or isDigit(cur) do
    if cur == '(' then
      value = expr()
      _require ')'
    else
      value = number()
    end
  end
  return value * (sign and -1 or 1)
end

fun1 = function() --> number
  local value = fun2()
  while cur == '*' or cur == '/' do
    value = value * ( cur == '*' and fun1() or (1/fun1()) )
  end
  return value
end

expr = function() --> number
  local value = fun1()
  while cur == '+' or cur == '-' do
    value = value + fun1() * ( cur == '-' and -1 or 1 )
  end
  return value
end

function main() --> nil
  while true do
    line = io.read()
    if #line == 0 then  break  end
    look = 1
    print(expr())
  end
end main()
