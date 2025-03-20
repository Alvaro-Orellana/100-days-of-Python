Sie können verschiedene Datentypen mischen und kombinieren, um Ihre gewünschte Struktur zu erreichen.

### Eine Liste in ein Dictionary schachteln
Anstelle eines String-Werts, der einem Schlüssel zugewiesen ist, können wir diesen durch eine Liste ersetzen. Sie können eine Liste in ein Dictionary folgendermaßen schachteln:

```
my_dictionary = {
    key1: [Liste],
    key2: Wert,
}
```

### PAUSE 1
Versuchen Sie herauszufinden, wie Sie "Lille" aus der geschachtelten Liste namens `travel_log` ausgeben können.
```
travel_log = {
    "Frankreich": ["Paris", "Lille", "Dijon"],
    "Deutschland": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  Um diesen Teil zu erhalten: <code>["Paris", "Lille", "Dijon"]</code>
benötigen Sie: <code>travel_log["Frankreich"]</code>

Daher benötigen Sie, um Lille zu erhalten:
<code>travel_log["Frankreich"][1]</code>
</div>

### Schachteln von Listen in andere Listen

Wir haben zuvor verschachtelte Listen gesehen:

```
nested_list = ["A", "B", ["C", "D"]]
```

### PAUSE 2
Erinnern Sie sich, wie man auf Elemente zugreift, die tief in einer Liste geschachtelt sind? Versuchen Sie, "D" aus der Liste `nested_list` auszugeben.

<div class="hint">
  Um diese Liste zu erhalten: ["C", "D"], benötigen wir den Code:

<code>nested_list[2]</code>

Daher benötigen wir, um "D" zu erhalten:

<code>nested_list[2][1]</code>
</div>

### Ein Dictionary in ein anderes Dictionary schachteln
Sie können auch ein Dictionary in ein anderes Dictionary schachteln:

```
my_dictionary = {
    key1: Wert,
    key2: {Schlüssel: Wert, Schlüssel: Wert},
}
```

### PAUSE 3
Finden Sie heraus, wie Sie "Stuttgart" aus der folgenden Liste ausgeben können:
```
travel_log = {
  "Frankreich": {
    "besuchte_städte": ["Paris", "Lille", "Dijon"], 
    "gesamt_besuche": 12
   },
  "Deutschland": {
    "besuchte_städte": ["Berlin", "Hamburg", "Stuttgart"], 
    "gesamt_besuche": 5
   },
}