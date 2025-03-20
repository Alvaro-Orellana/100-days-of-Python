Ein Wörterbuch (dictionary) in Python funktioniert ähnlich wie ein Wörterbuch im realen Leben. Es ist eine Datenstruktur, die es uns ermöglicht, einen Schlüssel mit einem Wert zu verknüpfen und diese beiden Datenstücke zusammenzuführen.

So erstellt man ein Wörterbuch in Python:
```
# Ein Beispiel-Wörterbuch
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

```

So ruft man Elemente aus einem Wörterbuch ab:
```
print(colours["pear"])
# Gibt "green" aus
```

So erstellt man ein leeres Wörterbuch:
```
my_empty_dictionary = {}
```

So können Sie neue Elemente zu einem vorhandenen Wörterbuch hinzufügen:

```
colours["peach"] = "pink"
```

So kann man einen vorhandenen Wert in einem Wörterbuch bearbeiten:
```
colours["apple"] = "green"
```

So durchläuft man ein Wörterbuch und gibt alle Schlüssel aus:
```
for key in colours:
    print(key)
```

So durchläuft man ein Wörterbuch und gibt alle Werte aus:
```
for key in colours:
    print(colours[key])