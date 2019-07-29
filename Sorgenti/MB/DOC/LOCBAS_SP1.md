 :  : HEA RESP(MAEOLI) STAT(10) USAG(FORFED) DTAG(20170629) ORAG(180000) AMBT(TE)


# La versione Roma Revision 1

Prendendo come base di conoscenza la NWS002272, andiamo ad approfondire i temi tecnici.

# Nuova struttura del file di configurazione wrapper.conf
Per semplificare la configurazione sono stati portati i principali parametri all'inizio del file di configurazione.


# Nuovi parametri
 * --cleandb :  indica la persistenza dei record nel database dei log. il formato è nnnF, dove
 **   nnnn è il un valore numerico
 ** F è il formato d per i giorni, h ore m minuti s secondi
 * --nodblog :  per disabilitare la loggatura su database
 * --intserver :  per attivre un provider in modalità interattiva, ovvero come se fosse un Loocup client. Server per poter fare manutenazione degli script (le dialog e i messaggi non sono silenziati)
 * --sbs : xxxxxxx, serve per indicare quale è il sottosistema dove funziona lo SmeupProvider, e migliorare la gestione di eventuali disconnessioni.


## Business continuity
Per migliorare l'affidabilità del provider, sono stati introdotti dei timeout su tutte le chiamate verso il server iSeries compiute sulla connessione principale.
Il timeout sulle chiamate è di 300 secondi.
Se una chiamata va in timeout il provider  inzia a gestire una probabile perdita di connessione.



Il provider è in grado di rimanere acceso e ricollegarsi al server iSeries a fronte di molti malfunzionamenti.

Quando l'iSeries non è raggiungibile o non è in gradi di accettare connessioni il provider continua a funzionare.
In questo caso i servizi che può soddisfare sono solamente quelli di upgrade e di fornitore delle risorse remote.

### I test compiuti
Abbiamo fatto test staccando il cavo di rete, spegnendo l'iSeries e chiudendo il sottosistema QBATCHUI forzatamente, chiudendo forzatamente i lavori o le code.

In tutte queste situaziuoni, quando l'iSeries è stato di nuovo raggiungibile e operante il provider si è ricollegato.

### Le situazioni irrecuperabili
Quando il sottositema QBATCHUI viene chiuso, poi riaperto ed eseguite operazioni di sostituzione delle librerie, il provider, in assenza del semaforo, si ricollega ma va a trovarsi in una situazione in cui non è in grado di funzionare e va in blocco.

