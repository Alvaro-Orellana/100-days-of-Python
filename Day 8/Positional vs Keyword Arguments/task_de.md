### Mehrere Eingaben
In Funktionen können Sie mehrere Eingaben verwenden. Alles, was Sie tun müssen, ist, sie durch ein Komma `,` zu trennen.

### PAUSE 1
Erstellen Sie eine Funktion mit mehreren Eingaben

<div class="hint">
  <code>
def greet(name, greeting):

    ____print(f"{greeting} {name}")
    
greet("Angela", "Yo!")
</code>
</div>

### PAUSE 2
Ändern Sie die Funktion so, dass sie die erwarteten Werte ausgibt.
```
def greet_with(name, location)
    Hallo name
    Wie ist es in location
```

### Positionsargumente
Standardmäßig wird in Python, wenn Sie eine Funktion erstellen, die Reihenfolge der Argumente in der Funktionsdefinition eingehalten.

z.B. In der unten stehenden Funktion wird das erste Argument, das hineingegeben wird, immer vor dem zweiten Argument ausgegeben. `a = 2, b = 1`

```
def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 # Es wird ausgegeben:
 # 2
 # 1
```

### Schlüsselwortargumente
Sie können Schlüsselwörter verwenden, wenn Sie die Argumente beim Aufrufen einer Funktion angeben, damit weniger Verwirrung darüber besteht, welcher Wert welchem Eingabeparameter zugeordnet wird.

### PAUSE 3
Rufen Sie die `greet_with()`-Funktion mithilfe von Schlüsselwortargumenten auf.

<div class="hint">
  <code>
greet_with(location="London", name="Angela")
</code>
</div>