### Wähle deinen Schwierigkeitsgrad
- **Normal** 😎: Verwende alle Hinweise unten, um das Projekt abzuschließen.
- **Schwer** 🤔: Verwende nur Hinweise 1, 2, 3, um das Projekt abzuschließen.
- **Extra Schwer** 😭: Verwende nur Hinweise 1 & 2, um das Projekt abzuschließen.
- **Experte** 🤯: Verwende nur Hinweis 1, um das Projekt abzuschließen.

### Unsere Blackjack-Spielregeln

- Das Deck hat eine unbegrenzte Größe.
- Es gibt keine Joker.
- Bube/Dame/König zählen jeweils als 10.
- Das Ass kann entweder als 11 oder 1 zählen.
- Verwende die folgende Liste als Kartenstapel:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- Die Karten in der Liste haben die gleiche Wahrscheinlichkeit gezogen zu werden.
- Karten werden nicht aus dem Stapel entfernt, nachdem sie gezogen wurden.
- Der Computer ist der Dealer.

<div class="hint" title="Hinweis 1">
  Besuche diese Website und probiere das Blackjack-Spiel aus: 

https://games.washingtonpost.com/games/blackjack/

Teste danach das abgeschlossene Blackjack-Projekt hier: 

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hinweis 2">
Lese diese Aufschlüsselung der Programmanforderungen: 

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Erstelle danach dein eigenes Flussdiagramm für das Programm.

</div>

<div class="hint" title="Hinweis 3">
  Lade dieses Flussdiagramm herunter und sieh es dir an, das ich erstellt habe:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

</div>

<div class="hint" title="Hinweis 4">
  Erstelle eine Funktion <code>deal_card()</code>, die die Liste unten verwendet, um eine zufällige Karte zurückzugeben.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Denke daran, dass 11 das Ass ist.
</div>

<div class="hint" title="Hinweis 5">
  Teile dem Nutzer und dem Computer jeweils 2 Karten zu, indem du <code>deal_card()</code> und <code>append()</code> verwendest.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hinweis 6">
  Erstelle eine Funktion mit dem Namen <code>calculate_score()</code>, die eine Liste mit Karten als Eingabe nimmt 
und die Summe aller Karten in der Liste als Punktzahl zurückgibt. 
Recherchiere die Funktion <code>sum()</code>, um dir dabei zu helfen.
</div>

<div class="hint" title="Hinweis 7">
Innerhalb von <code>calculate_score()</code> prüfe auf ein Blackjack (eine Hand mit nur 2 Karten: Ass + 10) und gib <code>0</code> anstelle der tatsächlichen Punktzahl zurück. <code>0</code> repräsentiert ein Blackjack in unserem Spiel.
</div>

<div class="hint" title="Hinweis 8">
  Innerhalb von <code>calculate_score()</code> prüfe auf eine 11 (Ass). Falls die Punktzahl bereits über 21 liegt, entferne die 11 und ersetze sie durch eine 1. Du musst möglicherweise nach der Dokumentation zu den Python-integrierten Funktionen <code>append()</code> und <code>remove()</code> suchen.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hinweis 9">
  Rufe die Funktion <code>calculate_score()</code> auf. Falls der Computer oder der Nutzer ein Blackjack (0) hat oder die Punktzahl des Nutzers über 21 liegt, endet das Spiel.
</div>

<div class="hint" title="Hinweis 10">
  Falls das Spiel noch nicht beendet ist, frage den Nutzer, ob er eine weitere Karte ziehen möchte. Wenn ja, benutze die Funktion <code>deal_card()</code>, um eine weitere Karte zur Liste <code>user_cards</code> hinzuzufügen. Falls nein, endet das Spiel.
</div>

<div class="hint" title="Hinweis 11">
  Die Punktzahl muss nach jeder neu gezogenen Karte erneut geprüft werden, und die Prüfungen aus Hinweis 9 müssen wiederholt werden, bis das Spiel endet.
</div>

<div class="hint" title="Hinweis 12">
  Sobald der Nutzer fertig ist, ist der Computer an der Reihe. Der Computer sollte weiterhin Karten ziehen, solange seine Punktzahl weniger als 17 beträgt.
</div>

<div class="hint" title="Hinweis 13">
  Erstelle eine Funktion <code>compare()</code> und übergib <code>user_score</code> und <code>computer_score</code>. 

- Wenn der Computer und der Nutzer die gleiche Punktzahl haben, ist es ein Unentschieden.
- Wenn der Computer ein Blackjack (0) hat, verliert der Nutzer. 
- Wenn der Nutzer ein Blackjack (0) hat, gewinnt der Nutzer. 
- Wenn die <code>user_score</code> über 21 liegt, verliert der Nutzer. 
- Wenn die <code>computer_score</code> über 21 liegt, verliert der Computer. 
- Falls keiner der oben genannten Fälle zutrifft, gewinnt der Spieler mit der höchsten Punktzahl.
</div>

<div class="hint" title="Hinweis 14">
  Frage den Nutzer, ob er das Spiel neu starten möchte. Wenn er mit ja antwortet, lösche die Konsole und starte ein neues Blackjack-Spiel und zeige das Logo aus art.py an.
</div>