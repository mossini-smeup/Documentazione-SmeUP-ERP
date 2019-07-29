## Obiettivo
Semplificare la gestione dei dati di un oggetto attraverso la configurazione di un input panel, o di una matrice, indipendentemente dal device utilizzato.
E' un strumento costituito da 3 componenti : 
* un'interfaccia grafica :  Costruttore A36.
* i driver oggetto :  Copy £K89.
* gli attributi dell'oggetto. Copy £OAV.

## Costruzione di una gestione
I Passi per costruire una gestione sono : 
* Costruire la finestra.
* Attivare la finestra.
* Introdurre assunzioni, controlli, aggiornamenti specifici.

## Prerequisiti
Esistenza del pgm B£K89_xx dove xx è il tipo oggetto e verifica del fatto che tale pgm sia stato rilasciato a standard tramite la matrice di controllo interrogabile in questo modo : 
* richiamando la scheda del costruttore A36 (oggetto V2LOCOS A36)
* selezionando il tab "Scheda esempi A36"
* selezionando il tab "Situazione K89 Rilasciati".
Solo se il pgm è qui presente flaggato significa che è stato rilasciato a standard, viceversa si tratta di un work in progress.
Se si sta trattando un oggetto X specifico cliente, si rimanda per prima cosa alla documentazione della /COPY £K89.

## Costruzione finestra
Per costruire una finestra è necessario definire la lista dei campi che si vuole trattare a video.
La lista dei campi può essere costruita con diversi metodi nel parametro "TipFlt" e "CodFlt". Per maggiori informazioni vedere la documentazione dei due parametri su TAG VAR degli script SCP_A36 ed SCP_A36PER.
Se nel "TipFlt" si utilizza il metodo "LAY" lo script dell'SCP_LAY conterrà sia la lista dei campi che le loro proprietà ed è sufficiente metterlo nel parametro "CodFlt".
Vediamo come costruire una finestra con quest'ultimo metodo "LAY"
Per costruire la finestra copiare un SCP_LAY esistente (es. AR_X01 copiandolo dallo script AR_001) e concentrarsi per il momento solo sull'elenco degli oav che si vogliono gestire a video. Si riporta in questa sede che l'SCP_LAY permette di suddividere i dati per formati (TAG Fmt, resi graficamente tramite differenti "Tab" e sezioni (Tag Sez, resi graficamente solo in webup, che permetto di suddividere la schermata con la stessa logica di suddivisione delle schede. In loocup invece vengono presentati in ordine tutti i campi come se fossero di un'unica sezione). Nelle sezioni indico i campi che la compongono (Tag Fld, per i quali al momento si consiglia di settare solo l'elenco dei campi).
Per ogni campo va indicato il nome o l'OAV (quando vi corrisponde). E' possibile mettere anche il campo del DB nel nome. In questo caso il campo OAV viene derivato automaticamente.
Se non indicato diversamente l'OAV è sempre dell'oggetto in gestione.
Se si vuole mettere un campo che non sia un OAV dell'oggetto in gestione, ma l'OAV di un campo della finestra, va indicato nel campo OavNam il nome del campo a cui fa riempimento l'OAV.
Oltre alla lista dei campi, nello script è possibile forzare le proprietà del campo.
Per ora è possibile forzare tutte le proprietà. Stiamo valutando la possibilità di bloccarne alcune in modo da evitare errori nel Data-Base.
Per esempio in questo momento potrei oggettizzare un campo articolo(Oggetto AR) con l'oggetto lotto(LO). La finestra lo controllerebbe come lotto e il programma di aggiornamento scriverebbe un lotto in un campo articolo.
Se non presente alcun SCP_LAY vengono campi presentati tutti i campi gestibili del DataBase, che sono gli oav di tipo "I" campi del DB, "N" Note, "P" parametri e "K" parametri estesi.
Per la documentazione specifica delle proprietà gestite nello script vedere in appendice.

Per testare/verificare un particolare SCP_LAY prima di attivarlo, si consiglia di usare la scheda di test seguendo i seguenti passaggi : 
* richiamando la scheda del costruttore A36 (oggetto V2LOCOS A36)
* selezionando il tab "Scheda esempi A36"
* selezionando il tab "Test Input Panel" .
A questo punto inserite i parametri "Tipo oggetto", "Parametro oggetto", "Codice oggetto", "Azione", "TipFld"=LAY e "CodFlt" il nome dell'SCP_LAY e confermare.
Viene a questo punto aperta la finestra di test.
E' importante tenere conto dei diversi device e valutare se prevedere SCP_LAY differenti in base alle potenzialità/caratteristiche di ogni device (webup, loocup, phone e tablet). Come si vedrà poi negli script di configurazione SCP_A36 e SCP_A36PER sarà possibile condizionare l'utilizzo di un scp_lay piuttosto che un altro attraverso il test sulla variabile _&_CO.DEV nella attributo del Cnz del tag VAR.

Visti i primi effetti si può poi operare l'aggiunta di eventuali caratteristiche grafiche degli attributi che si vogliono usare. In questo senso è però importante notare che le proprietà con cui viene presentato un campo posso dipendere da vari dati/elaborazioni : 
* Definizione dell'OAV
* Definizione del campo di database, quando l'OAV fa riferimento ad un campo di database
* Considerazioni effettuate dal pgm B£K89_xx
* Da caratteristiche della classe intestataria dell'oggetto OAV definite attraverso la classe K04 (es. il livello di un CNCLI ha come oggetto di riferimento TAB£W00, è quindi la K04 del TAB£W00 ad essere presa in considerazione). E' da tenere a sua volta conto che la K04 prevede un exit tramite cui ad esempio posso condizionare il trattamento di una particolare classe oggetto.
Tali caratteristiche possono essere sovrascritte nell'SCP_LAY oppure attraverso il pgm di exit che si potrà attivare come riportato a seguire negli script SCP_A36 ed SCP_A36PER. A senso utilizzare l'SCP_LAY o il pgm di exit a seconda di più considerazioni : 
* Se ho più formati e voglio centralizzare tutte le forzature in un unico punto, cioè l'exit, senza doverle replicare per ogni scp_lay che utilizzo (compresi quelli standard)
* Se devo fare del considerazioni articolare per decidere cosa fare (es. leggere tabelle o altri file per decidere che proprietà forzare, es. se il campo deve essere visibile, protetto o nascosto).

## Attivazione finestra
L'utilizzo di una finestra così costruita attraverso l'SCP_LAY va fissata in uno script SCP_A36 se si sta trattando una finestra standard o in uno script SCP_A36PER se si sta trattando una finestra non standard in un TAG VAR.

Ogni oggetto ha il suo script SCP_A36. Il nome del membro è l'oggetto (Per gli oggetti ID sarà IDXX dove XX corrisponde al programma specifico B£K89_XX)
E' strutturato su 3 livelli :  Azione, Nome, Varianti.
**AZI (AZIONE)**
Ogni richiamo della gestione cerca nel setup l'azione corrispondente. Se non è presente risale sull'azione fittizia "**".
Se non presente lo script o non trova alcun Setup viene richiamata la gestione con tutte i parametri di default dell'azione..
**NAM (NOME)**
All'interno dell'azione viene cercato il Setup con il nome ricevuto nella variabile "NamSet" se non ricevuto risale sul default "**".
(Per l'azione "00", azione derivata dall'azione "01" con attivazione  pre-immissione, è la varibile "NamSetA00")
**VAR (VARIANTE)**
All'interno dell'azione/nome viene attivato il Setup della prima variante che soddisfa le condizioni indicate nel campo "Cnz" .
Se una variante non ha condizioni è ritenuta valida.
Per questo bisogna prestare attenzione alla sequenza con cui si mettono le varianti. Se dovesse essere aggiunta come prima variante, una variante senza condizioni risultando sempre valida andrebbe a inibire tutte le successive.
Nelle condizioni si possono usare : 
* qualsiasi OAV dell'oggetto
* tipo oggetto "PAR"
* azienda "AZI"
* utente "UTE"
* gruppo utenti "GRU"
* device "DEV"
* componente grafico "GRA" (Input panel/Matrice)
Le condizioni possono essere anche multiple sia in AND che un OR.
Per un maggiore dettaglio si veda cmq la documentazione del wizard del campo Cnz del tag VAR.

**AZIONE 00**
L'azione "00" è un'azione virtuale di pre immissione. Virtuale perchè non viene chiamata direttamente nel A36 ma si attiva in modo automatico nell'azione "01" di immissione.
Quando si esegue l'azione di immissione il programma cerca prima nell'azione "00" se esiste un setup valido. In caso affermativo esegue l'azione "00" di pre-immissione con il corrispondente setup.
All'interno del setup delle azioni "00" il parametro "NamSuc" contiene il nome del prossimo Setup dell'azione "00" da eseguire. E così via. Costruendo un flusso di finestre. Per terminare il flusso e passare alla vera azione di immissione è necessario mettere  *FINE" nel parametro "NamSuc", Il parametro "NamSuc" può anche essere impostato nel programma di exit.

Per la documentazione specifica delle proprietà gestite nello script vedere in appendice
Gli SCP_A36 standard si trovano nel sorgente SCP_A36 della SMEDEV
Gli SCP_A36 personalizzati si trovano nel sorgente SCP_A36PER della libreria sorgenti dell'azienda.

Per verificare l'istruzione di SCP_A36 in elaborazione in quel momento, sempre dal bottone "Set'n play" aprire la sezione SCP_A36. Si entra nella scheda di gestione dell'SCP_A36. La scheda è un albero.
Il 1° livello separa gli SCP_A36 personalizzati(file SCP_A36PER) da quelli standard(file SCP_A36).
Il 2° livello separa le azioni disponibili
Il 3° livello separa i nomi disponibile per l'azione.
Il 4° e ultimo livello separa le varianti disponibili per il nome.
Espandere fino alla foglie, da dove si  entrare nella scheda di gestione dello script.
Un volta in gestione aggiungere la variante che attiva il setup con la finestra di esempio.
Se si vuole attivare solo per un'azione deve essere messa sotto quella azione, altrimenti se si vuole attivare per tutte le azioni va messa sotto l'azione "**".
Esempio di attivazione della finestra AR_TEST quando la classe materiale è "001" per tutte le azione come default
 :  : AZI Cod="**"
 :  : NAM Cod="**" Txt="Default"
 :  : VAR Cod="AR_TEST" Txt="Articoli TEST" Cnz="&CO.I/10 = 001" TipFlt="LAY" CodFlt="AR_TEST"
(Se  :  : AZI e  :  : NAM sono già presenti aggiungere solo  :  : VAR)
A questo punto rieseguendo la scheda di test senza i parametri "TipFlt" e "CodFlt" con un articolo di classe materiale "001" si apre automaticamente la nuova finestra.
ATTENZIONE :  NON MODIFICARE MAI gli script nel file SCP_A36 sono quelli distribuiti dallo standard, agire sempre su quelli SCP_A36PER che si trovano nella libreria del cliente.

##  Introdurre assunzioni, controlli, aggiornamenti specifici.
Parzialmente questo tipo di operazioni si è già visto possono essere attuate direttamente tramite l'SCP_LAY, ma un altro canale attraverso cui inserire queste considerazioni in modo più strutturato/controllato è tramite l'exit della £K89 che può essere attivata tramite la specifica proprietà della riga VAR (attributo PgmExi) degli script SCP_A36PER. Per un maggior dettaglio sulle funzionalità attuabili tramite l'exit si rimanda alla documentazione della K89.

## Scheda di esempi/test
E' possibile utilizzare la scheda LOA36_ES dove mettere esempi o fare dei test.
La sezione "Esempi" visualizza A36 di esempio che si trovano nello script SCP_SET/LOA36.
La sezione "Test" permette di richiamare qualsiasi gestione. Per evitare di perdersi nel molti parametri di input sono stati messi sono quelli più comunemente utilizzati nella gestione.

## Altre considerazioni

### Azioni automatiche
Le azioni automatiche sono delle azioni che gestiscono con una sola azione le azioni di immissione,
modifica, copia e cancella.
Quando si uliizza una azione automatica l'azione viene trasformata automaticamente in azione di immissione o di modifica in funzione dell'esistenza dell'oggetto. Se l'oggetto non esiste l'azione effettiva diventa "01" immissione, se l'oggetto esiste di venta "02" modifica.
Le azioni automatiche sono 4 :  "11", "12", "13", "14".
La loro diversità consiste solo nell'eventuale attivazione dei bottni di copia o cancella nel caso
l'azione effettiva diventi "02" modifica.
* "11" azione "01"/"02", nel caso "02" non vengono attivati i bottoni di copia e cancella
* "12" azione "01"/"02", nel caso "02"  vengono attivati i bottoni di copia e cancella
* "13" azione "01"/"02", nel caso "02"  viene attivato solo il bottone di copia
* "14" azione "01"/"02", nel caso "02"  viene attivato solo il bottone di cancella

### A36 come sottoscheda
l'A36 può essere inserito come sottoscheda all'interno di una scheda.
E' possibile far scatenare due dinamismi nelle varie sezioni della scheda attraverso due specifici parametri : 
- "SchDinNft" :  si scatena sempre ad ogni UDPATE dell'input panel (Enter su qualunque campo)
- "SchNtf" :  si scatena solo alla conferma andata a buon fine.
- "SchDinFun" :  si scatena sempre ad ogni UDPATE dell'input panel (Enter su qualunque campo)
- "FunSuc" :  si scatena solo alla conferma andata a buon fine.

### Funzione successiva
Parametro "FunSuc"
Dopo l'esecuzione dell'azione andata a buon fine è possibile eseguire una funzione libera.
 indicata nei parametri di input, nello script di setup, o nel programma di exit.
In automatico alla funzione viene passato l'oggetto nel codice 1 (Solo se non già indicato esplicitamente nella funzione). In questo modo alla fine di un'immissione arriva il nuovo codice.
E' possibile aggiungere nei parametri di input della funzione tutti i parametri di input del A36 e tutti i campi della matrice. I campi nella matrice sono nella forma NomeCampo(Valore).
Questa possibilità deve essere indicata esplicitamente nel parametro "FunSucInp", perchè se la funzione non è costruita per ricevere questi parametri oltre ad essere inutile passarli può mandarla in errore. Parametro "FunSucInp"

### Sottoscheda info in A36
Parametri :  "SscInf", "SscInfPos", "SscInfDim"
E' possibile dividere la scheda A36 in due sezioni. La sezione principale è il gestione dei dati A36, la sezione secondaria è una sottoscheda utente.
La sottoscheda è posizionabile in basso(Posizione H orizzontale) o a destra(Posizione V verticale). Con una dimensione variabile.
La sottoscheda con relativa posizione e dimensione va indicata nei parametri di input o dello script di setup.
La sottoscheda sente il dinamismo su ogni campo della finestra. Alla sottoscheda arrivano come dati input tutti i campi della finestra A36 di gestione indentificati con il nome del campo.
Può essere utilizzata per visualizzare informazioni aggiuntive mentre si stanno gestendo i dati nell'input panel.
Sono disponibili delle sottoscheda già costruite. Si possono usare come esempio. Si chiamano B£A36_XXYY dove XX è l'oggetto e YY un progressivo.
E' proposta questa nomenclatura per identificare facilmente tutte le sottoschede gestite nei LOA36. Per convezione il progressivo YY sarà alfanumerico per le schede standard Smeup e numerico per quelle utente.

### Passaggio dati
Parametro "InzDat"
Per le azioni "00" e "01" il parametro InzDat contiene i valori di inizializzazione.
La nomenclatura è NomeCampo(Valore).
Per le finestre che fanno parte di un flusso di pre-immissione, ogni finestra passa alla successiva l'InzDat ricevuto completato con i campi della finestra. Se un campo è presente sia nell'InzDat ricevuto che nella finestra viene passato con il valore della finestra.
E' possibile attivare l'import di campi con il parametro "InzDat" anche per l'azione "02" previa attivazione sul parametro "InzDatA02".

### Bottoni
Di seguito la documentazione dei bottoni previsti. Dove sotto inserimento/modifica/copia/cancellazione/visualizzazione per l'input panel ed attivazione per la matrice vedo 1 significa che il bottone è attivo di default, Yes solo se è specificato Yes dal SCP_A36.
Per quel che riguarda la posizione, di default è in basso a destra.

### Input Panel

| Bottone|Testo|Inserimento|Modifica|Copia|Cancellazione|Visualizzazione|Style|Posizione|Bottone|Test---|----|----|----|----|----|----|----|----|
| o|Icona|Note |
| F03|Esci|1|1|1|1|1||In alto destra|No||J1;KEY;*F03| |
| F06|conferma/conferma eliminazione/conferma e apri|1|1|1|1||||||No| |
| F07|Righe/gestione righe/gestione campi||1|||1|*BTNROW|In alto a destra|||No|Solo per gli oggetti che lo prevedono le righe, TR c'è solo sull'UP DEF |
| F07|Conferma e apri|Yes|||||||||No| |
| F08|Conferma e nuovo|Yes|||||||||No| |
| F09|Undo|1|1|1||||Basso Dx||No|VO;COD_VER;000099| |
| F10|Funzioni||Yes|Yes|Yes|Yes||Alto Dx|||No| |
| F11|Dati statistici||1|||1||Alto Dx|No||No| |
| F12|Indietro|1|1|1|1|1||Basso Dx||No|VO;COD_VER;000008| |
| F14|modifica|||||Yes|||||No| |
| F15|copia||Yes|||Yes|||||No| |
| F16|Elimina||Yes|||Yes|*BTNDEL||||No| |
| F17|Set'n'play|1|1|1|1|1||Alto Dx|No|No|VO;COD_VER;000117|Solo se User Level 01 |
| F18|Controllo||Yes|||Yes||Alto Dx|No||No| |
| 


### Matrice

| Bottone|Testo|Attivazione|Style|Posizione|Bottone|Testo|Icona|Note |
| ---|----|----|----|----|----|----|----|----|
| F03|Esci|1||In Alto a Destra|No||J1;KEY;*F03| |
| F06|Conferma|1|||||VO;COD_VER;000111/000020| |
| F09|Undo|1|||||VO;COD_VER;000099| |
| F12|Indietro|1||In Basso a Destra|||VO;COD_VER;000008| |
| F17|Set'n'play|1||In Alto a Destra|No||VO;COD_VER;000117|Solo user level 01 |
| 


### Parametri di input
I parametri di input sono : 
* Il tipo oggetto :  Obbligatorio
* Il parametro oggetto :  Obbligatorio in funzione del tipo oggetto, e se previsto dall'oggetto, sempre in immissione
* Il codice oggetto :  Sempre obbligatorio tranne per l'immissione
* l'azione :  Obbligatoria
* Tutti gli altri parametri di input sono facoltativi. Per alcuni viene assunto un default, che diventa fondamentale per quelli che sono necessari al funzionamento dello strumento.
* Il tipo, parametro e codice vengono passati nell'oggetto 1 :  1(&OG.T1;&OG.P1;&OG,K1) Tutti gli altri parametri vengono passati nel P() o nell' INPUT().

### Bottone Set'n play
Il bottone set'n play è una documentazione interattiva della finestra. Permette di capire come è stata costruita, e di seguire ogni passo della gestione.
E' composto da : 

**Parametri (Input/Setup)**
* Input
Visualizza i parametri di input passati nella chiamata della scheda A36. La regola è di mantenere le chiamate A36 il più semplice e pulite possibili e demandare il passaggio di eventuali parametri allo script di setup SCP_A36.
* Setup (da funzione SET della £K89)
Visualizza i parametri di input dopo aver eseguito la lettura del Setup SCP_A36.
Oltre ai parametri di input indica anche il setup utilizzato. Variabili :  FilSet, MemSet, AziSet, NamSet e VarSet.
I valori di setup dello script completano e mai sostituiscono quelli passati direttamente nel richiamo della scheda.

**Struttura (da funzione CAR della £K89)**
Presenta la struttura della finestra, ossia i campi in gestione con tutte le loro proprietà.
Per ogni proprietà viene indicato l'origine : 
Legenda Origine valore
A=Da definizione base (OAV)
B=Da programma struttura (B£K89S)
C=Da programma base (B£K89G)
D=Da programma specifico (B£K89_XX)
E=Da programma exit (B£K89_XXYY)
F=Da SCP_LAY
G=Da autorizzazioni

**Dati in elaborazione (da funzione CAR e CTR)**
Presenta i dati in essere in quell'instante, compresi anche di tutte le proprietà del campo.
Alcune proprietà possono essere modificate sia nella funzione di caricamento valori che nella funzione di controllo. In questo caso saranno diverse rispetto a quelle presenti nella struttura.
Per esempio posso decidere, sia in caricamento valori che in controllo, che un campo diventi hidden, di solo output o di input/output in funzione del valore digitato in un altro campo, Questo è possibile farlo modificano nella exit la proprietà £89I_IO del corrispondente campo.

**Messaggi errore**
Presenta i messaggi di errore. Ogni messaggio è costituito dall'indice del campo in errore, un codice o un testo, la gravità e il programma che ha generato l'errore. (In questo modo è facilmente identificabile l'origine dell'errore).
Se la gravità è minore o uguale a "33" il messaggio è di warning altrimenti è vincolante.
Se la gravità è "99" l'errore è vincolante anche se il campo non è presente in gestione.
Queste informazioni devono essere sempre compilate in eventuali errori generati nei programmi di exit.

**Memora UNDO**
Visualizza tutti i campi modificati. Ogni controllo determina un progressivo con tutti i suoi campi modificati. Un UNDO  tutti i campi di un controllo in modo decrescente.

**Campi disponibili**
Presenta la lista di tutti i campi disponibili per l'oggetto in gestione con le relative proprietà standard.

**Gestione  SCP_A36**
E' uno script che determina quale setup attivare nel richiamo della gestione degli script SCP_A36 e SCP_A36PER.

**Gestione SCP_LAY**
E' uno script che contiene la lista dei campi da mettere in gestione.

### Memoria
Tutti le schiere di gestione dell'input panel sono salvate in un file di work LOWKT0F dove la key è l'ID della matrice. In questo modo è possibile gestire l'aperura contemporanea di più LOA36.

## Flussi
Elenco dei flussi legati ad un oggetto

| 
| .COL Txt="Tipo" Lun="10" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="10" A="L" |
| 
| .COL Txt="Gestione 5250" Lun="10" A="L" |
| 
| .COL Txt="A36 Input panel" Lun="50" A="L" |
| 
| .COL Txt="A36 Matrice" Lun="50" A="L" |
| 
| .COL Txt="A40 Import" Lun="50" A="L" |
| B£H|Azioni Popup utente|A-|Da F10|Da F10(Previsto ma da gestire) |
| B£H|Immissione|I-|Da interfaccia o da pgm gestione| |
| B£H|Copia|C-|Da interfaccia o da pgm gestione| |
| B£H|Pre-eliminazone|P-|Da interfaccia o da pgm gestione| |
| B£H|Post-eliminazone|D-|Da interfaccia o da pgm gestione| |
| B£H|Pre-modifica|F-|Da interfaccia o da pgm gestione| |
| B£H|Post-modifica|M-|Da interfaccia o da pgm gestione| |
| B£H|Visualizazione|V-|| |
| B£H|Collegamento|K-|| |
| B£H|Scollegamento|S-|| |
| B£H|Esecuzione|E-|| |
| B£H|2° Collegamento(CoGe)|J-|| |
| B£H|2° Scollegamento(CoGe)|L-|| |
| B£H|Riferimento origine post delete|O-|| |
| B£H|Batch|B-|| |
| B£H|Transazione|T-|| |
| B£H|Stampa bolla|1-|| |
| B£H|Stampa fattura|2-|| |
| A11|Flussi LOA11||| |
| WF |Wrkflow||| |
| A36|Funzione successiva|| |
| 

completare documentazione quando si attivano adesso nel 5250 e quando si attiveranno sulla nuova gestione

## Appendice

Documentazione specifica script SCP_LAY
 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_LAY)

Documentazione specifica Script SCP_A36
 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_A36)

Documentazione specifica copy £K89
- [£K89](Sorgenti/MB/DOC_OGG/P_TSTK89)

