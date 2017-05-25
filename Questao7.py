Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = int(input("Digite o primeiro valor: "))
Digite o primeiro valor: 2
>>> b = int(input("Digite o segundo valor: "))
Digite o segundo valor: 1
>>> print("A soma é %i " % soma)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("A soma é %i " % soma)
NameError: name 'soma' is not defined
>>> soma=a+b
>>> print("A soma é %i " % soma)
A soma é 3 
>>> 
