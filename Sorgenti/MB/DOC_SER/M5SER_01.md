 :  : HEA RESP(GG) STAT(15)
# OBIETTIVO
Questo servizio consente di costruire l'XML necessario per la compilazione delle schede inerenti
l'M5CMRP.

# FUNZIONI/METODI
## Controllo scenario magazzino da impostare (CPS)
Questa funzione costruisce una matrice contenente informazioni usate per controllare se vanno inserite le informazioni relative a scenario e magazzino oppure possono essere recuperate automaticamente.
La matrice contiene due colonne relative allo scenario e due al magazzino e una relativa ai dati da inserire.
La prima colonna contiene un codice (di un carattere) che identifica la necessità o meno di inserimento dello scenario : 

- 0 :  identifica il fatto che gli scenari sono gestiti e nel database è presente più di uno scenario;
- 1 :  identifica il fatto che gli scenari non sono gestiti;
- 2 :  identifica il fatto che gli scenari sono gestiti, ma nel database è presente un unico scenario oppure non è presente nemmeno uno scenario.

La seconda colonna contiene il codice dell scenario da utilizzare nel caso la colonna precedente contenga i codici 1 o 2.
La terza e la quarta colonna sono analoghe alle prime due ma sono riferite al magazzino. In questo caso non si parla di gestione dello scenario ma di mono/multiplant.
La quinta colonna contiene una stringa ti testo con l'indicazione di cosa di necessario/possibile scegliere tra le informazioni di scenario e magazzino.
Le ultime tre colonne contengono il tipo , il parametro e la descrizione dell'oggetto di rottura.
## Estrazione oggetto di riferimento (OGR)
Questa funzione costruisce un albero con un unico nodo formato dall'oggetto di riferimento (H§OGRF) associato allo scenario passato in input.	
## Estrazione enti (ENT)
Questa funzione costruisce un albero con tutti gli enti associati ad una coppia scenario/magazzino.L'albero è strutturato su due livelli, dove nel primo livello c'è il tipo di ente e nel secondo il codice.
## Estrazione informazioni sulla chiave(I2K)
Questa funzione costruisce una matrice con la chiave del file M5CONS0F corrispondente al codice consiglio (M5) ricevuto in input e con alcune informazioni aggiuntive.
## Elenco degli scenari (SCE)
### Metodo ART
Questa funzione costruisce l'elenco degli scenari presenti nel database associati ad un particolare articolo.
### Metodo ENT
Questa funzione costruisce l'elenco degli scenari presenti nel database associati ad un particolare ente.
## Elenco dei magazzini (MAG)
### Metodo ART
Questa funzione costruisce l'elenco dei magazzini presenti nel database associati ad un particolare scenario e riferiti ad un preciso articolo.
### Metodo ENT
Questa funzione costruisce l'elenco dei magazzini presenti nel database associati ad un particolare scenario e riferiti ad un preciso ente.



 :  : PRO.SER Cod="EST.ACF.1" Tit="Presentazione testuale. Analisi coperture - fabbisogni" Fun="F(EXB;M5SER_01;EST.ACF) 1(M5;;-(O;;M5;Consiglio))"

 :  : PRO.SER Cod="EST.ESG.2" Tit="Presentazione testuale. Esposizione suggerimento" Fun="F(EXB;M5SER_01;EST.ESG)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.IMP.3" Tit="Lista. Impegni" Fun="F(EXB;M5SER_01;LIS.IMP)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.ASS.4" Tit="Lista. Assiemi" Fun="F(EXB;M5SER_01;LIS.ASS)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.COP.5" Tit="Lista. Coperture->Fabbisogni" Fun="F(EXB;M5SER_01;LIS.COP)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.FAB.6" Tit="Lista. Fabbisogni->Coperture" Fun="F(EXB;M5SER_01;LIS.FAB)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.LEG.7" Tit="Lista. Legami" Fun="F(EXB;M5SER_01;LIS.LEG)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.QML.8" Tit="Lista. Quadro multiplant" Fun="F(EXB;M5SER_01;LIS.QML)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="LIS.ROT.9" Tit="Lista. Svluppo ogg.rottura" Fun="F(EXB;M5SER_01;LIS.ROT) 1(TA;M5B;-(F;;TAM5B;Scenario)) 2(TA;MAG;-(F;;TAMAG;Magazzino)) 3(AR;;-(F;;AR;Articolo))"

 :  : PRO.SER Cod="DAP.PIA.10" Tit="Dati articolo/plant. Pianificazione" Fun="F(EXB;M5SER_01;DAP.PIA) 1(M5;;-(F;;M5;Consiglio)) 2(;;-(F;;;Mag./Articolo))"

 :  : PRO.SER Cod="DAP.MAG.11" Tit="Dati articolo/plant. Magazzino" Fun="F(EXB;M5SER_01;DAP.MAG)" Ref="DAP.PIA.10"

 :  : PRO.SER Cod="NAV.E1.12" Tit="Navigazione. Esplosione scalare" Fun="F(EXB;M5SER_01;NAV.E1)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.E2.13" Tit="Navigazione. Esplosione ai mat.base" Fun="F(EXB;M5SER_01;NAV.E2)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.E3.14" Tit="Navigazione. Fabbisogni del livello" Fun="F(EXB;M5SER_01;NAV.E3)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.E4.15" Tit="Navigazione. Esplosione riepilogata" Fun="F(EXB;M5SER_01;NAV.E4)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.I1.16" Tit="Navigazione. Implosione scalare" Fun="F(EXB;M5SER_01;NAV.I1)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.I2.17" Tit="Navigazione. Implosione ai prodotti finiti" Fun="F(EXB;M5SER_01;NAV.I2)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.I3.18" Tit="Navigazione. Coperture del livello" Fun="F(EXB;M5SER_01;NAV.I3)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.I4.19" Tit="Navigazione. Implosione riep.ai finiti" Fun="F(EXB;M5SER_01;NAV.I4)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="NAV.I5.20" Tit="Navigazione. Implosione riep,del livello" Fun="F(EXB;M5SER_01;NAV.I5)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="ANG.NOS.21" Tit="Analisi grafica. Non simula spostamenti" Fun="F(EXB;M5SER_01;ANG.NOS)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="ANG.SIS.22" Tit="Analisi grafica. Simula spostamenti" Fun="F(EXB;M5SER_01;ANG.SIS)" Ref="EST.ACF.1"

 :  : PRO.SER Cod="CPS.23" Tit="Ctr Scenario/magazzino. " Fun="F(EXB;M5SER_01;CPS)"

 :  : PRO.SER Cod="OGR.24" Tit="Oggetto di riferimento. " Fun="F(TRE;M5SER_01;OGR) 1(TA;M5B;-(O;;TAM5B;Scenario))"

 :  : PRO.SER Cod="ENT.25" Tit="Estrazione enti. " Fun="F(TRE;M5SER_01;ENT) 1(TA;M5B;-(O;;TAM5B;Scenario)) 2(TA;MAG;-(O;;TAMAG;Magazzino))"

 :  : PRO.SER Cod="ENT.26" Tit="Estrazione enti. " Fun="F(TRA;M5SER_01;ENT)" Ref="ENT.25"

 :  : PRO.SER Cod="I2K.27" Tit="Chiavi da IDOJ. " Fun="F(EXB;M5SER_01;I2K) 1(M5;;-(O;;M5;Consiglio)) P( MG(-(F;;;Magazzino o mag associato)) NA(-(F;;;Tipo di navigazione)))"

 :  : PRO.SER Cod="SCE.ART.28" Tit="Elenco degli scenari. Associati ad un articolo" Fun="F(TRE;M5SER_01;SCE.ART) 3(AR;;-(O;;AR;Articolo))"

 :  : PRO.SER Cod="SCE.ENT.29" Tit="Elenco degli scenari. Associati ad un ente" Fun="F(TRE;M5SER_01;SCE.ENT) 3(CN;;-(O;;CN;Ente))"

 :  : PRO.SER Cod="MAG.ART.30" Tit="Elenco dei magazzini di uno scenario. Associati ad un articolo" Fun="F(TRE;M5SER_01;MAG.ART) 1(TA;M5B;-(O;;TAM5B;Scenario)) 3(AR;;-(O;;AR;Articolo))"

 :  : PRO.SER Cod="MAG.ENT.31" Tit="Elenco dei magazzini di uno scenario. Associati ad un ente" Fun="F(TRE;M5SER_01;MAG.ENT) 1(TA;M5B;-(O;;TAM5B;Scenario)) 3(CN;;-(O;;CN;Ente))"

