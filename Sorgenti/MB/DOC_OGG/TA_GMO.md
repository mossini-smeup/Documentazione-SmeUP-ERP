# GMO - Tipo documento movimentazione
## OBIETTIVO
Definire le caratteristiche della testate delle richieste di movimentazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Identifica il codice del tipo documento.
 :  : FLD T$DESC Descrizione
 :  : FLD T$PA01 __Tipo oggetto origine__
Individuano il tipo dell'oggetto di origine della richiesta di movimentazione.
 :  : FLD T$PA11 __Parametro oggetto origine__
Individuano il parametro dell'oggetto di origine della richiesta di movimentazione.
 :  : FLD T$PA02 __Tipo/Parametro oggetto destinazione__
Individuano l'oggetto di destinazione della richiesta di movimentazione.
 :  : FLD T$PA12 __Parametro oggetto destinazione__
Individuano il parametro dell'oggetto di destinazione della richiesta di movimentazione.
 :  : FLD T$GMON __Numeratore richiesta movimentazione__
È un elemento della tabella CRNGM, che guida l'assegnazione automatica del numero della richiesta.
Se non impostato, si intende che la richiesta di movimentazione sarà senza testata.
 :  : FLD T$GMOA __Origine documento__
È un elemento dei valori fissi SMEUP V2/GMTMO :  definisce la natura del documento che ha originato la richiesta (documento ciclo esterno, ordine di produzione, ecc...).
 :  : FLD T$GMOB __Livello di nascita__
Se, in inserimento della richiesta non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$GMOC __Priorità assunta__
È un elemento della tabella B§A che viene proposto all'atto dell'inserimento della richiesta.
 :  : FLD T$GMOD __Tipo oggetto generazione__
Individuano il tipo dell'oggetto che ha generato la richiesta di movimentazione.
 :  : FLD T$GMOE __Parametro oggetto generazione__
Individuano il parametro dell'oggetto che ha generato la richiesta di movimentazione.
 :  : FLD T$GMOF __Gruppo Flag__
È un elemento della tabella B£Y. Se valorizzato, alle testate richieste vengono assegnati i flag di questo elemento.
 :  : FLD T$GMOG __Parametri impliciti__
È un elemento della tabella C£I. Definisce la natura dei campi liberi (5 numerici e 5 alfanuerici) della testata.
 :  : FLD T$GMOH __Tipo riga assunto__
È un elemento della tabella GMZ, che definisce il tipo di riga di richiesta, assunto all'inserimento di una richiesta di questo tipo.
 :  : FLD T$GMOK __Cat parametri ext__
È un elemento della tabella C£E. Definisce la categoria dei parametri legati ad una richiesta di movimentazione.
 :  : FLD T$GMOS __Pgm di stampa__
Il programma assunto per tutti i documenti è GMRM40A, impostando questo valore si assume che il programma di stampa per questo documento divenga GMRM40x, dove x assume il valore del pgm di stampa
