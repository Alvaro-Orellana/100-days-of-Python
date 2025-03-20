Python unterscheidet sich etwas von anderen Programmiersprachen, da es keinen Block-Scope besitzt.

Das bedeutet, dass Variablen, die innerhalb verschachtelter Code-Blöcke wie z. B. for-Schleifen, if-Bedingungen, while-Schleifen usw. erstellt werden, keinen lokalen Scope erhalten. Sie bekommen einen Funktions-Scope, wenn sie sich innerhalb einer Funktion befinden, oder einen globalen Scope, wenn das nicht der Fall ist.

z. B.

```
# Überall zugänglich
my_global_var = 1

def my_function():
    # Nur innerhalb von my_function() zugänglich
    my_local_var = 2
    
for _ in range(10):
    # Überall zugänglich
    my_block_var = 3