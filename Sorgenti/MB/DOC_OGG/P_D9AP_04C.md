# D9AP_04C - Estrazione da MRP
Estrae dall'archivio M5CONS0F, relativo alla pianificazione MRP


_2_Parametri origine

- Valorizzo? :  se compilato valorizzerà i materiali pianificati
- Tipo costo :  da tabella TCO determina quale costo considerare
- Livello costo :  da tabella CSDLC determina il livello del costo da utilizzare
- Scenario (' ' Tutti) se rilascio 4 permette di selezionare lo scenario MRP
- Sugger. su esistente si/no se si vogliono vedere i suggerimenti sull'esistente
- Sugger. pianificati si/no se si vogliono vedere i suggerimenti sul pianificato
- Data fine orizzonte :  fino a che data selezionare i suggerimenti
- Eccedenze? selezionare la modalità di estrazione delle eccedenze di fonte

_2_Oggetti origine

- Articolo
- Suggerimento (oggetto V2 M5SUG) dell' MRP
- Commessa
- Data fonte
- Data suggerimento
- Cliente
- Fornitore
- Oggetto 8 determinato dal contenuto della tabella M51 oggetto di rottura
- Oggetto 9 determinato dal contenuto della tabella M5B elemento '**' oggetto di riferimento

_2_Oggetti aggiuntivi piatti

- Tipo Suggerimento (oggetto V2 M5TSG) dell' MRP
- Livello (tabella B£W00)
- Fonte (generico)
- Esponente modifica (generico)

_2_Valori origine
Sono fissi : 

- Qta suggerimento; Qta fonte; Num. suggerimenti; Ìmporto sugg. Klire; Ìmporto fonte Klire; Num. suggerimenti

