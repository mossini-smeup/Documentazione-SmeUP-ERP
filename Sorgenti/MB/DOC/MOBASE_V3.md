# Sme.App V 3.00 (marzo 2014)
Sme.App rispetto alla versione precendente è caratterizzata da : 
* Piccole revisioni grafiche.
* Dinamica dell'applicazione completamente rivista, si basa ora su script di scheda di Looc.UP.
* Consente non solo la consultazione ma anche la modifica dei dati del nostro ERP.

Sme.App è scaricabile dall'Apple Store.
Sme.App, è disponibile per i dispositivi IOS iphone e ipad.
L'applicazione si presenta in lingua italiana o inglese in funzione della lingua del device.

**Seguono uno screeshot di esempio**

![010](http://localhost:3000/immagini/MOBASE_V3/010.png)
**Una volta scaricata l'applicazione ci si presenta questa videata : **

![009](http://localhost:3000/immagini/MOBASE_V3/009.png)
## Demo Mode

L'ambiente demo **"Demo Mode"** è accessibile senza specificare nessuna credenziale.
Chiunque scarichi l'app potrà accedere all' ambiente demo, al suo interno troverà un documento di aiuto che descrive la dinamica dell'applicazione.

**Segue la prima schermata dell' ambiente demo**

![007](http://localhost:3000/immagini/MOBASE_V3/007.png)
**Segue la schermata di come si presenta lo stesso ambiente in modalità Looc.UP**

![008](http://localhost:3000/immagini/MOBASE_V3/008.png)
**Segue lo script di questa prima schermata**

 :  : TBL Nam="TRE1" Tit="Image List di Scelta" Com="TRE"
   :  : DAT Tip="OG" Par="" Cod="FT" Txt="Fatturato" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_02)"
   :  : DAT Tip="TA" Par="PAG" Cod="" Txt="Portafoglio" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_03)"
   :  : DAT Tip="RR" Txt="Scaduto" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_04)"
   :  : DAT Tip="E1" Txt="Disponibilità" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_05)"
   :  : DAT Tip="CF" Txt="Aiuto" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://www.smeup.com/mobile/aiuto_demo.html))"
   :  : DAT Tip="DO" Txt="Company Profile" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://mobile.smeup.com/demo/images/companyprofile.pdf))"
   :  : DAT Tip="**" Txt="Informazioni su Sme.Up" Fun="F(EXD;*SCO;) 2(MB;SCP_SCH;MODEMO_00) 4(;;DOCHTM) P(HTMURL(http://www.smeup.com/mobile/info.html))"


## Login

Prima di poter accedere tramite Login dovremo aver configurato nella sezione del nostro device "impostazioni/Sme.app" il parametro "WS URL"

Per i tutti i collaboratori interni sarà possibile accedere, tramite login, ai dati reali del proprio ambiente gestionale con le proprie credenziali : 

Fatta la login, la dinamica della navigazione risulta intuitiva.

Trattandosi di dati reali si raccomanda la massima discrezione.


## Cosa dobbiamo sapere per rispondere ai nostri clienti : 

Siamo ora in grado di utilizzare l' applicazione e di farla apprezzare. Possiamo utilizzare le due modalità descritte, disponibili 24 per 7, esclusivamente in modalità "on line". I dati che esponiamo sono forniti dalle nostre "FUN". Quello che  siamo in grado di ottenere attraverso Looc.up, tendenzialmente lo potremo esporre sulla nostra app.
Questa versione supporta i seguenti componenti : 
* Alberi
* Matrici
* Input panel
* sezioni htm

Per approfondimenti vedi il seguente documento : 
- [Sme.App V 3.00 specifiche tecniche](Sorgenti/MB/DOC/MOBASE_V3T)



## NOTA BENE
Alla domanda del cliente che chiede l'utilizzo della app. con i dati del proprio gestionale dobbiamo rispondere che è necessario fare nascere un progetto.

## Il progetto prevede almeno le seguenti attività : 

* analisi dei dati da presentare nell'applicazione;
* selezione delle funzioni Sme.UP e definizione delle implementazioni;
* definizione della sequenza di navigazione;
* definizione dell'infrastruttura;
* realizzazione dell'applicazione in ambiente Looc.up;
* configurazione del server;
* test e collaudo;
* rilascio;


Queste attività sono le medesime che abbiamo sviluppato al nostro interno per quanto detto in precedenza.


