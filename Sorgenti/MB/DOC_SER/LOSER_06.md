 :  : HEA RESP(GR) STAT(80)
# OBIETTIVO
Il servizio LOSER_06 serve per eseguire una funzione o una serie di funzioni su un insieme di oggetti e avere la possibilità di misurarne le performance di esecuzione.

# FUNZIONI/METODI
## Funzioni generiche
  Calcolo del tempo di esecuzione di una singola funzione passata nel Tag Fun (in questo caso la funzione J1FUN)
 :  : PRO.SER Fun="F(EXB;LOSER_06;ESE) P(Fun([J1FUN]))" Cod="00001"

## Analisi a partire dallo SCRIPT LO_VERFUN
 Creazione dell'insieme di oggetti su cui eseguire massivamente la funzione da testare
 :  : PRO.SER Fun="F(EXB;LOSER_06;FUN.OGG)" Cod="00002"

### Albero dei gruppi di funzioni descritti nel LO_VERFUN - Albero a espansione
 Esegue una scansione dello script LO_VERFUN cercando le righe con T.FUN; queste rappresentano le foglie dell'albero.
 Le righe T.SEZ e T.SUB rappresentano rispettivamente il primo e il secondo livello di raggruppamento dell'albero.
 :  : PRO.SER Fun="F(EXB;LOSER_06;LIS)" Cod="00003"

### Lista delle funzioni del gruppo scelto.
 crea una matrice contenente la lista delle esecuzioni della funzione sugli oggetti dell'insieme
 :  : PRO.SER Fun="F(EXB;LOSER_06;FUN.LIS)" Cod="00004"

### Esecuzione della lista di funzioni del gruppo scelto.
 crea una matrice contenente la lista delle esecuzioni della funzione sugli oggetti dell'insieme con il calcolo del tempo di esecuzione.
 :  : PRO.SER Fun="F(EXB;LOSER_06;FUN.ESE)" Cod="00005"

 Le due funzioni sono state separate per ovvi motivi di performance; la prima, visualizzando solo la lista, non esegue nessun tipo di esecuzione, mentre la seconda misura i tempi di esecuzione della funzione eseguendola. Questo evita l'esecuzione "inutile" di una serie di funzioni.

### Visualizza il contenuto della memoria.
  Utile per visualizzare quello che è stato caricato nell'insieme degli oggetti ed effettuare delle verifiche
 :  : PRO.SER Fun="F(EXB;LOSER_06;MEM.GRU)" carica la lista dei gruppi di insiemi Cod="00006"
 :  : PRO.SER Fun="F(TRE;LOSER_06;MEM.ELE) 1(;;[K1])" visualizza il contenuto dell'insieme K1 Cod="00007"

## Analisi dei servizi
Le funzioni di un servizio - Lista o esecuzione
 :  : PRO.SER Fun="F(EXB;LOSER_06;SER.LIS) 1(MB;DOC_SER;[K1])" Cod="00008"
 :  : PRO.SER Fun="F(EXB;LOSER_06;SER.ESE) 1(MB;DOC_SER;[K1])" Cod="00009"
Le funzioni di tutti i servizi
 :  : PRO.SER Fun="F(EXB;LOSER_06;SER.LIS) 1(MB;DOC_SER;)" Cod="00010"
Utilizzo del servizio K2 in tutte le schede
 :  : PRO.SER Fun="F(EXB;LOSER_06;SCH) 1(MB;SCP_SCH;) 2(V3;ASE;[K2])" Cod="00011"

## Analisi delle schede
### Le funzioni di una scheda - Lista
In base al nome della scheda passato in K1, viene visualizzata una matrice con la lista di tutti i richiami di funzione presenti nello script preso in esame.
 :  : PRO.SER Fun="F(EXB;LOSER_06;SCH.LIS) 1(MB;SCP_SCH;[K1])" Cod="00012"

### Le funzioni di una scheda - Esecuzione
In base al nome della scheda passato in K1, viene visualizzata una matrice con la lista di tutti i richiami di funzione presenti nello script preso in esame e il tempo di esecuzione di ogni funzione.
 :  : PRO.SER Fun="F(EXB;LOSER_06;SCH.ESE) 1(MB;SCP_SCH;[K1])" Cod="00013"

### Le funzioni di tutte le schede
Scansione di tutte le schede presenti in SCP_SCH e visualizzazione di una matrice contenente tutti i richiami a funzioni di tutte le schede.
 :  : PRO.SER Fun="F(EXB;LOSER_06;SCH.LIS) 1(MB;SCP_SCH;)" Cod="00014"

 :  : SEZ
LIS            Lista          N
.LIS.LIS        Liste         N                                  EXB TRE
.LIS.ELE        Elementi      N
ADD            Aggiunta       N
.ADD.ELE        Elemento      N                        LIS.ELE
CLR            Pulizia        N
.CLR.LIS        Lista         N                        LIS.LIS
IMP            Importazione   N
.IMP.G40        da £G40       N

 :  : RIG
LIS.LIS
.*TOG.1  Cliente                        CNCLI                F  020
.*TOG.2  Commessa obbligatoria          CM                   O  020
.*TOG.3  Articolo                       AR                   O  020
.LISLIS1 uno                            .VTextAlign             020
.LISLIS2 due                            CNAZI                   020
LIS.ELE
.LISELE1 uno                            .VSet.Load              020
.LISELE2 due                            CM                      020
.LISELE3 tre                                                    020

 :  : LIS
Com.001
.EXB
.EXD
TextAlign
.LEFT           Left
.RIGHT          Right
.CENTER         Center
.TOP            Top
.BOTTOM         Bottom
Set.Load
.D              Differito
.I              Immediato
