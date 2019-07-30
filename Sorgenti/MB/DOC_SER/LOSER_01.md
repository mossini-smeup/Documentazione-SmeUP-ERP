 :  : HEA RESP(GR) STAT(80)
# OBIETTIVO
Fornire le funzioni richieste dalla scheda dei servizi.

# FUNZIONI/METODI
## SER
Restituisce un albero con i servizi disponibili, suddivisi per applicazione.
E' possibile filtrare i servizi restituiti indicando un'applicazione in Oggetto1

## FEM
Restituisce un albero con le funzioni/metodi supportati da un servizio.

## COM
Restituisce un albero con i componenti supportati da una funzione/metodo di un servizio.

## PAR
Restituisce una matrice con i parametri utilizzati da una funzione/metodo di un servizio.

## VAL
Restituisce una matrice con i valori utilizzati da una funzione/metodo di un servizio.
Il codice dell'oggetto 3 ha il formato xxxyyy, dove xxx e yyy sono formate da 3 cifre e indicano l'inizio e la fine dell'elenco dei valori.
Se ad esempio la funzione.metodo ha come gruppo di parametri quelli identificati dal parametro PA10, avrò che se il tipo di oggetto di una domanda è V 002005 andrò a recuparare la lista di valori dal secondo al quinto.
Un esempio di servizio è l'A£SER_03


## OGG
Restituisce una matrice con gli oggetti da passare alla funzione/metodo di un servizio.

## A.x, B.x, C.x, D.x
Funzioni fittizie per la dimostrazione del funzionamento delle autorizzazioni sui servizi (v. scheda

 :  : PRO.SER Cod="A.1.1" Tit="Autorizzazioni A. 1" Fun="F(TRE;LOSER_01;A.1)"

 :  : PRO.SER Cod="A.2.2" Tit="Autorizzazioni A. 2" Fun="F(TRE;LOSER_01;A.2)"

 :  : PRO.SER Cod="A.3.3" Tit="Autorizzazioni A. 3" Fun="F(TRE;LOSER_01;A.3)"

 :  : PRO.SER Cod="A.4.4" Tit="Autorizzazioni A. 4" Fun="F(TRE;LOSER_01;A.4)"

 :  : PRO.SER Cod="B.1.5" Tit="Autorizzazioni B. 1" Fun="F(TRE;LOSER_01;B.1)"

 :  : PRO.SER Cod="B.2.6" Tit="Autorizzazioni B. 2" Fun="F(TRE;LOSER_01;B.2)"

 :  : PRO.SER Cod="B.3.7" Tit="Autorizzazioni B. 3" Fun="F(TRE;LOSER_01;B.3)"

 :  : PRO.SER Cod="B.4.8" Tit="Autorizzazioni B. 4" Fun="F(TRE;LOSER_01;B.4)"

 :  : PRO.SER Cod="C.1.9" Tit="Autorizzazioni C. 1" Fun="F(TRE;LOSER_01;C.1)"

 :  : PRO.SER Cod="C.2.10" Tit="Autorizzazioni C. 2" Fun="F(TRE;LOSER_01;C.2)"

 :  : PRO.SER Cod="C.3.11" Tit="Autorizzazioni C. 3" Fun="F(TRE;LOSER_01;C.3)"

 :  : PRO.SER Cod="C.4.12" Tit="Autorizzazioni C. 4" Fun="F(TRE;LOSER_01;C.4)"

 :  : PRO.SER Cod="D.1.13" Tit="Autorizzazioni D. 1" Fun="F(TRE;LOSER_01;D.1)"

 :  : PRO.SER Cod="D.2.14" Tit="Autorizzazioni D. 2" Fun="F(TRE;LOSER_01;D.2)"

 :  : PRO.SER Cod="D.3.15" Tit="Autorizzazioni D. 3" Fun="F(TRE;LOSER_01;D.3)"

 :  : PRO.SER Cod="D.4.16" Tit="Autorizzazioni D. 4" Fun="F(TRE;LOSER_01;D.4)"

 :  : PRO.SER Cod="SER.ALL.17" Tit="Servizi. Tutti" Fun="F(TRE;LOSER_01;SER.ALL) 1(TA;B£A;-(F;;TAB£A;Applicazione))"

 :  : PRO.SER Cod="SER.DOC.18" Tit="Servizi. Solo i documentati" Fun="F(TRE;LOSER_01;SER.DOC)" Ref="SER.ALL.17"

 :  : PRO.SER Cod="FEM.19" Tit="Funzioni/metodo di un servizio. " Fun="F(TRE;LOSER_01;FEM) 1(V3;ASE;-(O;;V3ASE;Servizio))"

 :  : PRO.SER Cod="COM.20" Tit="Componenti supportati. " Fun="F(TRE;LOSER_01;COM) 1(V3;ASE;-(O;;V3ASE;Servizio)) 2(**;;-(O;;**;Funzione/metodo))"

 :  : PRO.SER Cod="PAR.21" Tit="Parametri. " Fun="F(EXB;LOSER_01;PAR)" Ref="COM.20"

 :  : PRO.SER Cod="VAL.ALL.22" Tit="Valori. Valori Tutti" Fun="F(EXB;LOSER_01;VAL.ALL)" Ref="COM.20"

 :  : PRO.SER Cod="OGG.23" Tit="Oggetti. " Fun="F(EXB;LOSER_01;OGG)" Ref="COM.20"

