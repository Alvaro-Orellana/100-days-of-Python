### Pseudorandom-Zahlengeneratoren
Computer sind nicht wirklich zufällig, da sie aus Schaltkreisen und Schaltern bestehen. Zufälligkeit ist jedoch sehr wichtig beim Erstellen von Software, insbesondere bei Spielen. Es wäre wirklich langweilig, wenn jede Bewegung in einem Videospiel vorbestimmt wäre.

Deshalb haben einige Informatiker Pseudorandom-Zahlengeneratoren erfunden, z. B. https://de.wikipedia.org/wiki/Mersenne-Twister.

Wenn du mehr über Pseudorandom-Zahlengeneratoren erfahren möchtest, empfehle ich dir dieses Video von der Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs.

### Das Random-Modul in Python
Lies die Dokumentation hier:
https://docs.python.org/3/library/random.html.

Um es verwenden zu können, musst du es zuerst importieren:

`import random`

### Zufällige ganze Zahlen innerhalb eines Bereichs

```
import random
rand_num = random.randint(1, 10)

#Dies erzeugt eine zufällige ganze Zahl zwischen 1 und 10 (einschließlich).
```

### Module in Python
Python erlaubt es uns, Code in verschiedene Dateien zu speichern und diesen Code bei Bedarf zu importieren. Das bedeutet, dass wir unseren Code besser organisieren und modularisieren können.

Du kannst ein neues Modul erstellen, indem du einfach eine neue `.py`-Datei erstellst. Anschließend kannst du Variablen oder Funktionen aus dieser Datei mithilfe des `import`-Schlüsselworts importieren.

### Zufällige Gleitkommazahlen
Du kannst eine zufällige Zahl zwischen 0.0 (einschließlich) und 1.0 (ausschließlich) mit folgendem Code aus dem Random-Modul generieren:

```
import random
rand_num_0_to_1 = random.random()
```
Dies kann auch so ausgedrückt werden:

`0.0 <= random.random() < 1.0`

Du kannst den Bereich der damit generierten Zufallszahlen erweitern, indem du eine Multiplikation hinzufügst.

z. B. `random.random() * 5`

Dies generiert eine zufällige Zahl zwischen 0 und 5.

Eine andere Methode, um zufällige Gleitkommazahlen zu erzeugen, ist die Verwendung der Funktion `uniform()`.

```
import random
random_float = random.uniform(1, 10)
#Dies generiert eine zufällige Gleitkommazahl zwischen 1 und 10.
```
Diese Methode kann die obere Grenze je nach Rundung der Gleitkommazahl eventuell einschließen oder nicht. Es wird daher am besten wie folgt dargestellt:

`a <= random.uniform(a,b) <= b`

Je nachdem, ob du die obere Grenze einschließen möchtest oder nicht, wählst du, ob du `random.random()` oder `random.uniform()` verwenden willst.

### PAUSE 1 - Kopf oder Zahl
Erstelle ein Programm für Münzwürfe unter Verwendung deines Wissens zur Randomisierung in Python. Es sollte jedes Mal beim Ausführen zufällig "Kopf" oder "Zahl" ausgeben.  

<div class="hint">
  Du musst darüber nachdenken, was du über bedingte Anweisungen in Python gelernt hast.
</div>