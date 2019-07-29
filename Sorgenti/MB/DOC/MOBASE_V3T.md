# Sme.App V 3.00 (marzo 2014) Specifiche tecniche

Questa versione supporta i seguenti componenti : 
- Alberi
- Matrici
- Input Panel
- Sezioni htm

Per i componenti alberi, input panel e sezioni htm il comportamento di Sme.app è analogo rispetto a Loocup.
Di seguito i dettagli da conoscere per un governo adeguato dei setup di matrice.

**MATRICE**

SETUP  : 
Attributi per la renderizzazione grafica della matrice : 

CellStyle="PSXX|LSXX"
L'attributo cellstyle, indica il layout grafico con cui i campi (al più 4) di una matrice standard di loocup vengono visualizzati all'interno di ogni cella di matrice.

L'attributo può contenere al più 2 valori, il cui prefisso, può essere PS o LS.

PS è il prefisso utilizzato per i layout di cella da visualizzare quando il telefono o tablet si trovano in posizione verticale (portrait syle)

LS è il prefisso utilizzato per i layout di cella da visualizzare quando il telefono o tablet si trovano in posizione orizzontale (landscape syle)

Per quanto riguarda l'intestazione della matrice, assumerà il medesimo PortraitStyle e LandscapeStyle, definito da attributo CellStyle, eccezion fatta per il tipo di font, definito fisso in Bold.

Di seguito un elenco di tutti i valori possibili di PS ed LS  : 

**- CellStyle="PS01"**

Schema campi  :   (4 campi, 2 colonne)


![TEC001](http://localhost:3000/immagini/MOBASE_V3T/TEC001.png)
Esempio IPhone 5  : 

![TEC002](http://localhost:3000/immagini/MOBASE_V3T/TEC002.png)
**- CellStyle="PS02"**

Schema campi  :   (2 campi, 2 colonne)


![TEC003](http://localhost:3000/immagini/MOBASE_V3T/TEC003.png)
Esempio IPhone 5  : 

![TEC004](http://localhost:3000/immagini/MOBASE_V3T/TEC004.png)
**- CellStyle="PS03"**

Schema campi  :   (1 campo, 1 colonna a sx)


![TEC005](http://localhost:3000/immagini/MOBASE_V3T/TEC005.png)
Esempio IPhone 5  : 

![TEC006](http://localhost:3000/immagini/MOBASE_V3T/TEC006.png)

**- CellStyle="PS04"**

Schema campi  :   (2 campi, 1 colonna a sx)


![TEC007](http://localhost:3000/immagini/MOBASE_V3T/TEC007.png)
Esempio IPhone 5  : 

![TEC008](http://localhost:3000/immagini/MOBASE_V3T/TEC008.png)
**- CellStyle="PS05"**

Schema campi  :   (1 immagine, 1 campo, 1 colonna a sx)


![TEC009](http://localhost:3000/immagini/MOBASE_V3T/TEC009.png)
Esempio IPhone 5  : 

![TEC010](http://localhost:3000/immagini/MOBASE_V3T/TEC010.png)
**- CellStyle="PS06"**

Schema campi  :   (1 immagine, 2 campi, 1 colonna a sx)


![TEC011](http://localhost:3000/immagini/MOBASE_V3T/TEC011.png)
Esempio IPhone 5  : 

![TEC012](http://localhost:3000/immagini/MOBASE_V3T/TEC012.png)
**- CellStyle="PS07"**

Schema campi  :   (1 immagine, 4 campi, 2 colonne)


![TEC013](http://localhost:3000/immagini/MOBASE_V3T/TEC013.png)
Esempio IPhone 5  : 

![TEC014](http://localhost:3000/immagini/MOBASE_V3T/TEC014.png)
**- CellStyle="PS08"**

Schema campi  :   (1 campo, 4 colonne)


![TEC015](http://localhost:3000/immagini/MOBASE_V3T/TEC015.png)
Esempio IPhone 5 _7_(attenzione  :  layout altamente sconsigliato su Iphone)  : 

![TEC016](http://localhost:3000/immagini/MOBASE_V3T/TEC016.png)
**- CellStyle="PS09"**

Schema campi  :   (1 immagine 2 campi, 2 colonne)

![TEC017](http://localhost:3000/immagini/MOBASE_V3T/TEC017.png)
Esempio IPhone 5  : 

![TEC018](http://localhost:3000/immagini/MOBASE_V3T/TEC018.png)
**- CellStyle="PS10"**

Schema campi  :   (4 campo, 1 colonna a sx)

![TEC019](http://localhost:3000/immagini/MOBASE_V3T/TEC019.png)
Esempio IPhone 5  : 

![TEC020](http://localhost:3000/immagini/MOBASE_V3T/TEC020.png)
**- CellStyle="PS11"**

Schema campi  :   (1 immagine, 4 campi, 1 colonna a sx)

![TEC021](http://localhost:3000/immagini/MOBASE_V3T/TEC021.png)
Esempio IPhone 5  : 

![TEC022](http://localhost:3000/immagini/MOBASE_V3T/TEC022.png)
A titolo puramente illustrativo, seguono gli stili in versione LS  : 

**- CellStyle="LS01"**

![TEC023](http://localhost:3000/immagini/MOBASE_V3T/TEC023.png)
**- CellStyle="LS02"**

![TEC024](http://localhost:3000/immagini/MOBASE_V3T/TEC024.png)
**- CellStyle="LS03"**

![TEC025](http://localhost:3000/immagini/MOBASE_V3T/TEC025.png)
**- CellStyle="LS04"**

![TEC026](http://localhost:3000/immagini/MOBASE_V3T/TEC026.png)
**- CellStyle="LS05"**

![TEC027](http://localhost:3000/immagini/MOBASE_V3T/TEC027.png)
**- CellStyle="LS06"**

![TEC028](http://localhost:3000/immagini/MOBASE_V3T/TEC028.png)
**- CellStyle="LS07"**

![TEC029](http://localhost:3000/immagini/MOBASE_V3T/TEC029.png)
**- CellStyle="LS08"**

![TEC030](http://localhost:3000/immagini/MOBASE_V3T/TEC030.png)
**- CellStyle="LS09"**

![TEC031](http://localhost:3000/immagini/MOBASE_V3T/TEC031.png)
**- CellStyle="LS010"**

![TEC032](http://localhost:3000/immagini/MOBASE_V3T/TEC032.png)
**- CellStyle="LS011"**

![TEC033](http://localhost:3000/immagini/MOBASE_V3T/TEC033.png)
In mancanza dell'attributo o di uno dei valori dell'attributo, i valori di default definiti sono PS07 ed LS07.

Attributi per la gestione delle immagini

_2_ImgField="nomecolonna" : 
Il valore di questo attributo, indica il nome della colonna che verrà utilizzata per recuperare l'immagine dell'oggetto.

_2_ImgUrl="http://www.smeup.com/immagine.png":
Serve a specificare un'immagine esterna, diretta da utilizzare (indipendentemente dall'oggetto)

_2_ImgUrlCmp="nomecolonna1|nomecolonna2"  : 
L'attributo, indica che il recupero dell'immagine sarà condizionato al confronto tra i due valori dei rispettivi campi nomecolonna1 e nomecolonna2.

Le immagini risultanti saranno  : 

Se valore colonna1 > valore colonna2
![TEC034](http://localhost:3000/immagini/MOBASE_V3T/TEC034.png)
Se valore colonna 1 < valore colonna 2
![TEC035](http://localhost:3000/immagini/MOBASE_V3T/TEC035.png)
Se valore colonna1 = valore colonna 2
![TEC036](http://localhost:3000/immagini/MOBASE_V3T/TEC036.png)
Politica di risalita immagini

1 - per prima cosa viene valutata la presenza dell'attributo ImgUrl (vince su tutto)

2 - seconda scelta è riservata alla presenza dell'attributo ImgUrlCmp

3- terza ipotesi è data dall'icona dell'oggetto.
Qui tuttavia ci possono essere 2 ipotesi

3.1- Icona dell'oggetto specificata in ImgField ha precedenza
3.2- Come seconda ipotesi, utilizzerà, se definita, l'icona standard dell'oggetto a cui fa
       riferimento il 1° campo in ordine , tra quelli definiti per la matrice

NB :  il tipo di immagine recuperata per defaulta è l'icona (ICO) , tuttavia se invece viene definito un ulteriore attributo di setup di matrice,  _2_IconType="IMG" viene recuperata l'immagine dell'oggetto al posto dell'icona

4- ultima ipotesi, se a questo livello non fosse stata trovata alcuna icona, è rappresentata dall'icona di default Sme.Up (logo aziendale in formato 40x40)

**Informazioni di Base per l'attivazione di un'app mobile**

1) Download App da Itunes Store

_2_https://itunes.apple.com/it/app/sme.app/id631578435?mt=8

2) Configurazione Web Service

Dopo aver scaricato ed installato l'app su iPhone o iPad, seguire i seguenti passi  : 


- Impostazioni


![TEC037](http://localhost:3000/immagini/MOBASE_V3T/TEC037.png)

- Selezionare la voce "Sme.App"
- Verificare l'mpostazione del parametro WS URL
Il valore di default del parametro sarà : _2_http://mobile.smeup.com/demo


3) Verifica dei parametri di configurazione/connessione del Web Service

Per verificare i parametri di accesso che il suddetto Web Service utilizza per effettuare la connessione al sistema AS400, aprire una finestra di browser web ed inserire l'URL.

Si aprirà una maschera del tutto simile alla seguente : 

![TEC038](http://localhost:3000/immagini/MOBASE_V3T/TEC038.png)
Selezionare quindi il tasto "Connection Data"

![TEC039](http://localhost:3000/immagini/MOBASE_V3T/TEC039.png)
Nella maschera, verranno visualizzate tutte le informazioni relative alla connessione.

4) Impostazione della scheda di partenza in ambiente Mobile

L'applicazione mobile, in fase di partenza, effettua la seguente chiamata, per recuperare la scheda di partenza definita per l'ambiente corrente. (nell'esempio qui riportato, è l'ambiente D13)

           F(EXB;LOSER_05;LIS.MVA)

Tale chiamata, ritornerà un XML, che l'app mobile interpreterà andando alla ricerca dei seguenti attributi  : 

_2_*SMOBILE
oppure
_2_*SFUNCTION

Il valore recuperato da SMOBILE o SFUNCTION costituirà il nome della scheda di default di partenza per l'ambiente Mobile.

5) Ulteriori personalizzazioni grafiche per il cliente finale

E' possibile sostituire il logo "Bringing Light", con quello del nostro cliente
(se presente un'immagine di nome customer.png in [WS_URL]/images/customer.png.
Dove WS_URL è l'url presente nei settings dell'Applicazione già citati al punto 2 del presente elenco.
L'esepio qui di seguito, sfrutta l'immagine presente in   : 

_2_http://mobile.smeup.com/mobile/images/customer.png

Il prodotto finale, della personalizzazione sarà il seguente  : 
(tralasciamo la qualità delle immagini utilizzate nell'esempio)

![TEC040](http://localhost:3000/immagini/MOBASE_V3T/TEC040.png)![TEC041](http://localhost:3000/immagini/MOBASE_V3T/TEC041.png)
## Analisi della Demo Mobile

Di seguito verrà mostrata l'applicazione utilizzata per la Demo Mobile, fruibile direttamente dal tasto "Demo Mode" della Sme.App.
Verrà inoltre mostrata in parallelo, la stessa applicazione visibile in Looc.UP.
Lo scopo di ciò sarà porre l'accento sul fatto che a parità di script di scheda, si ottengono le stesse visualizzazioni sia sul client Grafico di LoocUP che su uno Smartphone o Tablet.

**MENU INIZIALE (scheda MODEMO_00)**

__Script di scheda__

 :  : G.SEZ Pos(A)
 :  : G.SUB.TRE Tit="*NONE"
 :  : G.SET.TRE Icone="Yes" NodeText="Text"
 :  : G.DIN When="Click" Exec="[Fu]"
 :  : D.FUN.STD F(TRE;B£SER_46;WRK.SCP) 1(MB;SCP_SET;SMA_MOBILE) 2(;;TRE1) INPUT()

 :  : I.SCH Nam(DOCHTM)
 :  : G.SEZ Pos(A)
 :  : G.SUB.HTM Tit="*NONE"
 :  : D.HTM.URL &PA.HTMURL
 :  : I.SCH.END

__XML di scheda __

<?xml version="1.0" encoding="WINDOWS-1252"?>
<Base Testo="SMA_MOBILE Menu mobile - ">
  <Service Titolo1="" Titolo2="SMA_MOBILE Menu mobile" Funzione="F(TRE;B£SER_46;WRK.SCP) 1(MB;SCP_SET;SMA_MOBILE) 2(;;TRE1) INPUT()" Servizio="B£SER_46" TSep="." DSep=","/>
  <Header>
    <Livello Caratteristiche="201"/>
    <Livello Caratteristiche="A01"/>
  </Header>
  <Griglia/>
  <Oggetto Nome="" Tipo="OG" Parametro="" Codice="FT" Testo="Fatturato" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_02)" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="TA" Parametro="PAG" Codice="" Testo="Portafoglio" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_03)" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="RR" Parametro="" Codice="" Testo="Scaduto" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_04)" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="E1" Parametro="" Codice="" Testo="Disponibilità" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_05)" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="CF" Parametro="" Codice="" Testo="Aiuto" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://www.smeup.com/mobile/aiuto_demo.html))" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="DO" Parametro="" Codice="" Testo="Company Profile" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://mobile.smeup.com/demo/images/companyprofile.pdf))" Fld="" Leaf="Yes"/>
  <Oggetto Nome="" Tipo="**" Parametro="" Codice="" Testo="Informazioni su Sme.Up" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://www.smeup.com/mobile/info.html))" Fld="" Leaf="Yes"/>
  <UIPopup>
    <Oggetto Tipo="J1" Parametro="KEY" Codice="*F20" Testo="F20=Gestione Prototipo" Exec="F(EDT;*EDTLET;)1(MB;SCP_SET;SMA_MOBILE)"/>
  </UIPopup>
  <Setup>
    <Program Title="Image List di Scelta" Context=""/>
  </Setup>
</Base>


__Versione LOOC.UP__

![TEC042](http://localhost:3000/immagini/MOBASE_V3T/TEC042.png)
__Versione Mobile__

![TEC043](http://localhost:3000/immagini/MOBASE_V3T/TEC043.png)
**FATTURATO (scheda MODEMO_02)**

Considerazioni sulla scheda del fatturato  : 
Di seguito script di scheda (in evidenza, gli attributi specifici del mobile, già ampiamente discussi all'interno del presente documento)
Nota bene  :  la matrice, può visualizzare al più 4 campi (visualizzati graficamente in base al CellStyle definito)
Quindi sarà importante considerare che le prime 4 colonne dell'attributo Columns, verranno utilizzate.
Nel presente esempio, verranno considerate (evidenziate in azzurro) le colonne  : 
DES001 (Descrizione)
NUM001 (Fatturato)
NUM003 (Scost.%)
NUM002 (Fatturato|anno prec)
Siccome l'attributo CellStyle è stato definito nella demo, come PS07|LS07, i campi verranno visualizzati in questo schema  : 

DESCRIZIONE
FATTURATO

SCOST.%                                                    FATTURATO ANNO
PERC

Come si nota, l'ordine di definizione dell'attributo Columns, implica la scelta del posizionamento delle colonne all'interno della cella mobile.
In una sintassi di questo genere

Columns="COLONNA1|COLONNA2|COLONNA3|COLONNA4"

COLONNA 1
COLONNA 2

COLONNA 3
COLONNA 4

Ultime Note :  all'interno dello script viene utilizzato l'attributo ImgUrlCmp="NUM001|NUM002"
Tale specifica, implica la generazione dell'icona condizionata al raporto tra i due.

Infine, mediante l'attributo Styles, si sono andati a definire gli stili grafici da visualizzare per i font delle colonne specificate.

__Script di scheda__

 :  : S.EXD.LAY Width="50%" Height="50%" PosX="CENTER" PosY="CENTER"
 :  : G.SEZ Pos(1)
 :  : G.SUB.MAT Tit="Fatturato"

 :  : G.SET.MAT ShowHeader="Yes" ShowTotal="Yes" CellStyle="PS07|LS07" Styles="DES001=*BOLD|DES001=*DPBLUE" Columns="DES001|NUM001|NUM003|NUM002|COD001"
ImgUrlCmp="NUM001|NUM002"

 :  : G.DIN When="Click" Exec="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_02) 4(;;DFAT) P(COD1([COD001])) G(NFI)" Focus="Yes"
 :  : D.FUN.STD F(EXB;LOA15_SE;LIS.PAR) 1(;;PR.02.01) 2(;;04) P(PAR2(1)) INPUT()

__XML di scheda__

<?xml version="1.0" encoding="WINDOWS-1252"?>

<UiSmeup Testo="  - ">
  <Service Titolo1="" Titolo2=" " Funzione="F(EXB;LOA15_SE;LIS.PAR) 1(;;PR.02.01) 2(;;04) P(PAR2(1)) INPUT()" Servizio="LOA15_SE" TSep="." DSep=","/>
  <Griglia>
    <Colonna Cod="COD000" Txt="Origine" Tip="" Lun="20" IO="H" Ogg="OG" Dpy="" Fill="" Aut="" ETxt=""/>
    <Colonna Cod="COD001" Txt="Periodo" Tip="" Lun="15" IO="O" Ogg="TAXAB" Dpy="" Fill="" Aut="" ETxt=""/>
    <Colonna Cod="DES001" Txt="Descrizione" Tip="" Lun="30" IO="O" Ogg="" Dpy="" Fill="" Aut="" ETxt=""/>
    <Colonna Cod="NUM001" Txt="Fatturato" Tip="" Lun="20" IO="O" Ogg="NR" Dpy="" Fill="" Aut="" ETxt=""/>
    <Colonna Cod="NUM002" Txt="Fatturato|anno prec" Tip="" Lun="20" IO="O" Ogg="NR" Dpy="" Fill="" Aut="" ETxt=""/>
    <Colonna Cod="NUM003" Txt="Scost.%" Tip="" Lun="20" IO="O" Ogg="NR" Dpy="" Fill="" Aut="" ETxt=""/>
  </Griglia>
  <Righe>
    <Riga Fld="|001|Oggi|27.966,000000|30.334,000000|22.546,000000"/>
    <Riga Fld="|010|Ieri|30.858,000000|34.944,000000|26.465,000000"/>
    <Riga Fld="|020|Mese corrente|34.967,000000|33.680,000000|28.918,000000"/>
    <Riga Fld="|030|Anno corrente|49.998,000000|43.419,000000|39.759,000000"/>
  </Righe>
  <UIPopup/>
</UiSmeup>

__Versione LOOC.UP__

![TEC044](http://localhost:3000/immagini/MOBASE_V3T/TEC044.png)
__Versione Mobile__

![TEC045](http://localhost:3000/immagini/MOBASE_V3T/TEC045.png)