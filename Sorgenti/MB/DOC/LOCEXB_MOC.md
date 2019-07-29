# Generalità

Attraverso questo attributo su matrici ed alberi, quando questi componenti sono richiamati da device mobile (albero/matrice) è possibile condizionare il relativo layout grafico.

# Layout Portrait e Landscape

Nel mobile il layout grafico è condizionabile in modo differente a seconda che il device si trovi in posizione verticale o orizzontale. Per tale motivo in questo attributo possono essere indicate combinazioni delle due differenti situazioni. I valori dell'attributo sono infatti di questo tipo : 
* CellStyle="PSnn|LSnn"
** PS è il prefisso utilizzato per i layout di cella da visualizzare quando il telefono o tablet si trovano in posizione verticale (portrait syle)
** LS è il prefisso utilizzato per i layout di cella da visualizzare quando il telefono o tablet si trovano in posizione orizzontale (landscape syle)

# Valori Possibili

Di seguito i valori possibili indicabili in sostituzione dei caratteri nn. Si segnala che pur essendo tutti i valori applicabili anche al componente albero, risultano di fatto significativi per esso solo i valori 03 e 05.

* 01 :  4 Celle 1/2+3/4 - vengono presentate le prime 4 celle, la 1 e la 2 impilate in verticale sulla sinistra, la 3 e la 4 impilate in orizzonale sulla destra

![TEC001](http://localhost:3000/immagini/LOCEXB_MOC/TEC001.png)![TEC002](http://localhost:3000/immagini/LOCEXB_MOC/TEC002.png)![TEC023](http://localhost:3000/immagini/LOCEXB_MOC/TEC023.png)
* 02 :  2 Celle 1+2 - vengono presentate le prime 2 celle, una affiancata all'altra in orizzontale

![TEC003](http://localhost:3000/immagini/LOCEXB_MOC/TEC003.png)![TEC004](http://localhost:3000/immagini/LOCEXB_MOC/TEC004.png)![TEC024](http://localhost:3000/immagini/LOCEXB_MOC/TEC024.png)
* 03 :  1 Cella - viene presentata solo la prima cella

![TEC005](http://localhost:3000/immagini/LOCEXB_MOC/TEC005.png)![TEC006](http://localhost:3000/immagini/LOCEXB_MOC/TEC006.png)![TEC025](http://localhost:3000/immagini/LOCEXB_MOC/TEC025.png)
* 04 :  2 Celle 1/3 - vengono presentate impilate in verticale le celle 1 e 3

![TEC007](http://localhost:3000/immagini/LOCEXB_MOC/TEC007.png)![TEC008](http://localhost:3000/immagini/LOCEXB_MOC/TEC008.png)![TEC026](http://localhost:3000/immagini/LOCEXB_MOC/TEC026.png)
* 05 :  Icona + Cella 1 - viene presentata la prima cella con icona

![TEC009](http://localhost:3000/immagini/LOCEXB_MOC/TEC009.png)![TEC010](http://localhost:3000/immagini/LOCEXB_MOC/TEC010.png)![TEC027](http://localhost:3000/immagini/LOCEXB_MOC/TEC027.png)
* 06 :  Icona + 2 Celle 1/3 - come lo stile 04, ma affiancate ad un icona sulla sinistra

![TEC011](http://localhost:3000/immagini/LOCEXB_MOC/TEC011.png)![TEC012](http://localhost:3000/immagini/LOCEXB_MOC/TEC012.png)![TEC028](http://localhost:3000/immagini/LOCEXB_MOC/TEC028.png)
* 07 :  Icona + 4 Celle 1/2+3/4 - come lo stile 01, ma affiancate ad un icona sulla sinistra

![TEC013](http://localhost:3000/immagini/LOCEXB_MOC/TEC013.png)![TEC014](http://localhost:3000/immagini/LOCEXB_MOC/TEC014.png)![TEC029](http://localhost:3000/immagini/LOCEXB_MOC/TEC029.png)
* 08 :  4 Celle 1+3+2+4 - vengono affiancate orizzontalmente le prime 4 celle

![TEC015](http://localhost:3000/immagini/LOCEXB_MOC/TEC015.png)![TEC016](http://localhost:3000/immagini/LOCEXB_MOC/TEC016.png)![TEC030](http://localhost:3000/immagini/LOCEXB_MOC/TEC030.png)
* 09 :  Icona + 2 Celle 1+2 - come lo stile 02, , ma affiancate ad un icona sulla sinistra

![TEC017](http://localhost:3000/immagini/LOCEXB_MOC/TEC017.png)![TEC018](http://localhost:3000/immagini/LOCEXB_MOC/TEC018.png)![TEC031](http://localhost:3000/immagini/LOCEXB_MOC/TEC031.png)
* 10 :  4 Celle 1/3/2/4 - vengono impilate verticalmente le prime 4 celle

![TEC019](http://localhost:3000/immagini/LOCEXB_MOC/TEC019.png)![TEC020](http://localhost:3000/immagini/LOCEXB_MOC/TEC020.png)![TEC032](http://localhost:3000/immagini/LOCEXB_MOC/TEC032.png)
* 11 :  Icona + 4 Celle 1/3/2/4 - come lo stile 11, ma affiancate ad un icona sulla sinistra

![TEC021](http://localhost:3000/immagini/LOCEXB_MOC/TEC021.png)![TEC022](http://localhost:3000/immagini/LOCEXB_MOC/TEC022.png)![TEC033](http://localhost:3000/immagini/LOCEXB_MOC/TEC033.png)
NOTA BENE :  l'ordine delle celle presente in considerazione, se presente, tiene conto dell'attributo "Columns".

# L'Icona

Qualora sia stato utilizzato uno stile che prevede la visualizzazione di un icona, questa viene così determinata : 

* per prima cosa viene valutata la presenza dell'attributo ImgUrl (vince su tutto)
* seconda scelta è riservata alla presenza dell'attributo ImgUrlCmp
* terza ipotesi è data dall'icona dell'oggetto
* ultima ipotesi, se a questo livello non fosse stata trovata alcuna icona, è rappresentata dall'icona di default Sme.Up (logo aziendale in formato 40x40)

# 1. Da Url Specifica (ImgUrl)
Serve a specificare un'Url, diretta da utilizzare (indipendentemente dall'oggetto)
es._2_ImgUrl="http://www.smeup.com/immagine.png"

## 2. Da Confronto Celle (ImgUrlCmp)
L'attributo, indica che il recupero dell'immagine sarà condizionato al confronto tra i due valori dei rispettivi campi nomecolonna1 e nomecolonna2.
Le immagini risultanti saranno  : 
Se valore colonna1 > valore colonna2
![TEC034](http://localhost:3000/immagini/LOCEXB_MOC/TEC034.png)Se valore colonna 1 < valore colonna 2
![TEC035](http://localhost:3000/immagini/LOCEXB_MOC/TEC035.png)Se valore colonna1 = valore colonna 2
![TEC036](http://localhost:3000/immagini/LOCEXB_MOC/TEC036.png)
## 3. Da Oggetto
Per la terza ipotesi posso sussistere due sottocasistiche : 
* Se nel setup viene specificata un colonna nell'attributo "ImgField" sarà questo ad essere preso in considerazione per per la determinazione dell'icona.
* Come seconda ipotesi, utilizzerà, se definita, l'icona standard dell'oggetto a cui fa riferimento il 1° campo in ordine , tra quelli definiti per la matrice.

Nel caso dell'albero come oggetto viene preso in considerazione quello indicato nel nodo.

NB :  il tipo di immagine recuperata per default è l'icona (ICO) , tuttavia se invece viene definito un ulteriore attributo di setup di matrice,  _2_IconType="IMG" viene recuperata l'immagine dell'oggetto al posto dell'icona

