Sie können mit einer Python-Liste eine einfache Sammlung von geordneten Elementen erstellen, z. B.

`fruits = ["Cherry", "Apple", "Pear"]`

oder

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### zugriff auf Elemente in Listen

Sie können den Namen der Liste angeben, gefolgt von einer eckigen Klammer und dem Index des gewünschten Elements. Zum Beispiel:

`states_of_america[0]`

liefert "Delaware".

Denken Sie daran, dass im Computerbereich immer bei der Zahl 0 gezählt wird und nicht bei 1. Also 0, 1, 2, 3 statt 1, 2, 3, 4.

### negative Indizes

Sie können Elemente in der Liste von hinten zählen, indem Sie negative ganze Zahlen verwenden. Zum Beispiel:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] # dies ergibt "Pear"
```

### Elemente modifizieren
Sie können denselben Syntax verwenden, um ein Element in einer Liste zu ändern. Zum Beispiel:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits wird jetzt zu ["Orange", "Apple", "Pear"]
```

### Elemente hinzufügen
Sie können Elemente am Ende einer Liste mit der Funktion `append()` hinzufügen. Zum Beispiel:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits wird jetzt zu ["Cherry", "Apple", "Pear", "Orange"]
```

### Listen-Dokumentation
Die Dokumentation zu Python-Listen und anderen listenbezogenen Funktionen finden Sie hier: https://docs.python.org/3/tutorial/datastructures.html