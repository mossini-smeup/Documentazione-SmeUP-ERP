 :  : HEA RESP(PARFR) STAT(10)

# OBIETTIVO

Strutturare il lancio di SQL caricati da uno script.
Al costruttore "A25" sono affidate tutte le operazioni di sql.
 Tp : V2
 Pa : LOCOS
 Ogg : A25
Tecnicamente il motore (servizio LOA25_SE) esegue gli statement SQL presenti negli script
del file SCP_SET.
Gli script in oggetto hanno nomenclatura LOA25_xx dove xx=gruppo (CN, AR...)

## STRUTTURA
  Oggetto :      SE (Script di setup)
  Parametro :    GRU.A25 (gruppo)
               SEZ.A25 (sezione)
               SUB.A25 (sottosezione)
  Codice :       C£/CN ... (se param. gruppo)
               C£.LIS/CN.NOM ... (se param. sezione)
               C£.LIS.001/CN.NOM.01 (se param. sottosezione)

# GRUPPI
 Il codice C£.LIS.001, per esempio, si riferisce nella alla forma Gruppo.Sezione.Sottosezione : 
 Tp :   SE
 Par :  GRU.A25
 Ogg :  CN
 lo script in esame è pilotato dal gruppo, quindi LOA25_CN da cui vengono caricate sezioni e
 sottosezioni
# SEZIONI
 Tp :   SE
 Par :  SEZ.A25
 Ogg :  CN.NOM
 lo script in esame è pilotato dal gruppo, quindi LOA25_CN da cui vengono caricate le
 sottosezioni della sezione NOM.
  :  : SEZ Cod="NOM" ed eseguito lo statement del tag  :  : A25.ESE SQL(SELECT * ....)
# SOTTOSEZIONI
 Tp :   SE
 Par :  SUB.A25
 Ogg :  CN.NOM.01
 lo script in esame è pilotato dal gruppo, quindi LOA25_CN da cui viene caricata la
 sottosezione specifica 01
  :  : SEZ Cod="NOM" Txt="Comuni"
  :  : SUB Cod="01" ed eseguito lo statement del tag  :  : A25.ESE SQL(SELECT * ....)

## SINTASSI
La sintassi per l'esecuzione di un sql è la seguente : 
F(EXD;*SCO;) 1(;;01.A01.07) 2(MB;SCP_SCH;LOA25) 4(;;SCH_ESE) P(PG(EXB))
Dove : 
01.A01.07 -> Gruppo.Sezione.Sottosezione in cui compare lo statement SQL
EXB, REP, EXC -> output su matrice, report, excel

A fronte di quanto sopra quindi, volendo per esempio produrre un report con i dati
caricati da un SQL di gruppo CN (quindi sql contenuti in LOA25_CN) nella  sezione A01,
sottosezione 02 : 
F(EXD;*SCO;) 1(;;CN.A01.02) 2(MB;SCP_SCH;LOA25) 4(;;SCH_ESE) P(PG(REP))

E' possibile inoltre fornire schemi e filtri : 
 :  : SUB Cod="08" Txt="V5STAT"
 :  : A25.ESE SQL(SELECT * FROM V5STAT0F) FIL(V5STAT0F) Q3(E/*JOB) Q2(T/DFT)

##  Proprietà del tag  :   : A25.ESE
 :  : PAR L(TAB)
SQL|Istruzione SQL di selezione da eseguire
FIL|File di riferimento per l'applicazione del filtro Q3 o dello schema Q2
Q3|Codice del filtro da applicare (comunemente E/*JOB)
Q2|Codice dello schema da applicare
MDV|Codice della memorizzazione salvata con UP SQL
NRW|Numero di righe della paginazione iniziale


# VISTE
Una particolare attenzione va rivolta alla API standard £IVD (VISTE).
Il motore LOA25 è infatti in grado di utilizzare l'API in oggetto per eseguire
interrogazioni inerenti agli oggetti SmeUp, attraverso l'interfaccia fornita da £IVD.

Nella fattispecie la funzione : 
 :  : A25.ESE SQL(SELECT * FROM BRENTI0F) FIL(_OCNCLI) Q3(E/*JOB)
è in grado di estrarre i record dell'oggetto CNCLI, secondo la SELECT  memorizzata
nel filtro _OCNCLI risolto dalla £IDV, nel caso specifico : 

Input
  Funzione               Verifica
  Metodo                 Esistenza
  Tipo
  Codice      _OCNCLI
Output
  Descrizione Cliente
  File        BRENTI0F
  Libreria    SMEUP_DAT
  Tracciato   F-BRENTI0F
  Codice  ID  E§CRAG
  Descr.  ID  E§RAGS
  Assunto ID  E§TRAG
  Where       E§TRAG ='CLI' AND E§DINV<=20121003 AND E§DFNV>=20121003
  Select      *

Requisiti minimi per poterlo utilizzare DEV >= 3.x

