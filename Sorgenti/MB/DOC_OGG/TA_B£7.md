# B£7 - Personalizzazione Ambiente
 :  : DEC T(ST) K(B£7)
Attraverso questa tabella è possibile definire i parametri di gestione dell'ambiente.
## CONTENUTO DEI CAMPI
 :  : FLD T$B£7A **Attivaz.Salv.Num.OG**
Se impostato durante il calcolo dei numeri degli oggetti, tipicamente la £G37, questi saranno salvati.
Attivando il salvataggio dei numeri oggetti vengono resi disponibili gli attributi O/nnn, questi se l'oggetto non ha subito variazioni, utilizzeranno i numeri salvati in precedenza.
Si ricorda che la data e l'ora dell'oggetto potrebbero non essere sufficienti a determinare la validità dei numeri storicizzati, vanno quindi usati con criterio.
 :  : FLD T$B£7B **SV.Compilazione Documenti**
Se non impostato, non sarà data la possibilità di compilare o utilizzare i compilati esistenti.
Se impostato a 2, si potranno compilare i documenti, ma i compilati non saranno utilizzati durante la lettura.
Se impostato a 1, si potranno compilare i documenti  e, in lettura, se presente il compilato verrà letto quest'ultimo.
La compilazione dei documenti si esegue utilizzando le stesse funzionalità utilizzate oggi per la compilazione. (Comando CO dal seu, oppure tramite la scheda dell'oggetto OJ *FILE)
La compilazione produce uno USRSPC contenente : 
* Le informazioni di compilazione
* L'immagine del documento al momento della compilazione
* Un'eventuale immagine di pre-trattamento dello stesso
Questa funzionalità, permette di poter modificare un documento senza che questo diventi fruibile immediatamente ed un miglioramento di performance durante la lettura dello stesso.
Contenitori trattati : 
* Tutti i DOC
* Tutti i SCP
* BCDSRC
Tipi trattati (Iniziano per) : 
* TXT
* IND
* BAT
* VID
* FIX
 :  : FLD T$B£7C **Attiva Switch utente**
Permettere ad un utente abilitato di modificare il gruppo (o ruolo) a lui assegnato e/o impersonare un utente diverso.
Questo permette ad esempio ad un capo di assegnare le attività di un utente assente ad un collega presente.
In Sme.up, infatti, le autorizzazioni a livello di utente si basano su due ogetti :  il codice utente (elemento di tabella
B£U) ed il suo gruppo (campo della tabella utenti B£U).
E' possibile far sì che in un intervallo di date uno o entrambi questi valori vengano sostituiti, tramite l'impostazione
di opportuni parametri (quindi cella categoria C£E di nome B£U)
Definiamo questa possibilità "switch utente".
Lo switch sostutisce totalmenbte il valore originale :  **NON è attiva nessuna risalita**.
 :  : FLD T$B£7E**Exit Azioni oggetti**
È il suffisso del programma di aggiustamento B£GES0_x (dove x è il suffisso indicato), che viene
lanciato dal programma B£GES0 per impostare le azioni di oggetti personali non gestiti dal programma
standard. Un prototipo è il programma B£GES0_X
 :  : FLD T$B£7F **Disabilita menu Gruppo utente**
Attivando questo parametro il menù del gruppo utente sarà sostituito dal menu dell'applicazione.
 :  : FLD T$B£7G **Ctrl Multipiattafor.**
Attivando questo parametro il pre-compilatore verificherà l'assenza di specifiche non compatibili con la generazione del codice multipiattaforma.
 :  : FLD T$B£7H **Comunic. Emulaz. 2.0**
Impostando questo parametro si attiva la versione 2 della comunicazione dell'emulatore.
Lo scambio del buffer avviene in formato XML.
Per alcune lingue (es. cinese) questa modalità è attivata automaticamente.
 :  : FLD T$B£7K **Disab.Notifiche App.**
Impostando il campo a '1' si disabilita globalmente l'invio di notifiche all'app mobile per l'ambiente.
 :  : FLD T$B£7L **Tipo notifica £GPE**
Se impostato attiva l'invio di notifiche al client per esecuzioni della £GPE lanciate da Loocup.
Il tipo notifica da impostare è 01.01.P02 (Completato lavoro batch)
