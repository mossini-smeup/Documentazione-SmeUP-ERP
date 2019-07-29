# Personalizzazione

Agendo sulla exit indicata in V50 è possibile modificare i dati scritti nei differenti tracciati di EDSEND oppure aggiungerne (ad esempio aggiungendo righe di note, gli allegati o tracciati non gestiti dal programma di estrazione standard).
Il nome della exit è **V5ED04B_xx** dove xx è uguale a quanto indicato nel campo **Exit PGM estrazione.

Le funzioni e metodi della exit, i tracciati e i significati dei singoli campi sono illustrati nei commenti del prototipo **V5ED04B_ES** di cui viene distribuito il sorgente non compilato.

## Gestione Tipi prezzi non standard
Nel caso di **Metodo gestione prezzi non standard** (R§FL04 diverso da 1,3,4) il programma di estrazione della Fatturazione Elettronica espone come prezzo unitario il **prezzo netto** £5FV(04).
Se si desidera visualizzare gli sconti in fattura nel caso di tipo prezzo non standard, procedere nel seguente modo nel programma di exit : 
* Nella **routine FPRE_02 se R§FL04 diverso da 1, 3, 4 impostare il campo F02PRUL con il** **il prezzo lordo** e salvarsi in una schiera i valori degli sconti.
* Nella **routine FPRE_11 se R§FL04 diverso da 1, 3, 4 annullare la riga impostando P$IN35=*ON.
* Nella **routine FADD_11 se R§FL04 diverso da 1, 3, 4 impostare il campo F11TPSC='SC' e il  F11PCSC con la percentuale di sconto oppure F11CSIM con l'importo dello sconto.
** **Attenzione : ** ogni riga corrisponde a uno sconto applicato in sequenza. Il V5ED04B richiama la exit con funzione ADD finché non viene restituito messaggio 'FINE'. (Se si vogliono aggiungere 2 righe è necessario restituire 2 volte CONT e un'ulteriore volta FINE per uscire. Se riceve FINE esce dal loop senza scrivere il record).
** **Attenzione : ** nel tracciato ministeriale l'importo dello sconto ha un limite di soli 2 decimali. E' quindi preferibile indicare gli sconti come percentuali. Nel caso di importi di sconto con più di 2 decimali si consiglia di lasciare il prezzo netto senza indicare gli sconti, per evitare squadrature nei controlli da parte del Sistema di Interscambio e il conseguente scarto della fattura.
 :  : NPG
