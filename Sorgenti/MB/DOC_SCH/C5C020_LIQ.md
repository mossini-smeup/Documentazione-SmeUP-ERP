## Obiettivo
Obiettivo di questa scheda è analizzare la liquidazione IVA relativa ad un periodo oppure ad un esercizio

![C5C020_028](http://localhost:3000/immagini/MBDOC_SCH-C5C020_LIQ/C5C020_028.png)## Parametri di lancio

 * Anno :  indicare l'anno per il quale si voglia analizzare la liquidazione
 * Mese :  nel caso in cui si stia analizzando la liquidazione mensile, indicare il mese da analizzare
 * Settore Attività :  nel caso in cui si gestisca il settore di attivtà all'interno dei registri IVA indicare per quale settore analizzare i dati

## Dettaglio informazioni

All'interno dell'analisi mensile vengono riportate le stesse voci previste nella stampa della liquidazione mensile.
Saranno esposti quindi : 

- IVA acquisti. E' l'ammontare dell'IVA derivante da tutti i registri di tipo acquisto, fatta eccezione per quelli relativi agli acquisti Intracee e agli acquisti reverse charge.
- IVA acquisti CEE. E' l'ammontare dell'IVA derivante da tutti i registri di tipo acquisto IntraCee.
- IVA acquisti reverse. E' l'ammontare dell'IVA derivante da tutti i registri di tipo reverse charge.
- % Pro-rata. Viene reperita dai dati aggiuntivi Azienda.
- IVA detratta per il periodo. E' l'ammontare totale dell'IVA da detrarre per il periodo considerando la percentuale prorata impostata.
- IVA non detraibile. E' l'ammontare dell'IVA acquisti indetraibile presente su tutti i registri.
- IVA acquisti per cassa da liquidare. E' l'ammontare dell'IVA per cassa da liquidare nel periodo.
- Totale IVA acquisti. E' l'ammontare totale dell'IVA derivante da acquisti del periodo in liquidazione.

- IVA vendite. E' l'ammontare dell'IVA derivante da tutti i registri di tipo vendita, fatta eccezione per quelli derivati dai registri di acquisto Intracee o reverse charge.
- IVA debito su acquisti Cee. E' l'ammontare dell'IVA derivante da tutti i registri di debito ottenuti in copia da quelli di acquisto Intracee.
- IVA debito su acquisti reverse. E' l'ammontare dell'IVA derivante da tutti i registri di debito ottenuti in copia da quelli di acquisto reverse charge.
- IVA vendite per cassa da liquidare. E' l'ammontare dell'IVA relativa a fatture incassate nel periodo e quindi con IVA da liquidare.
- Totale IVA vendite. E' l'ammontare totale dell'IVA derivante da vendite del periodo in liquidazione.

- IVA corrispettivi. E' l'ammontare dell'IVA derivante da tutti i registri di corrispettivi (IVA a debito).
- IVA esigibile del periodo. E' il totale dell'IVA a debito, ovvero la somma di IVA vendite e IVA corrispettivi.

- IVA a debito o credito del periodo. E' il saldo IVA del periodo in liquidazione, differenza tra IVA detratta e IVA esigibile.

- Variazioni di imposta Debiti/Crediti. Riportano quanto immesso nei parametri di lancio della liquidazione, andando ad incrementare/decrementare l'importo da versare o da riportare a credito del periodo.
- IVA non versata. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a incrementare/decrementare l'importo da versare o da riportare a credito del periodo.
- Credito riportato da periodo precedente. Viene riportato l'eventuale credito scaturito dalla precedente liquidazione. Si sottolinea che in questo campo viene riportato solo il credito maturato nell'anno in corso.
- Acconto IVA. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a decrementare l'importo da versare o da riportare a credito del periodo.
- IVA a credito per il periodo. Viene riportato, se si verifica la condizione, l'importo del credito del periodo.
- Importo da versare per il periodo. Viene riportato, se si verifica la condizione, l'importo a debito del periodo.

- Interessi liquidazione. E' l'importo degli interessi da corrispondere in funzione di una liquidazione trimestrale/annuale.
- Totale con interessi. E' la somma dei due valori precedenti, nel caso di debito per il periodo.

- Credito anno precedente portato in detrazione. Riporta quanto immesso nei parametri di lancio della liquidazione, andando a decrementare l'importo da versare o da riportare a credito del periodo.

- Importo da versare/a credito. E' il risultato finale della liquidazione.

- Estremi del versamento. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso si debba effettuare un versamento dovuto per debito IVA tramite banca.
- Credito anno corrente chiesto a rimborso. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato richiesto un rimborso (che verrà riportato come credito nel periodo successivo).
- Compensazione esterna (F24) su credito anno corrente. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato utilizzato il credito IVA dell'anno corrente per compensare altri crediti (l'importo diminuirà il credito nel periodo successivo).
- Compensazione esterna (F24) su credito anno precedente. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato utilizzato il credito IVA dell'anno precedente per compensare altri crediti (l'importo diminuirà il credito nel periodo successivo).
- Credito anno precedente chiesto a rimborso. Riporta quanto immesso nei parametri di lancio della liquidazione, nel caso sia stato richiesto un rimborso sul credito IVA maturato nell'anno precedente (che verrà riportato come credito nel periodo successivo).


All'interno dell'analisi annuale vengono riportate le stesse voci previste nell'analisi mensile ma suddivise per mese : 

![C5C020_029](http://localhost:3000/immagini/MBDOC_SCH-C5C020_LIQ/C5C020_029.png)