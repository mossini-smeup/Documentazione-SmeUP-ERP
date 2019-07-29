## Obiettivo
Analizzare il partitario aziendale attivo e/o passivo

## Parametri di lancio
 * Codice oggetto :  in funzione dell'oggetto scelto all'interno del surf in questo campo sarà necessario indicare il codice cliente, la lista clienti, il codice fornitore, ecc. da analizzare
 * Partite :  permette di filtrare le partite visualizzate. Le opzioni disponibili sono : 
 ** Tutte :  permette di visualizzare sia le partite aperte che quelle chiuse
 ** ASC A scadere :  vengono incluse solo le partite non ancora scadute
 ** DPR Da presentare :  vengono incluse tutte le partite aperte che non sonno ancora incluse in una distinta di pagamento/incasso
 ** ESI Con Insoluti e Protesti :  vengono mostrate solo le partite che includono insoluti o protesti
 ** ESP In Esposizione :  include sia le partite aperte che quelle in rischio
 ** NEG Aperte Negative :  vengono incluse solo le note credito e gli anticipi
 ** RIS Rischio :  vengono incluse solo le partite in rischio
 ** SCA Aperte :  vengono incluse solo le partite aperte
 ** SCD Scaduto :  vengono incluse solo le partite scadute
 * Data Documento inizio/fine :  permette di filtrare i documenti per data
 * N° Doc. :  se compilato il programma mostrerà tutte le partite per cui il numero documento contiene la stringa qui immessa.
 * N° Prot. :  se compilato il programma mostrerà tutte le partite per cui il numero protocollo contiene la stringa qui immessa.
 * Dt.Reg. Inizio/Fine :  permette di filtrare le partite visualizzate per data registrazione
 * Dettaglio rate :  di default il sistema presenta le partite raggruppando le rate che appartengono a una stessa registrazione. Compilando questo campo verrà mostrato tutto il dettaglio delle rate. Quindi se ad esempio abbiamo una fattura composta da tre scadenze, lasciando il campo vuoto vedremo una sola riga con il totale della fattura, flaggandolo vedremmo invece il dettaglio delle tre righe.
 * Dividi Note/Fatture :  nel caso in cui ci siano note e fatture collegate tra loro permette di vedere il dettaglio della partita della fattura e della partita della nota credito. Per collegare la nota credito alla relativa fattura è necessario compilare i campi _Fattura Riferimento/Del sulla testata della registrazione della nota credito.
 * Escludi Movimenti Simulati :  permette di escludere le registrazioni provvisorie
 * Netto Ritenute :  nal caso in cui siano presenti ritenute d'acconto permette di visualizzare gli importi al netto delle ritenute
 * Righe per pagina :  permette di aumentare il numero di righe mostrato al lancio della funzione (di default vengono presentate le prime 1000 righe).

## Dettaglio informazioni
Confermando i parametri di lancio vengono visualizzate tutte le partite che rispettano tali parametri.
Sulla linea di totale di ogni partita vengono riportati : 
 * Progressivo partita
 * Numero e Data fattura
 * Totale Fattura nella valuta della fattura
Per le partite scadute la data scadenza è evidenziata in azzurro mentre per quelle in rischio è evidenziata in rosso : 
![C5D010_060](http://localhost:3000/immagini/MBDOC_SCH-C5SER_25/C5D010_060.png)
Nel caso in cui all'interno di una riga siano presenti più scadenze la riga viene sottolineata : 
![C5D010_061](http://localhost:3000/immagini/MBDOC_SCH-C5SER_25/C5D010_061.png)![C5D010_062](http://localhost:3000/immagini/MBDOC_SCH-C5SER_25/C5D010_062.png)
La colonna 'A' ha l'obiettivo di caratterizzare la partita e sarà compilata con : 
 * a se la partita è aperta
 * i se nella partita è presente un insoluto
 * r se la partita è in rischio
 * s se la partita è scaduta

Si ricorda che una nota credito viene visualizzata all'interno della partita della fattura a cui si riferise solo nel caso in cui sulla testata della nota credito siano stati compilati i campi _Fattura Riferimento/Del_  e non sia stato impostato il parametro _Dividi note/fatture._

### Pareggio partite
Nel caso in cui si vogliano paeggiare tra loro diverse partite è possibile selzionare le righe flaggando il campo P e quindi digitare F06 - Conferma pareggio : 
![C5D010_067](http://localhost:3000/immagini/MBDOC_SCH-C5SER_25/C5D010_067.png)
### Specificità per Account

Nel caso in cui vengano gestiti i nominativi, è possibile analizzare il partitario a livello di account visualizzando, quindi, sia le partite attive che quelle passive intestate al nominativo.
Nel caso in cui, inoltre, i nominativi siano gestiti a livello di gruppo aziendale, all'interno della matrice verranno esposti i record di tutte le aziende abilitate.
I record relativi alle aziende diverse da quella a cui l'utente è collegato compariranno in bianco e su questi non sarà possibile eseguire alcuna funzione.
Quindi se ad esempio siamo collegati all'interno dell'azienda 10 e il nominativo ha scadenze aperte anche per le aziende 02 e 15, queste scadenze verranno esposte ma non saranno manutenibili : 

![C5D010_065](http://localhost:3000/immagini/MBDOC_SCH-C5SER_25/C5D010_065.png)
Per disabilitare la visualizzazione delle partite di un'azienda sarà necessario definire l'autorizzazione AZ impostando nella classe il codice dell'azienda da nascondere e il valore dell'autorizzazione a NO.

