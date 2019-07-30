 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Attraverso questo servizio è possibile lanciare le elaborazioni previste relative ai viaggi. Esse
si articolano nel seguente modo : 
## VIA Funzioni su Viaggio
I vari metodi previsti permettono di ritornare matrici di dati relativi al singolo viaggio : 
### . RIC - Richieste
Elenco delle richieste di movimentazione che compongono il viaggio
### . RIG - Righe
Elenco delle righe delle richieste di movimentazione che compongono il viaggio
### . DOC - Documenti
Elenco dei documenti che hanno originato il viaggio
### . DES - Destinatari
Elenco dei destinatari del viaggio
### . SPE - Spedizioni
Elenco delle bolle originate del viaggio
### . RDO - Righe Documento Aperte
Elenco delle righe di documento aperte legate agli enti destinatari del viaggio con data
consegna inferiore rispetto alla data partenza prevista del viaggio.
## STA Statistiche
Tramite questa funzione è possibile elaborare delle statistiche sui viaggi
### . NRS - Numeri su Spedizionieri
Permette di distribuire uno dei numeri dei viaggi sugli spedizionieri. Per questo
metodo sono previsti due parametri specifici : 
- PE che identifica il periodo che si vuole prendere in considerazione per la statistica
- NR che identifica il numero che si vuole utilizzare
## APE Viaggi Aperti
I vari metodi legati alla funzione permettono di ritornare i dati in formato matriciale
aventi per oggetto non il singolo viaggio, ma tutte le richieste di movimentazione aperte
con un certo stato. Il fine sarebbe quello di avere una serie di servizi che permettano
di monitorare la preparazione dei viaggi. I vari metodi si possono dividere in due
sottogruppi :  i metodi di distribuzione e non. I primi distribuiscono il n° dei viaggi
per una certa caratteristica dei viaggi, mentre i secondi restituisco l'insieme di dati
di tutti i viaggi che rientrano nel gruppo selezionato.
## Significato dei parametri
 :  : PAR L(TAB)
Metodo|Parametro|Valore|Significato


 :  : PRO.SER Cod="VIA.RIC.1" Tit="Viaggio. Richieste" Fun="F(EXB;V5SER_03;VIA.RIC) 1(VG;;-(O;;VG;Viaggio))"

 :  : PRO.SER Cod="VIA.RIG.2" Tit="Viaggio. Righe" Fun="F(EXB;V5SER_03;VIA.RIG)" Ref="VIA.RIC.1"

 :  : PRO.SER Cod="VIA.DOC.3" Tit="Viaggio. Documenti" Fun="F(EXB;V5SER_03;VIA.DOC)" Ref="VIA.RIC.1"

 :  : PRO.SER Cod="VIA.DES.4" Tit="Viaggio. Destinatari" Fun="F(EXB;V5SER_03;VIA.DES)" Ref="VIA.RIC.1"

 :  : PRO.SER Cod="VIA.SPE.5" Tit="Viaggio. Spedizioni" Fun="F(EXB;V5SER_03;VIA.SPE)" Ref="VIA.RIC.1"

 :  : PRO.SER Cod="VIA.RDO.6" Tit="Viaggio. Righe Documento Aperte" Fun="F(EXB;V5SER_03;VIA.RDO)" Ref="VIA.RIC.1"

 :  : PRO.SER Cod="STA.NRS.7" Tit="Statistiche. Numeri su Spedizionieri" Fun="F(EXB;V5SER_03;STA.NRS) P( PE(-(F;;**;Periodo)) NR(-(F;;NR;Numero Viaggio)))"

 :  : PRO.SER Cod="STA.NRS.8" Tit="Statistiche. Numeri su Spedizionieri" Fun="F(EXA;V5SER_03;STA.NRS)" Ref="STA.NRS.7"

 :  : PRO.SER Cod="APE.DES.9" Tit="Viaggi Aperti. Destinazioni" Fun="F(EXB;V5SER_03;APE.DES) 1(TA;B£WDM;-(O;;TAB£WDM;Livello))"

 :  : PRO.SER Cod="APE.PCK.10" Tit="Viaggi Aperti. Picking List" Fun="F(EXB;V5SER_03;APE.PCK)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.VIA.11" Tit="Viaggi Aperti. Viaggi" Fun="F(EXB;V5SER_03;APE.VIA)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.SPE.12" Tit="Viaggi Aperti. Spedizioni" Fun="F(EXB;V5SER_03;APE.SPE)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DOC.13" Tit="Viaggi Aperti. Documenti" Fun="F(EXB;V5SER_03;APE.DOC)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DST.14" Tit="Viaggi Aperti. Distribuzione per stato" Fun="F(EXB;V5SER_03;APE.DST)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DST.15" Tit="Viaggi Aperti. Distribuzione per stato" Fun="F(EXA;V5SER_03;APE.DST)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DSP.16" Tit="Viaggi Aperti. Distribuzione per spedizioniere" Fun="F(EXB;V5SER_03;APE.DSP)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DSP.17" Tit="Viaggi Aperti. Distribuzione per spedizioniere" Fun="F(EXA;V5SER_03;APE.DSP)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DEV.18" Tit="Viaggi Aperti. Distribuzione per evasione" Fun="F(EXB;V5SER_03;APE.DEV)" Ref="APE.DES.9"

 :  : PRO.SER Cod="APE.DEV.19" Tit="Viaggi Aperti. Distribuzione per evasione" Fun="F(EXA;V5SER_03;APE.DEV)" Ref="APE.DES.9"

