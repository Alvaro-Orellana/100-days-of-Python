Sie können Docstrings verwenden, um mehrzeilige Kommentare zu schreiben, die Ihren Code dokumentieren.

### Syntax  
Schließen Sie Ihren Text einfach in ein Paar von drei doppelten Anführungszeichen ein.  

z. B.  
```
"""
Mein
mehrzeiliger
Kommentar
"""

```

### Funktionen dokumentieren  
Ein praktisches Merkmal von Docstrings ist, dass Sie sie direkt unter der Definition einer Funktion verwenden können, und dieser Text wird angezeigt, wenn Sie mit der Maus über einen Funktionsaufruf fahren. Es ist eine gute Möglichkeit, sich daran zu erinnern, was eine selbst erstellte Funktion macht.  

z. B.  
```
def meine_funktion(num):
    """Multipliziert eine Zahl mit sich selbst."""
    return num * num