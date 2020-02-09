##### My Simple Calculator v.1.0

*Written on Lua 5.2 & Python 3.7*

------

Syntax in EBNF:

```ebnf
<digit>  = '0'...'9'
<number> = <digit>, {<digit>}, ['.', <digit>, {digit}]
<fun2>   = ['+' | '-'], {('(', <expr>, ')') | <number>}
<fun1>   = <fun2>, {('*' | '/'), <fun2>}
<expr>   = <fun1>, {('+' | '-'), <fun1>}
```

Example:

```
5/(10.5+3)
^ start of current position

<expr> -> <fun1> -> <fun2>
                    '5' != ['+' | '-']
                    '5' != '('
                    <fun2> -> <number>
                              '5' == <digit>
                              '/' != <digit> | '.'
          <fun1> <- <fun2> <- <number>
          '/' == ('*' | '/')
          <fun1> -> <fun2>
                    ... (brackets)
       <----------- (in recursion)
```

