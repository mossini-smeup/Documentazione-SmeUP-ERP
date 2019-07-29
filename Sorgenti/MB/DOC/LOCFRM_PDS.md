# Il setup del PDF
La generazione del documento PDF, sia esso di documentazione piuttosto che di scheda, necessità di essere configurabile in alcuni dei suoi aspetti.
Le due macro-categorie che sono state definite sono :  gli stili (**STYLES**) e il setup della creazione (**PRINT**)
Questi due aspetti del setup devono muoversi parallelamente ed indipendentemente ed entrambi devono avere tre differenti _9_livelli di collocazione.
Per_9_ livello di collocazione si intende il momento in cui le informazioni relative al setup giungono al generatore del PDF.

I due setup possono : 

- giungere contestualmente al XML ottenuto a fronte del lancio della funzione di generazione (come già accade per i PDF della scheda quando siano presenti specifiche _r_S.FRM).
- essere ottenuti tramite l'esecuzione di una funzione specifica di richiesta setup ( il cui riferimento è contenuto nel XML ottenuto a fronte del lancio della funzione di generazione nella sezione predisposta sotto _r_Setup/Program/FRM).
- essere reperiti in un file di configurazione a scelta ( il cui riferimento è contenuto nel XML ottenuto a fronte del lancio della funzione di generazione nella sezione predisposta sotto _r_Setup/Program/FRM).

Se non viene sfruttata nessuna di queste possibilità il generatore accederà ai files di configurazione di default presenti nella installazione.
Se per qualche motivo anche questi sono irreperibili il generatore supporterà dei valori di default cablati a codice.

## Setup contestuale al XML dei dati del servizio
Nel caso il setup venga fornito contestualmente ai dati del servizio il nodo di setup, come avviene già per le specifiche _r_S.FRM, arriverà direttamente sotto la root : 
>< UiSmeup >
< Setup >
< Program >
< FRM where="inside" >
...__Specifiche di setup come di seguito riportate per i due casi** **PRINT** e **STYLES** ...
< /FRM >
< /Program >
< /Setup >

...__Dati relativi al servizio richiesto__...

< /UiSmeup >

## Funzione di richiesta setup
Nel caso venga attivata la possibilità di richiedere un setup tramite un servizio specifico, quest'ultimo dovrà restituire un XML di questo tipo : 
>< UiSmeup >
< Setup >
< Program >
< FRM where="exec" Exec="funzione per reperire il setup">
... Specifiche di setup come di seguito riportate per i due casi **PRINT** e **STYLES**
< /FRM >
< /Program >
< /Setup >
< /UiSmeup >

## Setup reperito da file di configurazione
Nel caso del setup della creazione (**PRINT**)
>< UiSmeup >
< Setup >
< Program >
< FRM where="file" Exec="percorso del file" >
< /FRM >
< /Program >
< /Setup >
< /UiSmeup >

## Quando entra in funzione il gestore del setup

 T(L'elaborazione di un setup avverrà in tre differenti casi : )
- Nel caso venga richiesto un PDF di un file di documentazione **F(FRM;JATRE_34C;DOC)**.
- Nel caso si richieda un PDF di una scheda **F(FRM;*SCO;)**.
- Nel caso ci sia una sezione HTM in una scheda che faccia riferimento ad un file di documentazione con un setup, eclusivamente di stile (**STYLES**), differente da quello della scheda.


### Setup del PDF di un file di documentazione
Quando si richiederà un PDF di un file di documentazione attraverso una F(FRM;JATRE_34C;DOC) verrà cercato l'elemento _r_Setup/Program/FRM da cui si estrarranno le categorie di informazioni presenti. Le altre per completare il setup della stampa verranno prese dal file di default _9_setupdocprint.xml. Se neppure il file di default viene trovato, verrà applicato il default cablato. Le informazioni sugli stili verranno cercate nell'elemento **STY** dove ci sarà il riferimento a dove reperire il setup degli stili. Se non viene trovato il riferimento si cercherà il file di default _9_setupdocprint.xml. Se neppure il file di default non viene trovato, verrà applicato il default cablato.

### Setup del PDF di una scheda.
Quando si richiederà un PDF di una scheda F(FRM;*SCO;) verrà cercato l'elemento _r_Setup/Program/FRM da cui si estrarranno le categorie di informazioni presenti. Le altre per completare il setup della stampa verranno prese dal file di default _9_setupdocprint.xml. Se neppure il file di default viene trovato, verrà applicato il default cablato. Le informazioni sugli stili verranno cercate nell'elemento **STY** dove ci sarà il riferimento a dove reperire il setup degli stili. Se non viene trovato il riferimento si cercherà il file di default _9_setupdocprint.xml. Se neppure il file di default non viene trovato, verrà applicato il default cablato.

### Setup di una sezione HTM all'interno del PDF di una scheda
Se nel corso della generazione del PDF di una scheda si incontra una sezione HTM all'interno della quale viene visualizzato un file di documentazione, quest'ultimo, relativamente alle informazioni di stile può avere una configurazione specifica che verrà cercata come se si trattasse della stampa del singolo file di documentazione.

## Il setup degli stili (STYLES)
 Racchiude gli stili dei PDF
attributi gestiti : 
>where :  dove reperire le informazioni sullo stile (inside|exec|file)
>Exec :  funzione da eseguire nel caso che l'attributo where sia valorizzato a "file" per reperire il setup in questione. Il servizio dovrà tornare un XML che abbia come root l'elemento style stesso
  < styles where="inside" Exec="" >

### Sezione fonts
Definisce i tipi di font riconosciuti : 
attributi gestiti : 
>name :  nome del tipo di font definito
>fontname :  nome del font da usare
>dim :  dimensione del font
>style :  stile del font (bold|normal|italic|strikethru)
>color :  colore nella codifica Loocup RxxxGxxxBxxx
>< fonts >
 < font name="00" fontname="Tahoma" dim="26" style="bold" color="R100G100B100"/ >
< /fonts >

### Sezione texts
Definisce le tipologie di testo (frasi) riconosciute : 
attributi gestiti : 
>name :  tipologia di frase definita
>font :  nome del tipo di font precedentemente definito.
>leading :  interlinea
_N.B._ :  per poter definire uno stile di testo che gestisce il default del documento va definito un par con name="DFT"
>< texts >
 < testo name="DFT" leading="12" font="DFT"/ >
 < testo name="TSEC" leading="27" font="TSEC"/ >
< /texts >

### Sezione pars
Definisce i tipi di tag PAR gestiti : 
attributi gestiti : 
>name :  tipo di PAR cui fa riferimento. se PAR è seguito da L è una lista, T è una tabella, X è un testo. La copia di numeri che segue indica la L() del PAR, quindi PARL01 indica una un paragrafo Lista con L(01).
>type :  è probabilmente ridondante e devo valutarne l'uso.
>align :  indica l'allineamento del testo (left, right, justify i valori ammessi)
>lf :  indica come gestire l'a capo (before e after sono i valori ammessi). Before forza un a capo prima del paragrafo, after lo forza dopo. Per il momento non è ancora supportato.indent :  indica l'indentazione del tipo di paragrafo. Se l'allineamento è a destra (right) l'indentazione è destra, altrimenti (left o justify) l'indentazione è sinistra
testo :  nome del tipo di testo precedentemente definito.
_N.B._ :  per poter definire uno stile di paragrafo che gestisce il default del documento va definito un par con type="dft"
>< pars >
 < par type="list" align="left" lf="after" testo="DFT"/ >
 < par type="list" format="01" align="left" lf="after" testo="PAR1"/ >
 < par type="list" format="02" align="left" testo="PAR2"/ >
 < par type="list" format="03" align="left" lf="after" testo="PAR3"/ >
 < par type="table" align="left" lf="before" testo="PAR1"/ >
 < par type="table" format="01" align="left" lf="after" testo="PAR1"/ >
 < par type="table" format="02" align="left" testo="PAR2"/ >
 < par type="table" format="03" align="left" lf="after" testo="PAR3"/ >
 < par type="text" align="justify" lf="after" testo="DFT"/ >
 < par type="text" format="01" align="justify" lf="after" testo="PAR1"/ >
 < par type="text" format="02" align="left" lf="after" indent="20" testo="PAR2"/ >
 < par type="text" format="03" align="justify" lf="after" testo="PAR3"/ >
 < par type="text" format="04" align="left" lf="after" indent="35" testo="PAR4"/ >
 < par type="dft" align="left" lf="after" indent="20" testo="DFT"/ >
< /pars >

### Come funzione il setup degli stili
La configurazione degli stili permette di definire la categoria dei __fonts__ che, come precedentemente esposto, fornisce gli elementi per caratterizzare un font.
Su tale categoria si basa una seconda famiglia (__texts__) di elementi i testi. Qui è possibile definire i tipi di testo che saranno utilizzati dal generatore e che si caratterizzano per il font usato e l'interlinea. Se il generatore trova un tag T02, cercherà negli elementi __texts** il __testo** di nome **T01**. Se lo trova userà la definizione in esso contenuta applicandola al tag, altrimenti cercherà il __testo** **DFT**. L'ultima categoria presente e quella dei __pars** che rappresenta i **PAR**. I  **PAR**  sono una struttura complessa con diverse chiavi di definizione, Possono essere liste numerate, liste puntate, liste letterali, tabelle e testi e tutte possono avere stili che vanno dallo 01 allo 04. Di conseguenza un elemento di definizione dei __par__ deve definire tutti questi attributi, come precedentemente riportato. Quando il generatore trova un tag __PAR__ analizza la L e sceglie se si tratta di testo (valore **text**), di tabella (valore **table**) o di lista (valore **list**). Poi prende in considerazione la F e vede se prendere il format 01, 02, 03, 04. Una volta identificato vede anche l'allineamento ed il tipo di testo da utilizzare.

## Il setup del documento generato (PRINT)

Racchiude il setup di generazione del documento
attributi gestiti : 
>where :  dove reperire le informazioni sullo stile (inside|exec|file)
>Exec :  funzione da eseguire nel caso che l'attributo where sia valorizzato a "file" per reperire il setup in questione. Il servizio dovrà tornare un XML che abbia come root l'elemento print stesso
>show :  visualizza o meno il setup di generazione del documento (yes|no)
>< FRM where="inside" Exec="" show="yes" >
 < FMT Livelli="001" AllInOne="Si" OnlyXml="No" Notransform="No" NewLayoutType="No"/ >
 < DOC Foglio="A4" Orientamento="V" PagXFog="1" TMargin="070" BMargin="070" LMargin="040" RMargin="040" NoColor="No" Legenda="No" NumerSect="No" ShowSet="Yes" PathDir="cartella destinazione" NameFile="nome.pdf"/ >
 < COV Copertina="Si" InfoInCover="No" ColoreSfondoCop="R204G255B255" ColoreTestoCop="R051G051B051" TestoCov="[*USER]-[*DATE]"/ >
 < IDX Indice="No" ColoreTitoloInd="R255G204B204" ColoreTestoInd="R153G102B000"/ >
 < HEA PagH="Yes" ImgH="percorso immagine.jpg" TestoH="[*USER]"/ >
 < FOO PagF="Yes" PagFTot="Yes" ImgF="percorso immagine.jpg" TestoF="PIEDE"/ >
 < MOD SplitTable="No"/ >
 < LAY Schema=""/ >
 < STY Stile=".\setupdocstyle.xml"/ >
< /FRM >

### Sezione FTM
Sezione con gli attributi che definiscono il formato del documento.
_Attributi gestiti_ : 
>Livelli :  richiede il livelli di riscorsione nell'esplosione  di sottoschede o documenti collegati.
>AllInOne** :  crea un PDF unico includendo riferimento **DEC** esterni.
>OnlyXml :  Visualizza solo l'xml che è giunto dall'AS400.
>NoTransform :  Il contenuto del PDF sarà lo script stesso.
>NewLayoutType :  _B_specifica non più utilizzata.

### Sezione DOC
Sezione con gli attributi che definiscono la struttura del documento
_Attributi gestiti_ : 
>Foglio :  le dimensioni del documento.
>Orientamento :  orizzontale o verticale.
>PagXFog :  numenro di pagine per foglio.
>TMargin :  margine alto.
>BMargin :  margine basso.
>LMargin :  margine sinistro.
>RMargin :  margine destro.
>Legenda :  generazione della legenda dei colori a fine documento. Ben presto _B_specifica non più utilizzata.
>NoColor :  PDF generato in scala di grigi.
>NumerSect :  Numeratore sulle sezioni create nel PDF.
>ShowSet :  _B_specifica non più utilizzata.
>PathDir :  cartella dove generare il pdf.
>NameFile :  nome del file pdf da creare.

### Sezione COV
Sezione con gli attributi che definiscono la copertina.
_Attributi gestiti_ : 
>Copertina :  presenza della copertina.
>InfoInCover :  informazioni tecniche relativamente al file stampato in copertina.
>ColoreSfondoCop :  colore di sfondo della copertina.
>ColoreTestoCop :  colore del testo della copertina.
>TestoCov :  testo della copertina.

### Sezione IDX
Sezione con gli attributi che definiscono l'indice del documento
_Attributi gestiti_ : 
>Indice :  presenza dell'indice.
>ColoreTitoloInd :  colore dei titoli dell'indice.
>ColoreTestoInd :  colore dei testi dell'indice.

### Sezione HEA
Sezione con gli attributi che definiscono la presenza e la struttura degli header di pagina
_Attributi gestiti_ : 
>PagH :  indicatore di pagina.
>ImgH :  logo nel header.
>TestoH testo del header.

### Sezione FOO
Sezione con gli attributi che definiscono la presenza e la struttura dei footer di pagina
_Attributi gestiti_ : 
>PagF :  indicatore di pagina.
>PagFTot :  indicatore del totale di pagine.
>ImgF :  logo nel footer.
>TestoF :  testo nel footer.

### Sezione MOD
Sezione con gli attributi che definiscono le impostazioni specifiche dei moduli che si presenteranno nel documento
_Attributi gestiti_ : 
>SplitTable :  dividi le matrici grandi su più fogli anche orizzontalmente.

### Sezione LAY
Sezione con gli attributi che definiscono le impostazioni del file di script del layout della stampa spool
_Attributi gestiti_ : 
>Schema :  membro del file SCP_SPL.

### Sezione STY
Sezione con gli attributi che definiscono il link agli stili.
_Attributi gestiti_ : 
>Stile :  link al file di stile che contiene gli styles o alla F per reperirlo..

## Cosa non prevede il setup
 T(Fra le cose che il setup non prevede vi sono : )
- La possibilità di estendere i tag conosciuti dal motore di generazione, vale a dire che se si decide di creare un nuovo tag (T08), si può inserire fra gli elementi di configurazione un elemento **testo** con attributo name="T08" e definizione conseguente, ma questo non abilita automaticamente il motore che converte il file di documentazione in PDF al riconoscimento del tag stesso, va fatta un'operazione nel codice per renderlo "reattivo" a tale tag. Generalizzando :  non abilita il generatore a riconoscere alcuna modifica alla sintassi dei dati.
- La possibilità di riconoscere variabili che non siano definite all'avvio del client o, nel momento in cui il servizio che fornisce i dati per il PDF lo farà, nella chiamata al servizio.
- La possibilità di salvare la modifica delle impostazioni di setup della stampa eventualmente intervenute mediante l'interfaccia utente sull'AS400. Vale a dire le impostazioni eventualmente modificate nella finestra che appare all'utente valgono solo per la generazione del pdf in essere.

