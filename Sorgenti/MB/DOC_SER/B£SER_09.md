 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Questo servizio (che emette una matrice) partendo da un oggetto gestisce : 
## Numeri dell'oggetto (come l'opzione 8 delle funzioni dell'oggetto)
Permette di gestirlo come elenco con rottura per titolo di riclassifica 1, oppure come tabella con colonne riclassifica 1, riclassifica 2, significato valore e valore.
In entrambi i casi posso visualizzare tutti i valori o solamente quelli valorizzati.
Sono ereditate dalla G37 le autorizzazioni a gruppi di valori in fase di visualizzazione.
## Scheda Parametri dell'oggetto
Ritorna una matrice che mostra la scheda parametri di un oggetto, recuperando la categoria parametri dall'oggetto stesso (come i parametri per tipo nelle funzioni oggetto).
E' possibile passare nei parametri (tag TPRC elemento TA C£E) una categoria specifica alternativa, per visualizzare una particolare scheda parametri.
Con 2 metodi differenti è possibile visualizzare tutta la scheda parametri oppure solamente quelli valorizzati.
## Scheda Attributi dell'oggetto
Ritorna una matrice che mostra la scheda attributi di un oggetto.
Gli attributi possono essere filtrati in tre differenti modi : 
- Impostando un limite iniziale e/o finale
  es. per visualizzare solo gli OAV che iniziano per J
  LII(J) LIF(J99)
- Elencando direttamente i codici degli OAV che si vogliono vedere
  es.
  L01(I/05) L02(I/03) L03(J/A01)
- Impostando la categoria cui l'OAV deve appartenere per essere visualizzato
  GRU(XXX)
- Impostando il gruppo cui l'OAV deve appartenere per essere visualizzato
  CAT(XXX)
 :  : PRO.SER Cod="NUM.ELE.1" Tit="Numeri dell'oggetto. Elenco a rottura Ricl.1 (tutti i valori" Fun="F(EXB;B£SER_09;NUM.ELE)"

 :  : PRO.SER Cod="NUM.ELE.2" Tit="Numeri dell'oggetto. Elenco a rottura Ricl.1 (tutti i valori" Fun="F(EXC;B£SER_09;NUM.ELE)"

 :  : PRO.SER Cod="NUM.EL0.3" Tit="Numeri dell'oggetto. Elenco a rottura Ricl.1 (solo valorizza" Fun="F(EXB;B£SER_09;NUM.EL0)"

 :  : PRO.SER Cod="NUM.EL0.4" Tit="Numeri dell'oggetto. Elenco a rottura Ricl.1 (solo valorizza" Fun="F(EXC;B£SER_09;NUM.EL0)"

 :  : PRO.SER Cod="NUM.DET.5" Tit="Numeri dell'oggetto. Ricl.1, Ricl.2, Sign., (tutti i valori)" Fun="F(EXB;B£SER_09;NUM.DET)"

 :  : PRO.SER Cod="NUM.DET.6" Tit="Numeri dell'oggetto. Ricl.1, Ricl.2, Sign., (tutti i valori)" Fun="F(EXC;B£SER_09;NUM.DET)"

 :  : PRO.SER Cod="NUM.DE0.7" Tit="Numeri dell'oggetto. Ricl.1, Ricl.2, Sign., (solo valorizzat" Fun="F(EXB;B£SER_09;NUM.DE0)"

 :  : PRO.SER Cod="NUM.DE0.8" Tit="Numeri dell'oggetto. Ricl.1, Ricl.2, Sign., (solo valorizzat" Fun="F(EXC;B£SER_09;NUM.DE0)"

 :  : PRO.SER Cod="PAR.DET.9" Tit="Scheda Parametri. tutti i parametri" Fun="F(EXB;B£SER_09;PAR.DET) P( TPRC(-(F;;TAC£E;Categoria Forzata Specifica)))"

 :  : PRO.SER Cod="PAR.DET.10" Tit="Scheda Parametri. tutti i parametri" Fun="F(EXC;B£SER_09;PAR.DET)" Ref="PAR.DET.9"

 :  : PRO.SER Cod="PAR.DE0.11" Tit="Scheda Parametri. solo i parametri valorizzati" Fun="F(EXB;B£SER_09;PAR.DE0)" Ref="PAR.DET.9"

 :  : PRO.SER Cod="PAR.DE0.12" Tit="Scheda Parametri. solo i parametri valorizzati" Fun="F(EXC;B£SER_09;PAR.DE0)" Ref="PAR.DET.9"

 :  : PRO.SER Cod="OAV.DET.13" Tit="Scheda oav. tutti gli attributi" Fun="F(EXB;B£SER_09;OAV.DET) 1(OG;;-(O;;OG;Oggetto)) P( LII(-(F;;**;Limite inferiore)) LIF(-(F;;**;Limite superiore)) GRU(-(F;;**;Gruppo)) CAT(-(F;;**;Categoria)) L01(-(F;;**;Attributo 1)) L02(-(F;;**;Attributo 2)) L03(-(F;;**;Attributo 3)) L04(-(F;;**;Attributo 4)) L05(-(F;;**;Attributo 5)) L06(-(F;;**;Attributo 6)) L07(-(F;;**;Attributo 7)) L08(-(F;;**;Attributo 8)) L09(-(F;;**;Attributo 9)) L10(-(F;;**;Attributo 10)) L11(-(F;;**;Attributo 11)) L12(-(F;;**;Attributo 12)) L13(-(F;;**;Attributo 13)) L14(-(F;;**;Attributo 14)) L15(-(F;;**;Attributo 15)) L16(-(F;;**;Attributo 16)) L17(-(F;;**;Attributo 17)) L18(-(F;;**;Attributo 18)) L19(-(F;;**;Attributo 19)) L20(-(F;;**;Attributo 20)))"

 :  : PRO.SER Cod="OAV.DET.14" Tit="Scheda oav. tutti gli attributi" Fun="F(EXC;B£SER_09;OAV.DET)" Ref="OAV.DET.13"

 :  : PRO.SER Cod="OAV.DE0.15" Tit="Scheda oav. solo gli attributi valorizzati" Fun="F(EXB;B£SER_09;OAV.DE0)" Ref="OAV.DET.13"

 :  : PRO.SER Cod="OAV.DE0.16" Tit="Scheda oav. solo gli attributi valorizzati" Fun="F(EXC;B£SER_09;OAV.DE0)" Ref="OAV.DET.13"

 :  : PRO.SER Cod="OAV.DEF.17" Tit="Scheda oav. tutti gli attributi (solo colonne dati" Fun="F(EXB;B£SER_09;OAV.DEF) 1(OG;;-(O;;OG;Oggetto)) P()"

 :  : PRO.SER Cod="OAV.DEF.18" Tit="Scheda oav. tutti gli attributi (solo colonne dati" Fun="F(EXC;B£SER_09;OAV.DEF)" Ref="OAV.DEF.17"

 :  : PRO.SER Cod="OAV.MAT.01" Tit="Scheda oav. attributi su una riga - significato oav"  Fun="F(EXC;B£SER_09;OAV.MAT) 1(OG;;-(O;;OG;Oggetto))" Ref="OAV.MAT.01"

 :  : PRO.SER Cod="OAV.MAT.02" Tit="Scheda oav. attributi su una riga - dettaglio (codice e descriz.)" Fun="F(EXC;B£SER_09;OAV.MAT) 1(OG;;-(O;;OG;Oggetto))  P(Det(*))" Ref="OAV.MAT.02"

 :  : PRO.SER Cod="OAV.MAT.03" Tit="Scheda oav. attributi su una riga - dettaglio (codice)" Fun="F(EXC;B£SER_09;OAV.MAT) 1(OG;;-(O;;OG;Oggetto))  P(Det(C))" Ref="OAV.MAT.03"

 :  : PRO.SER Cod="OAV.MAT.04" Tit="Scheda oav. attributi su una riga - dettaglio (descrizione)" Fun="F(EXC;B£SER_09;OAV.MAT) 1(OG;;-(O;;OG;Oggetto))  P(Det(D))" Ref="OAV.MAT.04"
