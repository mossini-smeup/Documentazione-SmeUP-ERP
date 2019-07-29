# Revisione tracciato archivio commesse (SV)
E' stata richiesta una revisione del tracciato dell'archivio BRCOMM per necessità emerse nell'ambito CRM.
Si è ritenuto opportuno non cambiare la natura dell'archivio, nato con una connotazione di natura trasversale, aggiungendo campi di tipo generalizzato, utilizzabili in modo specifico sul singolo modulo applicativo, anziché inserire campi specifici derivanti dall'attuale necessità di natura CRM.

## Normalizzazione campi di tipo generale
* Portare a 10 i parametri impliciti (10 codici, 10 numeri, 10 date)
* Portare a 40 i flag (20 smeup e 20 utente)
* Dati aggiornamento record completo
## Aggiunta di campi generali e specifici
* 6 oggetti definiti da 2 griglie, caratterizzati da tipo e codice (in cui collocare dati di utilizzo specifico applicativo, che siano oggetti di navigazione)
* Sottotipo commessa (tabella nuova con sottosettore definito nel tipo commessa)
* 2 enti aggiuntivi all'ente già presente
## Tabelle coinvolte
* Nuova tabella sottotipo commessa
** è una tabella definita per sottosettore definito su TA BSA
** solo descrittiva (come tabella P5E del P5EVEN per una simmetria)
* Aggiunta campi alla tabella BSA tipo commessa
** 2 griglie oggetti
** sottosettore stato
** stato di nascita
** stato di nascita
*** c'è già il livello occorre essere congruenti (programma controllo tabelle)
*** integrarne l'utilizzo
## Livello di intervento nei programmi
Occorre decidere il livello di adeguamento che questa modifica comporta, anche rispetto all'interfaccia utente.
Ci sono le modifiche strutturali che vanno obbligatoriamente allineate : 
* inizializzatore £BRY
* archivio, flaggatore
* £OAV
* schemi £Q2
* controller £K89
* CRM (REBASE, REMARK)
Si può decidere che alcuni dei nuovi campi non siano disponibili sull'interfaccia 5250, quindi non adeguiamo il BRCM01D per intenderci
## Copertura richieste CRM (riferimento Paolo Belotti)
* L'Azienda  (in verità questo l'abbiamo gestito nelle commesse dell'amministrazione) --> inserire in oggetto
* Un altro ente --> inserire in nuovi enti
* Un Agente --> inserire in oggetto
* Un referente "RN" --> inserire in oggetto
* Una sottotipo (avendo usato il tipo  commessa per identificare Campagne, lead, Opportunità, ci serviva un altro campo per il tipo campagna, tipo lead, e tipo opportunità. Abbiamo usato una stressa tabella con sottosettore nel tipo commessa per caratterizzarla in base al tipo --> ok nuovo campo
* Direi che non sarebbe male avere anche un Tipo documento, Numero documento e  Riga documento --> no, la riga documento contiene un campo commessa

