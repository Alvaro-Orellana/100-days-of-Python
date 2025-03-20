### TODO-1
- Erstelle einen leeren String namens `placeholder`.
- Füge für jeden Buchstaben im `chosen_word` ein `_` zu `placeholder` hinzu.
- Wenn also das `chosen_word` "apple" war, sollte `placeholder` `_ _ _ _ _` sein, wobei 5 `"_"` jeweils einen zu erratenden Buchstaben repräsentieren.
- Gib `hint` aus.

<div class="hint">
  Denke daran, dass du die Funktion range() in einer Schleife verwenden kannst, um eine Aktion eine bestimmte Anzahl von Malen auszuführen. 
</div>

### TODO-2
- Erstelle einen leeren String namens `display`.
- Durchlaufe jeden Buchstaben im `chosen_word`.
- Wenn der Buchstabe an dieser Position mit `guess` übereinstimmt, zeige diesen Buchstaben an der entsprechenden Position im `display` an.
- z.B. Wenn der Benutzer "p" geraten hat und das gewählte Wort "apple" war, sollte `display` `_ p p _ _` sein.
- Gib `display` aus und du solltest den geratenen Buchstaben an der richtigen Position sehen.
- Aber jeder Buchstabe, der nicht übereinstimmt, wird durch ein "_" dargestellt.

<div class="hint">
  Denke daran, dass die for-Schleife jeden Buchstaben im `chosen_word` der Reihe nach durchläuft. Du kannst diese Tatsache nutzen, um einen neuen String zu erstellen, indem du den Buchstaben oder ein "_" anhängst.
</div>