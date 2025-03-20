Schleifen erlauben es uns, dem Computer mitzuteilen, Aktionen zu wiederholen, ohne den Code mehrmals schreiben zu müssen. Wenn wir den Computer anweisen wollten, die Zahlen von 1 bis 100 auszugeben, wäre es sehr mühsam, für jede Zahl eine `print`-Anweisung zu schreiben oder sogar einfach alle Zahlen von 1 bis 100 abzutippen. Schleifen ermöglichen es uns, eine Regel zu erstellen, die der Computer befolgen kann, um eine wiederholte Aktion auszuführen.

### Syntax

```
for <Variablenname jedes Elements> in <eine Liste>:
    <etwas tun>
    <etwas anderes tun> 
```

### PAUSE 1 - Sei ein Computer  
Sage vorher, was durch den folgenden Code ausgegeben wird:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### Einrückungen  
Einrückungen sind in der Python-Programmierung äußerst wichtig. Jedes Mal, wenn das Symbol `:` verwendet wird, musst du auf die darauf folgende Einrückung achten.

z. B. Dieses Codebeispiel wird sich sehr unterschiedlich verhalten

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

im Vergleich zu diesem Code:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")