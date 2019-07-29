# BRE - Tipo contatto
 :  : DEC T(ST) K(BRE)
## OBIETTIVI
Permettere la caratterizzazione delle diverse sezioni in cui si sviluppa l'anagrafico dei soggetti.
## CONTENUTO DEI CAMPI
 :  : FLD T$BREA **Ambiente per ente/articolo**
Indica l'ambiente applicativo da cui reperire le informazioni per ente/articolo. Se non impostato si assume SM. In questo caso è possibile stabilire se l'origine delle informazioni è sull'archivio Ente/Articolo (BRARES0F) oppure su LISTINI, DOCUMENTI, ecc.
 :  : FLD T$BRED **Modo scelta enti di spedizione**
Sono enti di spedizione di un ente : 
 *     Tutti gli enti di qualsiasi tipo che hanno l'ente in esame come ente di contabilizzazione.
 *     Tutti gli enti definiti nell'estensione "£01" dei contatti.
 *     L'ente associato come ente di spedizione dell'ente in esame.

Si definisce come "assunto" l'ente associato come ente di spedizione dell'ente in esame.
Questo campo può assumere i valori seguenti : 
- ' '  :  Presenta il formato di scelta ente solo su specifica richiesta, ad esempio digitando "/" sull'ente di spedizione all'interno di una testata  documento. Se l'ente di spedizione viene determinato in modo univoco, verrà automaticamente impostato
- 'A'  :  Presenta sempre il formato di scelta ente, anche se si è riusciti a determinarlo in modo univoco.
- 'B'  :  Presenta il formato di scelta ente solo se non si è riusciti a determinarlo in modo univoco. L'ente di spedizione viene assunto se determinato in maniera univoca un solo ente associato (£01 o associato), oppure tra gli enti associati ne viene identificato solo uno
- 'C'  :  Come il valore ' ', con la differenza che il codice di spedizione assunto viene impostato solo dall'ente di spedizione associato all'ente intestatario, o eventualmente esso stesso, ma mai l'ente associato (£01 o ente associato), anche se singolo.
Se riscontrati più enti associati, non verranno scelti automaticamente, ma sarà possibile richiedere la ricerca mediante "/" sull'ente.
- 'D'  :  L'ente di spedizione viene assunto se specificato l'ente di spedizione dell'ente intestatario. Se vengono riscontrati enti associati (£01 o associato), viene presentato il formato di scelta, anche se tra gli enti associati ne viene identificato solo uno.
 :  : FLD T$BREG **Tipo ente in selezione enti di spedizione**
Nella selezione enti di spedizione, la cui modalità è definita nel campo di questa tabella "Modo scelta enti di spedizione" (T$BRED), indicando in questo campo un tipo ente valido, si ottiene una scelta filtrata sugli enti di questo tipo.
Lasciando vuoto questo campo, la selezione avviene sugli enti collegati di qualsiasi tipo.
 :  : FLD T$BREL **Lunghezza riempimento zero**
Se impostata (con un valore Da 01 a 15), il codice ente digitato viene riempito con il carattere zero, partendo da sinistra, fino al raggiungimento di questa lunghezza.
 :  : FLD T$BREM **Natura ente**
Definisce se gli enti di questo tipo sono clienti o fornitori.
 :  : FLD T$BREC **Calendario contabile**
È il tipo di risorsa utilzzata dal calendario nella generazione delle rate. Dopo che la funzione di generazione rate ha determinato la data di scadenza, se presente questo campo, viene letto il corrispondente calendario e spostata la data al primo giorno lavorativo.
 :  : FLD T$BREI **Suffisso programma aggiustamento**
È il suffisso x del programma B£IFCO_x. Se presente viene eseguito successivamente alla lettura del record dell'ente, dando la possibilità di valorizzare specificatamente tutti i campi. Nello standard è supportato solo dall'interfaccia SM.
 :  : FLD T$BREH **Codice solo numerico**
Se impostato nel campo codice verranno accettati solo caratteri numerici
 :  : FLD T$BREJ **Lunghezza fissa**
Questo campo è significativo solo se è impostato il campo T$BREL Lunghezza riempimento zero.
Se impostato, tutti i codici avranno lunghezza fissa, corrispondente a quella specificata nel campo T$BREL.
Se in fase di inserimento viene utilizzato un codice di lunghezza minore, verranno inseriti automaticamente degli zeri a sinistra del codice stesso.
 :  : FLD T$BREK **Attivazione Scenari**
Se previsto da BR2, attiva gli scenari per il tipo contatto. Il campo può assumere i seguenti valori : 
-" "=Gli scenari non sono attivati
-"1"=Attivo gli scenari ed il codice scenario è l'azienda
-"2"=Attivo gli scenari ed il codice scenario è dato dall'azienda + altre informazioni
-"3"=Attivo gli scenari ed il codice scenario può essere l'azienda o l'azienda + altre informazioni
 :  : FLD T$BREO **Sottosettore Scenari**
Se previsto da BR2, ed ho attivato gli scenari per tipo contatto, definisce il sottosettore della tabella
degli scenari di riferimento per il tipo contatto.
 :  : FLD T$BRER **Gestione a nominativi**
Se prevista da BR2, attiva la gestione a nominativi per il tipo contatto.
 :  : FLD T$BREU **Suffisso pgm di aggiustamento per aggiornamento
Definisce il suffisso del pgm di aggiustamento (B£IFCO_) da utilizzare in aggiornamento.
 :  : FLD T$BRES **Suffisso pgm aggiustamento pre/post-modifica del singolo record
Definisce il suffisso del pgm di aggiustamento (BRBR24_) da utilizzare per gestire particolarità
su pre/post-immissione/modifica/cancellazione di un singolo record dell'anagrafico nel caso sia
stata attivata la gestione degli scenari dei nominativi o la gestione dello storico (in questo
caso potrei avere più record per lo stesso tipo/codice contatto, ed i normali flussi verrebbero
lanciati esclusivamente una volta per tipo/codice e non per ogni record effettivamente utilizzato.
Questa exit serve proprio per permettere la gestione di tali considerazioni a livello di record.
Esempio con attiva la gestione dello scenario : 
- Sul codice xxx ho attivato gli scenari 01, 02 e 03. Sul file ho perciò 3 record se modifico il soggetto verranno   aggiornati tutti e tre i record, ma i flussi di pre e post-modifica verranno lanciati un'unica volta (prima e dopo   l'aggiornamento di tutti i record). Se perciò voglio ragionare a livello di record devo appoggiarmi a questa exit.
 :  : FLD T$BRET **Assunzione campi non pertitenti per data entry V2**
Se valorizzato questo campo fa si che tutti i campi non indicati nello script di definizione del tipo contatto vengano assunti come non pertinenti (è come se fossero indicati ma con assunta la valorizzazione di non pertinenza del campo)
 :  : FLD T$BREV **Suff.pgm.sel.Enti S.**
È il suffisso x del programma BREN30_x. Se presente viene richiamato dal programma BREN30 (selezione enti di spedizione) dopo i controlli intrinseci dando la possibilità di effettuare delle selezioni specifiche
E' presente il protitipo BREN30_X
 :  : FLD T$BREW **Ente Complementare**
Definisce il riferimento in base al quale può essere recuperato l'ente corrispondente nelle applicazioni (da cliente al fornitore e viceversa). Può assumere i seguenti valori : 
- " "= l'ente viene recuperato tramite la ricerca della corrispondeza per riferimento fiscale
- "1"= l'ente viene recuperato tramite la ricerca per ente corrispondente
 :  : FLD T$BREX **Costruzione Automatica**
Se impostato presuppone che sia stata associata all'elemento una BRZ che prevede una costruzione automatica del codice. In questo caso è possibile tramite questo campo far saltare la schermata di conferma del codice attribuito in fase di inserimento.
 :  : FLD T$BREY **Codice Non Univoco**
Se è attiva sia la gestione scenari che la gestione nominativi, tramite questo campo è possibile specificare che il codice ente non è univoco per scenario (es. codice 001 nella società 1 è Tizio, mentre nella società 2 il codice 001 è Caio). Avendo però attiva la gestione nominativo, l'integrità dei dati verrà mantenuta tramite tale legame.
 :  : FLD T1BREA **Natura Documento**
Definisce la natura dei documenti ammessi durante il fly del contatto.
Può assumere i seguenti valori : 
- " "= Tutti i documenti
- "1"= Documenti attivi
- "2"= Documenti passivi
- "3"= Nessun documeno
