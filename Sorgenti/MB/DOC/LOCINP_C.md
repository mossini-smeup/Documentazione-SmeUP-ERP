# Come si costruisce un input panel
## Definizione e Setup
Essendo un componente grafico interno alla scheda, le modalità di definizione di una sezione di tipo INP nello script di scheda sono equivalenti a quelle degli altri componenti.
E' possibile pertanto utilizzare la specifica G (Grafica) per definire una sezione e al suo interno una sottosezione di tipo input panel, come segue : 
 :  : PAR F(04)
..G.SEZ Pos(A)
..G.SUB.INP Tit="Input Panel"

Come tutti gli altri componenti, anche il componente INP è dotato di un setup che è possibile specificare tramite la riga : 
 :  : PAR F(04)
..G.SET.INP ...
 
Tutte le voci di setup del componente INP derivano dalle voci presenti nel setup della matrice (e verranno applicate SOLO in presenza di una matrice dei dati associata) ad eccezione di : 
 :  : PAR F(01) L(PUN)
- FormatName :  Specifica il nome del formato da usare, nel caso in cui l'input pane sia costruito sulla base di un file video.
- FldPerCol :  Specifica il numero di campi presenti per "colonna"  nel caso in cui l'input panel generi la sua interfaccia video automaticamente a partire dalla matrice dei dati.

Si rimanda alla documentazione del componente EXD ed EXB per le altre voci di definizione e di setup : 
- [Documentazione componente scheda](Sorgenti/MB/DOC/LOCEXD)
- [Componente Matrice](Sorgenti/MB/DOC/LOCEXB)
- [Setup di Input panel con -](Sorgenti/MB/DOC/LOCINP_1)

## Come si riempie un Input Panel
Precedentemente in questa documentazione sì è parlato di matrice dei dati associata, di file video etc. etc.
Perchè il componente INP abbia a disposizione dei dati e/o dei formati video è necessario fornirglieli tamite una specifica di tipo D (o eventualmente l'inclusione dell'XML nello script).
E' possibile fornire all'input panel diversi tipi di XML dei dati : 
 :  : PAR F(01) L(PUN)
- Xml Video :  Analogo ad un DSPFile convertito in XML come già avviene nell'emulatore Smeuiclt. Il componente INP è in grado di interpretare il file video (tradotti in Xml) dell'emulatore e posizionare i controlli di conseguenza. Tramite l'attributo di setup è possibile specificare quale formato video utilizzare nel caso in cui ve ne siano presenti più di uno.
- Xml Matrice :  Analogo all'XML di una matrice. Di norma l'input panel tratta il contenuto di questo tipo di XML come dati da visualizzare (o modificare) mappando i campi con presenti a video con le colonne della griglia specificata nell'xml. Se non è presente un xml video che definisce i campi, INP genera un video a partire dalla definizione delle colonne della griglia e della disposizione definita nel setup.

E' possibile fornire questi tipi di XML al componente tramite una o più funzioni, come avviene per gli altri componenti.
Ad esempio : 
 :  : PAR F(04)
..D.FUN.STD F(DSP;;LET) 1(OJ;*FILE;TESTPNL)
..D.FUN.STD F(EXB;*TBL;) 1(TA;X01;)

La prima chiamata a funzione restituisce l'Xml Video mentre la seconda un Xml in formato matrice che contiene i dati.
Non è obbligatorio che vengano effettuate entrambe le chiamate. Ad esempio se venisse scelta solo la seconda, il componente INP autogenererebbe il suo video a partire dalla griglia dei dati. Mentre se venisse utilizzata solo la prima funzione verrebbe creato un input panel non collegato ai dati, ma comunque completo di ogni dinamismo associato ai suoi eventi, a partire dal formato video scelto.










