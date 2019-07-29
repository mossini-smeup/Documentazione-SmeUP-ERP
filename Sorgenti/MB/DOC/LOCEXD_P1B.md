## Versione 1.2.p 25/05/2005

- Completato l'autofit delle colonne nella matrice nel caso di diversi stili.
- Risolto un problema che causava un "Access Violation" sul cambio di nodo in un albero, nel caso di consultazione della documentazione in HTML.
- Risolto un problema che si presentava all'apertura di documenti HTML e che causava un loop nella creazione delle sottosezioni.
- Aggiunto un pulsante nella bottoniera del grafico per abilitare/disabilitare la visione in una singola pagina di tutti i punti per serie.
- Risolto un problema nella assegnazione a variabili di stringhe contenenti delle parentesi tonde. Il valore da assegnare veniva "tagliato" alla prima parentesi tonda.
- Risolto un problema che avveniva alla chiusura di una scheda contenente una sezione HTML con barra di progressione. Alla distruzione della barra appariva un messaggio di Access Violation.
- Risolto un problema che generava un messaggio di "Index out of Bound" al cambio cella di una matrice di inserimento con una sola cella navigabile.

## Versione 1.2.q 30/05/2005

- Risolto un problema nella chiamata a funzione per la stampa della scheda. Se effettuata tramite la pressione del tasto F23 (Shift+F11) veniva interpretata come una richiesta di apertura in nuova finestra a causa della pressione di SHIFT, mandando in crisi lo stack delle finestre.
- Aggiunta la possibilità di scatenare l'evento change alla pressione del tasto tab, nelle matrici di inserimento.
- Modifica dei popup della matrice. Per mettere in maggiore evidenza le funzioni di totalizzazione, le voci di  menù sono state aggiunte anche al menù dell'header delle colonne oltre che nel footer.
- Sistemato un problema della matrice che bloccava la scheda, nel caso venisse passato un XML di una matrice con valori sballati di date e numeri o campi non compatibili con la definizione delle colonne. Ora vengono visualizzati i campi che è possibile visualizzare e viene generato un messaggio di errore che informa della presenza di un XML non coerente.
- Rimossa l'icona gialla che veniva visualizzata nella task bar di Windows, pur non essendo associata ad alcuna finestra attiva.
- Sistemato un problema sulle tabelle con sottotabelle correlate nel componente matrice. La scheda si bloccava in alcuni casi non permettendo la visualizzazione dei dati. Irrobustita anche in questi casi la visualizzazione dei dati in presenza di un XML di matrice non coerente.
- Uniformato nello stile e nel funzionamento il popup per la chiusura del client delphi, sulla nuova icona sulla traybar di windows.

## Versione 1.2.r 30/05/2005

- Risolto un problema sulla risoluzione delle variabili. Se veniva introdotto del testo incluso tra parentesi quadre, in alcuni casi particolari non venivano risolte tutte le variabili successive inficiando il funzionamento complessivo della scheda.
- Rimossa la voce Modifica Script dal menù delle sottosezioni.
- Aggiunta la voce di menù della sottosezione "Scheda Servizio" che richiama direttamente la scheda del servizio usato nella sottosezione in una nuova finestra. Se il servizio non è disponibile la voce è disabilitata.
- Aggiunta la gestione delle autorizzazioni da menù. I menù verranno pertanto abilitati o disabilitati in base alle autorizzazioni dell'utente.
- Risolto un problema del componente HTM che interpretava erroneamente la documentazione come un file XML in presenza dei tag di codifica.

### Operata la suddivisione in due versioni Stabile e Sviluppo.

## Versione 1.3.a 01/06/2005

- Aggiunto l'attributo "Expanded" nel setup del componente albero per condizionarne l'emissione in modo espanso o collassato. (Expanded="Yes/No". Default : Yes).
- Aggiunto l'attributo "Expanded" nel setup del componente matrice per condizionarne l'emissione in modo espanso o collassato. (Expanded="Yes/No". Default : No).
- Aggiunto l'attributo "AlignTotal" per condizionare l'emissione di una matrice con totali parziali allineati alle colonne. (AlignTotal="Yes/No". Default : No)
- Corretto un errore che provocava un messaggio di "Access Violation"  in fase di inserimento di un record in matrice aggiornabile.
- Corretto un problema sulla interpretazione dei valori numerici in matrice. Ora vengono considerati numerici anche se contenenti spazi prima e/o dopo il numero stesso.
- Modificata la modalità di reperimento di una sottosezione nel caso di sottoschede. Viene ora percorso in senso inverso l'intero albero delle sottoschede alla ricerca della sottosezione. Precedentemente veniva esaminata solo la scheda corrente e in subordine la scheda principale con tutte le sottoschede contenute. Questo poteva portare ad un'errata identificazione della sottosezione nel caso in cui essa fosse presente in una sottoscheda di livello superiore alla sottoscheda contenente la sezione di origine ed esistesse contemporaneamente una sottosezione con nome identico presente in una sottoscheda di un ramo (a sinistra) diverso da quello della sottosezione origine.
- Corretto un errore in visualizzazione dei caratteri CRLF nei nodi di raggruppamento di una matrice con colonne ad intestazione multilinea.
- Aggiunta la gestione delle autorizzazioni nel menù principale della scheda. Verranno abilitate solo le voci per cui l'utente dispone autorizzazione.
- Risolto un problema di esportazione delle celle numeriche con decimali da matrice ad Excel 2003. Veniva perso il separatore decimale.
- Risolto un problema sui bottoni principali della scheda che apparivano o scomparivano in maniera  +non corretta alla selezione di alcune sezioni prive di certe funzionalità.
- Risolto un problema sul dinamismo su sezioni con Title *NONE. Allo scattare del dinamismo veniva visualizzato una etichetta vuota invece che farla somparire.

## Versione 1.4.a 01/06/2005 (Sviluppo)

- Aggiunto l'attributo "Expanded" nel setup del componente albero per condizionarne l'emissione in modo espanso o collassato. (Expanded="Yes/No". Default : Yes).
- Aggiunto l'attributo "Expanded" nel setup del componente matrice per condizionarne l'emissione in modo espanso o collassato. (Expanded="Yes/No". Default : No).
- Aggiunto l'attributo "AlignTotal" per condizionare l'emissione di una matrice con totali parziali allineati alle colonne. (AlignTotal="Yes/No". Default : No)
- Corretto un errore che provocava un messaggio di "Access Violation"  in fase di inserimento di un record in matrice aggiornabile.
- Corretto un problema sulla interpretazione dei valori numerici in matrice. Ora vengono considerati numerici anche se contenenti spazi prima e/o dopo il numero stesso.
- Modificata la modalità di reperimento di una sottosezione nel caso di sottoschede. Viene ora percorso in senso inverso l'intero albero delle sottoschede alla ricerca della sottosezione. Precedentemente veniva esaminata solo la scheda corrente e in subordine la scheda principale con tutte le sottoschede contenute. Questo poteva portare ad un'errata identificazione della sottosezione nel caso in cui essa fosse presente in una sottoscheda di livello superiore alla sottoscheda contenente la sezione di origine ed esistesse contemporaneamente una sottosezione con nome identico presente in una sottoscheda di un ramo (a sinistra) diverso da quello della sottosezione origine.
- Corretto un errore in visualizzazione dei caratteri CRLF nei nodi di raggruppamento di una matrice con colonne ad intestazione multilinea.
- Aggiunta la gestione delle autorizzazioni nel menù principale della scheda. Verranno abilitate solo le voci per cui l'utente dispone autorizzazione.
- Risolto un problema di esportazione delle celle numeriche con decimali da matrice ad Excel 2003. Veniva perso il separatore decimale.
- Risolto un problema sui bottoni principali della scheda che apparivano o scomparivano in maniera non corretta alla selezione di alcune sezioni prive di certe funzionalità.
- Risolto un problema sul dinamismo su sezioni con Title *NONE. Allo scattare del dinamismo veniva visualizzato una etichetta vuota invece che farla somparire.
- Predisposta la scheda per gestire le autorizzazioni anche a livello della bottoniera principale come per il menù principale. Verranno abilitati solo i controlli per cui l'utente dispone autorizzazione.
- Predisposta la scheda per gestire le autorizzazioni su tutte le voci del popup menù delle sottosezioni.

## Versione 1.3.b 07/06/2005

- Modificata la chiamata al servizio per la visualizzazione della scheda del servizio di una sottosezione. Ora viene visualizzata la scheda del servizio e non del programma.
- Risolto un problema che impediva la visualizzazione delle matrici in cui veniva specificata da setup una totalizzazione su una colonna non esistente. Ora la matrice viene visualizzata correttamente ignorando il setup errato.
- Risolto un problema sui bottoni della scheda che si sovrapponevano in certe condizioni con quelli specificati eventualmente da script di scheda.
- Risolto un problema sulle matrici in inserimento. Non tutti i formati dei campi data erano trattati in maniera corretta e generavano errori all'inserimento.

## Versione 1.4.b 07/06/2005 (Sviluppo)

- Modificata la chiamata al servizio per la visualizzazione della scheda del servizio di una sottosezione. Ora viene visualizzata la scheda del servizio e non del programma.
- Risolto un problema che impediva la visualizzazione delle matrici in cui veniva specificata da setup una totalizzazione su una colonna non esistente. Ora la matrice viene visualizzata correttamente ignorando il setup errato.
- Risolto un problema sui bottoni della scheda che si sovrapponevano in certe condizioni con quelli specificati eventualmente da script di scheda.
- Risolto un problema sulle matrici in inserimento. Non tutti i formati dei campi data erano trattati in maniera corretta e generavano errori all'inserimento.
- Aggiunta, nel popup menù di sottosezione, l'indicazione della scheda a fianco della voce "Editor della Scheda".

## Versione 1.3.c 09/06/2005

- Risolto un Access Violation sulla matrice che si verificava alla pressione del tasto destro del mouse su un oggetto indiretto se la colonna era totalizzata.
- Risolto un problema dell'autofit della matrice in caso di matrici con un solo record.
- Risolto un problema sull'autofit delle matrici in cui sono selezionate e visibili serie e assi.
- Risolto un problema sulle variabili nulle, introdotto in una correzione di un altro problema. In alcuni casi le variabili nulle assumevano il valore _NULL_.
- Risolto un problema sulle totalizzazioni delle date che venivano sommate come se fossero celle numeriche nella matrice.
- Risolto un problema che impediva la visualizzazione di matrici senza record. Le intestazioni delle colonne non erano più visibili.


## Versione 1.4.c 09/06/2005 (Sviluppo)

- Risolto un Access Violation sulla matrice che si verificava alla pressione del tasto destro del mouse su un oggetto indiretto se la colonna era totalizzata.
- Risolto un problema dell'autofit della matrice in caso di matrici con un solo record.
- Risolto un problema sull'autofit delle matrici in cui sono selezionate e visibili serie e assi.
- Risolto un problema sulle variabili nulle, introdotto in una correzione di un altro problema. In alcuni casi le variabili nulle assumevano il valore _NULL_.
- Risolto un problema sulle totalizzazioni delle date che venivano sommate come se fossero celle numeriche nella matrice.
- Risolto un problema che impediva la visualizzazione di matrici senza record. Le intestazioni delle colonne non erano più visibili.
- Aggiunte la visualizzazione delle icone delle serie e dell'asse all'apertura della matrice dove definite nell'xml.
- Aggiunta la voce per rimuovere tutte le serie selezionate nell'header popup della matrice.
- Abilitata di default la barra di comando del componente grafico, quando viene richiamato a seguito di una elaborazione di matrice.
- Aggiunta una voce nell'header popup della matrice per abilitare e disabilitare il pannello e le funzioni di totalizzazione.
- Iniziata la ristrutturazione del passaggio da matrice a grafico elaborato (selezione runtime di assi, serie etc.).
- Iniziata l'introduzione delle funzioni "Preferiti" e "Carrello" nella scheda.

## Versione 1.4.d 20/06/2005 (Sviluppo)

- Aggiunta la possibilità di inserire nel carrello dei preferiti oggetti o funzioni tramite il popup menù della scheda, analogamente a come è possibile nel Java Client
- Rimossa l'apertura della gestione delle immagini sulla scheda alla pressione del tasto F4.
- Implementata la gestione del richiamo della ricerca con il tasto F4 dalla scheda, analogamente a quanto accade nel Java Client.
- Sistemato un problema sulla assegnazione del tipo di sezione alla apertura di una nuova scheda. Nel caso in cui tutte le sottosezioni venivano caricate con caricamento differito veniva assegnato un tipo foglio immagine.
- Sistemato un problema sulla visualizzazione dei bottoni di scheda corretti in correlazione con il problema elencato sopra. Erano abilitati dei bottoni non coerenti con il tipo di sottosezione.
- Ora la pressione dei tasti funzione assegnati ai bottoni funzionano solo se il bottone è visibile. In alcuni casi era possibile usare le funzionalità dei bottoni usando il tasto funzione associato anche se il bottone non era abilitato.
- Risolto un piccolo baco sui tasti funzione associati ai bottoni di scheda di Expand e Collapse degli alberi. I tasti funzione erano invertiti.
- Corretto un problema con il contatore delle Richieste/Risposte che contava erroneamente alcune richieste "extra".
- Risolto un problema che generava un AV nel richiamare il menù popup del footer di una matrice nel caso fosse abilitato runtime tramite la voce Abiltà del menù "Totalizzazioni".
- Aggiunta una "progress bar" nella form di ogni scheda indicante la progressione delle chiamate in modo visivo.
- Sistemato un problema sulla matrice nella selezione degli assi in presenza di assi multipli nell'xml. Non veniva marcato correttamente il secondo asse.
- Modificato radicalmente il codice delle matrici di aggiornamento. E' stata aggiunta la possibilità di aggiornare i dati anche a matrice raggruppata. Le comunicazioni con AS sono state semplificate.

## Versione 1.4.e 20/06/2005 (Sviluppo)

- Corretto un errore di tipo AV alla pressione del tasto F5 o del bottone di Refresh, introdotto nell'aggiungere la Progress Bar.
- Corretto un errore di tipo AV alla pressione del tasto Ctrl-F5 introdotto nell'aggiungere la Progress Bar.

## Versione 1.3.d 23/06/2005

- Risolto un problema che generava un access violation dell'albero dinamico che avveniva quando non era definito il When="Expand". Si è rivelato un errore sulla funzione di scambio sincrono di XML, nel caso in cui la chiamata mandata fosse nulla.

## Versione 1.4.f 23/06/2005 (Sviluppo)

- Aggiunta la gestore dei setup multipli. E' ora possibile per ogni componente specificare più righe di setup e scegliere runtime quale applicare al componente.
- E' presente una bottoniera che visualizza e permette di scegliere i setup da applicare al componente in caso sia presente più di un setup.
- Modificato l'aspetto e il funzionamento della progress bar. Ora viene mostrato esplicitamente l'istante di "fine caricamento".
- Risolto un problema che generava un access violation dell'albero dinamico che avveniva quando non era definito il When="Expand". Si è rivelato un errore sulla funzione di scambio sincrono di XML, nel caso in cui la chiamata mandata fosse nulla.
- Aggiunta la possibilità di usare le variabili su Where e Load nello script di scheda. E' così possibile scrivere schede generiche e usarle come template in modo facile.
- Aggiunto un l'attributo "IconeTesta" nel setup della matrice per rimuovere le icone in testata in caso si volesse una matrice particolarmente semplice e veloce. I valori validi per l'attributo sono Yes/No (Default :  Yes).
- Aggiunto un attributo di setup per la bottoniera in modo da potere specificare dove allineare il testo. L'attributo è "Align" e i valori consentiti sono :  Left/Right/Top/Bottom/Center (Default :  Left)
- Risolto un problema sulle label. I caratteri speciali come & non venivano correttamente visualizzati.

## Versione 1.3.e 24/06/2005

- Risolto un problema sui bottoni della scheda che non funzionavano se il componente non aveva esplicitamente il fuoco.  Problema risolto per tutti i bottoni e per tutti i componenti. Collateralmente il problema sulla stampa della matrice che a volte non funzionava è stato risolto.

## Versione 1.4.g 23/06/2005 (Sviluppo)

- Risolto un problema sui bottoni della scheda che non funzionavano se il componente non aveva esplicitamente il fuoco.  Problema risolto per tutti i bottoni e per tutti i componenti. Collateralmente il problema sulla stampa della matrice che a volte non funzionava è stato risolto.
- E' stata aggiunta al menù della scheda la voce "Editor dell Scheda". In questo modo riesco ad accedere allo script anche se è errato o in assenza di tab.
- Aggiunto un attributo nel setup sulla bottoniera in modo da potere definire dei bottoni disposti orizzontalmente. L'attributo è "Horiz" con valori ammessi Yes/No (Default :  No).

## Versione 1.4.h 01/07/2005 (Sviluppo)

- Completata gestione dei setup "globali". All'apertura di smetray viene ora richiamata una scheda denominata  J3_SET_STD nella quale sono definiti i setup globali. i setup globali possono essere utilizzati come parent di ogni setup ma non sono utilizzabili "da soli".
- Corretto errore AV su gestione sezioni Virtuali che impediva il corretto funzionamento delle schede in "transazione"
- Completata prima fase gestione setup utente di matrice. Viene ora data la possibilità di salvare (da buttonbar o a popup) la "vista" corrente di una matrice. Essa diventa automaticamente il setup di default dell'utente che ha comunque la possibilità di "switchare" tra gli altri setup preimpostati. I file di setup vengono memorizzati in "<LoocupDir>\LOOCUP_SET\EXD\<Username>\<scheda>_<Componente>_<IdSubSezione>.xml"

## Versione 1.3.f 05/07/2005

- Risolto un problema che impediva la corretta visualizzazione dei totali di default della matrice in caso di campi non numerici sulla funzione Count.


## Versione 1.4.i 04/07/2005 (Sviluppo)

- Modificata l'apertura dell'editor della scheda :  Ora apre la scheda che contiene la sottosezione selezionata e non più solo la scheda visualizzata.
- Modificato il sistema di memorizzazione dei setup utente delle matrici. I nomi dei file in cui vengono memorizzati contengono i nomi delle schede che ospitano il componente matrice e non più il nome della scheda visualizzata.
- Risolto un problema che impediva la corretta visualizzazione dei totali di default della matrice in caso di campi non numerici sulla funzione Count.

## Versione 1.4.l 13/07/2005 (Stabile)

- Risolto un problema che generava un AV alla pressione dei tasti Collapse ed Expand di alberi e matrici nel caso in cui nella sottosezione fossero pesenti più controlli.
- Modificata la gestione dei setup multipli con utente. Ora il setup dell'utente se viene creato a partire da un altro setup con nome, eredita le sue proprietà.
- Modificata la matrice, sul raggruppamento con totali allineati alle colonne. I totali vengono mostrati incolonnati e senza footer se il nodo è espanso.
- Modificato il salvataggio del setup utente per manteneva tutte le impostazioni della matrice. In particolare le totalizzazioni che prima non erano salvate correttamente.
- Risolto un problema di fuochi che si verificava sull'F12 da finestra Java a finestra Delphi.
- Aggiunti gli attributi relativi alla scelta del font, Tipo, colore, e dimensione nel setup del componente Cruscotto.
- Risolto un problema con l'attributo Load nei setup utente della matrice. In alcuni casi il caricamento differito non passava mai ad immediato.
- Risolto un problema sulla bottoniera dei setup multilpi che non veniva sincronizzata con il menù contestuale all'aggiornamento della sottosezione.
- Risolto un errore che impediva la corretta visualizzazione dell'impostazione FontSize del semaforo.
- Risolto un problema che bloccava completamente Smetray se venivano definiti dei campi di matrice più lunghi di 250 caratteri. Il limite dei 250 caratteri rimane, ma ora i campi vengono troncati.
- Risolto un problema di apertura dell'editor della scheda in caso di Scheda senza sottoschede.
- Risolto un problema di ricerca della scheda corretta alla creazione delle sottosezioni.
- Modificata la gestione della voce di menù "Editor della Scheda". Ora se la sottosezione non è caricata la voce è inibita.
- Risolto un errore sulla definizione e lettura da parte di Smetray dell'attributo UpdSrv nel setup della matrice.
- Ripristinato il salvataggio dell'ordine, dei raggruppamenti, del sorting e dei totali delle colonne del setup utente.

## Versione 1.5.a 13/07/2005 (Sviluppo)

- Risolto un problema che generava un AV alla pressione dei tasti Collapse ed Expand di alberi e matrici nel caso in cui nella sottosezione fossero pesenti più controlli.
- Modificata la gestione dei setup multipli con utente. Ora il setup dell'utente se viene creato a partire da un altro setup con nome, eredita le sue proprietà.
- Modificata la matrice, sul raggruppamento con totali allineati alle colonne. I totali vengono mostrati incolonnati e senza footer se il nodo è espanso.
- Modificato il salvataggio del setup utente per manteneva tutte le impostazioni della matrice. In particolare le totalizzazioni che prima non erano salvate correttamente.
- Risolto un problema di fuochi che si verificava sull'F12 da finestra Java a finestra Delphi.
- Aggiunti gli attributi relativi alla scelta del font, Tipo, colore, e dimensione nel setup del componente Cruscotto.
- Risolto un problema con l'attributo Load nei setup utente della matrice. In alcuni casi il caricamento differito non passava mai ad immediato.
- Risolto un problema sulla bottoniera dei setup multilpi che non veniva sincronizzata con il menù contestuale all'aggiornamento della sottosezione.
- Risolto un errore che impediva la corretta visualizzazione dell'impostazione FontSize del semaforo.
- Risolto un problema che bloccava completamente Smetray se venivano definiti dei campi di matrice più lunghi di 250 caratteri. Il limite dei 250 caratteri rimane, ma ora i campi vengono troncati.
- Risolto un problema di apertura dell'editor della scheda in caso di Scheda senza sottoschede.
- Risolto un problema di ricerca della scheda corretta alla creazione delle sottosezioni.
- Modificata la gestione della voce di menù "Editor della Scheda". Ora se la sottosezione non è caricata la voce è inibita.
- Risolto un errore sulla definizione e lettura da parte di Smetray dell'attributo UpdSrv nel setup della matrice.
- Ripristinato il salvataggio dell'ordine, dei raggruppamenti, del sorting e dei totali delle colonne del setup utente.

## Versione 1.5.b 25/07/2005 (Sviluppo)

- Risolto un problema sulla massimizzazione di sezioni di tipo htm, relative alla documentazione e loro contenitori.
- Modificata la voce "Visualizza come Editor" in modo da aprire una nuova finestra invece che sostituire quella di provenienza.
- Aggiunto l'attributo di setup delle sottosezioni "SetupName" che viene usato, se presente, per identificare un nome con cui viene salvato il setup.
- Aggiunta la gestione delle larghezze delle colonne nel salvataggio utente delle matrici.
- Aggiunta la gestione del salvataggio dei filtri nel setup utente della matrice.
- Modificata la gestione delle richieste dati ad AS400 in modo sincrono in caso di creazione di una scheda già in corso.
- Risolto un problema sulle matrici di aggiornamento, nei campi con oggetto variabile. Non veniva preso l'oggetto corretto.
- Modificato il sistema di filtri della matrice. Ora vengono visualizzati solo una volta gli elementi che si ripetono e solo i valori già filtrati.
- Introdotto il salvataggio dei setup su B£MEDE0F.
- Risolto un problema che generava un access violation al caricamento di una scheda con script errato.
- Aggiunto l'attributo per attivare/disattivare il caricamento del Setup Utente di una sottosezione. UserSetup On/Off, Default=Off.
- Risolto un problema di duplciazione dell'ultima colonna delle matrici in esportazione in excel.
- Risolto un AV che avveniva al salvataggio dei setup (sia da client che da AS) in caso si prendesse come base un setup utente già esistente.
- Aggiunta la possibilità di gestire con i semafori valori in virgola mobile.

## Versione 1.5.c 24/08/2005 (Sviluppo)

- Aggiunta la possibilità di inserimento, modifica, cancellazione (e quindi annullamento di tali operazioni) nella matrice aggiornabile, tramite l'utilizzo dell'attributo di setup DeferUpd. (Yes/No, Default=No). Le modifiche vengono inviate tutte assieme all'AS400 e sono marcate con un triangolino rosso se non ancora inviate, verde se già inviate.
- Modificata la gestione del modulo di esportazione in Excel. Il cambio di strutta ha aumentato le performance, non necessita di comunicazione esterna a Smetray e pone le basi per gli sviluppi futuri.
- Aggiunto l'attributo NoTransVar a G.DIN per bloccare la copia delle variabili di sezione da una sezione all'altra allo scattare di un dinamismo. (NoTransVar :  Yes/No, Default=No).
- Fissati alcuni bug minori.

## Versione 1.5.d 06/09/2005 (Sviluppo)

- Aggiunta la gestione del filtering automatico nell'esportazione in Excel di una matrice.
- Aggiunta la gestione dell'ordinamento nell'esportazione in Excel di una matrice. Il sorting ascendente e discendente di una colonna nel foglio esportato in excel segue le impostazioni della matrice.
- Sistemato un problema relativo al nome del file (invalido) nel caso di esportazione come SpreadSheetML di una matrice.
- Aggiunta la gestione delle colonne invisibili (sia runtime che designtime) nell'esportazione in Excel di una matrice. In caso una colonna venisse rimossa (resa invisibile) la colonna non viene esportata ed elaborata.
- Risolto un problema sulla matrice di Aggiornamento in setup multipli. Un flag non veniva correttamente resettato al passaggio da setup di aggiornamento a uno di sola visualizzazione impedendo l'esportazione in Excel.
- Risolto un problema sull'emissione del messaggio di errore in caso di dati sbagliati per una tabella/grafico e mancata visualizzazione degli stessi.
- Aggiunto l'attributo XlsColor nel setup di matrice. Se abilitato l'esportazione su foglio Excel viene effettuata mantenendo anche i colori della matrice.
(XlsColor=Yes/No, Default=No)
- Aggiunta la gestione dei totali nell'esportazione in Excel di una matrice. Nel foglio non vengono esportati solo i valori dei totali ma vengono generate le formule che li ricavano in base alle impostazioni della matrice esportata.
- Aggiunta la gestione dei filtri personalizzati nel modulo di esportazione in Excel. Vengono esportati anche filtri complessi con condizioni.
- Aggiunta la formattazione dei totali visualizzati nel foglio excel esportato da matrice. Sono formattati in base ai decimali della colonna a cui appartengono.
- Aggiunto da richiesta l'attributo "TitleLock" nel G.DIN per impedire il cambio di titolo della sezione di destinazione. Se l'attributo è abilitato non viene aggiornato il titolo della sezione.(TileLock=Yes/No, Default=No)
- Nella matrice di aggiornamento i valori non modificabili non vengono più forzati in maiuscolo, ma mantengono lo stile originale.
- Modificato il default dei grafici a torta per non visualizzare i marks (etichette di legenda su ogni "fetta").
- Semafori e Cruscotti ora gestiscono i valori in virgola.
- Aggiunta la possibilità di specificare semplici formule matematiche (racchiuse tra graffe) negli attibuti di valori e soglie di semafori e cruscotti. E' stata mantenuta anche la possbilità di usare delle variabili di scheda. E' possibile richiedere la risoluzione di una formula matematica racchiudendo tra parentesi graffe la stessa.

## Versione 1.5.e 21/09/2005 (Sviluppo)

- Cambiato il default dell'attributo XlsColor della matrice. Ora è impostato a Yes.
- Aggiunta l'esportazione completa in SpreadsheetML della matrice anche per Excel 2003, con tutte le caratteristiche già presenti nella versione precedente.
- Risolto un problema sul passaggio da matrice a grafico in caso di date mancanti. Veniva sempre visualizzato un errore di Xml errato.
- Risolto un problema sul passaggio delle date come variabile di sezione, in caso di eventi sulle celle di una matrice. Venivano formattate con il formato standard di loocup. Ora viene preservata la forma iniziale. E' stata comunque aggiunta una variabile CellTx che contiene il valore formattato secondo loocup.
- Risolto un problema di formattazione dei campi nelle matrici in caso di oggetti variabili. Non venivano mantenute le formattazioni negli standard loocup.
- Risolto un problema relativo alla presenza di colonne con codice duplicato nell'xml della matrice. La scheda si bloccava completamente. Ora viene creata una colonna fittizia dal nome Error+Timestamp.
- Aggiunto un messaggio che indica la presenza di colonne sbagliate o duplicate nella matrice.
- Aggiunta l'indicazione di record e campo nel messaggio che indica dati di riga di matrice non corretti.
- Risolti alcuni problemi relativi alla ricerca in campi matriciali con oggetti indiretti. La ricerca, in caso di matrice aggiornabile non sempre funzionava correttamente.
- Aggiunta la gestione dei raggruppamenti anche nell'esportazione in Excel. Nota :  Excel non gestisce i raggruppamenti annidati senza tabelle Pivot. Inoltre l'applicazione dei filtri modifica notevolmente la visualizzazione del raggruppamento. Si consiglia di esportare matrici raggruppate ad un livello, senza filtri attivi e massimo due totali.
- Aggiunti i bordi delle celle nell'esportazione in excel.
- Aggiunta la gestione dei subtotali in caso di esportazione in Excel di una matrice raggruppata.
- Modificata la chiama alla funzione di salvataggio e caricamento di Setup da AS400.

## Versione 1.5.f 27/09/2005 (Stabile)

- Aggiunto l'attributo ShowCmdBar nella script della sottosezione che influisce sulla posizione della della barra dei setup di sezione. I valori possibili sono AUTO/YES/NO/GLOBAL/GLOBALAUTO. Il valore di default è AUTO.
- Disabilitata la voce Visualizza XML sia nel popup di sezione sia nel menù principale nel caso in cui sia presente il caricamento differito e non sia ancora stato caricato l'XML : 
- Modificata la gestione delle date in matrice. Le date in formato diverso da D8*YYMD e D8*DMYY sono trattate come stringhe.
- Modificata la commandbar dei setup in modo da potere essere più customizzabile. Risolto un problema che impediva la corretta visualizzasione dei pulsanti da POPUP nella main bar.
- Rilasciata la prima versione del gestore dei setup multipli di componente dell'utente.
- Aggiunto la voce nel popup di sottosezione, relativa al gestore dei setup utente.
- Aggiunte le hotkeys relative ai bottoni della command bar di setup. Rispettivamente F7 per il salvataggio di default e F17 per aprire il gestore dei setup.

## Versione 1.6.a 27/09/2005 (Sviluppo)

- Aggiunto l'attributo ShowCmdBar nella script della sottosezione che influisce sulla posizione della della barra dei setup di sezione. I valori possibili sono AUTO/YES/NO/GLOBAL/GLOBALAUTO. Il valore di default è AUTO.
- Disabilitata la voce Visualizza XML sia nel popup di sezione sia nel menù principale nel caso in cui sia presente il caricamento differito e non sia ancora stato caricato l'XML : 
- Modificata la gestione delle date in matrice. Le date in formato diverso da D8*YYMD e D8*DMYY sono trattate come stringhe.
- Modificata la commandbar dei setup in modo da potere essere più customizzabile. Risolto un problema che impediva la corretta visualizzasione dei pulsanti da POPUP nella main bar.
- Rilasciata la prima versione del gestore dei setup multipli di componente dell'utente.
- Aggiunto la voce nel popup di sottosezione, relativa al gestore dei setup utente.
- Aggiunte le hotkeys relative ai bottoni della command bar di setup. Rispettivamente F7 per il salvataggio di default e F17 per aprire il gestore dei setup.

## Versione 1.5.g 29/09/2005 (Stabile)

- Risolto un problema relativo alla formattazione delle date contenute nelle variabili relative alle celle  e che si generano quando scatta un evento relativo alla matrice. Le variabili dei campi ora vengono riempite con i valori dei dati originali che provengono da AS400.
- Invertita, per comprensibilità, l'impostazione tramite wizard dell'attributo ReadOnly del setup di matrice.
- Risolto un problema relativo ai filtraggi di colonne numeriche nell'esportazione in Excel, che impediva la corretta visualizzazione dei dati nel foglio di calcolo.
- Implementata una User Request relativa al trattamento delle celle numeriche il cui valore è nullo, nell'esportazione in Excel. Ora non vengono visualizzate.

## Versione 1.6.b 29/09/2005 (Sviluppo)

- Risolto un problema relativo alla formattazione delle date contenute nelle variabili relative alle celle  e che si generano quando scatta un evento relativo alla matrice. Le variabili dei campi ora vengono riempite con i valori dei dati originali che provengono da AS400.
- Invertita, per comprensibilità, l'impostazione tramite wizard dell'attributo ReadOnly del setup di matrice.
- Risolto un problema relativo ai filtraggi di colonne numeriche nell'esportazione in Excel, che impediva la corretta visualizzazione dei dati nel foglio di calcolo.
- Implementata una User Request relativa al trattamento delle celle numeriche il cui valore è nullo, nell'esportazione in Excel. Ora non vengono visualizzate.
- Modificata la gestione del database del componente matrice. Ora viene salvato temporaneamente su disco per ovviare a problemi di dimensioni in memoria.
- Risolto un memory leak nel grafico che si verificava alla chiusura dello stesso. Non veniva liberata la memoria allocata per la tabella dei dati in memoria.
- Risolto un memory leak nella matrice e nel grafico che si verificava alla chiusura. Non veniva liberata la memoria allocata per le informazioni di colonna e riga.

## Versione 1.6.c 30/09/2005 (Sviluppo)

- Modificata la gestione dei dati tabellari per matrice e grafico. Il sistema prevede la scrittura in memoria fino a 30.000 celle. Se la matrice supera le 30.000 celle viene emesso un avviso e il database viene scritto su disco.

## Versione 1.6.d 11/10/2005 (Sviluppo)

- Risolto un problema che impediva la pressione di CTRL-F7 nelle matrici.
- E' ora possibile creare una immagine di qualsiasi grafico premendo l'apposito bottone.
- La stampa della scheda ora prevede una versione del grafico fedele all'originale.
- Smetray è ora in grado di gestire servizi interni. L'unico implementato è quello relativo alla stampa del grafico.
- Risolto un problema sulla scrittura su disco delle matrici con più di 30000 celle.
- Risolto un problema di visualizzazione delle finestre massimizzate che venivano traslate di alcuni millimetri.
- Risolto un problema che bloccava la scheda in caso di apertura di grafici i cui dati derivano da tabelle con inversione.
- L'evento Expand ora non scatta più alla chiusura di un nodo già espanso di un albero.
- Modificata la gestione delle comunicazioni della matrice aggiornabile. E' possibile modificare campi di altri record dal servizio AS400 e impostare delle variabili a qualunque livello. Riferirsi alla documentazione del servizio.
- Modificata la gestione dell'xml di tutti i componenti. E' ora possibile specificare nell'XML del singolo componente della variabili di qualsiasi livello.
- Ora viene effettuata la risoluzione delle variabili anche in tutti gli attributi ID e Tit.
- I dinamismi specificati con G.DIN vengono ora fatti scattare anche in caso di sezioni massimizzate a patto che non vi sia alcun where specificato per quell'evento.
- Cambiata completamente la barra dei bottoni generale della scheda per essere uguale a quella delle finestre Java. Aggiunti anche alcuni bottoni e funzionalità.

## Versione 1.5.i 13/10/2005 (Stabile)

- Risolto un problema che impediva la pressione di CTRL-F7 nelle matrici.
- L'evento Expand ora non scatta più alla chiusura di un nodo già espanso di un albero.
- I dinamismi specificati con G.DIN vengono ora fatti scattare anche in caso di sezioni massimizzate a patto che non vi sia alcun where specificato per quell'evento.
- Risolto un problema che impediva l'esportazione di una matrice in Excel se la chiamata era esterna o eseguita attraverso la voce di menù "Avvia modulo da File XML".
- Risolto un problema che generava un messaggio di Access Violation alla pressione del tasto "Stampa Matrice" se la matrice aveva una toolbar attiva.

## Versione 1.6.e 13/10/2005 (Sviluppo)

- Risolto un problema che impediva l'esportazione di una matrice in Excel se la chiamata era esterna o eseguita attraverso la voce di menù "Avvia modulo da File XML".
- Risolto un problema che generava un messaggio di Access Violation alla pressione del tasto "Stampa Matrice" se la matrice aveva una toolbar attiva.
- Modificati alcuni meccanismi di gestione interna del componente HTML per aumentarne la stabilità.
- Ora è possibile legarsi alll'evento CHANGE tramite la specifica G.DIN anche in sezioni di tipo HTM. L'evento scatta al completamento del caricamento di una pagina.

## Versione 1.5.l 14/10/2005 (Stabile)

- Risolto un problema, introdotto nella versione precedente, che impediva l'esportazione di una Matrice in Excel sotto determinate condizioni.

## Versione 1.6.f 14/10/2005 (Sviluppo)

- Risolto un problema, introdotto nella versione precedente, che impediva l'esportazione di una Matrice in Excel sotto determinate condizioni.

## Versione 1.6.g 21/10/2005 (Stabile)

- Risolto un problema che bloccava la risoluzione delle variabili nell'attributo "Title" di G.DIN
- Smetray ora è in grado di utilizzare anche l'active-x di Mozilla per le sezioni di tipo HTM.
- Aggiunto l'attributo Browser nel setup della sezione HTM per la selezione della modalità del browser. Browser IExplorer/Mozilla (Default=IExplorer).
- Cambiato l'agoritmo di compilazione di Excel in fase di esportazione per migliorarne le performance. I tempi di sono abbassati da 2-3 minuti per circa 2000 record, a 10-12 secondi.
- Le date nell'esportazione in Excel ora vengono formattate come date e non più come stringhe. Questo permette sorting e filtering corretto.
- Risolto un problema che aggiungeva una virgola (in fondo al numero) anche nei numeri privi di virgola durante l'esportazione in Excel.
- Risolto un problema nell'esportazione in Excel. In alcuni casi, con totalizzazioni abilitate, veniva perso l'ultimo record.
- Aggiunto un "refresh" automatico della sezione, in ritorno da una chiamata all'editor in caso di editazione di una documento. In questo modo le modifiche verranno visualizzate automaticamente appena usciti dall'editor.
- Risolto un problema che generava un AV su matrici raggruppate, alla pressione del mouse su l'header del raggruppamento.
- Risolto un problema sulla matrice che generava un messaggio di errore errato e successivamente bloccava la scheda, nel caso in cui il campo lunghezza di una colonna non fosse valido.
- Messa a punto e rilascio delle modifiche sulle matrici di aggiornamento in contemporanea al rilascio delle modifiche ai servizi AS400. Riferirsi alla documentazione dei servizi specifici.

## Versione 1.7.a 21/10/2005 (Sviluppo)

- Risolto un problema che bloccava la risoluzione delle variabili nell'attributo "Title" di G.DIN
- Smetray ora è in grado di utilizzare anche l'active-x di Mozilla per le sezioni di tipo HTM.
- Aggiunto l'attributo Browser nel setup della sezione HTM per la selezione della modalità del browser. Browser IExplorer/Mozilla (Default=IExplorer).
- Cambiato l'agoritmo di compilazione di Excel in fase di esportazione per migliorarne le performance. I tempi di sono abbassati da 2-3 minuti per circa 2000 record, a 10-12 secondi.
- Le date nell'esportazione in Excel ora vengono formattate come date e non più come stringhe. Questo permette sorting e filtering corretto.
- Risolto un problema che aggiungeva una virgola (in fondo al numero) anche nei numeri privi di virgola durante l'esportazione in Excel.
- Risolto un problema nell'esportazione in Excel. In alcuni casi, con totalizzazioni abilitate, veniva perso l'ultimo record.
- Aggiunto un "refresh" automatico della sezione, in ritorno da una chiamata all'editor in caso di editazione di una documento. In questo modo le modifiche verranno visualizzate automaticamente appena usciti dall'editor.
- Risolto un problema che generava un AV su matrici raggruppate, alla pressione del mouse su l'header del raggruppamento.
- Risolto un problema sulla matrice che generava un messaggio di errore errato e successivamente bloccava la scheda, nel caso in cui il campo lunghezza di una colonna non fosse valido.
- Messa a punto e rilascio delle modifiche sulle matrici di aggiornamento in contemporanea al rilascio delle modifiche ai servizi AS400. Riferirsi alla documentazione dei servizi specifici.

## Versione 1.6.h 27/10/2005 (Stabile)

- Modificati i meccanismi di elaborazione dell'XML. La nuova gestione ha quasi dimezzato i tempi di elaborazione.
- Modificato il componente cruscotto per avere fino a 5 soglie.
- Aggiunte le voci di Setup del componente cruscotto per specificare soglie, massimi e minimi. I nuovi attributi sono Max, Min, Soglia1, Soglia2, Soglia3 etc. I valori ammessi sono valori numerici anche in virgola.
- Rimosso l'avviso che appariva quando una matrice troppo grande veniva salvata su disco.
- Risolto un problema correlato alla mancata visualizzazione delle matrici che venivano salvate su disco.
- Rilascio di una nuova dll Delphifunctions per la gestione dei fuochi. Risolve il problema che vedeva Looc.up rubare il fuoco anche ad  applicazioni esterne.
- Sistemato un problema che faceva scattare i dinamismi legati all'evento click anche in caso di semplice unexpand dell'albero.

## Versione 1.7.b 27/10/2005 (Sviluppo)

- Modificati i meccanismi di elaborazione dell'XML. La nuova gestione ha quasi dimezzato i tempi di elaborazione.
- Modificato il componente cruscotto per avere fino a 5 soglie.
- Aggiunte le voci di Setup del componente cruscotto per specificare soglie, massimi e minimi. I nuovi attributi sono Max, Min, Soglia1, Soglia2, Soglia3 etc. I valori ammessi sono valori numerici anche in virgola.
- Rimosso l'avviso che appariva quando una matrice troppo grande veniva salvata su disco.
- Risolto un problema correlato alla mancata visualizzazione delle matrici che venivano salvate su disco.
- Rilascio di una nuova dll Delphifunctions per la gestione dei fuochi. Risolve il problema che vedeva Looc.up rubare il fuoco anche ad  applicazioni esterne.
- Sistemato un problema che faceva scattare i dinamismi legati all'evento click anche in caso di semplice unexpand dell'albero.
- Innalzato a 60000 celle il limite prima dello swap su disco del database delle matrici.
- Aggiunta la gestione della selezione delle celle di una matrice tramite tastiera per il copia/incolla.

## Versione 1.6.i 02/11/2005 (Stabile)

- Risolto un Access Violation introdotto con le versioni precedenti al ricaricamento di sottosezioni già caricate, dotate di dinamismi.
- Risolto un problema con l'albero dinamico che in certe condizioni non aggiungeva correttamente i nodi foglia.

## Versione 1.7.c 02/11/2005 (Sviluppo)

- Risolto un Access Violation introdotto con le versioni precedenti al ricaricamento di sottosezioni già caricate, dotate di dinamismi.
- Risolto un problema con l'albero dinamico che in certe condizioni non aggiungeva correttamente i nodi foglia.

## Versione 1.7.d 21/11/2005 (Stabile)

- Sistemato un baco sulle matrici superiori alle 60000 celle (scritte su disco) e il loro ricaricamento. Veniva cancellata la tabella dal sistema operativo in fase di distruzione della matrice generando il blocco completo di smetray.
- Sistemato un problema che bloccava la matrice in presenza di un nodo di tabelle correlate vuoto.
- Aggiunto un attributo di setup nella bottoniera che consente di girare la disposizione dei bottoni.
- Aggiunta la riconversione nel formato originale delle date quando viene chiamata una scheda oggetto.
- Aggiunta la gestione di tutti i formati numerici di Loocup nelle matrici e non solo di NP e NR.
- Risolto un problema che faceva perdere il fuoco a loocup se non veniva chiamata la scheda con il parametro NFI.
- Aggiunto il Popup menù sull'Header Button della matrice e sui campi non tipizzati per permettere il copia e incolla.
- Sistemate la funzionalità di selezione in caso di matrice raggruppata.
- Conclusa la funzionalità di Delete singolo e multiplo, tramite popup nella matrice di inserimento.
- Sistemato un piccolo difetto di allineamento dei numeri nella matrice in caso di colonne con oggetto indiretto.
- Aggiunta la funzionalità di copia su matrici raggruppate, che tiene conto degli indici di raggruppamento.
- Aggiunta la funzionalità di incolla su matrici raggruppate e in inserimento, che tiene conto degli indici di raggruppamento.
- Sistemato un problema sugli indici in caso di duplicazione di record su matrice raggruppata e di inserimento.
- Sostituita completamente la barra delle opzioni del componente matrice.
- Sono stati aggiunti i bottoni di salvataggio per matrice differita, di copia, incolla e cancella nella barra opzioni della matrice.
- Modificata la gestione delle sezioni con dimensione 0% in modo da evitare alcuni errori di tipo AV.
- Aggiunto un handler di messaggi alla matrice per gestire le notifiche di copia ed incolla dall'esterno.
- Sistemata definitivamente la nuova barra dei pulsanti della matrice.
- Modificata la gestione della risposta da AS400 nell'aggiornamento matrice in modo da gestire anche Line Id non dichiarati dal Client. E' possibile quindi forzare il client ad eseguire altre operazioni sui dati da AS.
- Aggiunto l'evento OnUpdate che scatta quando vi è l'aggiornamento di una matrice e non ci sono errori. E' possibile usarlo nel G.DIN chiamando Update.
- Aggiunto il riferimento al codice finestra nelle chiamate generiche tra delphi e java come richiesto da Dario.
- Sistemato il math resolver di smetray che non comparava correttamente date e stringhe che contenevano spazi.


## Versione 1.8.a 21/11/2005 (Sviluppo)

- Sistemato un baco sulle matrici superiori alle 60000 celle (scritte su disco) e il loro ricaricamento. Veniva cancellata la tabella dal sistema operativo in fase di distruzione della matrice generando il blocco completo di smetray.
- Sistemato un problema che bloccava la matrice in presenza di un nodo di tabelle correlate vuoto.
- Aggiunto un attributo di setup nella bottoniera che consente di girare la disposizione dei bottoni.
- Aggiunta la riconversione nel formato originale delle date quando viene chiamata una scheda oggetto.
- Aggiunta la gestione di tutti i formati numerici di Loocup nelle matrici e non solo di NP e NR.
- Risolto un problema che faceva perdere il fuoco a loocup se non veniva chiamata la scheda con il parametro NFI.
- Aggiunto il Popup menù sull'Header Button della matrice e sui campi non tipizzati per permettere il copia e incolla.
- Sistemate la funzionalità di selezione in caso di matrice raggruppata.
- Conclusa la funzionalità di Delete singolo e multiplo, tramite popup nella matrice di inserimento.
- Sistemato un piccolo difetto di allineamento dei numeri nella matrice in caso di colonne con oggetto indiretto.
- Aggiunta la funzionalità di copia su matrici raggruppate, che tiene conto degli indici di raggruppamento.
- Aggiunta la funzionalità di incolla su matrici raggruppate e in inserimento, che tiene conto degli indici di raggruppamento.
- Sistemato un problema sugli indici in caso di duplicazione di record su matrice raggruppata e di inserimento.
- Sostituita completamente la barra delle opzioni del componente matrice.
- Sono stati aggiunti i bottoni di salvataggio per matrice differita, di copia, incolla e cancella nella barra opzioni della matrice.
- Modificata la gestione delle sezioni con dimensione 0% in modo da evitare alcuni errori di tipo AV.
- Aggiunto un handler di messaggi alla matrice per gestire le notifiche di copia ed incolla dall'esterno.
- Sistemata definitivamente la nuova barra dei pulsanti della matrice.
- Modificata la gestione della risposta da AS400 nell'aggiornamento matrice in modo da gestire anche Line Id non dichiarati dal Client. E' possibile quindi forzare il client ad eseguire altre operazioni sui dati da AS.
- Aggiunto l'evento OnUpdate che scatta quando vi è l'aggiornamento di una matrice e non ci sono errori. E' possibile usarlo nel G.DIN chiamando Update.
- Aggiunto il riferimento al codice finestra nelle chiamate generiche tra delphi e java come richiesto da Dario.
- Sistemato il math resolver di smetray che non comparava correttamente date e stringhe che contenevano spazi.

## Versione 1.7.e 15/12/2005 (Stabile)

- Risolti alcuni piccoli problemi che generavano dei messaggi di Access Violation.
- Risolto un AV che si visualizzava quando nell'xml della matrice era descritta una colonna con oggetto variabile non valido.


## Versione 1.8.b 15/12/2005 (Sviluppo)

- Risolto un problema relativo alla stampa della scheda. In particolare alla sezione grafico.
- Aggiunti e abilitati i bottoni per la gestione del Carrello, Setup e visualizzazione della barra del titolo in Smetray.
- Risolti due problemi sull'expression solver di Smetray. Uno relativo ai confronti con campi Data e uno con campi stringa generica.
- Risolto un problema di visualizzazione dei totali nei raggruppamenti della matrice. I totali negativi venivano scritti in modo errato.
- Aggiunto l'attributo SelectItem nel setup dell'albero. E' possibile così specificare il numero del nodo di partenza da caricare.
- Modificata la gestione del Where del G.DIN. In caso di presenza di variabili nel campo Where, ora la risoluzione viene chiamata ogni volta e non solo al caricamento della sezione.
- Sistemati i problemi sui colori delle matrici in caso di configurazioni non predefinite di windows che rendevano illeggibili i dati.
- Sistemata la barra dei pulsanti della matrice in modo che appaiano solo i tasti abilitati a seconda della presenza o meno di setup utente, deferred update etc.
- Sistemato il popup di sezione modo da mostrare solo le voci abilitate a seconda della presenza di setup utente etc.
- Risolto un AV che si verificava se era presente un campo sbagliato con oggetto variabile nella matrice.
- Risolto un problema che generava un AV sulla stampa di alcuni grafici il cui XML conteneva caratteri non ISO.
- Corretto un problema di comunicazione Delphi-Java.
- Modificata la bottoniera principale di smetray. E' ora possibile definire una sezione particolare all'interno della scheda (tramite l'attributo Type(*KETYBOTTOM)), il cui contenuto viene visualizzato all'interno della barra dei pulsanti. In questo modo definendo più sezioni di tipo BTN all'interno di questa è possibile visualizzare dei bottoni analoghi agli ormai obsoleti bottoni UIPOPUP ma che mantengono tutte le proprietà legate alla bottoniera (Dinamismi, Setup etc. etc.).
- Aggiunta la voce di menù di sezione "Visualizza come Nuova Scheda" che apre una scheda in nuova finestra.
- E' stato realizzato un restyling grafico di tutto smetray, che rimuove bordi e imperfezioni grafiche delle etichette di sottosezione.
- Aggiunta la funzionalità di "Colonna calcolata" nelle matrici. E' stato aggiunto nell'xml di definizione di una colonna un attributo Formula in cui si può specificare una operazione ad eseguire. Il sistema è anche in grado di recuperare i valori dei campi di altre colonne e usarli nelle formule.
- Aggiunta la possibilità di creare uno screenshot di ogni singola sottosezione nel menù di sezione.
- Aggiunto un nodo di setup di stampa all'xml della stampa della sezione se specificato nella scheda.
- Aggiunta la funzionalità di salvataggio delle impostazioni di stampa di una matrice. Le impostazioni si dividono in due parti. Una parte di DesignSetup e una parte di PageSetup. La prima parte viene salvata automaticamente. Per la seconda è necessario che l'utente salvi uno stile (voce di menù Print Style) che verrà automaticamente ricaricato alla successiva apertura della preview di stampa. Entrambe le parti vengono salvate su AS nel file b£mede0f usando come chiavi l'utente e un identificativo univoco della matrice.



### Note : 

- Da attenta analisi è risultato che le versioni 6.0.3 e 6.0.4 dell'active-x che viene usato in smetray di Acrobat reader sono"stabili".
  Mentre la versione 6.0 è instabile e causa notevoli problemi in apertura di un PDF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
