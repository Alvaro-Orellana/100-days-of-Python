### TODO-1
- Verwenden Sie eine while-Schleife, um dem Benutzer zu ermöglichen, erneut zu raten.  
- Die Schleife sollte nur stoppen, wenn der Benutzer alle Buchstaben im `chosen_word` erraten hat.  
- Zu diesem Zeitpunkt enthält `display` keine Leerzeichen ("_") mehr. Dann können Sie dem Benutzer mitteilen, dass er gewonnen hat.

<div class="hint">
  Sie können das Schlüsselwort `in` verwenden, um zu prüfen, ob ein String oder eine Liste ein bestimmtes Element enthält.  

z. B. Google: prüfen, ob ein Buchstabe in einem String vorhanden ist python  
</div>

### TODO-2
- Aktualisieren Sie die for-Schleife, damit vorherige Eingaben zum String `display` hinzugefügt werden.  
- Im Moment wird, wenn der Benutzer eine neue Eingabe macht, die vorherige Eingabe durch ein "_" ersetzt. Wir müssen das korrigieren, indem wir die for-Schleife aktualisieren.  

<div class="hint">
  Überlegen Sie, wie Sie die gefundenen Buchstaben speichern können, und verwenden Sie ein `elif`, um zu prüfen, ob ein Buchstabe zuvor gefunden wurde.  
</div>