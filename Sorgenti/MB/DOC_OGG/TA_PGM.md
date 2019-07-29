# PGM - Programma
## OBIETTIVO
Questa tabella viene letta all'inizio dei programmi che la prevedono, per derivarne condizioni esterne desiderate dall'utente.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC __Descrizione__
 :  : FLD T$PGMA __Solo simulazione__
Se previsto dal programma, la presenza di tale scelta fa in modo che il programma non esegua le funzioni di aggiornamento o esecuzione di passi. Si può, ad esempio, produrre una stampa per controllo.
 :  : FLD T$PGMB __Stampa log__
Se impostato, attiva la produzione della stampa di controllo. Tale metodo è utilizzato in particolare come standard da tutti i servizi. Se attivato, vengono stampate tutte le aggiunte al file XML inviato su coda.
 :  : FLD T_PGMC __Stampa condizioni__
Utilizzata dai programmi standard di stampa che prevedono parzializzazioni e ordinamento (utilizzano COPY £B£S*).
Permette di scegliere se stampare le condizioni impostate.
Le opzioni possibili sono : 
A = Si stampano le condizioni su una pagina separata.
B = Le condizioni sono sulla prima pagina, seguite dai dati richiesti, senza salto pagina.
 :  : FLD T_PGMD __Attiva performance__
Se previsto dal programma, la presenza di tale scelta fa in modo che il programma registri i tempi di
esecuzione dello stesso. Le registrazioni sono mantenute in memoria fino ad un massimo di 20.000 istanze.
L'analisi dei tempi è fruibile attraverso la scheda di debug.
Le opzioni possibili sono : 
0 = Tutti i tempi
1 = Solo tempi superiori ai 10 millisecondi
2 = Solo tempi superiori ai 20 millisecondi
3 = Solo tempi superiori ai 30 millisecondi
4 = Solo tempi superiori ai 40 millisecondi
5 = Solo tempi superiori ai 50 millisecondi
6 = Solo tempi superiori ai 60 millisecondi
7 = Solo tempi superiori ai 70 millisecondi
8 = Solo tempi superiori ai 80 millisecondi
9 = Solo tempi superiori ai 90 millisecondi
 :  : FLD T_PGME __Condizioni log__
E' un campo in cui si possono inserire filtri alla stampa di log.
Ad esempio, se si attiva la stampa all'interno di un programma che implementa una strategia particolare di schedulazione
un filtro potrebbe essere il codice di un centro di lavoro, in modo tale da tracciare i passi di schedulazione dei soli
impegni apppartenenti al centro impostato.
 :  : FLD T_PGMF __Attivaz. log £GPE __
Mediante questo campo è possibile attivare il log (su JALOGT0F) delle sottomissioni batch effettuate tramite £GPE.
Le opzioni possibili sono : 
blank :  Utilizza l'impostazione inserita in tabella B£5
1 :      Forza la scrittura del log (indipendentemente dal valore in B£5)
2 :      Forza la NON scrittura del log (indipendentemente dal valore in B£5)


