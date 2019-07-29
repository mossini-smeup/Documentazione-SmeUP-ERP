Esistono principalmente due Tecniche di trasferimento di sorgenti : 
 * tramite SAVF;
 * tramite Client Access.

## Tramite SAVF
Il SAVF è in sostanza la versione AS400 del .ZIP.
Seguire questa procedura : 
 * Creare un file SAVF tramite il comando **CRTSAVF** (è consigliabile creare un SAVF nella propria libreria (per esempio W_NOMEUTENTE)). Questo comando, in sostanza, crea il file ZIP vuoto.
 * A questo punto il file SAVF va riempito, per fare ciò esistono due comandi : 
 ** _2_SAVLIB (salvo un'intera libreria);
 ** _2_SAVOBJ (salvo un oggetto).

I campi da compilare sono rispettivamente, per il comando SAVOBJ : 
 * Oggetti :  dove indico il nome dell'oggetto che voglio copiare;
 * Libreria :  vado ad indicare il nome della libreria in cui è contenuto l'oggetto/i che devo copiare;
 * Unità :  dove inserisco *SAVF (come viene poi spiegato sotto);
 * Tipi oggetti :  in cui specifico il tipo di oggetti/o che vado a copiare, solitamente anche *ALL è sufficiente, se devo copiare ad esempio un singolo programma;
 * File salvataggio :  dove vado ad indicare il file che ho creato in cui voglio inserire il mio  oggetto/i;
 * Libreria (riferita al file salvataggio) :  nella quale bisogna indicare la libreria dove si trova il file SAVF (lo zip).

Per quanto riguarda il comando SAVLIB invece : 
 * Libreria :  devo indicare la libreria che voglio copiare;
 * Unità :  dove vado a specificare *SAVF;
 * File salvataggio e Libreria si riferiscono al file e la libreria in cui voglio copiare.

In entrambi i casi nel prompt del comando devo mettere come "Unità" *SAVF e poi fare **F10**, in modo che il prompt si adegui e possa indicare il SAVF in cui salvare l'oggetto o la libreria.

Un aspetto molto importante sono le release degli AS di origine e di destinazione, poichè i salvataggi ad una release superiore non sono compatibili con quelle di livello inferiore. In entrambi i comandi l'indicazione avviene tramite il parametro **TGTRLS** (= Release di destinazione).

Un altro aspetto da considerare è la pulizia del SAVF :  per poter salvare un nuovo oggetto all'interno di un SAVF già utilizzato è necessario o pulire in precedenza il SAVF (tramite il il comando CLRSAVF oppure specificare il dovuto valore nel parametro aggiuntivo del comando di salvataggio CLEAR (Cancellazione dati), tenendo conto che se lascio il default *NONE il salvataggio non verrà effettuato.

A questo punto, per scaricare il SAVF su PC, esistono dei software specifici, ma il medesimo risultato è ottenibile anche tramite comandi DOS.

I passi sono  i seguenti : 
 * FTP + indirizzo AS400
 * UTENTE : 
 * PASSWORD : 
 * BIN
 * GET
 * Indirizzo del SAVF sull'AS (Libreria/NomeSavf)
 * Indirizzo del file su PC es. C : \savf (non è necessario che il file esista già)

Per poi portare il SAVF su un altro AS la procedura è simile, ma è necessario aver prima creato un SAVF vuoto sull'AS di destinazione.
 * FTP + indirizzo AS400
 * UTENTE : 
 * PASSWORD : 
 * BIN
 * PUT
 * Indirizzo del file su PC es. C : \savf
 * Indirizzo del SAVF sull'AS (Libreria/NomeSavf) (il savf deve esistere già sull'AS e deve essere vuoto).

Una volta fatto, si pone il problema di rispristinare l'oggetto :  a questo scopo sono disponibili i comandi **RSTLIB** e **RSTOBJ** :  in entrambi i casi è possibile cambiare il nome della libreria o rispristinare l'oggetto in una differente, attraverso il parametro **RSTLIB** (= Caricamento nella libreria).

Per riutilizzare il SAVF, devo prima pulirlo tramite il comando **CLRSAVF**

## Tramite Client Access
Per salvare un sorgente usando il client access : 
 * dalla barra dei menù scegliere **azioni - ricevi file da host**;
 * nella parte superiore indicare il file sorgente presente sull AS da copiare sul proprio pc;
 * nella parte inferiore indicare il nome del file e la directory da usare per salvare il file sul proprio pc;
 * ove indicato il tipo di salvataggio / emissione, è importante impostare, tramite il **pulsante dettagli, il formato di salvataggio : 
 ** Tipo file :  testo ASCII
 ** Converti dati server :  ANSI

Per ripristinare un sorgente dal proprio pc verso l'AS è necessario seguire le seguenti procedure : 
 * dalla barra dei menù scegliere **azioni - invia file a host**;
 * nella parte superiore del nome indicare il file da inviare all'AS;
 * nella parte inferiore si indica il file sorgente su AS da usare nella copia.

Note : 
 * a differenza del salvataggio con SAVF, il Client Access permette di creare un solo membro alla volta e comunque il salvataggio su filesystem esterno AS comporta la perdita delle date di modifica;
 * usare Client Access invece che SAVF risulta utile quando le porte FTP sono chiuse;
 * nel ripristino bisogna impostare gli stessi dettagli del trasferimento e definire come trattare membro e file di trasferimento (di default specificare che si vuole creare il file).
