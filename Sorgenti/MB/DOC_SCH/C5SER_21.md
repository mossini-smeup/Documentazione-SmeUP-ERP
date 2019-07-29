## Obiettivo
Analizzare lo scadenzario aziendale attivo e/o passivo

![C5D010_064](http://localhost:3000/immagini/MBDOC_SCH-C5SER_21/C5D010_064.png)
## Parametri di lancio
 * Codice oggetto :  in funzione dell'oggetto scelto all'interno del surf in questo campo sarà necessario indicare il codice cliente, la lista clienti, il codice fornitore, ecc. da analizzare
 * Forma :  permette di visualizzare il dettaglio delle scadenze (campo blank) oppure di visualizzarne una sintesi (campo impostato a 1)
 * Tipo Sintesi :  nel caso in cui il campo precedente sia impostato con 1 permette di impostare la sintesi da visualizzare (per soggetto, per banca, per tipologia di pagamento, ecc.)
 * Scadenze :  permette di filtrare le scadenze visualizzate. Le opzioni disponibili sono : 
 ** Esposizione :  include sia le scadenze aperte che le scadenze in rischio
 ** SCA Aperte :  vengono incluse solo le scadenze aperte
 ** RIS Rischio :  vengono incluse solo le scadenze in rischio
 ** ASC A scadere :  vengono incluse solo le rate non ancora scadute
 ** SCD Scaduto :  vengono incluse solo le rate scadute
 ** NEG Negative :  vengono incluse solo le note credito e gli anticipi
 ** DPR Da presentare :  vengono incluse tutte le scadenze aperte che non sonno ancora incluse in una distinta di pagamento/incasso
 ** ESI Insoluti e Protesti :  vengono mostrate solo le scadenze che derivano da insoluti o protesti
 * Data Situazione :  permette di impostare la data di analisi dello scadenzario. Verranno quindi escluse tutte le registrazioni fatte successivamente e le analisi scaduto/a scadere/rischio verranno fatte alla data qui impostata. Se il campo viene lasciato vuoto viene assunta la data odierna
 * Data scaduto :  permette di impostare la data minima a cui considerare scadute le rate. Se il campo viene lasciato vuoto il sistema risale ai giorni per scaduto impostati nella tabella C51
 * Escludi Movimenti Simulati :  permette di escludere le registrazioni provvisorie
 * Data Documento inizio/fine :  permette di filtrare i documenti per data
 * Raggruppa/Includi Soggetti :  nel caso in cui un cliente sia anche fornitore attraverso questo parametro è possibile vederne la posizione netta e, quindi, includere sia le scadenze attive che quelle passive. In questo parametro sarà necessario indicare come effettuare il collegamento cliente/fornitore. Le scelte possibili sono : 
 ** Per codice fiscale / Partita IVA :  il sistema cerca di accoppiare i clienti/fornitori in funzione del codice fiscale/partita iva
 ** Per ente corripondente :  il sistema leggerà l'ente corrispondente impostato sull'anagrafica del cliente/fornitore
 ** Per Nominativo :  il sistema risalirà al nominativo comune tra cliente e fornitore
 ** Per ente di gruppo :  attraverso questo campo è possibile individuare dei gruppi aziendali. Il gruppo a cui appartiene un soggetto è impostabile tramite l'estensione anagrafica £53
 * DSO su Sintesi Soggetti :  permette di calcolare e mostrare l'indice DSO nel caso in cui si sia scelta come forma di analisi la Sintesi
 * Ageing :  questo parametro è utilizzato solo nel caso in cui si sia scelta la forma di Sintesi. Attraverso il parametro è possibile impostare le colonne nell'analisi dell'ageing. In particolare in questo campo è possibile inserire l'elemnto della tabella C6J da utilizzare. Per maggiori dettagli sull'impostazione delle colonne si rimanda alla documentazione della tabella stessa
 * Cumuli Effetti :  in caso di effetti cumulati permette i visualizzare una scadenza unica o il dettaglio delle scadenze
 * Netto Ritenute :  nal caso in cui siano presenti ritenute d'acconto permette di visualizzare gli importi al netto delle ritenute
 * Segno :  permette di visualizzare solo le scadenze positive o solo quelle negative
 * gg Ritardo :  permete di includere una colonna con il calcolo dei giorni di ritardo delle rate scadute
 * Forza Data Rischio :  se impostato tutte le rate in rischio con data scadenza inferiore a quella impostata usciranno dal rischio
 * Solo Valuta :  permette di visualizzare solo le scadenze con la valuta qui impostata
 * Movimenti Valuta :  permette di convertire le scadenze in una valuta diversa da quella contabile
 * Cambio :  permette di forzare il cambio da utilizzare per la conversione della valuta delle scadenze nella valuta impostata nel campo precedente
 * Schema :  permette di impostare uno schema sulle colonne visualizzate
  * Righe per pagina :  permette di aumentare il numero di righe mostrato al lancio della funzione (di default vengono presentate le prime 1000 righe).

## Dettaglio informazioni
Nel caso in cui si stia analizzando lo scadenzario in forma Dettaglio verranno esposte le scadenze che rispettano i parametri impostati.
Per le rate scadute la data scadenza è evidenziata in azzurro mentre per quelle in rischio è evidenziata in rosso : 
![C5D010_058](http://localhost:3000/immagini/MBDOC_SCH-C5SER_21/C5D010_058.png)
Nel caso in cui si stia analizzando lo scadenzario in forma di Sintesi verrà presentato l'ageing di ogni voce di sintesi (quindi potrei avere l'ageing dei clienti, delle banche, delle tipologie di pagamento, ecc.) : 
![C5D010_059](http://localhost:3000/immagini/MBDOC_SCH-C5SER_21/C5D010_059.png)Si ricorda che all'interno della sintesi cliccando con il tasto destro del mouse all'interno di ogni cella e scegliendo la voce _Dettaglio_ è possibile visualizzare il dettaglio delle scadenze che compongono il valore.
Si sottolinea, inoltre, che le scadenze in rischio compaiono sempre come 'A scadere' e non come 'Scadute' anche se la data scadenza è tra quelle scadute.

### Specificità per Account

Nel caso in cui vengano gestiti i nominativi, è possibile analizzare lo scadenzario a livello di account e di lista di account visualizzando, quindi, sia le scadenze attive che quelle passive aperte per il nominativo.
Nel caso in cui, inoltre, i nominativi siano gestiti a livello di gruppo aziendale, all'interno della matrice verranno esposti i record di tutte le aziende abilitate.
I record relativi alle aziende diverse da quella a cui l'utente è collegato compariranno in bianco e su questi non sarà possibile eseguire alcuna funzione.
Quindi se ad esempio siamo collegati all'interno dell'azienda 10 e il nominativo ha scadenze aperte anche per le aziende 02 e 15, queste scadenze verranno esposte ma non saranno manutenibili : 

![C5D010_063](http://localhost:3000/immagini/MBDOC_SCH-C5SER_21/C5D010_063.png)
Per disabilitare la visualizzazione delle scadenze di un'azienda sarà necessario definire l'autorizzazione AZ impostando nella classe il codice dell'azienda da nascondere e il valore dell'autorizzazione a NO.
