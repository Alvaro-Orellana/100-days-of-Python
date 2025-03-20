Ihr Ziel ist es, ein [Hangman-Spiel](https://de.wikipedia.org/wiki/Hangman) zu erstellen, indem Sie alles anwenden, was Sie über Python-Programmierung gelernt haben.

### Demo-Abschlussprojekt  
https://appbrewery.github.io/python-day7-demo/

Das Projekt ist in 5 Hauptschritte unterteilt. In jedem Schritt gibt es mehrere TO-DOs. Ihr Ziel ist es, jedes To-Do der Reihe nach durchzugehen und zu bearbeiten.

Sie können alle To-Dos ganz einfach in PyCharm anzeigen, indem Sie zu Ansicht -> Werkzeugfenster -> To-Dos navigieren.

### TO-DO-1  
Wählen Sie zufällig ein Wort aus der `word_list` aus und weisen Sie es einer Variablen namens `chosen_word` zu. Anschließend drucken Sie es aus.

### TO-DO-2  
Fragen Sie den Nutzer nach einem Buchstaben und speichern Sie seine Eingabe in einer Variablen namens `guess`. Wandeln Sie den in `guess` gespeicherten String in Kleinbuchstaben um.

<div class="hint">  
  Recherchieren Sie bei Google nach der Funktion `lower()` in Python.  
</div>

### TO-DO-3  
Überprüfen Sie, ob der vom Nutzer geratene Buchstabe `guess` einer der Buchstaben im `chosen_word` ist. Durchlaufen Sie jeden Buchstaben in der `chosen_word` und drucken Sie "Richtig", wenn der Buchstabe übereinstimmt, und "Falsch", wenn dies nicht der Fall ist.

<div class="hint">  
  Sie können Strings genauso durchlaufen wie Listen - indem Sie die `for in`-Schleife verwenden.  
  Versuchen Sie bei Google zu suchen: "Strings in Python durchlaufen".  
</div>