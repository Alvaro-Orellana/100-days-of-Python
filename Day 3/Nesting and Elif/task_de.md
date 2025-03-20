### Verschachtelte konditionale Anweisungen  
Sie können if/else-Anweisungen innerhalb anderer if/else-Anweisungen platzieren. Dies wird als Verschachtelung bezeichnet.  
z. B.

```
if maths_score >= 90:
    if english_score >= 90:
        print("Du bist in allem gut")
    else:
        print("Du bist gut in Mathe")
if english_score >= 90:
    print("Du bist gut in Englisch")
```

In diesem Fall erhält ein Schüler nur dann die Ausgabe "Du bist in allem gut", wenn er in Mathe und Englisch über 90 erreicht.

Hinweis: Sie können auch if-Anweisungen verwenden, die keine zugehörige else-Anweisung haben.