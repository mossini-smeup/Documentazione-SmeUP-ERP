# V5B - Tipo riga
 :  : DEC T(ST) K(V5B)
## OBIETTIVO
Definire le caratteristiche relative alle righe ordine.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il tipo riga del documento.
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5BT __Tipo oggetto__
È un elemento della tabella B£G, che identifica l'oggetto (tipo e parametro) a cui è intestata la riga del documento.
Di questa tabella è significativo solo il primo dei tre codici.
Per compatibilità con i programmi che utilizzano questo campo, la lunghezza dev'essere di 2 caratteri.
Se identifica l'oggetto articolo, la griglia deve**obbligatoriamente**chiamarsi AR.
 :  : FLD T$V5BS __Sez. listini riga__
È un elemento della tabella C£V che definisce la sezione usata nel reperimento del listino.
 :  : FLD T$V5BA __Causale movimento magazzino 1__
È un elemento della tabella GMC. Definisce la causale di magazzino utilizzata nella movimentazione di magazzino collegata a questa riga. Se questo campo non è impostato non viene eseguito il collegamento a magazzino.
 :  : FLD T$V5BH __Ente movimentazione 1__
Indica l'ente da inserire nel campo "Codice Ente" del movimento di magazzino legato alla causale 1 (Causale Mov.Mag). I valori possibili sono leggibili tramite ricerca del campo.
 :  : FLD T$V5BO __Ente movimentazione 2__
Indica l'ente da inserire nel campo "Codice Ente" del movimento di magazzino legato alla causale 2 (Causale Mov.Mag.Tra.). I valori possibili sono leggibili tramite ricerca del campo.
 :  : FLD T2V5BH __Ente 2 M.1__
Indica l'ente da inserire nel campo "Codice ente secondario" del movimento di magazzino legato alla causale 1 (Causale Mov.Mag). I valori possibili
sono leggibili tramite ricerca del campo.
 :  : FLD T2V5BO __Ente 2 M.2__
Indica l'ente da inserire nel campo "Codice ente secondario" del movimento di magazzino legato alla causale 2 (Causale Mov.Mag.Tra.). I valori possibili sono leggibili tramite ricerca del campo.
 :  : FLD T$V5BM __Causale movimento di magazzino di trasferimento__
È un elemento della tabella GMC. Se è impostata, ed è impostata la causale precedente, viene eseguito un ulteriore movimento di magazzino con questa causale. Si utilizza nel caso in cui la movimentazione sia 'a partita doppia'.
Se il documento interessato è di trasferimento tra magazzini (è presente il magazzino di trasferimento), questo secondo movimento viene eseguito sul magazzino di trasferimento.
Negli altri casi le due movimentazioni vengono eseguite sullo stesso magazzino e descrivono le situazioni in cui il documento sia di trasferimento da un'area interna ad una esterna o viceversa (ad esempio spedizione o reso in c/to visione).
 :  : FLD T$V5BC __Gest. Prezzo O/N__
Se impostato ad O il prezzo sulla riga è obbligatorio.
 :  : FLD T$V5BE __Gest. Quantità O/N__
Se impostato ad O la quantità sulla riga è obbligatorio.
 :  : FLD T$V5BY __Gruppo Flag Riga__
È un elemento della tabella B£Y. Se valorizzato, alle righe documenti vengono assegnati i flag di questo elemento.
 :  : FLD T$V5BP __Sez. provvigioni riga__
È un elemento della tabella C£V che definisce la sezione usata nel reperimento del listino.
 :  : FLD T$V5BF __Forma/Percorso__
È un elemento della tabella B£Q. Se valorizzato, viene usato come visualizzatore di righe il programma inserito in questa tabella.
 :  : FLD T$V5BD __Presentazione ridotta__
Se non si definisce un percorso e viene inserito il carattere 'S' verrà presentata la riga del documento in modalità ridotta (Standard).
 :  : FLD T$V5BR S/S Stati gestiti
È un sottosettore della tabella B£W che raggruppa gli stati possibili per questo tipo documento.
 :  : FLD T$V5BL __Livello di nascita__
Se, in inserimento della riga del documento, non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$V5BI S/S __Tipo riga dest.__
Serve in abbinamento al campo successivo.
**Attenzione** :  deve essere lo stesso sottosettore del tipo riga di origine (che si sta trattando).
 :  : FLD T$V5B6 __Stato di nascita__
Se impostato, viene proposto questo valore nell'inserimento di una riga documento. Deve appartenere al sottosettore degli stati impostato in questa stessa tabella.
 :  : FLD T$V5B7 __Livello minimo articolo__
È un valore facoltativo e rappresenta il valore minimo del livelllo dell'articolo in inserimento righe (assume ' ')
 :  : FLD T$V5B8 __Livello massimo articolo__
È un valore facoltativo e rappresenta il valore massimo del livelllo dell'articolo in inserimento righe (assume '9')
 :  : FLD T$V5BN __Tipo riga destinaz.__
Se impostato, è il tipo riga (appartenente al sottosettore definito nel campo precedente) in cui si trasformerà una riga di questo tipo nei flussi entrate/uscite.
__Esempio__ :  si può impostare che da una riga di tipo ordine cliente, all'atto dell'evasione, si ottiene una nuova riga
di tipo bolla cliente.
Se non impostato si assumerà lo stesso tipo riga.
 :  : FLD T$V5BG __Param. Cto Lavoro__
È un elemento della tabella V5L :  se codificato (e se la riga è di conto lavoro) definisce i parametri relativi al conto lavoro delle righe di questo tipo (modalità di costruzione degli impegni, di determinazione della disponibilità, ecc..).
 :  : FLD T$V5BQ __Ente sc.C/L__
Indica l'ente da inserire nel campo "Codice Ente" del movimento di magazzino legato alla causale di magazzino, specificata in tabella P5I legata all'elemento della tabella V5L, descritta precedentemente e alla causale di versamento CL.
I valori possibili sono leggibili tramite ricerca del campo.
 :  : FLD T2V5BQ __Ente S2.C/L__
Indica l'ente da inserire nel campo "Codice Ente Secondario" del movimento di magazzino, legato alla causale di magazzino, specificata in tabella P5I legata all'elemento della tabella V5L descritta precedentemente e alla causale di versamento CL.
I valori possibili sono leggibili tramite ricerca del campo.
 :  : FLD T$V5BK __Ogg.in campo operaz.__
Si può indicare l'oggetto che si intende inserire nel campo operazione. Il campo può assumere i seguenti valori : 
- ' ' Facoltativo (l'inserimento non viene controllato);
- 'A' Operazione;
- 'B' Fase del ciclo dell'oggetto;
- 'C' Fase dell'ordine.
 :  : FLD T$V5BW __Tipo mod.riga E/ /U__
Il campo è di immissione facoltativa. Se inserito può assumere i valori 'E' o 'U'. Questi stanno a rappresentare rispettivamente che la riga indica una entrata o una uscita. Questo campo verrà utilizzato per controllare la compatibilità con il tipo modello della testata.
 :  : FLD T$V5BJ __Tipo impegno risorse__
È un elemento della tabella P5S. Definisce la modalità di costruzione degli impegni di risorse collegabili a righe di documenti di questo tipo.
Nel caso in cui l'oggetto in campo operazione sia una fase di ciclo, il tipo ciclo intestatario della fase sarà il tipo ciclo origine impostato nell'elemento della P5S inserita in questo punto.
 :  : FLD T$V5BU __Causale avanzamento__
È un elemento della tabella P5C :  se codificato (e se la riga è di conto lavoro a fronte di un ordine/fase P5), all'atto del collegamento di questa riga, verrà eseguita una dichiarazione di avanzamento di produzione relativa all'ordine/fase di questa riga, con la causale qui impostata, e per una quantità pari alla quantità modificabile di questa riga.
La causale di avanzamento deve avere come tipo origine un ordine di produzione (VP).
 :  : FLD T$V5BZ __Causale versamento C/Lav__
È un elemento della tabella GMC :  se codificato (e se la riga è di conto lavoro a fronte di un ordine/fase P5), all'atto del collegamento di questa riga, se la fase è l'ultima dell'ordine, questa causale sostituirà la causale del movimento di magazzino impostata in precedenza. In questo modo è possibile caricare aree e tipi giacenza diversi a seconda che la fase sia l'ultima o meno, oppure decidere, in fasi intermedie, di non caricare nessuna area (l'oggetto articolo/fase rimane in wip).
Il movimento di magazzino di versamento avrà inoltre l'effetto di aumentare la quantità prodotta dell'ordine di produzione (con eventuale completamento dell'ordine stesso e scarico dei componenti a prelievo automatico).
**NB** :  questo comportamento è indipendente da quanto codificato nel campo causale di avanzamento. Si può quindi eseguire il versamento automatico senza l'avanzamento automatico.
 :  : FLD T$V5B0 __Condizionamento riga__
Se impostato il tipo condizionamento riga nel modello documento, in inserimento di una riga viene controllato che i due valori siano uguali.
__NB__ :  se lasciato vuoto non significa che è una riga sempre valida. È tale solo se il condizionamento sul modello è anch'esso vuoto.
 :  : FLD T$V5B1 __Gestione esponente di modifica__
Se valorizzato, inserisce nella riga del documento, all'atto dell'inserimento e della variazione, l'esponente di modifica dell'oggetto, secondo quanto impostato : 
- '1'  Data documento;
- '2'  Data consegna richiesta riga;
- '3'  Data consegna confermata riga.
- '4'  Come 1 senza ricalcolo se presente doc.origine;
- '5'  Come 2 senza ricalcolo se presente doc.origine;
- '6'  Come 3 senza ricalcolo se presente doc.origine.
 :  : FLD T$V5B2 __Categoria parametri esterni__
Definisce il luogo in cui sono contenuti i parametri collegati alle righe documenti di questo tipo.
 :  : FLD T$V5B$ __Categoria parametri interni__
Definisce il luogo in cui sono contenuti i parametri che descrivono i campi liberi (5 numerici e 5 alfanumerici), contenuti nell'archivio righe documenti di questo tipo.
 :  : FLD T$V5B3 __Suffisso programmma di aggiustamento__
Se impostato un valore 'x', all'atto del collegamento, viene eseguito nei vari punti in cui è previsto il programma di exit 'V5COL0_x', con le opportune funzioni e metodi.
In questo modo, realizzando funzioni specifiche, si potranno forzare comportamenti particolari al collegamento.
_9_Esempio :  variare la causale di movimentazione di magazzino in funzione della tipologia dell'articolo.
 :  : FLD T$V5B4 __Suff.controllo campi__
Se impostato, nel programma di gestione delle righe documento, viene lanciato il programma V5DO05C_x (dove 'x' = al suff.) che permette di modificare la tipologia degli oggetti dei campi presenti nella riga (per esempio si veda V5DO05C_A).
 :  : FLD T$V5B5 __Tipo ordine di produzione collegato__
Se impostato, nella funzione di collegamento tra ORDINI DI VENDITA e ORDINI di PRODUZIONE, è il tipo dell'ordine di produzione generato. Se NON impostato, nello stesso programma viene assunta la ricerca standard prevista, ovvero risalendo nei dati magazzino/articolo (cat.parametri £P3, 1P3, 2P3).
 :  : FLD T$V5B9 __Tipo lotto__
È un elemento della tabella CQL.
Se impostato e il documento è da collegare alla qualità (vedi flag e tabella V5A), indica la tipologia del lotto da creare per questo tipo riga.
Se non impostato, viene assunto il campo corrispondente inserito in tabella V5A (modello documento).
 :  : FLD T$V5BV __Modello ATP__
È un elemento della tabella M5H.
Se impostato, per la riga è possibile un calcolo ATP, con le modalità definite in questa tabella, sempre che sia presente nel tipo documento l'abilitazione all'ATP. Per un'esposizione più dettagliata dell'argomento, fare riferimento alla documentazione della tabella V5D (tipo documento), relativamente al campo 'ATP abilitato'.
 :  : FLD T$V5B£ __Suff.inizial.__
Se impostato, all'atto dell'inizializzazione di una riga documento con questo tipo, come ultima cosa viene eseguito il programma V5V5Z0_X, che permette di modificare il contenuto del record.
 :  : FLD T2V5BA __Integrazione lotto__
All'atto dell'integrazione a magazzino la causale di magazzino 1 (T$V5BA) e la Causale versam.C/Lavoro (T$V5BZ) vengono sostituite con le causali specificate in tabella CRP, in funzione del piano di campionamento e del tipo lotto, qualora lo si imposti a '1' e si verifichino le seguenti condizioni : 
- 1 Il campo T$CQ1C (Integ.Mag.tab. CRP) della tabella CQ1 è impostato a '1'.
- 2 l'entrata in oggetto ha un lotto presente.
 :  : FLD T$V5BB __Riservato Sme.up1__	
Campo riservato Sme.Up per sviluppi futuri.
 :  : FLD T$V5BX.T$V5BB
 :  : FLD T2V5B1  __Mag.Mov. 1__
Tramite questo campo è possibile scegliere il campo di magazzino da utilizzare nel movimento di magazzino generato dalla 1° causale del tipo riga (T$V5BA  Causale Mov.Mag).
Questo campo può assumere i valori seguenti : 
- ' '  Mag.princip. **il movimento di magazzino utilizza il magazzino principale (R§CDMG)**
- 'T'  Mag.Traferim.**il movimento di magazzino utilizza il magazzino di trasferimento (R§CDMT) nel caso non sia = ' '
 :  : FLD T2V5B2  __Mag.Mov. 2__
Tramite questo campo è possibile scegliere il campo di magazzino da utilizzare nel movimento di magazzino generato dalla 2° causale del tipo riga (T$V5BM  Causale Mov.Mag.Tra.).
Questo campo può assumere i valori seguenti : 
- ' '  Mag.Trasfer. **il movimento di magazzino utilizza il magazzino di trasferimento (R§CDMT)**
- 'P'  Mag.Princip. **il movimento di magazzino utilizza il magazzino principale (R§CDMG)**
 :  : FLD T2V5B3  __Mag.Mov.CL__
Tramite questo campo è possibile scelgliere il campo di magazzino da utilizzare nei movimenti di magazzino di contolavoro generati da questo tipo riga.
Questo campo può assumere i valori seguenti : 
- ' '  Mag.princip. **il movimento di magazzino utilizza il magazzino principale (R§CDMG)**
- 'T'  Mag.Traferim.**il movimento di magazzino utilizza il magazzino di trasferimento (R§CDMT) nel caso non sia = ' '
 :  : FLD T2V5B4  __No Prel.int.__
Nel caso di entrata di un ordine di conto lavoro di fase, se questa è l'ultima, il programma di
collegamento lancia il programma dello scarico in backflushing (con l'effetto di avere i prelievi
doppi).
Inserendo il valore '1' nel campo inibisce questa funzione.
