Die meisten IDEs (Intelligente Entwicklungsumgebungen), wie PyCharm, verfügen über integrierte Tools zum Debuggen. Dies wird normalerweise als Debugger bezeichnet. In vielerlei Hinsicht ähneln sie print-Anweisungen, sind jedoch wesentlich leistungsfähiger.

Debugger ermöglichen es uns, während der Ausführung Einblicke in unseren Code zu gewinnen und an ausgewählten Zeilen anzuhalten, um die inneren Mechanismen zu verstehen und herauszufinden, wo ein Fehler liegt.

Es gibt einige Funktionen, die in den meisten IDEs gleich sind und mit denen du vertraut sein solltest:

1. **Breakpoint (Haltepunkt)** - Du kannst einen Haltepunkt setzen, indem du auf eine Zeile im Randbereich des Codes klickst (dort, wo sich die Zeilennummern befinden). Diese Zeile ist der Punkt, an dem das Programm während des Debuggens anhält.

2. **Step Over (Überspringen)** - Diese Schaltfläche führt den Code Zeile für Zeile aus und ermöglicht es dir, die Zwischenergebnisse deiner Variablen zu sehen.

3. **Step Into (Hineingehen)** - Diese Funktion tritt in andere Module ein, auf die dein Code verweist. Zum Beispiel: Wenn du eine Funktion aus dem random-Modul verwendest, zeigt es dir den Originalcode dieser Funktion, damit du deren Funktionalität und Zusammenhang mit deinen Problemen besser verstehst.

4. **Step Into My Code (In meinen Code hineingehen)** - Dies funktioniert ähnlich wie Step Into, beschränkt jedoch den Umfang auf den Code deines eigenen Projekts und ignoriert Bibliothekscode wie beispielsweise random.

### PAUSE 1  
Verwende den Debugger von PyCharm, um das Problem im Startcode zu identifizieren und zu beheben.