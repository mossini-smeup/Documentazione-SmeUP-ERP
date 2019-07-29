## OBIETTIVI
Gestione/Controllo/Decodifica campi video del data entry delle registrazioni di contabilità.

## Modo di richiamo : 
 * Inserimento
 ** CTR / LOC
 ** PRE
 * Variazione o inserimento batch
 ** DEC
 ** CTR / LOC
 ** PRE
 * Visualizzazione/Annullamento
 ** DEC

## FUNZIONI/METODI
 * RES       Reset Aree di Memoria
 ** ALL       Globale -  Chiude il programma
 ** LOR       Aree di lettura record origine   Reinizializza ottimizzazioni lettura record origine
 * INI       Inizializzazione Controllo - Pulisce tutti i messagggi e inizializza tutte le variabili di ottimizzazione
 * FIN       Fine Controllo - Esegue i controlli finali di validità del record
 * DEC       Decodifica - Carica i campi video dal file stesso e li controlla :  riceve il record aggiorna la DS (campi W$) e li decodifica (lancia la CTR e spegne gli errori)
 * CTR       Controllo dettaglio -  Controlla/Decodifica i campi video :  riceve la DS (campi W$) li controlla e li decodifica
 ** GLO       Globale
 ** LOC       Locale
 * PRE       Presentazione - Carica i campi del file dai campi video :  riceve la DS (campi W$) e il record di cui aggiorna i campi
