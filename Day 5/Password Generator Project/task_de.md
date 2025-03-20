Das Programm wird fragen:
```
Wie viele Buchstaben möchten Sie in Ihrem Passwort haben?
Wie viele Symbole möchten Sie?
Wie viele Zahlen möchten Sie?
```
Das Ziel ist, die Eingaben des Benutzers zu diesen Fragen zu nehmen und dann ein zufälliges Passwort zu generieren. Nutzen Sie Ihr Wissen über Python-Listen und Schleifen, um die Aufgabe zu lösen.

### Demo
https://appbrewery.github.io/python-day5-demo/

### Einfache Version
Generieren Sie das Passwort in einer bestimmten Reihenfolge: Buchstaben, dann Symbole, dann Zahlen. Wenn der Benutzer möchte:

4 Buchstaben  
2 Symbole und  
3 Zahlen,  

dann könnte das Passwort so aussehen:

`fgdx$*924`

Sie können sehen, dass alle Buchstaben zusammen sind. Alle Symbole sind zusammen, und alle Zahlen folgen ebenfalls nacheinander. Versuchen Sie zunächst, dieses Problem zu lösen.

<div class="hint">
  Denken Sie daran, dass Sie mit der Funktion random.choice() ein zufälliges Element aus einer Liste erhalten können! Aber Sie müssen zuerst das Modul random importieren.
</div>

### Schwierige Version
Wenn Sie die einfache Version abgeschlossen haben, sind Sie bereit, die schwierige Version anzugehen. In der fortgeschrittenen Version dieses Projekts folgt das endgültige Passwort keinem Muster. Das obige Beispiel könnte also so aussehen:

`x$d24g*f9`

Und jedes Mal, wenn Sie ein Passwort generieren, sind die Positionen der Symbole, Zahlen und Buchstaben unterschiedlich. Dies macht das Passwort schwieriger für Hacker zu knacken.

Eine essenzielle Fähigkeit eines guten Programmierers ist es, Google zu nutzen, um das zu finden, was man benötigt. Ihr Gehirn ist zum Denken da, nicht zum Auswendiglernen von Funktionen! Sie müssen Google verwenden, um dieses Projekt auf der schwierigen Stufe zu lösen. Wenn Sie stecken bleiben, schauen Sie sich den Hinweis unten an, was Sie googeln sollten.

<div class="hint">
  Versuchen Sie zu googeln: "Wie mischt man Elemente in einer Liste in Python"
</div>