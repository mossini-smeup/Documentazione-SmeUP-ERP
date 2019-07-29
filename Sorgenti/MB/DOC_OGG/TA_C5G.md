# C5G - Tipo pagamento
 :  : DEC T(ST) K(C5G)
## OBIETTIVO
Definire i caratteri generali dei pagamenti presenti nel sistema.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Contiene la descrizione di questo specifico tipo di pagamento.
 :  : FLD T$C5GA **Natura pagamento**
È un elemento V2/C5NAP :  definisce se il pagamento è un effetto, un bonifico o altro. Viene riportato nella rata di dovuto all'atto dell'inizializzazione. Questo elemento determina l'inclusione o meno delle rate di pagamento nel calcolo del rischio (vengono infatti incluse solo le rate con natura di tipo effetto).
 :  : FLD T$C5GB **Incasso/Pagamento Immediato**
Se impostato, all'atto della registrazione del documento viene derivata in automatico la registrazione del relativo incasso/pagamento.
In particolare  : 
'1' - La funzionalità è attiva sia per le rate clienti che fornitori
'2' - La funzionalità è attiva solo per le rate clienti
'3' - La funzionalità è attiva solo per le rate fornitori
Il tipo registrazione, la causale ed il conto di contropartita devono essere definiti nell'elemento "PGIMM" della tabella C5U con risalita con desinenza del tipo pagamento.
Eccezioni sono le riba attive e le rid attive :  nel caso delle riba attive i riferimenti vengono ripresi dal tipo elemento "PADA9", mentre nel caso delle rid attive dal "PADAR".
Inoltre per le rid la data registrazione è la data di scadenza della rid ed il conto viene
ripreso dalla banca aziendale se indicata.

Tali logiche possono essere cmq rettificate tramite l'utilizzo di un pgm exit, avente nome fisso C5RR13E_X. La sua attivazione è determinata dalla presenza dell'oggetto stesso.

Inoltre, è da tener conto che la creazione della nuova registrazione avverrà sempre tramite il lancio in modalità batch di un lavoro indipendente. I parametri di esecuzione di tale lavoro sono modificabili tramite il comando UP GPE, impostando come programma "C5RR13E".
 :  : FLD T$C5GC **N° Titolo**
Gestisce l'utilizzo del campo n° titolo nelle registrazioni di saldaconto con titoli : 
- Se impostato a 1 significa il n° titolo è obbligatorio e va imputato a mano.
- Se impostato a 2 significa il n° titolo è obbligatorio e viene automaticamente attribuito tramite un numeratore (sottosettore C5, codice "C5G"+Azienda+'.'+elemento C5G).
 :  : FLD T$C5GD **Insollecitabilità**
E' un elemento V2Si/NO. Se impostato le rate con questo tipo pagamento non saranno soggette a sollecito.
 :  : FLD T$C5GE **Conto portafoglio**
È il conto contabile del portafoglio effetti aziendale, alimentato dalla contabilizzazione di una pratica quando è attiva la contabilizzazione banca (Tabella C5U).
 :  : FLD T$C5GF **Contabilizzazione portafoglio effetti banca**
Se attivo, e se per la relativa C5U è prevista la contabilizzazione della maturazione degli effetti, la contabilizzazione della presentazione effetti verrà effettuata in due step : 
- con la prima contabilizzazione alla data di presentazione verrà chiuso il portafoglio effetti aziendale e caricato il portafoglio effetti dell'istituto creditizio
- con la seconda contabilizzazione alla data di maturazione degli effetti, verrà chiuso il portafoglio effetti dell'istituto di credito e caricato il relativo conto di c/c
Se disattivo la contabilizzazione sarà in unico step alla data di maturazione con storno del conto portafoglio azienda e caricamento del relativo conto di c/c
Se il campo viene valorizzato a "2" verrà prevista solo la prima contabilizzazione.

 :  : FLD T$C5GH **Pratica non contab.**
E' un elemento V2Si/NO.
 :  : FLD T$C5GI **Tracciato Trasmissione**
Tramite esso può essere specificato un tracciato di trasmissione diverso rispetto a quello standard, deducibile dalla natura del pagamento.
 :  : FLD T$C5GL **Giorni di rischio**
Definisce un numero di giorni di rischio specifico per il tipo pagamento, a sostituzione di quanto indicato nella tabella C51.
 :  : FLD T$C5GN **Cumulo**
Definisce la modalità di utilizzo del cumulo per il tipo pagamento nelle pratiche. I valori ammessi sono : 
- "1" = No (Il cumulo non può essere utilizzato).
- "2" = Sempre (Il cumulo viene sempre forzato automaticamente).
- " " = Si (Il cumulo può essere utilizzato).
 :  : FLD T$C5GO **Forzatura rischio**
Se valorizzato, questo flag permette di considerare a rischio anche i pagamenti effettuati con una natura differente da quella dell'effetto.
 :  : FLD T$C5GP **Massimo importo dell'effetto**
Se impostato, indica il massimo importo per l'emissione di un effetto. Tale limite viene applicato nella gestione delle pratiche :  se vengono selezionate rate per un importo superiore, queste rate vengono automaticamente spezzate per il delta.
 :  : FLD T$C5GQ **Cumulo in presentazione**
Se impostato a '1', in fase di deselezione delle rate nella gestione distinte,
le rate raggruppate, vengono decumulate, pronte per essere nuovamente cumulate per la prossima
presentazione.
Se impostato a blank (default), in fase di deselezione delle rate non viene tolto l'eventuale
raggruppamento fatto in precedenza.
