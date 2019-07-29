# Introduzione
La scelta del dettaglio da schedulare è il fulcro della schedulazione :  infatti definisce in quale ordine eseguire le operazioni e, se attive le risorse specifiche, dove eseguirle.
Il programma che esegue questa funzione è il S5SMES_11E (saturazione estesa).
E' presente anche il programma S5SMES_11S (saturazione base), per compatibilità con precedenti installazioni.
Essi richiamano rispettivamente i programmi S5SMES_12E e S5SMES_12S, che implementano una parte delle funzioni.
Nel seguito tratteremo solo della saturazione estesa.

# Modalità base
Si esaminano gli impegni pronti non ancora schedulati. Per ciascuno di essi si sceglie il dettaglio più scarico (quello la cui risorsa ha l'istante di inizio disponibnilità più basso).
Si determina il vincolo al più presto dell'impegno :  se esso è minore dell'inizio disponibilità vuol dire che si creerebbe coda.
Se ci sono dettagli in questa situazione (vale a dire che fanno coda), si sceglie come dettaglio da schedulare quello, tra questi, con cror più basso.
Se invece non c'è nessun dettaglio che fa coda, si sceglie quello con vincolo più basso e, a pari vincolo, quello con cror più basso.
Questo significa che, se su una risorsa c'è coda, si sceglie il lavoro più urgente, se invece non c'è, si sceglie quello che si può fare prima.

In questo processo non viene sfruttato il fatto che i dettagli di un gruppo siano ordinati.
Questa proprietà è utilizzata, a standard, nel trattamento della parte congelata, ed è a disposizione dell'utente per realizzare strategie di tiro e spinta, per percorrere la coda in
modo ordinato.

# Modalità di trattamento della zona congelata
I dettagli congelati sono ordinati per numero progressivo :  se il primo non schedulato è pronto, viene scelto, altrimenti tutta la coda viene sospesa finchè esso diventa pronto, ed a quel punto lo si schedula.

Per un impegno pronto non congelato che può essere eseguito su più risorse, non vengono considerate quelle su cui vi sono ancora impegni congelati non schedulati; se si può eseguire solo su di esse, viene trascurato fino a quando si libera una risorsa (si esaurisce la parte congelata), ed esso entra in competizione con gli altri impegni.


# Tiro
Si può impostare una strategia di 'tiro', vale a dire, dopo aver schedulato un'impegno su una risorsa specifica, accodarvi altri impegni eseguibili sulla stessa risorsa, con comunanze con l'operazione schedulata (stesso articolo, attrezzaggio breve, ecc...), ed eventualmente all'interno di un determinato orizzonte temporale (per ottenere un compromesso tra la riduzione dell'attrezzaggio e l'eccessivo anticipo degli impegni.

Si imposta il suffisso del programma che implementa il 'tiro', ed è lanciato dal programma standard di colloquio S5SMES_15.

Questo programma viene lanciato, in 'inizializzazione' dopo aver schedulato le operazioni iniziate :  se sulle loro risorse non vi sono zone congelate, si verifica se si possono tirare altre operazioni a partire dall'ultima iniziata. Questo richiamo viene eseguito nello script.

Viene poi lanciato in memorizzazione, dopo aver scelto il dettaglio da schedulare e prima di schedularlo, per memorizzarne il valore (la schdulazionme lo potrebbe cambiare, se schedulasse in cascata dettagli su risorse a capacità infinita), ed in ripresa, che è il punto in cui viene eseguito il programma specifico di tiro. Anche questo richiamo viene eseguito nello script.

Inoltre, all'interno del programma di scelta del dettaglio da schedulare (S5SMES_11E), si valuta il tiro (vale a dire lo si lancia in memorizzazione e ripresa a cavallo della schedulazione) quando si sta schedulando l'ultimo impegno congelato su ogni risorsa specifica.

Il programma specifico di tiro S5SMX_03x, dove x è un carattere impostato nello script di parametri, riceve il puntatore all'ultimo dettagio eseguito, e torna quello successivo da schedulare.
Viene richiamato con l'ultimo puntatore che ha restituito, fino a quando torna un puntatore a zero, per interrompere la catena.
Esso deve eseguire unicamente una scelta :  è compito della parte standard che la richiama schedulare effettivamente l'operazione.

Per documentazione, sui dettagli tiranti viene impostato il campo XGTIRO a '1', su quelli tirati viene impostato a '2'.

# Spinta
Si può implementare una strategia più elaborata di schedulazione, impostando il suffisso 'x' di spinta nello script dei parametri che farà eseguire il programma S5SMX_05x.
Questa strategia è da utilizzare (anche se non viene eseguito alcun controllo in tal senso) in presenza di risorse specifiche, in quanto la sua funzione è di "spingere" l'impegno su un dettaglio che non sia obbligatoriamente il più scarico. Ciò piò essere fatto, ovviamente, solo se l'impegno ha più di un dettaglio, vale a dire quando sono attive le risorse specifiche.

In questo modo è possibile condizionare la scelta del dettaglio da eseguire in due modi diversi : 
 * quando la spinta è chiamanta con funzione 'DET' essa sostituisce il programma S5SMES_12E, di scelta del dettaglio più scarico per l'impegno ricevuto in £A01, ed il dettaglio ricevuto entra in competizione con gli altri. Il significato di questa strategia è di scegliere il dettaglio più opportuno, in base a considerazioni personali (ad esempio parcheggiate nella memoria della exit di spinta) se non produce un ritardo maggiore di un valore impostato rispetto al dettaglio più scarico.
 * quando la spinta è chiamanta con funzione 'FIN' essa riceve il dettaglio schedulato, e lo può modificare.
Naturalmente i due richiami sono logicamente in alterrnativa, anche se non viene fatto nessun controllo/forzatura in tal senso.
Il programma di spinta viene richiamato inoltre
 * con funzione 'INZ' all'inizio della schedulazione.
 * con funzione 'PAR' all'inizio di ogni scelta del dettaglio
Questi richiami danno la possibilità di preparare e modificare aree di memoria di lavoro utili al processo.

Una modalità 'leggera' di utilizzare questa funzione può essere la seguente (da implementare nel richiamo FIN).
Dopo aver determinato il dettaglio da eseguire, e posto che esso si possa eseguire su più risorse, lo si devia su un altra risorsa meno scarica se : 
 * sulla risorsa scelta originariamente ci sono altri dettagli pronti ed eseguibili solo su di essa
 * se l'esecuzione sulla nuova risorsa non produce holes nè ritardi inaccettabili.

Attenzione :  nella exit di spinta si può ritornare un dettaglio qualsiasi, ed è quindi cura di chi scrive le exit di evitare incongruenze. Ad esempio, nella funzione "DET" si può ritornare un dettaglio estraneo all'impegno ricevuto, e nella funzione "FIN" un dettaglio non appartenente all'impegno del dettaglio scelto.

# Strategia esterna
Si può implementare una strategia esterna nell'exit S5SMX_14x.
Essa viene lanciata in inizializzazione con la funzione "INZ" per costruire le eventual memorie.
Viene inoltre lanciata all'inizio della scelta del dettaglio da schedulare con funzione "RIT".
Essa può ritornare un dettaglio £A05. In tal caso viene scelto come dettaglio da schedulare senza alcuna altra considerazione. Se invece questo campo viene ritornato a zero, il programma di scelta procede normalmente. Può essere il caso, ad esempio, che questa exit implementa una sottostrategia (solo per alcuni gruppi) e soltanto quando essi hanno tutti gli impegni pronti essa entra in gioco. Inoltre, sempre se il dettaglio ritornato è zero, può ritornare il messaggio "END", il che significa che la sottostrategia ha terminato il suo compito, e quindi la sua exit non verrà più richiamata.

# Traccia per impostare una strategia personale (sia completa sia parziale)
Quando si vuol impostare una strategia personale sia completa (scegliere il dettaglio da schedulare) sia parziale (scegliere il dettaglio di un impegno da mettere in competizione con gi altri), una strada seguire può essere la seguente.
Si crea un programma mongolfiera, che crea le estensioni orizzontali alle memorie standard (normalmente agli impegni, ai dettagli, alle risorse, ai gruppi) e memorie specifiche adatte al caso.
Questo programma, di struttura BCD, va richiamato normalmente con tre funzioni : 
Inizializzazione :  lanciato dalla exit generale di inizializzazione S5SMX_11x, per creare le estensioni alle memorie e le memorie personali
Calcolo :  lanciato dalla exit opportuna. Ad esempio, se è la scelta delal risorsa specifica particolare, è l'exit di spinta S5SMX_05, con funzione "DET"
Registrazione :  lanciato dal passo di schedulazione S5SMX_01x, per registrare nelle memorie interne il risultato del dettaglio schedulato.
Le exit sono quindi dei semplici ponti, che richiamano un unico programma che costruisce le sue memorie, le utilizza e le aggiorna.
Questa struttura (senza passare da exit ma lanciando programmi standard, se la funzione è prevista dallo script) è utilizzata nella gestione dei batch, delle RSV, del parallelismo. In questo modo le memorie specifiche, oltre ad essere facilmente modificabili (sono utilizzate in un unico programma) occupano spazio soltanto se sono necessarie.

Una modalità per costruire le memorie personali, se esse devono essere riempite da campi di S5IRIS, per evitare di rileggerlo nella funzione di costruzione della memoria, può erssere la seguente.
Si realizza la exit S5SMX_02x, lanciata nella costruzione della memoria DSIRIS.
Quando questa exit è lanciata con funzione "INZ" si lancia la mongolfiera con lo scopo di azzerare la memoria (questa funzione è necessaria nelle rischedulazioni)
Quando è lanciata con funzione vuota essa riceve la DS di S5IRIS e può impostare di scartare il record. Se non lo fa, può, a sua volta, lanciare la mongolfiera sempre con la DS di S5IRIS, che può registrare nelle sua memorie le informazioni necessarie (flag, campi liberi, ecc..).
Una modalità più "sporca" di passare queste informazioni è quella di memorizzarle (in questa exit, oppure addiruttura nella scrittura dell'archivio S5IRIS) se non sono eccessive, nella parte finale, meno significativa, del CROR. In tal modo esse sono presenti nella memoria DSIRIS, e quindi utilizzabili dalla exit del completamento dell'inizializzazione.

# Sospensione fase
E' possibile, con la exit S5SMX_12x, lanciata quando viene preso in considerazione un impegno pronto, "sospendere" l'impegno stesso, vale a dire non trattarlo in quel giro di scelta, in quanto non sono pronti altri impegni che devono essere eseguiti contemporaneamente (informazione dedotta dalle opportune memorie specifiche). Questa funzione è normalmente realizzata (a standard) con la gestione dei batch. La presente exit, anteriore a tale implementazione, potrebbe essere utlizzata in casi particolari in cui non si vuol implementare la gestione dei batch e il legame tra impegni è automatico.
Un utilizzo più proficuo di tale sospensione si verifica in abbinamento alla strategia esterna. Supponiamo che essa si attivi quando tutti gli impegni di un particolare gruppo sono pronti. In caso contrario la strategia esterna non entra ancora in funzione. In questo caso però bisogna evitare che vi sia una "fuga" degli impegni pronti del gruppo, vale a dire che vengano scelti nel normale processo. Con la presente exit si può quindi decidere di sospendere indiscriminatamente gli impegni del gruppo da schedulare in modo esterno.

# Impostazione vincolo al più presto
L'istante di vincolo al più presto VPP viene determinato con la seguente sequenza.
Se presente un valore sul dettaglio si assume (questo valore viene valorizzato unicamente in presenza di sovrapposizione tra fasi, e quindi sostituisce in modo indiscriminato quello originale dell'impegno.
Altrimenti si assume il valore dell'impegno.
Se presente, sull'impegno, un vincolo esterno maggiore del precedente, si assume.
Questo istante viene poi avanzato con la disponibilità delle RSV se impostata.
Come ultima azione, se presente la exit S5SMX_21x, può venire ulteriormente avanzato (ci si protegge da modifiche indiscriminate impedendo che la exit ritorni un istante inferiore a quello che ha ricevuto.





