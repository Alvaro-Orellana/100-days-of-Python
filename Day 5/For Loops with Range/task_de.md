Die Kombination der `range()`-Funktion mit der Python-For-Schleife ermöglicht es uns, eine Schleife so oft auszuführen, wie wir möchten. Anstatt durch jedes Element in einer Liste zu iterieren, können wir durch einen Zahlenbereich iterieren.

### Range-Funktion

`range(1, 10)`

Dieser Code tut alleine nichts. Zum Beispiel, wenn Sie versuchen würden, ihn auszugeben, würde er keine einzelnen Zahlen anzeigen.

Aber er kann in Verbindung mit For-Schleifen verwendet werden. Zum Beispiel:

```
for number in range(1, 10):
    print(number)
```

Das wird jede Zahl von 1 bis 9 ausgeben. Der Bereich kann daher folgendermaßen ausgedrückt werden:

`a <= range(a, b) < b`

Dabei ist der Zahlenbereich inklusive der unteren Grenze, aber exklusive der oberen Grenze.

### PAUSE 1 - Die Gauss-Herausforderung  
Berechne die Summe der Zahlen zwischen 1 und 100, einschließlich sowohl 1 als auch 100.