Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> input("Digite um numero")
Digite um numero3
'3'
>>> 
=============================== RESTART: Shell ===============================
>>> a=input("Digite um numero: ")
Digite um numero: 2
>>> print("O número informado foi %d" %a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("O número informado foi %d" %a)
TypeError: %d format: a number is required, not str
>>> print ("O número informado foi " a)
SyntaxError: invalid syntax
>>> print ("O numero informado foi " + a)
O numero informado foi 2
>>> 
