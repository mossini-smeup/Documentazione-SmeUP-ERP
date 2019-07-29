# S5B - Scenari schedulazione avanzata
 :  : DEC T(ST) K(S5B)
## OBIETTIVO
Definisce i parametri che guidano l'esecuzione della schedulazione in questo scenario
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM
Indica il codice dello scenario
 :  : FLD T$DESC
Indica la descrizione dello scenario
 :  : FLD T$S5BA __Tipo risorsa principale__
Definisce il tipo risorsa che caratterizza la risorsa principale.
 :  : FLD T$S5BB __Tipo risorsa specifica__
Definisce il tipo risorsa che caratterizza la risorsa specifica. Nella creazione degli impegni risorse nella risorsa specifica (tipo e codice), vengono riportati i valori della risorsa principale.
Quando si esegue la schedulazione fine con scelta della risorsa specifica (ad esempio, la macchina di un centro di lavoro), vengono modificati i valori della risorsa specifica (tipo e codice).
Quindi in questo campo, se non si esegue la schedulazione fine, o la si esegue senza scelta della risorsa specifica, va riportato il tipo risorsa principale.
 :  : FLD T$S5BC __Oggetto Priorità__
Definisce l'oggetto che viene inserito nel campo criterio di ordinamento
Riferirsi all'aiuto specifico dell'oggetto V2_CRORD per l'esposizione dei valori implementati.
 :  : FLD T$S5BD __Parametro Priorità__
Quando il criterio di ordinamento è 'O', in questo campo si inserisce l'OAV specifico.
Quando il criterio di ordinamento è 'P' o 'Q' in questo campo si inserisce il programma che viene eseguito per calcolare il criterio di ordinamento
 :  : FLD T$S5BE __Modo suddivisione operazione__
Definisce il livello di dettaglio con cui vengono suddivisi gli impegni risorse : 
Un'operazione  può essere : 
- I - Iniziata
- P - Pronta (se è la prima o se la precedente è terminata)
- S - Iniziata la precedente   (*)
- U - Pronta la precedente     (*)
- Z - Non disponibile
Se questo campo è impostato, vengono determinati anche gli stati (*), se invece è lasciato in bianco vengono determinati solo i rimanenti stati.
Questa suddivisione è utilizzata nella rappresentazione degli impegni di risorse in modalità work list.
 :  : FLD T$S5BF __Tipo schedulazione capacità inf. ril.__
_7_Schedulazione a capacità infinita
Valido sugli ordini rilasciati.
Nella creazione degli impegni risorse, se questo campo viene impostato, essi vengono datati, in base a quanto impostato in questo campo : 
' ' - Nessuna schedulazione
'A' - Schedulazione in avanti a partire dalla data inizio richiesta dell'ordine
'I' - Schedulazione all'indietro a partire dalla data fine richiesta dell'ordine
'E' - Entrambe le schedulazioni (in avanti e all'indietro)
 :  : FLD T$S5BG __Efficienza operaz.__
_7_Schedulazione a capacità finita ed infinita
Se impostato, le ore totali di carico verranno aumentate dell'efficienza (della risorsa principale)
 :  : FLD T$S5BH __Trattamento Attrezzaggio__
_7_Schedulazione a capacità finita ed infinita
Definisce il modo in cui verranno riportate le ore di attrezzaggio nel campo specifico dell'impegno risorse.
Innanzitutto, va ricordato che il componente di carico 2 contiene le ore di attrezzaggio, se è previsto nel codice di carico della risorsa principale di considerare l'attrezzaggio.
Questo campo puà assumere i seguenti valori : 
' ' - Le ore di attrezzaggio verranno forzate a 0
'1' - Il componente di carico 2 verrà copiato nelle ore di attrezzaggio
'2' - Il componente di carico 2 verrà copiato nelle ore di attrezzaggio aumentato dell'efficienza della risorsa principale
 :  : FLD T$S5BI __Considera sovrapposizione__
_7_Schedulazione a capacità finita
Se impostato, verranno considerati i valori di sovrapposizione impostati, sia a livello di singola fase di ciclo, sia a livello del gruppo risorsa a cui appartiene la risorsa generale.
 :  : FLD T$S5BJ __Considera code__
_7_Schedulazione a capacità infinita
Se impostato questo campo, verranno considerate le code.
Normalmente le code vanno considerate in una schedulazione che vuol dare una datazione di massima degli impegni risorse.
Quando invece la schedulazione ha lo scopo di determinare il carico effettivo dei centri per rispettare le date di consegna, le code non vanno considerate. questo in quanto introdurrebbero un effetto perturbativo di slittamento dannoso se, ad esempio, alla schedulazione a capacità infinita si facesse seguire un livellamento per eliminare i picchi di sovracapacità.
_7_Schedulazione a capacità finita
Se impostato questo campo, verranno considerate le code per le risorse definite a capacità infinita.
 :  : FLD T$S5BK __Alternative di ciclo__
_7_Schedulazione a capacità finita
Se impostato questo campo, verranno esaminate le alternative di ciclo.
In questo caso deve essere attiva (in tabella BR1) la gestione multipla delle alternative di cicli.
Implemento in sviluppo :  lasciare in bianco questo campo
 :  : FLD T$S5BL __Accostamento fasi__
_7_Schedulazione a capacità finita
Definisce la modalità di accostamento della fase schedulata con la successiva.
È significativa in presenza di alternativa di ciclo e/o di risorsa specifica
Se impostato il valore '1' e la fase successiva può essere eseguita sulla stessa risorsa (principale e specifica) della fase precedente, essa verrà eseguita in questa risorsa.
Se impostato un altro valore 'x' verrà eseguito il programma di aggiustamento S5SMES_UTx, che permette una gestione specifica dell'accostamento.
!!!! ATTENZIONE !!!!
Questa impostazione NON è compatibile con la funzione di tiro, in quanto all'interno di quest'ultima è possible realizzare anche l'accostamento.
Se si attivano entrambe, l'accostamento viene trascurato e viene data segnalazione, nella schedulazione, come errore non bloccante.
 :  : FLD T$S5BM __Rett.part.su rilasc.__
_7_Schedulazione a capacità infinita
_Se impostato, nella schedulazione a capacità infinita in avanti degli ordini rilasciati, la data di inizio schedulazione (data inizio richiesta) viene portata ad oggi se inferiore.?????
 :  : FLD T$S5BN __Rett.part.su pianif.__
_7_Schedulazione a capacità infinita
_Se impostato, nella schedulazione a capacità infinita in avanti degli ordini pianificati, la data di inizio schedulazione (data suggerimento) viene portata ad oggi se inferiore.?????
 :  : FLD T$S5BO __Tipo sch.cap.inf.pia__
_7_Schedulazione a capacità infinita
Valido sugli ordini pianificati.
Nella creazione degli impegni risorse, se questo campo viene impostato, essi vengono datati, in base a quanto impostato in questo campo : 
' ' - Nessuna schedulazione
'A' - Schedulazione in avanti a partire dalla data inizio richiesta dell'ordine
'I' - Schedulazione all'indietro a partire dalla data fine richiesta dell'ordine
'E' - Entrambe le schedulazioni (in avanti e all'indietro)
 :  : FLD T$S5BP __Scenario dipendente__
Se impostato il valore '1', gli impegni risorse su questo scenario verranno rigenerati contestualmente alla rifasatura dello scenario di produzione '**'.
Se impostato il valore '2', oltre al comportamento precedente, quando vengono memorizzati l'inizio e la fine della schedulazione fine su questo scenario, essi vengono riportati anche sullo scenario '**'. Quando gli impegni su questo scenario sono effetto di uno split a partire da quello dello scenario **, verranno riportati su quest'ultimo i valori iniziali e finali rispettivamente più basso e più alto.
Naturalmente questo flag non è significativo sullo scenario **.
 :  : FLD T$S5BQ __Numeri avanzamento__
Se impostato, vengono calcolati i numeri che caratterizzano la situazione di avanzamento dell'oggetto intestatario, quali le ore rimanenti, lo slack time, la critical ratio, ecc...
Può assumere i seguenti valori : 
1 - Calcolati sugli impegni rilasciati
2 - Calcolati sugli impegni pianificati
3 - Calcolati su tutti gli impegni
Essi sono memorizzati in un elemento di D5COSO, con le seguenti impostazioni : 
- contesti 'OR' / 'DR' / 'M5'
- temi     '£I1' del sottosettore OR / DR / M5
È significativo solo per lo scenario '**'.
 :  : FLD T$S5BR __Memorizzazione ind.__
Se impostato, gli indici della schedulazione vengono memorizzati nell'archivio indici (D5COSO).
Viene memorizzato un elemento per scenario / origine / ambito / data.
Come prerequisiti vanno inseriti i seguenti oggetti : 
- sottostettore dei temi (tabella D5O) 'S5'
- contesto (Settore D5S, Elemento TAS5B).
- tema     (Settore D5O, Sottosettore S5, Elemento £I1).
Utilizzare la funzione di creazione automatica di substettori ed elementi D5FS01A
 :  : FLD T$S5BS __Esclude liv.0__
Se impostato, per gli ordini / righe documenti a livello '0', in questo scenario non verranno creati gli impegni risorse
 :  : FLD T$S5BT __Attributo Ambito__
Se impostato, l'ambito di schedulazione viene memorizzato leggendolo da un OAV dell'oggetto schedulato.
L'oggetto da cui viene derivato l'OAV, a seconda del Tipo impegno Risorse, può essere : 
-l'oggetto Ordine Produzione per tipo impegno "VP"
-l'oggetto Documento Riga per tipo impegno "DR"
-l'oggetto Consiglio Pianificazione per tipo impegno "M5"
Si noti che questa impostazione sovrascrive quanto impostato nella tabella BRM.
Se nello stesso scanario sono presenti oggetti diversi, l'OAV deve essere comunque lo stesso.
 :  : FLD T$S5BU __Priorità in ordinamento__
Se si imposta questo campo, la priorità, inserita nella testata dell'ordine di produzione, viene posto all'inizio
del criterio d'ordinamento, in modo da costituirne la parte più importante.
Se, invece, si lascia vuoto questo campo, la priorità rimane un campo descrittivo.
 :  : FLD T$S5BV __Priorità standard__
Se la priorità costituisce l'inizio del criterio di ordinamento, in questo campo si imposta il valore che essa assume se
è stata lasciata in bianco.
Va ricordato che la priorità 'bianca' è la più alta, e quindi, se questo campo non è compilato, i valori inseriti
nell'ordine di produzione agiscono in modo 'peggiorativo', vale a dire questi ordini sono considerati memo prioritari
rispetto a quelli in cui la priorità non è stata compilata.
Si consiglia quindi di inserire in questo campo il valore di prorità 'normale', in modo da poter inserire nell'ordine di
produzione sia valori più alti sia più bassi.
