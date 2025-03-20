### Lokaler Gültigkeitsbereich (Local Scope)
Variablen (oder Funktionen), die innerhalb von Funktionen deklariert werden, haben einen lokalen Gültigkeitsbereich (auch Funktions-Gültigkeitsbereich genannt). Sie sind nur für andere Codes innerhalb desselben Codeblocks sichtbar.

z. B.
```
def my_function():
    my_local_var = 2
    
# Dies führt zu einem NameError
print(my_local_var) 
```

### Globaler Gültigkeitsbereich (Global Scope)
Variablen oder Funktionen, die auf der obersten Ebene (ohne Einrückung) einer Code-Datei deklariert werden, haben einen globalen Gültigkeitsbereich. Sie sind überall in der Code-Datei zugänglich.

z. B.

```
my_global_var = 3

def my_function():
    # Das funktioniert ohne Probleme
    print(my_global_var)