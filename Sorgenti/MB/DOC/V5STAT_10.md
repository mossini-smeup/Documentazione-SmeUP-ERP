# I flag statistici del modulo V5


## Flag statistici
L'estrazione statistica considera tutti i flag statistici attualmente presenti sui file V5 (V5TDOC e V5RDOC).
Sul flag D6FL02 del V5STAT viene riportata l'informazione relativa ai flag statistici V5 origine. I documenti esclusi vengono comunque riportati in statistica con valori e/o quantità nulli.

**Esempio**
Una riga del V5 con flag R§FL19='4' (statistica solo valore), verrà riportata in statistica azzerando la quantità, ma lasciando inalterata il valore. Il flag D6FL02 del V5STAT assumerà valore '2'.
Un documento V5 con flag di testa T§FL02='9' verrà riportato in statistica con qtà e valori nulli. Il flag D6FL02 del V5STAT assumerà valore '1'

Per riassumere : 
 * _2_D6FL02='1' , deriva da flag V5TDOC - T§FL02='9'  - da non integrare in statistica
 ** i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO
 * _2_D6FL02='2'  , deriva da flag V5RDOC - R§FL19='4'  - statistica solo valore
 ** i campi su V5STAT relativi a QTA' sono uguali a ZERO
 * _2_D6FL02='3'  , deriva da flag V5RDOC - R§FL19='5'  - non genera statistiche
 ** i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO
 * _2_D6FL02='4'  , deriva da flag V5RDOC - R§FL19='6'  - statistica solo qtà
 ** i campi su V5STAT relativi a VALORE sono uguali a ZERO
 * _2_D6FL02='5'  , deriva da flag V5RDOC - R§FL22='1'  - escludo da statistica
 ** i campi su V5STAT relativi a QTA' e VALORE sono uguali a ZERO

I valori esclusi da statistica vengono salvati sul campo D6NUM0 del V5STAT per eventuali controlli.
