Mit `global` können Sie den Code dazu zwingen, Ihnen zu erlauben, etwas zu ändern, indem Sie das Schlüsselwort `global` verwenden, bevor Sie es nutzen.

z. B. Dies führt zu einem Fehler:

```
a = 1
def my_function():
    a += 1
    print(a)
```

Aber das wird funktionieren:
```
a = 1
def my_function():
    global a
    a += 1
    print(a)