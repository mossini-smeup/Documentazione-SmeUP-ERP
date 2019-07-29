# INTERFACCIA TESTATE DOCUMENTI
### Obiettivo
Gestire tramite le sue viste logiche ogni accesso al file V5TDOC0F.
### FUNZIONI
-    Indicano quale operazione si vuole eseguire.
-    Le funzioni disponibili sono : 
 * SL   esegue una SETLL
 * SG   esegue una SETGT
 * RD   esegue una READ
 * RP   esegue una READP
 * CHA   esegue una CHAIN
 * RE   esegue una READE
 * RPE   esegue una REDPE
 * SLRE   esegue una SETLL & READE

Esiste poi la funzione BLANK (' ') che, a partire da un Tipo Documento, gestisce la ricerca (se richiesta tramite !/?) e la decodifica sul campo Nr. Documento; esegue poi la lettura sulla vista logica principale V5TDOC0L, tramite CHAIN con chiavi Tipo documento - Numero documento.
La funzione Blank NON ha metodi.

## METODI
-    Indicano quale vista logica si vuole utilizzare.

# AMBIENTE
-    Non utilizzato.
# NR. CHIAVI
-    La £IDO è sensibile al numero di chiavi valorizzate (diverse da BLANKS) che riceve; in particolare, in modo indipendente dalla funzione selezionata, utilizza per le sue operazioni solo i campi realmente valorizzati.
Si consideri ad es. il caso in cui viene utilizzata la funzione READE con il metodo 1L.
Il metodo è composto da 3 campi chiave : 
>. Tipo documento - Tipo modello - Nr. documento
Si consideri inoltre che il file oggetto dell'operazione contenga i seguenti dati : 
    OVE            OCI            000140
    OVE            OCI            000140
    OVE            OCI            000140
    OVE            OCL            000141
    OVE            OCL            000141

Se nell'esecuzione della £IDO vengono valorizzati nel seguente modo ('OVE', 'OCI') solo il tipo ed il modello documento, allora un ciclo " DO ... EXSR £IDO ... ENDDO " leggerà tutte le righe dell'ordine 000140.
Si noti che se venisse considerato il campo numero doc. pari a BLANK la lettura non avrebbe buon fine.
Il campo Nr. Chiavi serve in quelle situazioni in cui si vuole che venga considerato anche il campo valorizzato con BLANKS.
Tramite il Nr. chiavi si indica appunto alla £IDO il numero di chiavi che essa deve utilizzare indipendente dal fatto che siano valorizzate oppure BLANK.

Un caso d'esempio in cui valorizzare il numero di chiavi è il seguente : 
Consideriamo la funzione CHAIN con il metodo 8L, composto dalle chiavi Tipo documento, codice viaggio, nr. documento.
Si consideri inoltre che il file oggetto dell'operazione contenga (a meno dell'ordinamento) i seguenti dati : 
>. Tipo documento - Codice viaggio - Nr. Documento
    OVE            AS0140              001
    OVE            X02                 002
    OVE                                003
    OVE            X02                 004

Se nell'esecuzione della £IDO viene valorizzato nel seguente modo ('OVE') solo il tipo documento, ma viene specificato in numero chiavi £IDRNK = 2 allora la £IDO restituirà il terzo record, quello cioè con il codice viaggio a BLANK.
N.B. In ogni caso, in assenza di un valore per numero chiavi, la £IDO determina il numero di chiavi da utilizzare sulla base della posizione dell'ultima chiave valorizzata; in presenza di una serie di chiavi valorizzate nel seguente modo (VALORE1, BLANKS, VALORE3, BLANKS, VALORE-N, BLANKS, ... BLANKS) la £IDO utilizzerà N chiavi (e quindi anche quelle di valore BLANKS che precedono l'N-esima chiave).
## NOTE SULLA EXSR £IDO
 - Se viene utilizzata la funzione BLANK (scansione e ricerca) devono essere valorizzati i parametri £IDOTD, £IDOND; per le altre funzioni devono invece essere valorizzati i campi della DS V5TDOC (ad es. T§TDOC, T§COMM ...). In ogni caso dopo una lettura la £IDO valorizza in output sia la V5TDOC che i campi £IDOTD, £IDOND, £IDODE.
 - Il numero chiavi (£IDONK) non è un parametro della £IDO ma è una variabile messa a disposizione dalla £IDO stessa.
