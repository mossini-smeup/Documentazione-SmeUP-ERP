# INTERFACCIA RIGHE DOCUMENTI
Obiettivo
Gestire tramite le sue viste logiche ogni accesso al file V5RDOC0F.
# FUNZIONI
-    Indicano quale operazione si vuole eseguire.
-    Le funzioni disponibili sono : 
SL   esegue una SETLL
SG     "     "  SETGT
RD     "     "  READ
RP     "     "  READP
CHA    "     "  CHAIN
RE     "     "  READE
RPE    "     "  REDPE
SLRE   "     "  SETLL & READE
Esiste poi la funzione BLANK (' ') che, a partire da un Tipo
Documento, gestisce la ricerca (se richiesta tramite !/?) e la decodifica sia sul campo Nr. Documento che sulla Riga
Documento; esegue poi la lettura sulla vista logica principale V5RDOC0L, tramite CHAIN con chiavi Tipo documento -
Numero documento - Riga documento.
Oss. La funzione Blank NON ha metodi.
# METODI
-    Indicano quale vista logica si vuole utilizzare.
-    I metodi disponibili sono i seguenti : 
chiave composta da  Tipo doc. - Nr. doc. - Nr. riga
1L     "             "   Tipo doc. - Nr. doc. - Tipo riga
2L     "             "   Tipo doc. - Nr. doc. - Tipo oggetto -
Cod. ogg. - Data consegna confermata(DTCC)
3L     "             "   Tipo doc. - Tipo riga - Tipo ente intest.
Cod. ente - Cod. magaz. - Codice ogg.
4L     "             "   Tipo doc. - Livello - Cod. Magaz. -
Tipo ogg. - Cod. ogg. - DTCC
5L     "             "   Tipo doc. - Livello - DTCC
6L     "             "   Tipo doc. - Tipo ente intest. - Cod. ente
- Livello - Cod. magaz. - Tipo ogg. -
Cod.ogg. - DTCC
7L     "             "   Tipo doc. - Nr. doc. - Livello
8L     "             "   Tipo doc. origine - Nr. doc. orig. - Nr.
riga doc. orig. - Flag 01
9L     "             "   Tipo doc. - Tipo ente intest. - Cod. ente
- Livello - Cod. Magaz. - DTCC - Tipo ogg. - Cod. ogg.
AL     "             "   Nr. ordine. prod. - Operazione - Livello
BL     "             "   Tipo doc. - Nr. doc. - Tipo doc. origine
- Nr. doc. orig. - Nr. riga orig. - Nr.
riga
CL     "             "   Tipo doc. - Livello - Commessa- Tipo ogg.
- Cod. ogg. - DTCC
DL     "             "   Tipo doc. - Cod. magaz. - Tipo ogg. -
Cod. ogg. - Tipo ente intest. - Cod. ente
- DTCC
EL     "             "   Tipo doc. - Nr. doc. - Nr. riga riferimento master - Nr. riga
FL     "             "   Tipo doc. - Tipo ente spediz. - Cod. ente
- Livello - DTCC
# AMBIENTE
-    Non utilizzato.
# NR. CHIAVI
-    La £IDR è sensibile al numero di chiavi valorizzate (diverse da
BLANKS) che riceve; in particolare, in modo indipendente dalla funzione selezionata, utilizza per le sue operazioni
solo i campi realmente valorizzati. Si consideri ad es. il caso in cui viene utilizzata la funzione READE con il
metodo 0L. Il metodo è composto da 3 campi chiave : 
. Tipo documento - Nr. documento - Nr. riga
Si consideri inoltre che il file oggetto dell'operazione contenga i seguenti dati : 
OVE            000140         1
OVE            000140         2
OVE            000140         3
OVE            000141         1
OVE            000141         2
Se nell'esecuzione della £IDR vengono valorizzati nel seguente modo ('OVE', '000140') solo il tipo ed il numero
documento, allora un ciclo " DO ... EXSR £IDR ... ENDDO " leggerà tutte le righe dell'ordine 000140. Si noti che se
venisse considerato il campo numero riga pari a BLANK la lettura non avrebbe buon fine.
Il campo Nr. Chiavi serve in quelle situazioni in cui si vuole che venga considerato anche il campo valorizzato con
BLANKS. Tramite il Nr. chiavi si indica appunto alla £IDR il numero di chiavi che essa deve utilizzare indipendente
dal fatto che siano valorizzate oppure BLANK.
Un caso d'esempio in cui valorizzare il numero di chiavi è il seguente.
Consideriamo la funzione CHAIN con il metodo 2L, composto dalle chiavi Tipo documento, nr. documento, tipo oggetto,
codice oggetto, data consegna confermata. Si consideri inoltre che il file oggetto dell'operazione contenga (a meno
dell'ordinamento) i seguenti dati : 
. Tipo documento - Nr. documento - Tipo ogg. - Cod. ogg.- DTCC
OVE            000140              AR        001
OVE            000140                        X02
OVE            000140              A/C       AAA
OVE            000140              AR        002
Se nell'esecuzione della £IDR vengono valorizzati nel seguente modo ('OVE', '000140') solo il tipo ed il numero
documento, ma viene specificato in numero chiavi £IDRNK = 3 allora la £IDR restituirà il secondo record, quello cioè
con il tipo oggetto a
BLANK.
OSS. In ogni caso, in assenza di un valore per numero chiavi, la £IDR determina il numero di chiavi da utilizzare
sulla base della posizione dell'ultima chiave valorizzata; in presenza di una serie di chiavi valorizzate nel seguente
modo (VALORE1, BLANKS, VALORE3,
BLANKS, VALORE-N, BLANKS, ... BLANKS) la £IDR utilizzerà N chiavi (e quindi anche quelle di valore BLANKS che
precedono l'N-esima chiave).
# NOTE SULLA EXSR £IDR (1)
Se viene utilizzata la funzione BLANK (scansione e ricerca) devono essere valorizzati i parametri £IDRTD, £IDRND,
£IDRNR; per le altre funzioni devono invece essere valorizzati i campi della DS
V5RDOC (ad es. R§TDOC, R§COMM ...). In ogni caso dopo una lettura la £IDR valorizza in output sia la V5RDOC che i
campi £IDRTD, £IDRND, £IDRNR, £IDRDE.
# NOTE SULLA EXSR £IDR (2)
Il numero chiavi (£IDRNK) non è un parametro della £IDR ma è una variabile messa a disposizione dalla £IDR stessa.
