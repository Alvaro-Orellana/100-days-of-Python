### TODO-1: 
Importieren Sie das Logo aus art.py und geben Sie es aus, wenn das Programm startet.

### TODO-2: 
Was passiert, wenn der Benutzer eine Zahl/ein Symbol/ein Leerzeichen eingibt, das nicht in der Liste `alphabet` enthalten ist?

Können Sie den Code so korrigieren, dass die Zahl/das Symbol/das Leerzeichen beibehalten wird, wenn der Text codiert/decodiert wird?

z. B. 
```
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```

<div class="hint">
  Wenn es kein Buchstabe in der Liste alphabet ist, können Sie es vielleicht einfach als unverändertes Zeichen am Ende von cipher_text hinzufügen?
</div>


### TODO-3: 

Können Sie eine Möglichkeit herausfinden, wie das Verschlüsselungsprogramm neu gestartet werden kann?

z. B.

`Geben Sie 'yes' ein, wenn Sie erneut starten möchten. Andernfalls geben Sie 'no' ein.`

Wenn sie 'yes' eingeben, fragen Sie erneut nach Richtung/Text/Verschiebung und rufen Sie die Funktion `caesar()` erneut auf.

<div class="hint">
  Versuchen Sie, eine while-Schleife zu erstellen, die das Programm weiterhin ausführt, wenn der Benutzer 'yes' eingibt.
</div>