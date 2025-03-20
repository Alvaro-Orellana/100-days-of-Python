Sie können so viele if-Anweisungen schreiben, wie Sie benötigen, um unterschiedliche, voneinander unabhängige Bedingungen zu überprüfen.  
Vergleichen Sie die Codeblöcke unten:  
```
# If/elif/else
if <Bedingung 1 ist wahr>
    <führe A aus>
elif <Bedingung 2 ist wahr>
    <führe B aus>
else
    <führe C aus>
```
```
# Verschachtelte if-Anweisungen
if <Bedingung 1 ist wahr>
    <führe A aus>
    if <Bedingung 2 ist wahr>
        <führe B aus>
        if <Bedingung 3 ist wahr>
            <führe C aus>
```

```
# Mehrere if-Anweisungen
if <Bedingung 1 ist wahr>
    <führe A aus>
if <Bedingung 2 ist wahr>
    <führe B aus>
if <Bedingung 3 ist wahr>
    <führe C aus>
```

Im If/elif/else-Block kann nur eines der Ergebnisse A, B oder C eintreten, weil if/elif/else sich gegenseitig ausschließen. Die erste Bedingung muss fehlschlagen, um in die elif-Anweisung zu gelangen, und die elif-Anweisung (oder mehrere elif-Anweisungen) müssen fehlschlagen, damit der else-Block ausgeführt wird. Bedingung 2 wird nur überprüft, wenn Bedingung 1 falsch ist.

In den verschachtelten if-Anweisungen können A, B und C alle eintreten, aber die Bedingungen 1, 2 und 3 müssen alle wahr sein. Der Computer überprüft Bedingung 2 nur, wenn Bedingung 1 wahr ist.

In den mehreren if-Anweisungen können A, B und C alle eintreten. Diese sind jedoch vollständig voneinander unabhängig. C kann eintreten, selbst wenn A und B nicht eintreten. Jede Bedingung wird überprüft, unabhängig vom Ergebnis der anderen.