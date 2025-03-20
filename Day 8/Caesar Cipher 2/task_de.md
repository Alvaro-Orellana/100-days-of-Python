### TODO-1: 
Erstellen Sie eine Funktion namens `decrypt()`, die `original_text` und `shift_amount` als 2 Eingaben annimmt.

### TODO-2: 
Innerhalb der Funktion `decrypt()` verschieben Sie jeden Buchstaben des `original_text` vorwärts im Alphabet *rückwärts* um den `shift_amount` und geben Sie den entschlüsselten Text aus.

<div class="hint">
  Sie können jede Zahl mit -1 multiplizieren, um diese in eine negative Zahl umzuwandeln.
</div>

### TODO-3: 
- Kombinieren Sie die Funktionen `encrypt()` und `decrypt()` in eine einzige Funktion namens `caesar()`.  
- Verwenden Sie den Wert der vom Benutzer gewählten Variablen `direction`, um zu bestimmen, welche Funktionalität genutzt werden soll.  
- Rufen Sie die Funktion `caesar` anstelle von encrypt/decrypt auf und übergeben Sie alle drei Variablen `direction`/`text`/`shift`.

<div class="hint">
  Denken Sie daran, dass die Multiplikation einer Zahl mit -1 ihr Vorzeichen umkehrt.  
z. B. <code>3 + (5 * -1)</code> ist dasselbe wie <code>3 - 5</code>.
</div>

<div class="hint">
Es sollte heißen:  

<code>Hier ist das kodierte Ergebnis: XXX</code>

oder  

<code>Hier ist das dekodierte Ergebnis: XXX</code> 
</div>