# M5A - Politica di riordino
## OBIETTIVO
Definisce i parametri che guidano la pianificazione di ogni articolo.
Per ogni articolo, a livello di dettaglio, di famiglia o generale, si possono definire fino a tre politiche di riordino, che guidano la pianificazione di ordini di produzione, di acquisto e di lavorazione.
I parametri che guidano l'emissione di ordini pianificati sono assunti da queste politiche.
Altri parametri che guidano la pianificazione generale dell'articolo sono assunti dalla poltica 'master', che è la prima presente tra quelle di produzione, acquisto e lavorazione.
Di seguito, per ogni parametro, verrà segnalato se è assunto dalla politica master o dalla politica specifica.
Inoltre, se è stato impostato in tabella M51 il tipo oggetto di riferimento a cui possono essere intestati i parametri di pianificazione, e la politica è definita di pianificazione per riferimento, alcuni campi della politica specifica sono sovrapposti  da quelli della politica dell'oggetto di riferimento.
Di seguito, questi campi saranno individuati come campi sovrapponibili dal riferimento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice della politica.
 :  : FLD T$DESC Descrizione
 :  : FLD T$M5AA __Tipo raggruppamento__
Assunto dalla politica master.
È un elemento V2-M5TRA :  definisce, insieme con il periodo di raggruppamento, il modo di determinare la data massima che verrà considerata all'atto della pianificazione di un ordine, per raggruppare i fabbisogni.
 :  : FLD T$M5AB __Modo di pianificazione__
Assunto dalla politica master.
È un elemento V2-M5MPN :  definisce la modalità di pianificazione degli articoli appartenenti a questa politica  (fabbisogno, punto di riordino, ecc..), oppure se sono esclusi dalla pianificazione.
Per la congruenza di questo campo con il campo "Pianificazione per codice di rottura", di questa tabella, nel caso di punto di riordino, riferirsi all'aiuto di quest'ultimo campo.
 :  : FLD T$M5AC __Fonte di pianificazione__
Assunto dalla politica specifica. Campo sovrapponibile dal riferimento.
È un elemento della tabella M5F :  definisce la fonte che verrà assegnata in fase di completamento del suggerimento.
L'origine fonte dovrà essere 'PN'; il suggerimento sarà PR/AQ/LV a seconda che questa politica, nei parametri di pianificazione, sia nella casella della politica di produzione, acquisto o lavorazione.
La fonte ha, tra i suoi campi, il parametro di suggerimento (campo che verrà ugualmente riportato nei consigli, in fase di completamento), che contiene il programma di rilascio del consiglio stesso. Quindi, se, ad esempio, si vorrà distinguere, all'interno degli acquisti, tra articoli da passare a richieste e a ordini a programma, si definiranno due politiche che punteranno a due fonti diverse.
Può verificarsi anche il caso di politiche diverse che puntano alla stessa fonte :  ad esempio codici a punto diriordino e codici a fabbisogno, che danno luogo a richieste d'acquisto dello stesso tipo.
 :  : FLD T$M5AD __N.Periodi di raggruppamento__
Assunto dalla politica master.
È un parametro numerico che definisce il numero di giorni, settimane, mesi o periodi, che verranno raggruppati, in base al tipo di raggruppamento selezionato. Se non impostato si assume 1.
 :  : FLD T$M5AX __Periodo di massimo anticipo__
Assunto dalla politica master.
È un parametro numerico che definisce il numero di giorni, settimane, mesi o periodi, che verranno considerati come massimo anticipo. È significativo se è stato selezionato il criterio '1' come criterio moc (make or change). È dello stesso tipo del periodo di raggruppamento (giorni, settimane, mesi, ecc) ed è sottoposto allo stesso arrotondamento.
 :  : FLD T$M5AO __Tipo arrotondamento periodo__
Assunto dalla politica master.
Può assumere i valori ' ', '+', '-'. Nel caso di tipo raggruppamento per settimane o per mesi, definisce se arrotondare il periodo : 
- alla fine della settimana o mese attuale (+);
- alla fine della settimana o mese precedente (-);
- non eseguire nessun arrotondamento (se lasciato in bianco).

_9_Esempio 1
--> Tipo raggruppamento '3' (settimanale)
--> Periodi di raggruppamento :  2
--> Data partenza 02/09/1998 (mercoledì)

Tipo arrotondamento  |  Data arrivo  | Giorno arrivo
       ' '           |  15/09/1998   | Martedì
       '+'           |  20/09/1998   | Domenica
       '-'           |  13/09/1998   | Domenica

_9_Esempio 2
--> Tipo raggruppamento '4' (mensile)
--> Periodi di raggruppamento :  2
--> Data partenza 03/04/1998


Tipo arrotondamento  |  Data arrivo
      ' '            |  02/06/1998
      '+'            |  30/06/1998
      '-'            |  31/05/1998

 :  : FLD T$M5AE __Fonte di impegno__
Assunto dalla politica specifica. Campo sovrapponibile dal riferimento.
È un elemento della tabella M5F :  se impostata, definisce la fonte degli impegni che verranno generati a fronte di un ordine pianificato da questa politica. Se non impostato, l'ordine pianificato non genererà nessun impegno.
L'origine fonte dovrà essere 'IP'; il suggerimento verrà ereditato da quello dell'ordine di origine (PR/LV).
 :  : FLD T$M5AF __Tipo distinta__
Assunto dalla politica specifica. Campo sovrapponibile dal riferimento.
È un elemento della tabella BRL. Va impostato se è stata specificata una fonte di impegno :  è il tipo distinta usato nella costruzione degli impegni. Se assente, viene assunto 'ART'.
 :  : FLD T$M5AG __Tipo esplosione distinta__
Assunto dalla politica specifica. Campo sovrapponibile dal riferimento.
Va impostato se è stata specificata una fonte di impegno :  definisce il tipo di esplosione della distinta. Se assente, viene assunto '3' (esplosione di produzione).
 :  : FLD T$M5AH __Periodicità__
Assunto dalla politica master.
È un elemento della tabella A£Q :  va impostato se il tipo raggruppamento è per periodicità. Se non impostato, per i raggruppamenti di questo tipo verrà assunta la periodicità definita a livello di tabella generale M51.
 :  : FLD T$M5AI __Gruppo fonti__
Assunto dalla politica master.
Se impostato, per gli articoli di questa politica verrà usato in pianificazione questo gruppo fonti, in luogo di quanto impostato all'atto del lancio.
In questo modo si può suddividere in modo flessibile l'ambito della pianificazione :  ad esempio si può considerare la giacenza di un'area solo per alcuni codici, oppure trattare selettivamente gli impegni di produzione.
 :  : FLD T$M5AL __Trattamento lotto massimo__
Assunto dalla politica specifica. Campo sovrapponibile dal riferimento.
È un elemento V2-M5LMX. Definisce la modalità di trattamento del lotto massimo :  se esso è puramente indicativo, oppure se si dovrà tenerne conto per suddividere gli ordini pianificati in serie o in parallelo. Fare riferimento all'aiuto specifico per maggiori dettagli.
 :  : FLD T$M5AM __Modo assegnazione ente__
Assunto dalla politica specifica. Campo non sovrapponibile dal riferimento.
Se impostato, è un metodo della funzione 'ASS' della routine di assegnazione £V5U.
Se questo campo è stato impostato, all'atto della scrittura del suggerimento di pianificazione, esso verrà completato (o eventualmente duplicato, in caso di assegnazione mista su più enti) con i valori (ente ed eventualmente quantità) ritornati da questa routine.
 :  : FLD T$M5AN __Parametro assegnazione ente__
Assunto dalla politica specifica. Campo non sovrapponibile dal riferimento.
Va impostato se è stato impostato il modo di assegnazione ente e ha la funzione di specificarlo.
Le posizioni da 1 a 3 hanno il seguente significato : 
-- se è un'assegnazione per contratto, è il tipo documento di contratto;
-- se è un'assegnazione per ente preferenziale, è il tipo ente.
La posizione 4 identifica un programma specifico di assegnazione enti che si deve chiamare V5V5U0_x, dove x è il carattere qui impostato.
Si deve tener presente che il programma di assegnazione specifico, in funzione del modo di assegnazione ente, potrà appartenere alla famiglia degli enti preferenzali (per i quali si imposterà il tipo ente) o a quella dei contratti (per i quali si imposterà il tipo documento).
Le posizioni da 5 a 10 contengono delle informazioni libere passate al programma di assegnazione specifico, per caratterizzarne il comportamento.
 :  : FLD T$M5AP __Pianificazione a codice di rottura__
Assunto dalla politica master.
Se impostato, gli articoli di questa politica saranno pianificati separatamente, per il codice di rottura definito nella tabella di impostazioni generali M51.
La pianificazione a punto di riordino è incompatibile con quella a codice di rottura.
Quindi, se è stato impostato il tipo pianificazione a punto di riordino, questo campo deve essere obbligatoriamente vuoto.
Se, sempre in caso di pianificazione a punto di riordino, questo campo è vuoto, ma è valorizzato l'omonimo campo di tabella M51, si assume "implicitamente" che per questa politica esso sia vuoto.
La pianificazione a punto di riordino "vince" su quella a codice di rottura.
Si può quindi evitare di valorizzare questo campo su tutte le politiche ad eccezione di quelle a punto di riordino.
 :  : FLD T$M5AQ __Fonte per eccedenza presente__
Assunto dalla politica master.
È un elemento della tabella M5E :  se impostato, e se l'articolo ha una giacenza eccedente, verrà generato un suggerimento di quantità eccedente, in data zero.
L'origine della fonte dovrà essere 'QE', il tipo suggerimento sarà 'PN' ed il codice suggerimento sarà 'EL'.
 :  : FLD T$M5AR __Fonte per eccedenza futura__
Assunto dalla politica master.
È un elemento della tabella M5F :  se impostato, viene considerato nei seguenti casi : 
-- se l'ultima copertura (ordine di produzione, acquisto, lavorazione) è necessaria solo parzialmente, e quindi viene suggerito di ridurla. Tuttavia tale riduzione non può essere eseguita integralmente, per la presenza di lotto minimo e multiplo; verrà allora generato un suggerimento di riduzione quantità per la differenza tra la riduzione teorica e quella effettiva, posto allla data di fine dell'ordine da ridurre.
-- se l'ultimo ordine pianificato viene proposto per una quantità superiore a quella necessaria, sempre per la presenza di lotto minimo e multiplo, verrà generato un suggerimento di riduzione quantità, per la differenza tra la quantità pianificata e la quantità necessaria, posto alla data di fine dell'ordine da generare.
L'origine della fonte dovrà essere 'QE', il tipo suggerimento sarà 'PN' ed il codice suggerimento sarà 'EL'.
 :  : FLD T$M5AS __Produzione a disponibilità chiamata__
Assunto dalla politica master.
Se impostato, gli articoli di questa politica saranno trattati nell'elaborazione dei risultati della pianificazione, che produrrà gli impegni di risorse nella modalità di produzione a disponibilità chiamata.
 :  : FLD T$M5AT __Spostamento extraperiodo__
Assunto dalla politica master.
Se impostato, verranno emessi suggerimenti di spostamento date, soltanto se andranno all'esterno del periodo di raggruppamento fabbisogni.
Questa impostazione vale soltanto per i periodi a raggruppamento 'fisso', ovvero i raggruppamenti con periodicità e quelli a settimane o mesi, per i quali il periodo risulta di una sola settimana o mese di calendario (solo in questo modo si riesce a definire univocamente il periodo).
FONDAMENTALE :  impostare tipo arrotondamento = '-' se si vuole che funzioni
Questi ultimi periodi vanno impostati nel seguente modo : 
-- Periodo di una settimana :  Tipo raggruppamento='2'
-- Periodo di un mese :   Tipo raggruppamento='4'
In entrambi i casi :   N.ro Periodi di raggrruppamento= 0 oppure 1 / Tipo arrotondamento periodo='-'
 :  : FLD T$M5AU __Parametri di pianificazione per riferimento__
Assunto dalla politica specifica. Campo non sovrapponibile dal riferimento.
Se impostato, e nella tabella generale M51 è stato definito il tipo oggetto intestatario dei parametri, verranno usati, se presenti, i tempi di approvvigionamento, le politiche e i lotti (quantità minima, multipla, massima), definiti per i singoli oggetti.
 :  : FLD T$M5AV __Suffisso pgm. di aggiustamento__
Assunto dalla politica master.
Se impostato, è il suffisso x del programma 'M5M5R0_x', che viene lanciato durante il calcolo della pianificazione, per indurre comportamenti specifici.
 :  : FLD T$M5AZ __Elimina impegni pianificati__
Assunto dalla politica master.
Se impostato, gli impegni pianificati verranno portati a livello '8', in modo da non essere visualizzati normalmente, nelle analisi e stampe della pianificazione.
Per questa politica, questo campo va impostato in presenza di un gruppo fonti che contiene una fonte a bilanciamento. Questa, a sua volta, nel suo gruppo fonti, contiene gli impegni pianificati.
Tale impostazione non ha effetto sulla pianificazione, che si comporta comunque correttamente.
 :  : FLD T$M5AJ __Validità politica__
Consente di definire se la politica è applicabile solo alla produzione, solo agli acquisti o solo alle lavorazioni esterne. Il controllo viene effettuato in fase di manutenzione dei dati di pianificazione.
Dato che questo campo non è trattato nel processo di pianificazione, l'informazione 'assunto da politica master o specifica', non ha significato.
 :  : FLD T$M5AW __Criterio make or change__
Assunto dalla politica master.
È un elemento V2-M5MOC :  se impostato, definisce il modo in cui si imposta se pianificare nuovi ordini oppure anticipare gli esistenti.
 :  : FLD T$M5AY __Fonte trascurata__
Assunto dalla politica master.
Se impostato, il suggerimento di pianificare un nuovo ordine verrà emesso con questa fonte, se per una quantità minore o uguale al limite definito nei campi successivi
 :  : FLD T$M5A1 __Modo trasc.__
Assunto dalla politica master.
Definisce la soglia di quantità per la quale viene emesso un suggerimento di fonte trascurata.
Va impostato insieme alla fonte trascurata.
Se vale %, il campo successivo è una percentuale del lotto minimo.
Se vale Q, il campo successivo è una quantità fissa.
 :  : FLD T$M5A2 __Quantità trascurata__
Assunto dalla politica master.
Definisce la soglia di quantità per la quale viene emesso un suggerimento di fonte trascurata
Va impostato insieme al modo trasc.
E' una quantità oppure una percentuale in base a quanto inserito nel modo trasc.
NB :  per il 20% del lotto minimo si deve inserire 20
 :  : FLD T$M5A3 __Scorta tarscurata__
Assunto dalla politica master.
Se impostato, e se l'ordine da pianificare copre la scorta per una percentuale non superiore al valore impostato nel campo successivo, il suggerimento verrà emesso con questa fonte.
 :  : FLD T$M5A4 __%__
Assunto dalla politica master.
Definisce la soglia di quantità per la quale viene emesso un suggerimento di scorta trascurata.
Va impostato insieme alla scorta trascurata.
**NB** :  per il 20% della scorta si deve inserire 20
 :  : FLD T$M5A5 __Suff.__
Assunto dalla politica master.
Se presente, è il suffisso x del programma di aggiustamento M5AGP01_x. Questo permette di modificare, a livello di
scenario / plant / articolo / oggetto di rottura, i seguenti campi della politica : 
- n° periodi di raggruppamento     (campo T$M5AD);
- tipo arrotondamento             (campo T$M5AO);
- massimo anticipo                (campo T$M5AX);
 :  : FLD T$M5A6 __Estensione parametri £V5U assegnazione ente__
E' una elemento della tabella M5U. Contiente l'estensione dei parameti usati dalla copy £V5U per l'ssegnazione dell'ente.
 :  : FLD T$M5A7 __Calcolo EM__
Assunto dalla politica master.
Se impostato, in un MRP a rottura di EM, in caso di articolo non gestito a rottura, viene calcolato l'EM valido ad una delle seguenti date : 
'1' - data fonte
'2' - data suggerimento
'3' - data fine pianificata
