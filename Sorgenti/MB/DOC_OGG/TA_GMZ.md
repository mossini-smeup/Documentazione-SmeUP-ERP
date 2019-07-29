# GMZ - Tipo riga movimentazione
## OBIETTIVO
Definire le caratteristiche delle righe delle richieste di movimentazione.
Ricordiamo che, oltre agli utilizzi standard, può essere interessante definire un tipo riga particolare da utilizzare per le attività che prevedono recupero di materiale dalla produzione. In questi casi, gestendo in distinta base coeff. negativi, è possibile arrivare ad impegni di produzione negativi che potrebbero a loro volta generare richieste di movimentazione per materiale da recuperare (vedi struttura LDA x funzione 'P5FURIM')
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Identifica il codice del tipo riga.
 :  : FLD T$DESC Descrizione
 :  : FLD T$GMZA __Causale 1 assunta__
È un elemento della tabella GMC. Se valorizzato, definisce il movimento di magazzino che verrà eseguito all'atto dell'applicazione della riga.
 :  : FLD T$GMZB __Causale 2 assunta__
È un elemento della tabella GMC. Se valorizzato, definisce l'ulteriore movimento di magazzino che verrà eseguito all'atto dell'applicazione della riga (in caso di transazione doppia).
 :  : FLD T$GMZC __Livello di nascita__
Se, in inserimento della riga della richiesta, non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$GMZD __Gruppo Flag__
È un elemento della tabella B£Y. Se valorizzato, alle righe della richiesta vengono assegnati i flag di questo elemento.
 :  : FLD T$GMZE __Prelievo/Versamento/Trasferimento__
E' un valore V2-TRRIM che determina l'azione delle richieste di movimentazione di questo tipo.
 :  : FLD T$GMZG __Parametri impliciti__
È un elemento della tabella C£I. Definisce la natura dei campi liberi (5 numerici e 5 alfanumerici) della riga.
 :  : FLD T$GMZH __Attività collegata__
È un elemento della tabella GMH. Qualora si voglia eseguire l'allocazione a partire da una riga di questo tipo, definisce il motore inferenziale che ne guida l'esecuzione.
 :  : FLD T$GMZI __Cod 1/5 trasferiti__
Si definisce se nell'assegnazione con trasferimento (fissa origine o destinazione) quali codici saranno riportati (rispettivamente nella destinazione o nell'origine). Se, ad esempio, la chiave 2 è il lotto, che si vuole mantenere nel trasferimento, si imposta '1' nel secondo carattere di questo elemento. (NB :  la quinta posizione è per il N.collo).
**Nota tecnica** :  questa attività à eseguita all'interno della funzione £GMR.
 :  : FLD T$GMZL __Assegnazione in inserimento__
Se impostato, all'atto dell'inserimento manuale di una riga, vengono aggiornate in automatico le quantità assegnate/attese sull'archivio giacenze (GMQUAN), con i codici (ubicazione, lotto, ecc..) impostati dall'utente; la riga viene dichiarata assegnata (flag 2 a '1').
Se la riga era stata dichiarata 'da non assegnare', vale a dire con il flag 2 a '9' (impostato nel gruppo flag), quest'ultima condizione ha la prevalenza, quindi non viene eseguita l'assegnazione.
 :  : FLD T$GMZM __Quantità assegnata facoltativa__
Se impostato, nel formato di assegnazione di richieste di movimentazione di questo tipo, non viene chiesta la quantità da assegnare, che viene invece determinata dal motore inferenziale che viene eseguito.
 :  : FLD T$GMZN __Assegnazione totale da motore__
Se impostato, per le richieste di questo tipo, l'assegnazione viene eseguita sempre nei passi del motore inferenziale (non solo per le righe spezzate), e non dalla funzione che lancia l'assegnazione (GMRM30A).
 :  : FLD T$GMZO __Compatta righe in disassegnazione__
Se impostato, per le richieste attive e disassegnate a parità di articolo, causali e numero riga, compatta in una sola riga disassegnata.
 :  : FLD T$GMZP __Forza Data Movimento su richieste di movimentazione__
Se impostato, verrà portata la data movimento presente sulla riga della richiesta di movimentazione nella data di registrazione
 :  : FLD T$GMZQ __Suff.pgm controllo__
È il suffisso del pgm GMRM10D_x che permette di gestire controlli e aggiornamenti specifici in fase di gestione del file (es. GMRM10D_F).
 :  : FLD T$GMZR __Cat parametri ext__
È un elemento della tabella C£E. Definisce la categoria dei parametri legati ad una riga di una Richiesta di movimentazione.
