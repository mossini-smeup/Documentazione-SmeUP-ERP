# IGL - Livelli di totale
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$DESC Descrizione
È la descrizione codice di totalizzazione
 :  : FLD T$IGLA __Programma__
È una Exit che permette una gestione utente nella creazione della totalizzazione. Se non specificata, è attivato il Pgm. IGCO02.
 :  : FLD T$IGLB __Parametro__
Il risultato della totalizzazione può essere scritto in due archivi :  IGREPT lo storico IGSTOR o entrambe *ALL
 :  : FLD T$IGLC __Scenario__
Definito l'archivio di memorizzazione della totalizzazione, è possibile separare i risultati in membri diversi, permettendo di migliorare le prestazioni in interrogazione/stampa e di gestire al meglio operazioni di riorganizzazione/salvataggio dati.
 :  : FLD T$IGLJ __Inizializzazione__
L'archivio risultato viene pulito prima di iniziare il calcolo e in fase di sviluppo.
 :  : FLD T$IGLF __Area/Tema/Livello di sintesi__
È la struttura del record, risultato dalla totalizzazione Area e Tema. Se non vengono impostate, assumono quelle di provenienza.
 :  : FLD T$IGLD.T$IGLF
 :  : FLD T$IGLE.T$IGLF
 :  : FLD T$IGLS SS.__Metodi/Metodi 1/2/3.__
Indica, tramite la tabella IGR, come reperire le aggregazioni da utilizzare in relazione alla tabella IGS, risultato della totalizzazione.
 :  : FLD T$IGLG.T$IGLS __Metodo campo1__
 :  : FLD T$IGLH.T$IGLS __Metodo campo2__
 :  : FLD T$IGLI.T$IGLS __Metodo campo3__
