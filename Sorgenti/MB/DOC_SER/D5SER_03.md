 :  : HEA RESP(AS) STAT(80)
# OBIETTIVO
Questo servizio fornisce funzionalità per effttuare confronti particolari tra chivi del D5COSO.

# FUNZIONI/METODI
## CFR Confronti particolari
Costruisce una matrice con i confronti tra varie chiavi del D5COSO
### Metodo EXT
I dati relativi a quali chiavi confrontare (gli ID) vengono forniti da un programma esterno.
Le varie chiavi vengono inserite in altrattante colonne dove i vari valori presenti sono presentati sulle righe.
E' possibile confrontare al massimo 100 chiavi differenti.
Il programma esterno che fornisce gli ID delle chiavi da confrontare può ricevere alcuni dati in  input, tra cui : 

- funzione
- metodo
- parametro libero
- ID di partenza

L'ID di partenza può essere fornita al servizio direttamente altrimenti viene calcolata automaticamente partendo dai dati della chiave forniti al servizio stesso.
## QRY Confronti da script
Costruisce un report confrontando vari elementi, leggendo la struttura del report da uno script.
### Metodo SCP
Estrae un elenco degli script che contengono definizioni di report.
### Metodo LIC
Estrae un elenco dei report definiti in un certo script.
### Metodo CFR
Costruisce un report.

_1_NOTA della funzione QRY  _7_- Sintassi dello script che contiene le strutture dei report.
In uno script è possibile definire più di un confronto.
Per iniziare le specifiche di un nuovo report (in uno script è possibile definirne più di uno) è necessario usare l'istruzione CFR, per definire poi gli elementi di confronto è necessario usare le istruzioni COL (uno per ogni elemento da inserire nel report).
Vediamo nel dettaglio la sintassi di queste istruzioni.

**..CFR**
_Sintassi : _
..CFR Cod="XXX" Des="YYY"
_Significato attributi : _
Cod  :  definisce il codice del confronto
Des :  definisce la descrizione del confronto
 :  : PAR T(Esempio : ) F(04)
 :  : CFR Cod="CF1" Des="Confronto pippo"

questa istruzione indica che le istruzioni seguenti costituiscono un confronto di codice CF1 e descrizione confronto pippo.

**..COL**
questa istruzione definisce un singolo elemento di confronto. E' possibile inserire come elemento di confronto due "entità" :  un record del D5COSO oppure un calcolo basato su entità già inserire nel confronto.
_Sintassi nel caso di "entità" record D5COSO : _
..COL Codc="XXX" Desc="YYY" Type="REC" Tipa="AAA" Codi="BBB" Trot="CCC" Cod1="DDD" Cod2="EEE" Cod3="FFF" Dtva="GGG" Ricl="J"
_Significato attributi : _
Codc :  definisce il codice dell'elemento di confronto. Sono ammessi fino a 7 caratteri, non sono ammessi spazi.
Desc :  definisce la descrizione dell'elemento di confronto.
Type :  definisce il tipo di elemento di confronto (in questo caso è REC, ossia record D5COSO).
Tipa, Codi, Trot, Cod1, Cod2, Cod3 e Dtva :  definiscono le chiavi del record da recuperare
Ricl :  identifica un'eventuale riclassifica
 :  : PAR F(04) T(Esempio : )
 :  : COL Codc="UNO" Desc="Primo agente" Type="REC" Tipa="CNAGE" Codi="000001" Trot="£AG" Cod1="01" Cod2="A01" Cod3="000001" Dtva="200501" Ricl=""
 :  : COL Codc="DUE" Desc="Secondo agente" Type="REC" Tipa="CNAGE" Codi="000004" Trot="£AG" Cod1="01" Cod2="A01" Cod3="000001" Dtva="200501" Ricl=""

queste istruzioni definiscono due elementi da confrontare, recuperati da due record D5COSO. I due record sono identificati dalle chiavi inserite.

_Sintassi nel caso di calcolo basato su entità già inserite : _
..COL Codc="XXX" Desc="YYY " Type="FOR" Oper="JJJ" Para="KKK"
_Significato attributi : _
Codc e Desc :  hanno lo stesso significato visto nel caso precedente (codice e descrizione dell'elemento di confronto)
Type :  definisce il tipo di elemento di confronto (in questo caso è FOR, ossia formula basata su altri elementi)
Oper :  specifica il tipo di operazione
Para :  specifica eventuali parametri da passare all'operazione
Vediamo adesso quali sono i tipi di operazione permessi e i parametri che necessitano : 
Oper="DEL" :  delta percentuale tra due colonne, nell'attributo Para è necessario specificare le due colonne tra cui calcolare il delta. Il formato è il seguente Para="-CO.XXX--CO.YYY" dove XXX e YYY sono i codici di elementi di confronto (valore dell'attributo Codc di altre istruzioni ..COL). In questo caso si calcola lo scostamento dell'elemento XXX rispetto a YYY.
Oper="DEP" :  delta percentuale tra due colonne, il formato del parametro è lo stesso visto per l'operazione DEL.
Oper="STO" :  subtotale, sommo i valori di tutti gli elementi inseriti fino a questo. Non necessita di parametri. Non vengono inclusi nella somma eventuali elementi di altri subtotali o subtotali intermedi (STO e STI).
Oper="STI" :  subtotale intermedio, sommo i valori di tutti gli elementi a partire dall'ultimo subtotale intermedio fino a questo. Non necessita di parametri. Non vengono inclusi nella somma eventuali elementi di altri subtotali o subtotali intermedi (STO e STI).
Oper="INC" :  incidenza percentuale, nel parametro è necessario indicare di quale elemento di confronto è necessario calcolare l'incidenza percentuale e a quale subtotale (da 1 a 5 specificabile nella IGI) riferirsi. Para="-CO.XXX : Y", XXX è il codice del confronto, mentre Y è il subtotale di riferimento (e quindi va da 1 a 5).
 :  : PAR T(Esempio : ) F(04)
 :  : COL Codc="UNO" Desc="Primo agente" Type="REC" Tipa="CNAGE" Codi="000001" Trot="£AG" Cod1="01" Cod2="A01" Cod3="000001" Dtva="200501" Ricl=""
 :  : COL Codc="DUE" Desc="Secondo agente" Type="REC" Tipa="CNAGE" Codi="000004" Trot="£AG" Cod1="01" Cod2="A01" Cod3="000001" Dtva="200501" Ricl=""
 :  : COL Codc="FFF" Desc="delta % tra secondo e primo agente" Type="FOR" Oper="DEP" Para="-CO.DUE--CO.UNO"

In questo esempio due elementi sono presi da D5COSO, il terzo è lo scostamento percentuale tra il secondo e il primo.

Da notare che gli elementi da confrontare devono avere valori "confrontabili". Non viene fatto nessun controllo di questo vincolo, deve essere chi costruisce il confronto che si preoccupa di inserire solo elementi (colonne) confrontabili. Per quanto riguarda le decodifiche dei valori, vengono usate quelle relative all'ultimo record D5COSO agganciato (l'ultima colonna di tipo REC).


 :  : PRO.SER Cod="CFR.EXT.1" Tit="Confronti. Dati da pgm esterno" Fun="F(EXB;D5SER_03;CFR.EXT) 1(**;;-(F;;**;Contesto/codice)) 2(TA;D5O**;-(F;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(F;;**;Data/periodo)) P( NM(-(F;;**;Nome programma)) FU(-(F;;**;Funzione)) ME(-(F;;**;Metodo)) PA(-(F;;**;Parametro)) RC(-(F;;**;Riclassifica)) ID(-(F;;IDD5COSO0F;ID di partenza)))"

 :  : PRO.SER Cod="QRY.SCP.2" Tit="Confronti da script. Elenco script" Fun="F(TRE;D5SER_03;QRY.SCP) 2(OJ;*LIB;-(O;;OJ*LIB;Libreria))"

 :  : PRO.SER Cod="QRY.LIC.3" Tit="Confronti da script. Elenco report" Fun="F(TRE;D5SER_03;QRY.LIC) P( NS(-(F;;**;Nome script)))"

 :  : PRO.SER Cod="QRY.CFR.4" Tit="Confronti da script. Report" Fun="F(EXB;D5SER_03;QRY.CFR) P( NS(-(F;;**;Nome script)) CC(-(F;;**;Codice confronto)))"

