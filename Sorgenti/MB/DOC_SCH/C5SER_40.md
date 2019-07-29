### Obiettivo
Fornire un'analisi sintetizzata per soggetto o dettagliata per movimento dell'analisi degli incassi/pagamenti in un periodo.
L'analisi può essere effettuata secondo due criteri temporali : 
* Per data registrazione :  vengono analizzati tutti i movimenti registrati nel periodo considerando inoltre tutti le scadenze aperte o ancora da maturare prima dell'inizio del periodo (ho quindi una corrispondenza precisa con i movimenti del mastrino, apertura compresa.
* Per data documento :  vengono analizzati tutti i movimenti che fanno riferimenti ad una data documento compresa fra le date. Per tali movimenti vengono considerati gli incassi sino alla data indicata come data registrazione limite (assume data odierna). Questo criterio permette di controllare la situazione creditoria/debitoria dei documenti emessi in un certo periodo.

### Note aggiuntive sui calcoli
* Sono esclusi tutti i movimenti simulati
* Le colonne saldo iniziale/periodo/finale corrispondono a quelle degli allegati di bilancio (per dare/avere il discorso è diverso essendo che a parità di riga di registrazione si possono avere movimenti di natura differente).

Per una documentazione più tecnica/dettagliata si rimanda alla documentazione della /COPY £C6A.
 :  : DEC T(MB) P(QILEGEN) K(£C6A) L(1)

### Azioni disponibili sulla sintesi per soggetto
* **Dettaglio completo** :  cliccando sull'icona a sinistra sarà possibile aprire una finestra in cui verranno dettagliati tutti i movimenti del soggetto che sono stati elaborati
* **Tasto destro cella numerica** :  premendo tasto destro su un qualsiasi numero e selezionando la voce di popup, dettaglio, sarà possibile aprire una finestra con il dettaglio dei movimenti che hanno costruito quel numero.

### Azioni disponibili sul dettaglio
Premendo tasto destro sull'icona di sinistra sarà possibile aprire : 
* **la scheda di dettaglio della partita**
* **la modifica/visualizzazione della registrazione di dovuto**
* **la modifica/visualizzazione della registrazione di regolamento (qual'ora sia presente)**

### Significato dei setup del dettaglio
* **Analisi Movimenti** :  evidenzia, raggruppati per natura, gli importi che si sono movimentati nel periodo
* **Analisi Ritardo ed Esito** :  evidenzia, gli importi che sono stati oggetto di ritardo e/o gli effetti che sono stati oggetto di esito (insoluto/protesto/richiamo)
* **Controllo saldi** :  ha il solo scopo di poter verificare la quadratura rispetto ai totali degli allegati di bilancio e degli scadenzari. NOTA BENE :  il rischio viene sempre calcolato forzando come data rischio la data successiva alla data registrazione limite (in modo che tutto quello che scade nel periodo sia considerato maturato).
* **Completo** :  evidenzia il dettaglio di tutte le informazioni elaborate

### Significato Importi in Colonna
* **Importo Dovuto** :  importo corrispondente ai crediti/debiti maturati nel periodo in analisi e nel caso in cui l'elaborazione sia effettuata secondo il criterio della data registrazione, anche agli importi da saldare/maturare pre-esistenti all'inizio del periodo.
** **Dovuto da Documento** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo che sono stati originati dall'emissione di un documento
** **Dovuto da Esito** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo per effetto dell'esito di un effetto (Insoluto/Protesto/Richiamo)
** **Dovuto da Anticipo** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo per effetto di corrispettivi effettuati in anticipo
** **Dovuto da Altro** :  è un di cui dell'importo dovuto, vi rientrano tutti i crediti/debiti maturati che non rientrano nelle precedenti casistiche.
* **Importo da Saldare** :  evidenzia la quota parte dei dovuti maturati nel periodo in esame che non sono ancora stati saldati (nell'analisi per data registrazione, questo importo corrisponde al saldo finale dello scadenzario)
** **Importo Scaduto** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che sono scaduti
** **Importo a Scadere** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che sono ancora a scadere
** **Importo a Debito** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che rappresentano dei debiti (tali importi non vengono inclusi nei due precedenti numeri)
* **Importo Regolato** :  evidenzia la quota parte dei dovuti maturati nel periodo in esame che corrisponde agli incassi/pagamenti effettuati nel periodo
** **Importo Incassato** :  è un di cui dell'importo regolato, in cui vengono evidenziati gli incassi (entrata di denaro)
** **Importo Esitato** :  è un di cui dell'importo regolato, in cui vengono evidenziati gli importi che sono stati esitati (effetti insoluti/protestata/richiamati)
** **N° Contatore Esiti** :  è un contatore del n° di esiti maturati nel periodo
** **Importo Pagato** :  è un di cui dell'importo regolato, in cui vengono evidenziati i pagamenti (uscita di denaro)
* **Importo a Costo/Ricavo** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto in un costo/ricavo aggiuntivo (perdite, abbuoni, oscillazioni ecc.)
** **Abbuoni/Oscillazioni** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da abbuoni o oscillazioni cambio.
** **Sconti** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da sconti
** **Perdite** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da perdite
* **Importo a Pareggio** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto con un movimento di pareggio con un'altra posta di segno opposto.
* **Importo a Rischio** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto in un effetto la cui maturazione avverrà in un periodo successivo a quello in esame. NOTA BENE : 
** **Quadratura** :  ha il solo fine di evidenziare il fatto che l'operazione aritmetica Importo Dovuto - Importo da Saldare - Importo Regolato - Importo a Costo/Ricavo - Importo a Pareggio - Importo a Rischio è pari a Zero.
* **Regolato in Ritardo** :  è un di cui dell'importo Regolato in cui vengono evidenziati i regolamenti che sono avvenuti in ritardo, rispetto alla scadenza prevista
* **gg previsti** :  evidenzia il n° di giorni previsti dalla scadenza originale per l'effettuazione del regolamento. Nella sintesi è il risultato della media ponderata dei movimenti.
* **gg ritardo** :  evidenzia il n° di giorni di ritardo corrispondenti al numero di giorni compresi fra la data scadenza prevista e la data di regolamento consuntiva (se il regolamento è avvenuto) o fra la data scadenza prevista e la data registrazione finale (se il regolamento non è ancora avvenuto). Questo n° viene calcolato solo il numero di giorni è positivo. Nella sintesi è il risultato della media ponderata dei movimenti.
* **gg consuntivi** :  evidenzia il n° di giorni in cui i regolamenti sono stati effettivamente effettutati. Nella sintesi è il risultato della media ponderata dei movimenti.
* **Costo di incasso previsto** :  è il costo di incasso calcolato rispetto al n° di gg previsti
* **Costo del ritardo** :  è il costo di incasso calcolato rispetto al n° di gg di ritardo
* **Costo di incasso effettivo** :  è il costo di incasso calcolato rispetto al n° di gg di incasso effettivo, quando questo è avvenuto, mentre quando non lo è viene  calcolato rispetto ai giorni che intercorrono fino alla data registrazione finale.
* **Rischio iniziale** :  evidenzia gli importi degli effetti che erano in attesa di maturare all'inizio del periodo
* **Saldo iniziale** :  evidenzia gli importi che costituivano gli importi ancora da saldare pre-esistenti all'inizio del periodo.
* **Dare** :  evidenzia i movimenti avvenuti in Dare
* **Avere** :  evidenzia i movimenti avvenuti in Avere
* **Saldo periodo** :  differenza fra le due precedenti colonne
* **Saldo finale** :  evidenzia gli importi che costituivano gli importi ancora da saldare a fine periodo
* **Quadratura Saldi** :  ha il solo fine di evidenziare il fatto che l'operazione aritmetica di Saldo Iniziale + Saldo Periodo - Saldo Finale è pari a Zero.
* **Rischio finale** :  evidenzia gli importi degli effetti che sono in attesa di maturare alla fine del periodo
* **Esposizione finale** :  si vede se si analizza la sintesi, evidenzia il totale in esposizione alla fine del periodo
* **DSO** :  si vede solo se si analizza la sintesi. La sigla sta per Days Sales Outstanding. E' un indice che misura i crediti in vendite ancora da incassare. Esistono alcuni metodi alternativi per determinarlo. In questo caso è stato utilizzando il metodo "a gambero" o "count-back" con anno commerciale. Attraverso esso il numero dei gg viene determinato sottraendo a ritroso, il fatturato dall'esposizione. Per l'ultimo mese determinato (salvo vi sia corrispodenza perfetta) il numero dei gg viene calcolato in questo modo :  30/fatturato del mese*importo scalato dall'esposizione.

### Colonna Segnalazioni su Dettaglio
In questa colonna vengono segnalate eventuali anomalie riscontrate nell'effettuazione dell'elaborazione (es. se vengono trovati movimenti di insoluto su cui è assente il collegamento con una riba tale situazione viene evidenziata come anomala, in quanto non è possibile determinare i giorni di ritardo compresi fra la data scadenza originale della riba ed la data registrazione dell'insoluto. Si ricorda che tale situazione può essere corretta tramite l'utilizzo del pgm C5UT53A).
