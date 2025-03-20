### Länge einer Liste
Sie können die Länge einer Liste (Anzahl der Elemente in der Liste) oder die Länge eines Strings (Anzahl der Zeichen im String) mit der Funktion `len()` ermitteln. https://docs.python.org/3/library/functions.html#len

### IndexError
Wenn Sie versuchen, auf ein Element zuzugreifen, das sich außerhalb des Bereichs der Liste befindet, erhalten Sie einen IndexError. Zum Beispiel:  

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #Das wird ein IndexError sein
```

### Verschachtelte Listen
Sie können Listen innerhalb anderer Listen platzieren; dies nennt man eine "verschachtelte Liste" oder eine "2D-Liste". Zum Beispiel:  

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#Die Liste würde so aussehen: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
Sie können die Liste auch im 2D-Format so darstellen:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]