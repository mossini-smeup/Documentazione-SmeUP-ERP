# Obiettivo
La finalità delle notifiche è quella di poter generare un avviso visualizzabile tramite un'apposita funzione presente in Loocup, Webup e Mobile.

La notifica è l'insieme delle seguenti caratteristiche : 
* oggetto scatenante
* Responsabile dell'oggetto
* Istante
* Numerosità

Distinguiamo tra **notifiche in pull**, generate in base ad una temporizzazione e a delle regole, e **notifiche in push**, inviate puntualmente da un programma all'accadere di qualcosa.
Una notifica è in push se nel tag **A60.COS** l'attributo Cos="", mentre se è impostato il suffisso del programma costruttore da richiamare è in pull.

## Definizione di un tipo notifica
Il tipo notifica è un oggetto di tipo SESUB.A60 ,  che corrisponde a una subsezione in uno script LOA60_xx .

## Costruttori (Notifiche in pull)
Attraverso il Tag **A60.COS** si definiscono le logiche di generazione delle notifiche.
E' resa disponibile la variabile &RES (responsabile) da utilizzare nel tag A60.PRE
Sono stati predisposti i seguenti costruttori : 
* 01 - Comandi SQL
* 02 - Fonti della reportistica (A15)
* 03 - Membri sorgenti

### Comandi SQL
- [Comandi SQL](Sorgenti/MB/DOC/LOA60_01)

### Fonti della reportistica (A15)
- [Fonti della reportistica](Sorgenti/MB/DOC/LOA60_02)

### Membri sorgenti
- [Membri di sorgenti](Sorgenti/MB/DOC/LOA60_03)

## Schedulare la costruzione
Il programma LOA60_LM esegue la costruzione di ciascun motore di notifica (ciascun SE SUB.A60) in base all'intervallo previsto per ciascun motore.
Il lancio del programma (CALL LOA60_LM) va schedulato su una coda *NOMAX per ciascun ambiente per il quale si desideri costruire le notifiche.

## Notifiche in push
Un tipo notifica è definito come "in push" se non ha il costruttore valorizzato.
Deve quindi essere gestita a programma tramite la api £K14.

## Funzione di presentazione
La funzione che viene lanciata quando si clicca sul dettaglio della notifica, tipicamente la scheda che permette di vedere ciò a cui la notifica si riferisce, è impostata tramite il Tag **A60.PRE** .

## Notifica via mail


| 
| .COL Txt="Codice" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Valore" |
| Dis|Disabilita|' ' :  abilita l'invio , '1' :  disabilita l'invio |
| A17|Subsezione LOA17|Configurazione relativa a mittente, destinatari, contenuto della mail da inviare. |
| Whe|Invia mail se|'1' :  Aumenta il nr di notifiche , '2' :  Diminuisce il nr di notifiche , '3' :  Cambia il nr di notifiche , '4' :  Sempre (ad ogni esecuzione) |
| Ste|Passo incremento/diminuzione|Numero che serve a condizionare il parametro precedente |
| 


In assenza del tag **A60.MAI** viene assunto che le mail siano disabilitate.

## Notifica ad app mobile
L'invio delle notifiche all'app mobile è configurabile tramite il tag **A60.APP** .


| 
| .COL Txt="Codice" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Valore" |
| Dis|Disabilita|' ' :  abilita l'invio , '1' :  disabilita l'invio |
| Whe|Invia ad app se|'1' :  Aumenta il nr di notifiche , '2' :  Diminuisce il nr di notifiche , '3' :  Cambia il nr di notifiche , '4' :  Sempre (ad ogni esecuzione) |
| Ste|Passo incremento/diminuzione|Numero che serve a condizionare il parametro precedente |
| A38|Subsezione LOA38 (opzionale)|da valorizzare nel caso inviino notifiche ad app "brandizzate" |
| Tit|Titolo (ozionale)|Testo del titolo della notifica |
| Bod|Corpo del messaggio (ozionale)|Testo del corpo della notifica |
| 


In assenza del tag **A60.APP** viene assunto che le notifiche ad app mobile siano abilitate e inviate al cambio con passo 1.

### Device abilitati
Quando ci si collega con l'app mobile ad un ambiente viene registrato l'dentificativo del device che consente l'invio della notifica.
E' possibile disabilitare globalmente per l'ambiente l'invio delle notifiche a tutti i device tramite un campo in B£7.
E' inoltre possibile disabilitare l'invio a tutti i device di un utente o a singoli device di un utente tramite la sottoscheda "Device dell'utente" della scheda del costruttore LOA60.

## Cancellazione di una notifica
La funzione che viene eseguita per cancellare una notifica è definita tramite il Tag **A60.DEL** .
In caso non sia specificata assume come default una funzione che azzera il contatore per il tipo notifica, senza eseguire altre operazioni.
Qualora si utilizzi una funzione specifica è necessario che la stessa decrementi o azzeri il contatore per il tipo notifica tramite £K14.

## Disabilitare le notifiche client per un utente
Per disabilitare le notifiche Web.UP e Looc.UP per un utente (tipicamente per gli utenti utilizzati per accessi web condivisi o per gli utenti di servizio dei provider) si può intervenire sullo script di SCP_CLO dell'utente.
.. Disattivo notifiche
..  :  : C.VAR Cod="*NOTIFICATION" Txt="Notifiche" Value=""

## Note
La funzione "SND" del LOA60_SE invia al client tutte le notifiche presenti per un utente come messaggi di tipo NOTIF.

## Dettagli tecnici
- [Notifiche - Dettagli tecnici](Sorgenti/MB/DOC/LOA60_SV)
