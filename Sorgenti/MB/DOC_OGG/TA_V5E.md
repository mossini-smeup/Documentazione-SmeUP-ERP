# V5E - Gestione intracee
 :  : DEC T(ST) K(V5E)
## OBIETTIVO
Definisce i parametri generali relativi alla gestione INTRA.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$DESC Note
 :  : FLD T$V5EA __Periodo per cessioni__
Questo campo è obbligatorio. Indica la cadenza con la quale gli elenchi devono essere presentati. Il significato può essere : 
- _9_1 = presentazione mensile;
- _9_2= presentazione trimestale.
 :  : FLD T$V5EB __Periodo per acquisti__
Questo campo è obbligatorio. Indica la cadenza con la quale gli elenchi devono essere presentati. Il significato può essere : 
- _9_1 = presentazione mensile;
 :  : FLD T$V5ED __U.M. chilogrammi__
È un elemento della tabella UMS. Indica l'unità di misura dei chilogrammi.
 :  : FLD T$V5EL __Esen.Val.Stat.Cess.__
Tramite esso viene condizionata l'obbligatorietà, nell'ambito della gestione del dettaglio del Valore Statistico, nonché della modalità di trasporto e delle condizioni di scelta (tale obbligatorietà è determinata dall'ammontare complessivo delle precendeti presentazioni).
 :  : FLD T$V5EM __Esen.Val.Stat.Acq.__
Tramite esso viene condizionata l'obbligatorietà, nell'ambito della gestione del dettaglio del Valore Statistico, nonché della modalità di trasporto e delle condizioni di scelta (tale obbligatorietà è determinata dall'ammontare complessivo delle precendeti presentazioni).
 :  : FLD T$V5EN __Tipo/Codice Soggetto Delegato__
Viene riportato il riferimento al Soggetto Delegato (se esistente) i cui dati anagrafici verrano riportati nella stampa dei frontespizi.
 :  : FLD T$V5EP __Suff. Agg. Spese__
Se presente rappresenta il suffisso del programma V5V5E2_SM che viene lanciato per il calcolo personalizzato della ripartizione delle spese sui record del file C5ICEE0F. Se lasciato bianco viene eseguito un calcolo di default che ripartisce spese e sconti in proporzione all'importo della singola riga di C5ICEE0F.
 :  : FLD T$V5EQ __Suff. Pgm.Aggiustam.__
Se presente rappresenta il suffisso del programma V5V5E2_SM che viene lanciato per il calcolo personalizzato di vari dati della comunicazione Intra. Si veda la relativa documentazione del programma di estrazione.
 :  : FLD T$V5ER __Sezione Doganale__
E' un elemento della tabella V§*IH e identifica la sezione doganale presso cui l'azienda effettua la presentazione degli elenchi intracomunitari. Se compilato il campo viene automaticamente ripreso nella compilazione del modello quinquies relativo alle rettifiche di prestazioni.
 :  : FLD T$V5ES __Raggruppamento Servizi__
A partire del 2015, diventa obbligatori per i servizi i soli campi : 
* Numero di identificazione delle controparti
* Codice servizio
* Paese di pagamento
* Valore delle transazioni
A parità delle prime 3 chiavi, gli importi andranno sommati. Per trasmettere i dati in questa modalità semplificata, sarà necessario valorizzare il campo in oggetto.
NOTA BENE :  mentre per i servizi ricevuti/resi nel periodo l'applicazione sarà completamente trasparente, nel caso delle rettifiche non verrà applicato alcun raggruppamento, essendo che potrebbe essere necessario rettificare dati trasmessi in modo completo, il raggruppamento viene quindi applicato in base alle effettive chiavi indicate.
NOTA BENE 2 :  qualora nasca l'esigenza di ritrasmettere una trasmissione precedentemente inviata senza il raggruppamento dei servizi, sarà necessario togliere temporaneamente l'attivazione del raggruppamento dalla tabella, per ripristinarla una volta che la ritrasimissione sarà stata effettuata.

 :  : FLD T$V5ET __Dati Cessioni__
Indica quali dati si ha vincolo a trasmettere, fra beni e servizi.
NOTA BENE :  tale scelta ha effetto solo sull'estrazione dei dati (e non quindi sull'immissione manuale e la trasmissione). Inoltre vengono escluse da questa considerazione le note di accredito essendo che queste potrebbe riferirsi ad un periodo in cui vigeva l'obbligo di trasmissione per la corrispondente fattura.

 :  : FLD T$V5ET __Dati Cessioni__
Indica quali dati si ha vincolo a trasmettere, fra beni e servizi.
NOTA BENE :  tale scelta ha effetto solo sull'estrazione dei dati (e non quindi sull'immissione manuale e la trasmissione). Inoltre vengono escluse da questa considerazione le note di accredito essendo che queste potrebbe riferirsi ad un periodo in cui vigeva l'obbligo di trasmissione per la corrispondente fattura.


