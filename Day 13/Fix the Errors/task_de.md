Beheben Sie alle Fehler (rote Unterstriche), die im Editor angezeigt werden, bevor Sie Ihren Code ausführen. Die Warnungen (gelb) sind optionale Korrekturen, manchmal führen sie später zu einem Problem, manchmal sind sie in Ordnung und der Editor versteht einfach nicht, was Sie tun möchten.

### Ausnahmen abfangen
Sie können in Python einen try/except-Block verwenden, um Ausnahmen abzufangen, die möglicherweise auftreten könnten. Zum Beispiel, wenn Sie annehmen, dass ein Benutzerfehler möglich ist. Sie können verhindern, dass Ihr Code abstürzt, indem Sie dies vorhersehen. Sie fangen den gefährlichen Code in einem try-Block ab und verwenden einen except-Block, um potenzielle Fehler zu behandeln. Dann definieren Sie, was passieren soll, wenn dieser Fehler auftritt, anstatt den Code einfach abstürzen und stoppen zu lassen.

z.B.

```
try:
    print(6 > "five")
except TypeError:
    print("Man kann keine Ganzzahlen und Zeichenketten in einem Vergleich mischen")
```

### PAUSE 1 
Beheben Sie den Fehler, sodass die print-Anweisung den korrekten Wert von age im Ausgabebereich anzeigt.