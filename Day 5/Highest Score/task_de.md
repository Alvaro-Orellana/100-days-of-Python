### Sum
Python hat viele eingebaute Funktionen, die uns beim Arbeiten mit Zahlen helfen. Eine davon hilft uns, die Summe (den Gesamtwert) zu berechnen.  
z. B.
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
```
Aber wie funktioniert `sum()` hinter den Kulissen? Der Code wird von den Leuten geschrieben, die Python entwickelt haben, und könnte in etwa so aussehen:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
```



### pause 1 - max
Es gibt auch eingebaute Python-Methoden namens `max()` und `min()`, mit denen Sie eine Liste von Zahlen übergeben können, um die höchste bzw. die niedrigste Zahl zu erhalten.  

Ihre Aufgabe ist es, herauszufinden, wie die Python-Programmierer diese Funktionalität mithilfe von Schleifen und Bedingungen erstellt haben könnten.

## LÖSEN SIE DIESE AUFGABE OHNE VERWENDUNG VON max()

Sie erhalten eine Liste von Prüfungsergebnissen und müssen die höchste Punktzahl aus der Liste ausgeben.  
Dazu müssen Sie das, was Sie über Listen, For-Schleifen und Bedingungen gelernt haben, nutzen, um die höchste Punktzahl aus der Liste `student_scores` auszugeben.  
Zum Beispiel, wenn die Ergebnisse lauten:  
```
8 65 89 86 55 91 64 89
```
sollte Ihr Code ausgeben:
```
91
```