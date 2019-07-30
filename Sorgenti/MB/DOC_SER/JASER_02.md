 :  : HEA RESP(RM) STAT(10)
# OBIETTIVO
Questo servizio fornisce le funzionalità di ricerca oggetti avvalendosi dell'oggetto Q1 (Query)


Oggetti coinvolti : 
Q1    - Query
Q2    - Schema
Q3    - Filtro
Q4    - Ordinamento
V3PQ3 - Fonte

# QUERY

Una query puo' essere rappresentata come un'aggregazione di 4 elementi : 
- Fonte dati
- Schema
- Filtro
- Ordinamento

### Vengono fornite le seguenti query di default : 
  Cod      Descrizione                Fonte Note
  *KEY     Ricerca per codice         *INT
  *DEC     Ricerca per descrizione    *INT
  *FIL     Ricerca su file            *FIL  Richiede la compilazione di TAB§O

 Le query vengono definiti nello script SCP_QRY, dove il nome del membro
  e' il nome dell'oggetto gestendo risalita tipo/parametro
 Le query di default possono subire override a livello di oggetto, tramite
 la compilazione del tag QRY nello script.

# FONTE
 Rappresentata il contenitore in cui ricercare gli oggetti, e' implementata da un programma di tipo V3PQR (B£IQR_xx)

### Vengono fornite le seguenti fonti di default : 
  *INT Accesso da interfaccia oggetto (B£IQR_01)
  *FIL Accesso da file (B£IQR_02)
  *JAC Accesso da tabella JAC (B£IQR_03)

 Le fonti dati possono essere estese tramite la compilazione dello script : 
  :  : SRC Cod="Nome fonte" Des="Descrizione fonte" Pgm="XX"
  Per informazioni circa lo sviluppo di un B£IQR_XX consultare il prototipo in SMESRC.

# SCHEMA

 Rappresenta l'insieme delle colonne della query ed e' un valore multiplo.
 Gli schemi possono essere delle seguenti tipologie : 

> P/xx - 	Schemi del barratore
 Sono schemi pubblici, utilizzabili quindi in ogni lista oggetti, sono cablati nel programma xxxx_M (vedi £BAR)

 I/xx - 	Schemi da £G25
 Sono anch'essi schemi pubblici, ma da importare con appostita direttiva (INC.SCH.G25)

 S/xx - Schemi dello script
 Definiti nello script, possono essere pubblici o privati.
 Nel caso in cui uno schema venga definito come pubblico la logica di sviluppo e' strettamente legata ad un OAV,
 se non viene espressa quindi una funzione a livello di campo, il codice della colonna si intende OAV.
 Nel caso di uno schema venga definito come privato, esso puo' essere utilizzato solo dalle query che lo includono
 con direttiva QRY Sch="s1,s2,s3". Gli schemi privati risultano quindi strettamente legati al programma di fonte,
 il loro utilizzo si richiede nel caso di formule SQL legate al campo.

 yy.xx - Schemi della fonte
 Vengono forniti dal programma di fonte, dove yy=fonte xx=schema


 Appartengono quindi alla query tutti gli schemi pubblici
 + gli schemi impliciti del programma di fonte + gli schemi privati della query.


# FILTRO
 Rappresenta l'insieme delle colonne della query che si intende filtrare.
 Viene definito nella query dall'attributo Flt="f1" nel tag QRY,
 Se non specificato vale il default del programma di fonte.
 Se non viene espressa una funzione a livello di campo il codice del filtro si intende OAV.

# ORDINAMENTO
 Rappresenta l'insieme delle colonne della query con cui si intende ordinare.
 Viene definito nella query dall'attributo Ord="o1,o2,o3" nel tag QRY,
 se non specificato vale il default del programma di fonte.
 E' multiplo, il primo elemento costituisce il default, ma puo' essere cambiato dalle impostazioni.
 Non possono essere specificati colonne di ordinamento calcolate dinamicamente(OAV),
 risulta quindi strettamente legato al programma di fonte.

# FUNZIONI/METODI
OGG.LIS

## Lista oggetti
Restituisce un XML di tipo matrice.


 :  : PRO.SER Cod="OGG.LIS.1" Tit="Oggetto. lista" Fun="F(QRY;JASER_02;OGG.LIS) 1(OG;;-( ;;OG;))"

 :  : PRO.SER Cod="OGG.LIS.2" Tit="Oggetto. lista" Fun="F(EXB;JASER_02;OGG.LIS)" Ref="OGG.LIS.1"

 :  : PRO.SER Cod="OGG.LIS.3" Tit="Oggetto. lista" Fun="F(EXA;JASER_02;OGG.LIS)" Ref="OGG.LIS.1"

 :  : PRO.SER Cod="SER.GLI.4" Tit="Funzioni di servizio. .Da scheda passa a gestione in lista" Fun="F(FBK;JASER_02;SER.GLI)" Ref="OGG.LIS.1"

