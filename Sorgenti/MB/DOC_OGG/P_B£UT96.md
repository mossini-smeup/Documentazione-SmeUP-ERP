# GESTIONE LISTA MEMBRI
 Questa utility presenta una lista di "lista membri".
 Vengono visualizzate le scansioni effettuate dall'utente ordinate per data in modo discendente (per
 modificare i parametri di selezione vedi F17). Vengono indicate le informazioni relative alla
 ricerca effettuata, in che librerie e file sorgenti è stata eseguita la scansione e vengono
 visualizzate le note associate alla ricerca.

 Nota a proposito della ricerca effettuata.
 Quando nell'UP SCA viene effettuata una ricerca di tipo 2 Espressione (_&_R riga; "..." testo)
 viene elaborata un'espressione nella scansione dove _&_R indica la singole riga in scansione.
 Ecco un paio di esempi : 
 - {E1(_&_R : 22 : 1 = F AND _&_R : 36 : 4 = DISK) E2()}
   cerca F a colonna 22 (lunghezza 1) e cerca DISK a colonna 36 (lunghezza 4)
 - {E1(M5CMRP >> _&_R AND £AUARA >> _&_R)
   cerca la prezenza di M5CMRP e £AUARA nella stessa riga
 E' possibile inserire due espressioni e la scansione verifica che siano soddisfatte entrambe
 all'interno dello stesso membro sorgente. Ognuna delle espressioni viene elaborata a livello
 di singola riga del membro sorgente, pertanto viene verificato che le due espressioni siano
 soddisfatte anche in due righe diverse dello stesso membro sorgente.

## Azioni eseguibili
 * 'X ' - Passa agli elementi della lista selezionata (visualizzazione dei membri)
 * '02' - Permette di inserire o modificare una breve nota che verrà esposta sulla destra
 * '04' - Elimina la lista (viene richiesto di confermare con F06)
 * '05' - Alias di 'X'
 * 'DA' - Differenza Insiene A (A-B), crea una lista dei membri non presenti ove imputato DB
 * 'DB' - Differenza Insiene B (A-B), vedi sopra
 * 'UA' - Unione Insieme A (A-B) U (B-A), crea una lista di tutti i membri ove imputato UA e UB
 * 'UB' - Unione Insieme B (A-B) U (B-A), vedi sopra
 * 'RT' - Ricerca RETURN, crea una lista dei membri che contengono RETURN
 * '? ' - Scelta tra le opzioni ammesse
 * '??' - Caratteristiche delle azioni ammesse
 * '!!' - Azioni Utente
 * '91' - Dati della £FUND1
 * '92' - Caratteristiche della riga
 * '% ' - Funzioni di Stringa


## F17 Filtro
 Premendo F17 è possibile modificare i eguenti parametri di selezione : 

### Tipo Lista
 I tipo di liste ad oggi gestite sono : 
 * SCASCA - Scansione UP SCA (prodotta dall'utility UP SCA);
 * SCASRC - Scansione controllo sorgenti;
 * CMPMAS - Compilazione massiva (prodotta dall'utility B£UT11).

### Utente
 Permette di selezionare l'utente che ha eseguito a scansione, in modo da condividere il
risultato della scansione e le annotazioni relative alle operazioni da effettuare in un
gruppo di lavoro.

### Data inizio
 Permette di selezionare le scansioni oltre la data richiesta.


## F07 Ripeti opzione
 Ripete l'opzione inserita a video in tutte le righe successive.


## F01 Trova
 Effettua la ricerca della stringa richiesta.


## F09=Trova precedente
 Ripete a ritroso la ricerca della stringa richiesta dopo aver premuto F01.


## F10=Trova successivo
 Prosegue la ricerca della stringa richiesta dopo aver premuto F01.


