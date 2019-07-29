## Obiettivo
Gestire il conguaglio degli anticipi corrisposti all'agente.

## Parametri di lancio
* Anno :  è l'anno di riferimento
* Data limite :  la data all'interno dell'anno a cui voglio la situazione
* Agente :  permette di limitare l'analisi ad un singolo agente

## Dettaglio informazioni

* Dettaglio :  mi permette di vedere il dettaglio delle provvigioni che hanno generato i totali della riga.
* Agente
* Importo provvigioni :  l'importo viene recuperato nel seguente modo : 
** Dalle sole provvigioni immesse con data corrispondente all'anno di riferimento, se così viene fissato nella tabella V58, tramite il campo "Escludi provvigioni degli anni precedenti". ** Dalle immesse nell'anno o aperte ad inizio anno se il succitato campo non è stato impostato.
** In entrambi i casi sono inoltre escluse le provvigioni che nella tabella V5P hanno impostato il tipo provvigione valorizzato a : 
*** 0 :  fisso
*** 2 :  minimo garantito
*** 9 :  anticipo
** Vengono infine escluse le provvigioni che nella tabella V5P hanno impostato il campo "Escludi da conguaglio anticipi".
* Provvigioni liquidate :  a partire dallo stesso insieme di provvigioni definito al punto precedente, viene recuperato l'importo già liquidato definitivamente.
* Provvigioni in liquidazione :  come sopra solo che nell'importo finisce quello che è in al momento dell'interrogazione.
* Provvigioni escluse :  è dato alla sommatoria delle provvigioni liquidate ed in liquidazione lette secondo lo stesso criterio dell'importo provvigioni, ma contando solo le provvigioni che hanno valorizzato nella tabella V5P il campo "Escludi da conguaglio anticipi".
* Minimo garantito :  come sopra, ma contando solo le provvigioni che hanno valorizzato nella,
tabella V5P il tipo imponibile a "2" e solo se di segno positivo.
* Anticipi :  come sopra, ma contando solo le provvigioni che hanno valorizzato nella,
tabella V5P il tipo imponibile a "9" e solo se di segno positivo.
* Conguagli :  come sopra, ma contando solo le provvigioni che hanno valorizzato nella, tabella V5P il tipo imponibile a "2" o "9", ma con segno negativo. Sono infatti le provvigioni negative di tipo anticipo ad essere riconosciute come operazioni di conguaglio.
* Totale anticipi :  è dato dalla sommatoria delle tre precedenti colonne : 
** + minimo garantito
** + anticipi
** - conguagli
* Proposta conguaglio :  solo se il totale anticipazioni è diverso da 0, tale importo viene messo a confronto con differenza fra totale conguagliabile ed il totale conguagli. L'importo più basso fra i due è quello che viene indicato come proposta conguaglio.
* Residuo anticipi :  è dato dalla differenza totale anticipazioni e proposta conguaglio

## Funzioni Disponibili

* Premendo F06 si aprirà una schermata in cui verranno riportati tutte le proposte di conguaglio con la possibilità di poter modificare tali importi. Confermando verranno generate delle provvigioni di conguaglio. NOTA BENE :  è importante che venga attribuito un tipo provvigione pertinente, quindi con tipo imponibile anticipo ed il flag 08 di inversione valori. Tale tipo può essere fissato nella tabella V58, attraverso il campo "Tipo provvigione conguaglio anticipi".

