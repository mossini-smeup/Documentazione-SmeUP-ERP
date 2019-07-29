<?xml version="1.0" encoding="UTF-8"?>
<Xml>
<UiSmeup Descrizione="Elemento root (L'elemento 'Base' dovrà essere sostituito con questo in tutti gli XML vecchi)" Obbligatorio="SI" Molteplicità="1">
<Configurazione Descrizione="Le configurazioni sono identificate da codice (nome del file XML),modulo e 2 gruppi di chiavi :  AMBIENTALI e FUNZIONALI.Il Questionario-Modulo non è chive della configurazione in quanto costiuisce l'identificativo del Setup" Obbligatorio="NO" Molteplicità="*">
<Modulo Descrizione="Modulo di Loocup al quale assegnare la configurazione che si sta definendo. Per identificare una configurazione il modulo del setup deve ricevere le chiavi della configurazione. " Obbligatorio="SI" Molteplicità="1"/>
<Utente Descrizione="Elemento che (insieme all'ambiente) costituisce una chiave ambientale per risalire alla configurazione." Obbligatorio="SI" Molteplicità="1"/>
<Funzione Descrizione="Funzione di chiamata :  elemento che determina una chiave FUNZIONALE per risalire alla configurazione" Obbligatorio="SI" Molteplicità="1"/>
<CfgKey3 Descrizione="Elemento della chiave per risalire alla configurazione.Il modulo effettua la risalita eliminando via via le chiavi passate secondo l'ordine CfgKey3-Funzione-Utente" Obbligatorio="SI" Molteplicità="1"/>
</Configurazione>
<Sez Descrizione="Nell'Xml di setup iniziale della scheda di Loocup indica le caratteristiche generali di stile" Obbligatorio="SI" Molteplicità="1">
<Styles Descrizione="Nell'Xml di setup iniziale della scheda di Loocup contiene la definizione degli stili applicabili alla scheda" Obbligatorio="SI" Molteplicità="1">
<Style Descrizione="Nell'Xml di setup iniziale della scheda di Loocup definisce le caratteristiche di un singolo stile" Obbligatorio="SI" Molteplicità="*"/>
</Styles>
</Sez>
<Service Descrizione="Primo elemento negli Xml che contengono le direttive per la costruzione dei moduli. Contiene le caratteristiche generali di ciò che Looc.up sta visualizzando" Obbligatorio="NO" Molteplicità="1"/>
<Header Descrizione="Elemento necessario per la costruzione dei menu con la parte Java - (Inutilizzato dalla parte Delphi?)" Obbligatorio="NO" Molteplicità="1">
<Livello Descrizione="Sottoelemento di Header - Contiene le caratteristiche di posizionamento dell'albero relative al layout" Obbligatorio="NO" Molteplicità="*"/>
</Header>
<Setup Descrizione="Contiene, nell'elemento figlio Program, l'elemento EDT, BAS, ... con le informazioni su ciò che si sta utilizzando" Obbligatorio="NO" Molteplicità="1">
<Program Descrizione="Contiene l'elemento EDT, BAS, ... con le informazioni sul componente che si sta utilizzando" Obbligatorio="SI" Molteplicità="1">
<GNT Descrizione="Contiene le caratteristiche dello schema di GANTT che si sta utilizzando" Obbligatorio="SI(per il Gantt)" Molteplicità="1"/>
<BAS Descrizione="Elemento relativo al modulo grafico di base (J1-GRA-BAS) che tratta la comunicazione con As/400, gestisce utenti, finestre, il loro richiamo e la comunicazione tra i vari moduli Java e non." Obbligatorio="NO" Molteplicità="1">
<Authorizations Descrizione="Elemento che contiene la gestione delle autorizzazioni. Tale gestione si basa su una matrice di 100 elementi divisi in 10categorieX10livelli " Obbligatorio="NO" Molteplicità="1">
<Authorization Descrizione="Elemento descrittivo di una classe di autorizzazioni. Per poter accedere a una scheda contenente la chiamata a un servizio che mostri dati riservati l'utente dovrà superare autorizzazioni a livello di Chiave di menù(poter selezionare la scheda), Scheda	(poter visualizzare la sezione contenente la chiamata),Servizio(poter eseguire la funzione richiesta),Oggetto(poter accedere ai dati riservati)" Obbligatorio="SI" Molteplicità="Almeno 1"/>
</Authorizations>
</BAS>
<EDT Descrizione="Elemento che contiene le caratteristiche del testo che si sta visualizzando nell'editor" Obbligatorio="SI" Molteplicità="1"/>
<SCH__Program Descrizione="Definisce lo schema (default, geofrafico, utente...) utilizzato per la ricerca. Rappresenta l'insieme delle colonne della query ed e' un valore multiplo." Obbligatorio="SI" Molteplicità="1"/>
<ORD Descrizione="Definisce l'ordinamento utilizzato per la ricerca ()" Obbligatorio="SI" Molteplicità="1"/>
<ORDLIST Descrizione="Contiene una lista di oggetti che identifica la lista di ordinamenti possibili (è il contenuto del menu a tendina da Ordinamento)" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</ORDLIST>
<SCHLIST Descrizione="Contiene una lista di oggetti che identifica la lista di schemi possibili (è il contenuto del menu a tendina da Schema)" Obbligatorio="" Molteplicità="">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</SCHLIST>
<QRY Descrizione="Definisce le caratteristiche della ricerca :  la chiave e i filtri utilizzati" Obbligatorio="SI" Molteplicità="1">
<TEXT Descrizione="Contiene la riga HTML che definisce la barra in alto del componente es :  HTML Query :  Ricerca per codice BR Schema :  Geografico BR Filtro :  BR Order :  BR /HTML" Obbligatorio="SI" Molteplicità="1"/>
</QRY>
<QRYLIST Descrizione="Contiene una lista di oggetti che identifica la lista dei possibili tipi di ricerca (è il contenuto del menu a tendina da Query)" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</QRYLIST>
<EXU Descrizione="Indica (tramite codice) che il componente grafico utilizzato è l'updater della matrice" Obbligatorio="NO" Molteplicità="1">
<Actions__EXU Descrizione="Elemento che indica i permessi (di lettura, scrittura, cancellazione) relativi alle azioni eseguibili sulla matrice" Obbligatorio="SI" Molteplicità="1"/>
<Fields Descrizione="Definisce l'elenco dei campi della matrice che devono essere aggiornati" Obbligatorio="SI" Molteplicità="1">
<Field Descrizione="Definisce un singolo campo della matrice" Obbligatorio="SI" Molteplicità="*"/>
</Fields>
</EXU>
</Program>
<Pres Descrizione="Definisce come deve essere mostrato il questionario" Obbligatorio="SI" Molteplicità="1"/>
<Resp Descrizione="Definisce come utilizzare l'XML in input al questionario e come formattare l'XML in output al questionario delle risposte " Obbligatorio="SI" Molteplicità="1"/>
<Rules Descrizione="Definisce il tipo di esecuzione della regola" Obbligatorio="NO" Molteplicità="1"/>
</Setup>
<UISezG30 Descrizione="" Obbligatorio="" Molteplicità="">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</UISezG30>
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*">
<Proprieta Descrizione="" Obbligatorio="" Molteplicità=""/>
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
<Regole Descrizione="" Obbligatorio="" Molteplicità="">
<PRE Descrizione="" Obbligatorio="" Molteplicità=""/>
</Regole>
</Oggetto>
<Griglia Descrizione="Elemento per la definizione delle colonne di una matrice. Contiene tanti elementi 'Colonna' quanti i campi della matrice da visualizzare" Obbligatorio="NO" Molteplicità="1">
<Colonna Descrizione="Elemento descrittivo di una colonna per la costruzione di una matrice tramite XML" Obbligatorio="SI" Molteplicità="*"/>
</Griglia>
<LisOgg Descrizione="" Obbligatorio="" Molteplicità=""/>
<Condizioni Descrizione="Insieme delle condizioni di controllo sui campi della videata" Obbligatorio="NO" Molteplicità="1">
<Condizione Descrizione="Singola condizione di controllo sui campi della videata. La condizione è espressa tramite gli attributi 'Se' e 'Allora'" Obbligatorio="SI" Molteplicità="*"/>
</Condizioni>
<Righe Descrizione="Elemento per la definizione delle righe di una matrice. Contiene tanti elementi 'Riga' quante sono le righe della matrice da visualizzare" Obbligatorio="NO" Molteplicità="*">
<Riga Descrizione="Elemento descrittivo di una riga all'interno della matrice." Obbligatorio="SI" Molteplicità="*"/>
<Riga__FRM Descrizione="Nell'Xml del form per la stampa in pdf della sezione/scheda indica le caratteristiche di stampa" Obbligatorio="SI" Molteplicità="*"/>
</Righe>
<LisVal Descrizione="Nell'Xml del form per la stampa in pdf della sezione/scheda indica l'elenco dei valori delle istanze associate alle risposte" Obbligatorio="SI" Molteplicità="1">
<Val Descrizione="Nell'Xml del form per la stampa in pdf della sezione/scheda indica il valore della singola istanza associata ad una risposta" Obbligatorio="SI" Molteplicità="*"/>
</LisVal>
<Script>
<Riga__SCRIPT Descrizione="" Obbligatorio="" Molteplicità=""/>
</Script>
<UIPopup Descrizione="Consente di passare da AS delle voci di menu che integrano quelle cablate nel client. Tali voci di menu sono contenute negli elementi figli Oggetto" Obbligatorio="NO" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero." Obbligatorio="SI" Molteplicità="*"/>
</UIPopup>
<Video Descrizione="Elemento dell'Xml relativo ad una schermata dell''emulatore" Obbligatorio="SI" Molteplicità="1">
<Formato Descrizione="Fornisce le caratteristiche della videata che si sta visualizzando" Obbligatorio="SI" Molteplicità="1">
<Modello Descrizione="Contiene le caratteristiche della videata che si sta visualizzando negli elementi figli Controlli, Comandi, Campi" Obbligatorio="SI" Molteplicità="1">
<Controlli Descrizione="Contiene i controlli relativi alla videata che si sta visualizzando. Da la possibilità di impostare azioni condizionali in base al contenuto dello schermo" Obbligatorio="NO" Molteplicità="1">
<Controllo Descrizione="Caratteristiche del singolo controllo sui campi della videata :  condizioni e reazioni associate" Obbligatorio="SI" Molteplicità="*">
<Condizioni Descrizione="Insieme delle condizioni di controllo sui campi della videata" Obbligatorio="NO" Molteplicità="1">
<Condizione Descrizione="Singola condizione di controllo sui campi della videata. La condizione è espressa tramite gli attributi 'Se' e 'Allora'" Obbligatorio="SI" Molteplicità="*"/>
</Condizioni>
</Controllo>
</Controlli>
<Comandi Descrizione="Elemento presente negli XML relativi alla costruzione del componente emulatore (J1-GRA-EMU). Contiene l'associazione tra i comandi possibili (es. F5, F12, ...) e le descrizioni testuali delle relative azioni da eseguire" Obbligatorio="NO" Molteplicità="1">
<Comando Descrizione="Contiene l'associazione tra un preciso comando (ex. F5, F12,..) e la descrizione testuale dell'azione da eseguire in corrispondenza di tale comando" Obbligatorio="SI (in Comandi)" Molteplicità="*"/>
</Comandi>
<Campi Descrizione="Insieme delle caratteristiche dei singoli campi della videate" Obbligatorio="SI" Molteplicità="1">
<Campo Descrizione="Caratteristiche di un singolo campo" Obbligatorio="SI" Molteplicità="*"/>
</Campi>
</Modello>
</Formato>
</Video>
<UIDoc Descrizione="Elemento base per gli xml che definiscono l'apertura e le caratteristiche dell'editor. Contiene gli elementi Service,Key,Buttons,Setup,Contenuto,Messaggi,Esito" Obbligatorio="SI (per l'editor)" Molteplicità="1">
<Service Descrizione="Contiene le direttive generali per la costruzione del modulo, le caratteristiche generali di ciò che Looc.up sta visualizzando" Obbligatorio="SI" Molteplicità="1"/>
<Key Descrizione="Contiene nei sottoelementi K1, K2, K3 le chiavi di riferimento del documento." Obbligatorio="NO" Molteplicità="1">
<K1 Descrizione="Prima chiave di riferimento del documento per identificare l'oggetto da editare. (T-P-K)" Obbligatorio="SI" Molteplicità="1"/>
<K2 Descrizione="Seconda chiave di riferimento del documento per identificare l'oggetto da editare (identificazione della libreria)" Obbligatorio="SI" Molteplicità="1"/>
</Key>
<Buttons Descrizione="Gestisce, attraverso la presenza di elementi Button (da 1 a 3), delle funzioni di Salva, Salva con Nome e Elimina all'interno dell'editor. Questo elemento non è presente nel caso in cui avvenga l'apertura in modalità di sola lettura (non si possono applicare modifiche,quindi non sono necessari i relativi comandi)" Obbligatorio="NO" Molteplicità="1">
<Button Descrizione="Caratteristiche del singolo bottone" Obbligatorio="SI" Molteplicità="0..3"/>
</Buttons>
<Setup Descrizione="Contiene, nell'elemento figlio Program, l'elemento EDT, BAS, ... con le informazioni su ciò che si sta utilizzando" Obbligatorio="NO" Molteplicità="1">
<Program Descrizione="Contiene l'elemento EDT, BAS, ... con le informazioni sul componente che si sta utilizzando" Obbligatorio="SI" Molteplicità="1">
<BAS Descrizione="Elemento relativo al modulo grafico di base (J1-GRA-BAS) che tratta la comunicazione con As/400, gestisce utenti, finestre, il loro richiamo e la comunicazione tra i vari moduli Java e non." Obbligatorio="NO" Molteplicità="1">
<Authorizations Descrizione="Elemento che contiene la gestione delle autorizzazioni. Tale gestione si basa su una matrice di 100 elementi divisi in 10categorieX10livelli " Obbligatorio="NO" Molteplicità="1">
<Authorization Descrizione="Elemento descrittivo di una classe di autorizzazioni. Per poter accedere a una scheda contenente la chiamata a un servizio che mostri dati riservati l'utente dovrà superare autorizzazioni a livello di Chiave di menù(poter selezionare la scheda), Scheda	(poter visualizzare la sezione contenente la chiamata),Servizio(poter eseguire la funzione richiesta),Oggetto(poter accedere ai dati riservati)" Obbligatorio="SI" Molteplicità="Almeno 1"/>
</Authorizations>
</BAS>
<EDT Descrizione="Elemento che contiene le caratteristiche del testo che si sta visualizzando nell'editor" Obbligatorio="SI" Molteplicità="1"/>
<SCH__Program Descrizione="Definisce lo schema (default, geofrafico, utente...) utilizzato per la ricerca. Rappresenta l'insieme delle colonne della query ed e' un valore multiplo" Obbligatorio="SI" Molteplicità="1"/>
<ORD Descrizione="Definisce l'ordinamento utilizzato per la ricerca ()" Obbligatorio="SI" Molteplicità="1"/>
<ORDLIST Descrizione="Contiene una lista di oggetti che identifica la lista di ordinamenti possibili (è il contenuto del menu a tendina da Ordinamento)" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</ORDLIST>
<SCHLIST Descrizione="Contiene una lista di oggetti che identifica la lista di schemi possibili (è il contenuto del menu a tendina da Schema)" Obbligatorio="" Molteplicità="">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</SCHLIST>
<QRY Descrizione="Definisce le caratteristiche della ricerca :  la chiave e i filtri utilizzati" Obbligatorio="SI" Molteplicità="1">
<TEXT Descrizione="Contiene la riga HTML che definisce la barra in alto del componente es :  HTML Query :  Ricerca per codice BR Schema :  Geografico BR Filtro :   BR Order :   BR  /HTML " Obbligatorio="SI" Molteplicità="1"/>
</QRY>
<QRYLIST Descrizione="Contiene una lista di oggetti che identifica la lista dei possibili tipi di ricerca (è il contenuto del menu a tendina da Query)" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</QRYLIST>
</Program>
<Pres Descrizione="Definisce come deve essere mostrato il questionario" Obbligatorio="SI" Molteplicità="1"/>
<Resp Descrizione="Definisce come utilizzare l'XML in input al questionario e come formattare l'XML in output al questionario delle risposte " Obbligatorio="SI" Molteplicità="1"/>
<Rules Descrizione="Definisce il tipo di esecuzione della regola" Obbligatorio="" Molteplicità=""/>
</Setup>
<Contenuto Descrizione="All'interno del campo CDATA contiene testo libero racchiuso tra parentesi quadre Es :  [CDATA[Testo libero multiriga] ]. Tale testo può contenere caratteri alfanumerici qualsiasi; l'interpretazione di tale testo libero è a carico del modulo di destinazione" Obbligatorio="NO" Molteplicità="1"/>
<Messaggi Descrizione="Contiene eventuali messaggi di errore generati durante l'elaborazione compiuta dal servizio. Tali messaggi hanno un livello di importanza definito 0-100; quindi vengono registrate anche le semplici segnalazioni (livello es. 0)" Obbligatorio="SI" Molteplicità="1">
<Messaggio Descrizione="Contiene le caratteristiche di un singolo messaggio di errore (se presente)" Obbligatorio="NO" Molteplicità="*"/>
</Messaggi>
<Esito Descrizione="Esito dell'elaborazione del servizo. In caso di errori/anomalie si trova una descrizione dettagliata nell'elemento Messaggi" Obbligatorio="SI" Molteplicità="1"/>
</UIDoc>
<Risposte Descrizione="" Obbligatorio="" Molteplicità="">
<Risposta Descrizione="" Obbligatorio="" Molteplicità=""/>
<DATI Descrizione="" Obbligatorio="" Molteplicità=""/>
</Risposte>
<Key Descrizione="Contiene nei sottoelementi K1, K2, K3 le chiavi di riferimento del documento." Obbligatorio="NO" Molteplicità="1">
<K1 Descrizione="Chiave di riferimento del documento" Obbligatorio="SI" Molteplicità="1"/>
<K2 Descrizione="Chiave di riferimento del documento" Obbligatorio="NO" Molteplicità="1"/>
<K3 Descrizione="Chiave di riferimento del documento" Obbligatorio="NO" Molteplicità="1"/>
</Key>
<Buttons Descrizione="Gestisce, attraverso la presenza di elementi Button (da 1 a 3), delle funzioni di Salva, Salva con Nome e Elimina" Obbligatorio="NO" Molteplicità="1">
<Button Descrizione="Caratteristiche del bottone" Obbligatorio="SI" Molteplicità="*"/>
</Buttons>
<OpzioneOggetti Descrizione="" Obbligatorio="" Molteplicità=""/>
<Proprieta Descrizione="" Obbligatorio="" Molteplicità=""/>
<Layout Descrizione="Contiene il layout della sezione principale della scheda, con il posizionamento delle sottoschede definito nell'elemento figlio 'Sez'" Obbligatorio="SI" Molteplicità="1">
<Sez__InLayout Descrizione="Elemento di definizione del posizionamento di una sottoscheda all'interno della scheda" Obbligatorio="SI" Molteplicità="*">
<Sez__Definizione Descrizione="Contiene la definizione della scheda attraverso gli elementi figli (almeno uno) ' Sub ' ">
<Sub Descrizione="Definizione di una sottoscheda" Obbligatorio="SI" Molteplicità="Almeno 1">
<SCH Descrizione="Definizione di una scheda" Obbligatorio="NO" Molteplicità="*">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__SCH Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</SCH>
<HTM Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da una pagina HTML" Obbligatorio="NO" Molteplicità="1">
<Dati Descrizione="Definizione dei dati associati" Obbligatorio="NO" Molteplicità="1">
<UIDoc__HTM Descrizione="Contiene il riferimento al documento che deve essere visualizzato" Obbligatorio="SI" Molteplicità="1">
<Links Descrizione="Contiene i collegamenti ai documenti" Obbligatorio="SI" Molteplicità="1">
<Link Descrizione="Indica il percorso per individuare il documento da visualizzare" Obbligatorio="SI" Molteplicità="*"/>
</Links>
</UIDoc__HTM>
</Dati>
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="NO" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
</HTM>
<IMG Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da un'immagine" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__IMG Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</Dati>
</IMG>
<MAT Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da una matrice" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__MAT Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</MAT>
<TRE Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da un albero" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__TRE Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
<Base__TRE Descrizione="Contiene l'elenco degli elementi dell'albero" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Singolo oggetto appartenente all'albero che deve essere visualizzato" Obbligatorio="NO" Molteplicità="*"/>
</Base__TRE>
</TRE>
<DYN Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è di tipo dinamico" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__DYN Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</DYN>
<TRA Descrizione="" Obbligatorio="" Molteplicità="">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__TRA Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</TRA>
<CHA Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è di tipo chart" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__CHA Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</CHA>
<BTN Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da una bottoniera" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__BTN Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</Dati>
</BTN>
<LAB Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da label" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__LAB Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1">
<Oggetto Descrizione="Racchiude le caratteristiche di ciascun oggetto all'interno di un albero" Obbligatorio="NO" Molteplicità="*"/>
</Dati>
</LAB>
<SEM Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da un semaforo" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__SEM Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione dei dati associati" Obbligatorio="NO" Molteplicità="1">
<Elemento Descrizione="Indica le caratteristiche del semaforo/del cruscotto" Obbligatorio="" Molteplicità=""/>
</Dati>
</SEM>
<GAU Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da un cruscotto" Obbligatorio="NO" Molteplicità="1">
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__GAU Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione dei dati associati" Obbligatorio="NO" Molteplicità="1">
<Elemento Descrizione="Indica le caratteristiche del semaforo/del cruscotto" Obbligatorio="" Molteplicità=""/>
</Dati>
</GAU>
<IML>
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="SI" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
<Setup__IML Descrizione="Impostazione delle caratteristiche della sezione e del setup del contenuto" Obbligatorio="SI" Molteplicità="1"/>
<Dati Descrizione="Definizione della funzione associata" Obbligatorio="SI" Molteplicità="1"/>
</IML>
<PDF Descrizione="Indica, all'interno di una scheda, che il contenuto della sezione è costituito da un documento in formato pdf" Obbligatorio="NO" Molteplicità="1">
<Dati Descrizione="Definizione dei dati associati" Obbligatorio="NO" Molteplicità="1">
<UIDoc__PDF Descrizione="Contiene il riferimento al documento che deve essere visualizzato" Obbligatorio="SI" Molteplicità="1">
<Links Descrizione="Contiene i collegamenti ai documenti" Obbligatorio="SI" Molteplicità="1">
<Link Descrizione="Indica il percorso per individuare il documento da visualizzare" Obbligatorio="SI" Molteplicità="*"/>
</Links>
</UIDoc__PDF>
</Dati>
<Targets Descrizione="Include le regole che regolano la dinamicità indotta tra sezioni" Obbligatorio="NO" Molteplicità="1">
<Target Descrizione="Contiene la definizione dell'induzione di dinamicità tra sezioni" Obbligatorio="SI" Molteplicità="1"/>
</Targets>
</PDF>
</Sub>
</Sez__Definizione>
</Sez__InLayout>
</Layout>
<Actions Descrizione="" Obbligatorio="" Molteplicità="">
<Action Descrizione="" Obbligatorio="" Molteplicità=""/>
</Actions>
<Contenuto Descrizione="All'interno del campo CDATA contiene testo libero qualsiasi racchiuso tra parentesi quadre Es :  [CDATA[Testo libero multiriga] ] la cui interpretazione è a carico del modulo di destinazione" Obbligatorio="NO" Molteplicità="1"/>
<Messaggi Descrizione="Contiene eventuali messaggi di errore generati durante l'elaborazione compiuta dal servizio." Obbligatorio="SI" Molteplicità="1">
<Messaggio Descrizione="Contiene le caratteristiche di un singolo messaggio di errore" Obbligatorio="NO" Molteplicità="*"/>
</Messaggi>
<Esito Descrizione="Esito dell'elaborazione del servizo. In caso di errori/anomalie si trova una descrizione dettagliata nell'elemento Messaggi" Obbligatorio="SI" Molteplicità="1"/>
</UiSmeup>
<Base Descrizione="VECCHIO - In sostituzione deve essere utilizzato UiSmeup -"/>
</Xml>
