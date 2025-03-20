Funktionen enden bei dem `return`-Schlüsselwort. Wenn du Code unterhalb der Return-Anweisung schreibst, wird dieser Code nicht ausgeführt.

Du kannst jedoch mehrere Return-Anweisungen in einer Funktion haben. Wie funktioniert das also?

### Bedingte Returns

Wenn wir Kontrollfluss haben, d. h. der Code verhält sich unterschiedlich (geht verschiedene Ausführungspfade entlang), abhängig von bestimmten Bedingungsprüfungen, können wir auf mehrere Enden (Returns) stoßen.

z. B.
```
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
```

### Leere Returns
Du kannst auch ein Return ohne etwas dahinter schreiben, und das signalisiert der Funktion einfach, dass sie beendet werden soll.

z. B.
```
def canBuyAlcohol(age):
    # Wenn der Datentyp der Eingabe „age“ kein int ist, dann beenden.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False