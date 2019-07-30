 :  : HEA RESP(GR) USAG(AS) STAT(80)
# OBIETTIVO
Questo servizio fornisce le funzionalità di base di interrogazione dei costi D5.

## SET'N'PLAY
Da LOOC.up :  "call D5CO03L" da linea di comando, si riempiono i campi del guida e si possono lanciare dalla
bottoniera a dx le funzioni del D5SER_01 che abbiano sufficienti parametri.

La Entry degli oggetti è comune per tutte le funzioni : 
T1,P1 :   Contesto      D$TIPA
K1 :      Codice        D$CODI[rrr
T/P/K2 :  Tema          D$TROT
T/P/K3 :  Chiave 1      D$COD1
T/P/K4 :  Chiave 2      D$COD2
T/P/K5 :  Chiave 3      D$COD3
T/P/K6 :  Data validità D$DTVA

Nei parametri si possono specificare altri input :  riclassifica (RC), valore specifico (VA), lista valori (LV), attributo dell'oggetto (AT).
**NB** :  VA e LV servivano per limitare i valori visualizzati nelle matrici. Ora è più comodo, se la chiamata è
 effettuata all'interno di una scheda, utilizzare il setup della matrice (G.SET.MAT) per indicare quali colonne
 visualizzare.

# FUNZIONI/METODI

## VAL Valori di un oggetto
Vanno specificati almeno un contesto, codice e tema :  restituisce una matrice con i valori presenti, eventualmente
filtrati dalle altre chiavi specificate negli oggetti da 3 a 6.
È possibile indicare se visualizzare i valori di una determinata riclassifica.
Metodo ***BLANKS**
La chiave non deve essere univoca, possono essere mostrati vari record in orizzontale.
È possibile limitare il numero dei valori mostrati specificando un valore singolo o una lista valori.
Metodo **SCH**
Data una chiave univoca del D5COSO presenta una matrice che riassume il costo con i subtotali.

## CFR Confronto tra valori
Metodo **OGG**
È necessario valorizzare la chiave del D5COSO a meno del codice (K1). Viene presentata una matrice
di valori, dove ad ogni riga corrisponde un oggetto diverso con il resto della chiave fissata.
É possibile specificare un attributo degli oggetti da presentare insieme ai valori del D5COSO, per potenziare i
raggruppamenti offerti dalla matrice.
Metodo **ESE**
È necessario valorizzare la chiave del D5COSO, omettendo la data di validità ma specificando un esercizio.
La matrice di valori presentata varia con i mesi dell'esercizio.
Per entrambi i metodi si può limitare il numero dei valori mostrati specificando un valore singolo o una lista valori;
si può anche indicare se visualizzare i valori di una determinata riclassifica.

## SIG Significato dei valori
Dati un contesto e un tema restituisce una matrice con informazioni sui valori del tema.
Possono essere documentati anche i valori di una determinata riclassifica.

## SVI Sviluppo dei temi
Metodo **TRE**
Costruisce un albero con informazioni sui temi valorizzati per l'Oggetto 1 (T1/P1 :  Contesto, K1 :  Codice)
Metodo **TRG**
Associa anche una matrice di valori, e negli oggetti da 2 a 6 è possibile specificare altri campi chiave.

## PER Periodi valorizzati
I primi 3 metodi richiedono una chiave completa a meno della data : 
Metodo **PER**Periodi valorizzati di un esercizio
Dato un esercizio restituisce un albero con i sottoperiodi valorizzati.
Metodo **ESE**
Data una chiave di D5COSO a meno della data (Oggetti da 1 a 5) restituisce un albero con gli esercizi valorizzati.
Metodo **DTA**
Restituisce semplicemente le date valorizzate, indipendentemente dal fatto che siano date, periodi o esercizi.
Metodo **ALL**
Data una chiave qualunque (anche parziale) di D5COSO restituisce un albero con i periodi valorizzati - non distingue tra esercizi e periodi.

## MTP Elenco temi e periodi con possibilità di filtro
Restituisce una matrice (o un albero) con i temi e i periodi attivi, eventualmente filtrati con il codice contesto, il tema e il periodo/data di validità.
ATTENZIONE :  eventuali D$COD1, D$COD2 o D$COD3 specificati vengono ignorati.

## COD Elenco codici attivi di un contesto filtrati per tema e data
Restituisce un albero con tutti i codici attivi per un dato contesto, eventualemente filtrati con il tema e/o il periodo/data di validità.
ATTENZIONE :  eventuali D$COD1, D$COD2 o D$COD3 specificati vengono ignorati.

## CON Elenco dei contesti attivi
Restituisce un elenco dei contesti attivi.

## OGG Espansione dinamica codici D$COD1, D$COD2 e D$COD3
Metodo usato per costruire dinamicamente l'albero dei codici D$COD1, D$COD2 e D$COD3. Richiede in ingresso il contesto, il codice del contesto e il tema. La data/periodo è facoltativa. Se non viene passato il D$COD1 (ed è utilizzato in quel tema) viene costruito un albero contenente la lista dei codici D$COD1 attivi per quel contesto/tema. Se viene passato il D$COD1 ma non il D$COD2 (ed è utilizzato in quel tema) viene costruito un albero contenente la lista dei codici D$COD2 attivi per quel contesto/tema/D$COD1 (l'albero viene costriuito inserendo un padre in modo che possa essere agganciato dinamicamente). Analogamente avviene per il D$COD3.
Se non è stato spedificato il periodo/data di validità (e il parametro DTVA non è presente oppure è diverso da 0), specificando tutti i codici richiesti dal tema viene costruito un albero con i periodi/date di validità (sempre inserendo un nodo padre per consentire l'aggancio dinamico).

 :  : PRO.SER Cod="VAL..1" Tit="Valori di un oggetto. in orizzontale" Fun="F(EXA;D5SER_01;VAL.) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(F;;**;Data/periodo)) P( VA(-(F;;**;Valore specifico)) LV(-(F;;**;Lista valori)) RC(-(F;;**;Riclassifica)))"

 :  : PRO.SER Cod="VAL..2" Tit="Valori di un oggetto. in orizzontale" Fun="F(EXB;D5SER_01;VAL.)" Ref="VAL..1"

 :  : PRO.SER Cod="VAL..3" Tit="Valori di un oggetto. in orizzontale" Fun="F(EXC;D5SER_01;VAL.)" Ref="VAL..1"

 :  : PRO.SER Cod="VAL.SCH.4" Tit="Valori di un oggetto. schema riassuntivo" Fun="F(EXA;D5SER_01;VAL.SCH) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(O;;**;Data/periodo)) P( RC(-(F;;**;Riclassifica)))"

 :  : PRO.SER Cod="VAL.SCH.5" Tit="Valori di un oggetto. schema riassuntivo" Fun="F(EXB;D5SER_01;VAL.SCH)" Ref="VAL.SCH.4"

 :  : PRO.SER Cod="VAL.SCH.6" Tit="Valori di un oggetto. schema riassuntivo" Fun="F(EXC;D5SER_01;VAL.SCH)" Ref="VAL.SCH.4"

 :  : PRO.SER Cod="CFR.OGG.7" Tit="Confronto valori. Lista di valori su più oggetti" Fun="F(EXA;D5SER_01;CFR.OGG) 1(**;;-( ;;**;Solo contesto)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(O;;**;Data/periodo)) P( VA(-(F;;**;Valore specifico)) LV(-(F;;**;Lista valori)) AT(-(F;;OA;Attributo)) RC(-(F;;**;Riclassifica)))"

 :  : PRO.SER Cod="CFR.OGG.8" Tit="Confronto valori. Lista di valori su più oggetti" Fun="F(EXB;D5SER_01;CFR.OGG)" Ref="CFR.OGG.7"

 :  : PRO.SER Cod="CFR.OGG.9" Tit="Confronto valori. Lista di valori su più oggetti" Fun="F(EXC;D5SER_01;CFR.OGG)" Ref="CFR.OGG.7"

 :  : PRO.SER Cod="CFR.ESE.10" Tit="Confronto valori. Lista di valori su un esercizio" Fun="F(EXA;D5SER_01;CFR.ESE) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) P( LV(-(F;;**;Lista valori)) RC(-(F;;**;Riclassifica)) ES(-(F;;TAPER;Esercizio)))"

 :  : PRO.SER Cod="CFR.ESE.11" Tit="Confronto valori. Lista di valori su un esercizio" Fun="F(EXB;D5SER_01;CFR.ESE)" Ref="CFR.ESE.10"

 :  : PRO.SER Cod="CFR.ESE.12" Tit="Confronto valori. Lista di valori su un esercizio" Fun="F(EXC;D5SER_01;CFR.ESE)" Ref="CFR.ESE.10"

 :  : PRO.SER Cod="SIG.13" Tit="Significato dei valori. " Fun="F(EXB;D5SER_01;SIG) 1(**;;-( ;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema))"

 :  : PRO.SER Cod="SIG.14" Tit="Significato dei valori. " Fun="F(TRE;D5SER_01;SIG)" Ref="SIG.13"

 :  : PRO.SER Cod="SVI.TRE.15" Tit="Sviluppo dei temi. Normale" Fun="F(TRE;D5SER_01;SVI.TRE)" Ref="SIG.13"

 :  : PRO.SER Cod="SVI.TRG.16" Tit="Sviluppo dei temi. Con griglia valori" Fun="F(TRG;D5SER_01;SVI.TRG) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(F;;**;Data/periodo))"

 :  : PRO.SER Cod="PER.ESE.17" Tit="Periodi valorizzati. Esercizi" Fun="F(TRE;D5SER_01;PER.ESE) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3))"

 :  : PRO.SER Cod="PER.PER.18" Tit="Periodi valorizzati. Periodi di un esercizio" Fun="F(TRE;D5SER_01;PER.PER) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) P( ES(-(F;;TAPER;Esercizio)))"

 :  : PRO.SER Cod="PER.DTA.19" Tit="Periodi valorizzati. Date valorizzate" Fun="F(TRE;D5SER_01;PER.DTA)" Ref="PER.ESE.17"

 :  : PRO.SER Cod="PER.ALL.20" Tit="Periodi valorizzati. Chiave generica" Fun="F(TRE;D5SER_01;PER.ALL) 1(**;;-(F;;**;Contesto/codice)) 2(TA;D5O**;-(F;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3))"

 :  : PRO.SER Cod="MTP.21" Tit="Elenco temi periodi. " Fun="F(EXB;D5SER_01;MTP) 1(**;;-(F;;**;Contesto/codice)) 2(TA;D5O**;-(F;;TAD5O**;Tema)) 6(**;;-(F;;**;Data/periodo)) P( CODLST(-(F;;**;Informazione da elencare)))"

 :  : PRO.SER Cod="MTP.22" Tit="Elenco temi periodi. " Fun="F(TRE;D5SER_01;MTP)" Ref="MTP.21"

 :  : PRO.SER Cod="COD.23" Tit="Elenco codici attivi. " Fun="F(TRE;D5SER_01;COD) 1(**;;-(F;;**;Contesto/codice)) 2(TA;D5O**;-(F;;TAD5O**;Tema)) 6(**;;-(F;;**;Data/periodo))"

 :  : PRO.SER Cod="CON.24" Tit="Elenco contesti attivi. " Fun="F(TRE;D5SER_01;CON)"

 :  : PRO.SER Cod="OGG.25" Tit="Espansione dinamica D$COD1, D$COD2, D$CO. " Fun="F(TRE;D5SER_01;OGG) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Chiave 1)) 4(**;;-(F;;**;Chiave 2)) 5(**;;-(F;;**;Chiave 3)) 6(**;;-(F;;**;Data/periodo)) P( DTVA(-(F;;**;Visualizza D$DTVA)))"

