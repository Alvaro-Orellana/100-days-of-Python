Sie werden ein Verschlüsselungs- und Entschlüsselungsprogramm mithilfe des [Cäsar-Chiffre-Verfahrens](https://de.wikipedia.org/wiki/C%C3%A4sar-Verschl%C3%BCsselung) erstellen.

### Demo
https://appbrewery.github.io/python-day8-demo/

### TODO-1: 
Erstellen Sie eine Funktion namens `encrypt()`, die `original_text` und `shift_amount` als 2 Eingaben entgegennimmt.

### TODO-2: 
Innerhalb der Funktion `encrypt` verschieben Sie jeden Buchstaben des `original_text` im Alphabet um die Anzahl `shift_amount` nach vorne und geben Sie den verschlüsselten Text aus.

Sie können die eingebaute Python-Funktion `index()` verwenden, um die Position eines Elements in einer Liste zu ermitteln. z. B.
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

z. B. Wenn wir die folgenden Werte haben:
```
plain_text = "hello"
shift_amount = 1
```
Die finale verschlüsselte Ausgabe sollte sein:

`Hier ist das codierte Ergebnis: ifmmp`

Dabei wird jeder Buchstabe von 'hello' um 1 nach oben verschoben. 

<div class="hint">
Lassen Sie uns das Problem aufschlüsseln:

  1. Sie benötigen eine for-Schleife, um durch jeden Buchstaben im `plain_text` zu iterieren. 
  2. Finden Sie die Position jedes Buchstabens in der Alphabet-Liste.
  3. Addieren Sie die vom Benutzer gewünschte `shift_amount` zur Position, um die Position des codierten Buchstabens zu ermitteln.
  4. Finden Sie den entsprechenden Buchstaben für diese Position.
  5. Fügen Sie jeden codierten Buchstaben zu einem neuen String hinzu und geben Sie diesen nach Ende der Schleife aus.

</div>

### TODO-3: 
Rufen Sie die Funktion `encrypt()` auf und übergeben Sie die Benutzereingaben. Sie sollten den Code testen können, um eine Nachricht zu verschlüsseln.

### TODO-4: 
Was passiert, wenn Sie versuchen, den Buchstaben 'z' um 9 nach vorne zu verschieben? Können Sie den Code korrigieren?

<div class="hint">
  Es gibt viele Ansätze, dies zu lösen.
1. Sie können mehr als 1 Satz des Alphabets zur Liste der Alphabet-Buchstaben hinzufügen.
2. Sie können die `shift_amount` so anpassen, dass sie immer im Bereich von 0 bis 25 liegt und in die Liste passt.
3. Sie können den Modulo verwenden, um den Rest zu erhalten.
</div>