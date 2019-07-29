# CRN - Numeratori
 :  : DEC T(ST) K(CRN)
## OBIETTIVO
Questa tabella guida alla costruzione dei numeratori associati ad un determinato oggetto.
In base alla compilazione dei campi della tabella in sequenza, viene determinata la forma e i valore del numeratore. la sequenza per il calcolo è : 
prefisso, separatore 1, anno, separatore 2, mese, separatore 3, giorno, separatore 4, progressivo numerico.
Il campo azienda, come documentato in seguito, può essere inserito opzionalmente in vari punti nella struttura.
Tutti i campi, a parte il progressivo, sono facoltativi. In questo modo è possibile costruire numeratori dai più semplici (solo numerici), ai più complessi, contenenti prefissi, separatori e variabili derivate da data e azienda.
La parte progressiva numerica va sempre a completamento della lunghezza totale impostata al numeratore, al netto dei prefissi impostati.
## SOTTOSETTORI
Ogni ambito specifico punta ad un sottosettore specifico, ad esempio C5 i numeratori della contabilità, P5 per la produzione, BR per i dati di base, ecc..
Per la gestione della documentazione aziendale esiste il sottosettore CRNDO, che compone un numero progressivo di documento per ogni tipo di documento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice numeratore**
Rappresenta il codice del numeratore, ad ogni elemento è associata una logica di numerazione.
 :  : FLD T$DESC **Descrizione**
Descrive il codice numeratore.
 :  : FLD T$PREF **Prefisso**
Se compilato, il contenuto fisso di questo campo viene utilizzato come prefisso del numeratore. Se compilo ad esempio P- il valore del numeratore risultante inizierà per P-, seguito da altri caratteri e numeri in base alle altre impostazioni.
 :  : FLD T$SEP1 **Separatore 1**
Se compilato con un carattere, viene utilizzato dopo il prefisso (anche se in bianco) e prima dell'anno.
 :  : FLD T$ANNO **Anno (X - XX - A )**
Permette di utilizzare l'anno, derivato dalla data passata al costruttore del numeratore (/COPY £CRN) in base al contesto (per esempio data fattura, data registrazione, data ordine, data di esecuzione), come prefisso del numeratore.
In base all'opzione scelta varia la sintassi : 
XX emette l'anno a 2 cifre (ad. esempio 18 se anno è il 2018)
X+spazio emette solo la cifra del decennio (ad esempio 2 se anno è 2028)
spazio+X emette solo la cifra dell'anno dell'unità (ad esempio 7 se anno è 2037)
Per l'opzione A, si assume la lettera A per il 2000, B per il 2001 fino alla Z per il 2019, poi riparte da A per il 2020, e cosi via per tutti i multipli di 20.
 :  : FLD T$SEP2 **Separatore 2**
Se compilato con un carattere, viene utilizzato dopo l'anno (anche se in bianco) e prima del mese.
 :  : FLD T$MESE **Mese (X-A)**
Permette di utilizzare il mese, derivato dalla data passata al costruttore del numeratore (/COPY £CRN).
In base all'opzione scelta varia la sintassi : 
X emette il mese numerico occupando 2 caratteri (01, 02, ecc..)
A emette il mese alfabetico occupando 1 carattere (A, B, C....)
 :  : FLD T$SEP3 **Separatore 3**
Se compilato con un carattere, viene utilizzato dopo il mese (anche se in bianco) e prima del giorno.
 :  : FLD T$GIOR **Giorno (X-A-J)**
Permette di utilizzare il giorno, derivato dalla data passata al costruttore del numeratore (/COPY £CRN).
In base all'opzione scelta varia la sintassi : 
X emette il giorno del mese in formato numerico, occupando 2 caratteri (01, 02, ecc..)
A emette il giorno utilizzando un carattere alfabetico, dalla A alla Z, ed esaurite le lettere arriva a 31 utilizzando caratteri speciali 27=$ 28=£ 29=& 30=% 31=*
J emette il giorno in formato giuliano utilizzando 3 caratteri. E' un progressivo numerico di cifre che corrisponde al progressivo assoluto del giorno partendo da inizio anno, e va da 1 a 365 (o 366 per gli anni bisestili).
 :  : FLD T$SEP4 **Separatore 3**
Se compilato con un carattere, viene utilizzato dopo il giorno (anche se in bianco) e prima del progressivo.
 :  : FLD T$PROG **Progressivo corrente**
Indica l'ultimo progressivo utilizzato
 :  : FLD T$NLUN **Lunghezza numeratore**
E' un campo obbligatorio e definisce la lunghezza totale del numeratore costruito. Può variare da 1 a 15 max.
 :  : FLD T$AZZE **Azzeramento automatico**
Se per il numeratore è previsto un prefisso temporale (anno/mese/giorno), impostando tale campo al variare del valore di tale prefisso (memorizzato nei campi ultimo anno/mese/giorno) verrà automaticamente attuato l'azzeramento del progressivo.
Attenzione, l'azzeramento non avviene per un progressivo puro, che non contenga almeno una variabile temporale.
Ad esempio il numero DDT composto da un numerico di 6, non si azzera al cambio anno in automatico anche se il campo viene compilato.
 :  : FLD T$COMM **Gestione a COMMIT**
Dove gestito dalle funzioni chiamanti, permette di bloccare l'incremento del numeratore per altri utenti e funzioni, fino ad uno sblocco esplicito, mediante funzione C nella chiamata alla /COPY £CRN.
 :  : FLD T$ATCO **Stato COMMIT**
Viene autocompilato quando attivo il commit in incremento, per segnalare che l'incremento è inibito fino allo sblocco.
 :  : FLD T$LANN **Ultimo anno**
In questo campo viene memorizzato l'anno della data di riferimento dell'ultimo protocollo utilizzato.
Nel caso siano impostati i campi azzeramento automatico (T$AZZE) e il prefisso anno (T$ANNO), in funzione di questo campo viene deciso l'azzeramento del progressivo.
 :  : FLD T$LMES **Ultimo mese**
In questo campo viene memorizzato il mese della data di riferimento dell'ultimo protocollo utilizzato.
Nel caso siano impostati i campi azzeramento automatico (T$AZZE) e il prefisso mese (T$MESE), in funzione di questo campo viene deciso l'azzeramento del progressivo.
 :  : FLD T$LGIO **Ultimo giorno**
In questo campo viene memorizzato il giorno della data di riferimento dell'ultimo protocollo utilizzato.
Nel caso siano impostati i campi azzeramento automatico (T$AZZE) e il prefisso giorno (T$GIOR) in funzione di questo campo viene deciso l'azzeramento del progressivo.
 :  : FLD T$CRN1 **Passo di numerazione**
Permette di modificare il passo standard di numerazione (default = 1), indicando di quanto incrementare il progressivo ad ogni richiesta di incremento.
Compilando per esempio con 5, la parte progressiva del numeratore passerà da 5, poi 10, poi 15 ecc..
 :  : FLD T$CRN2 **Azienda**
Si ha la possibilità di inserire il contenuto del campo azienda nel numeratore.
Inserendo il valore '1' il campo azienda viene inserito "prima del prefisso" (inizio numeratore)
Inserendo il valore '2' il campo azienda viene inserito "dopo il prefisso" (prima del separatore)
Inserendo il valore '3' il campo azienda viene inserito "prima del Progressivo"
