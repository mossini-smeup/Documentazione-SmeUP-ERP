# BR1 - Personalizzazione brec_up
 :  : DEC T(ST) K(BR1)
## OBIETTIVO
Permettere la personalizzazione della gestione dei dati base
## CONTENUTO DEI CAMPI
 :  : FLD T$BR1D **Distinta multipla**
Se impostato, è abilitata la gestione di più distinte per lo stesso articolo; in caso contrario il tipo distinta è fissato ad ART.
 :  : FLD T$BR1T **Tipo tempo assunto**
È il tipo tempo di default che viene assunto nel calcolo dei tempi di ciclo, in assenza del valore impostato nella riga del ciclo.
 :  : FLD T$BR1C **Codice ente univoco**
Se impostato, il codice ente è univoco su tutti i tipi di ente e non solo all'interno del singolo tipo ente.
 :  : FLD T$BR1A **Tipo gestione alternative articoli**
È un elemento fisso V2/TPALT :  definisce la modalità con cui si definiscono le alternative di un articolo (internamente all'anagrafica, con distinta base, ecc..).
Nel caso di modalità U (Definita da Utente) per determinare gli articoli alternativi verrà richiamato il programma B£G38G_U per la costruzione della schiera degli articoli alternativi.
 :  : FLD T$BR1B **Parametro gestione alternative articoli**
È in funzione del tipo gestione alternative :  ad esempio, se è per distinta base, si deve impostare il tipo distinta che contiene le alternative.
 :  : FLD T$BR1E **Gruppo fonti per alternative**
Se impostato, nella visualizzazione degli articoli alternativi, verrà presentata la disponibilità finale di ciascuno di essi, calcolata con questo gruppo fonti.
 :  : FLD T$BR1F **Livello iniziale esclusione articoli**
Se impostato, gli articoli con livello superiore a quello indicato, benchè visualizzati nella lista di scelta, non sono ritenuti validi, quindi tutti i programmi emettono un messaggio di errore come se il codice non fosse presente. In tal modo si vuole permettere di conservare il codice (esempio a livello 8 o 9) al fine di impedirne il riutilizzo ma evitare ogni gestione.
 :  : FLD T$BR1M **Livello iniziale inclusione articoli**
Se impostato, in maniera simile al precedente ma opposta, gli articoli con livello inferiore a quello indicato, benchè visualizzati nella lista di scelta, non sono ritenuti validi, quindi tutti i programmi emettono un messaggio di errore come se il codice non fosse presente. In tal modo si vuole permettere di inserire articoli (ad esempio a livello 0 non
ancora effettivi).
Il livello iniziale di esclusione e quello di inclusione hanno effetto sempre in condizione "and".
 :  : FLD T$BR1G **Ricalcolo lead time cumulato**
Se impostato, dopo il calcolo del livello minimo, viene calcolato, per lo stesso tipo distinta il lead time cumulato (di tutti i livelli), e memorizzato nello stesso archivio (BRARDT0F).
 :  : FLD T$BR1H **Criterio configurazione assunto**
È un elemento della tabella BRC :  se impostato, viene assunto come criterio di configurazione se assente a livello di singolo codice articolo. Può essere utile qualora la configurazione abbia un significato univoco per l'intera azienda.
Esempio :  la commessa che guida la selezione dei legami di distinta base.
 :  : FLD T$BR1I **Gestione matricole**
Se impostato, è attiva la gestione matricole (per gli articoli che la richiedono).
Questa impostazione ha lo scopo di alleggerire alcune elaborazioni, in cui la ricerca, se un articolo è gestito a matricola, non viene eseguita se non è attiva la gestione matricole.
 :  : FLD T$BR1J **Tipo matricola assunto**
È un elemento della tabella BRU :  se presente, non viene mai richiesto il tipo matricola, ma viene assunto il valore qui impostato.
 :  : FLD T$BR1K **Abilita multinazione**
Permette di gestire le tabelle legate alle informazioni geografiche (V§R Regioni V§P Province V§K Zip code) suddivise per subsettori, dove ogni subsettore contiene gli elementi specifici di ogni nazione. Se attivata, è obbligatorio gestire la tabella V§N (nazioni) codificando i codici nazioni secondo la tabella ISO 3166 (Country Codes), utilizzando il codice a due caratteri.
I nomi dei subsettori delle sopraindicate tabelle corrisponderanno a tale codice a due caratteri.
L'attivazione di questa opzione rende OBBLIGATORIO l'inserimento del codice nazione nell'anagrafica contatti.
 :  : FLD T$BR1L **Descrizione articoli minuscola**
Permette di abilitare la gestione dei campi descrizione dell'anagrafica articoli consentendo l'utilizzo anche di caratteri minuscoli.
 :  : FLD T$BR1N **Inibisce 2ª descrizione**
Consente di inibire la gestione della seconda riga di descrizione dell'anagrafica articoli.
 :  : FLD T$BR1O **Fornitore preferenziale**
Questo campo è utilizzato dalla routine £G26.
Consente di specificare le modalità di scelta del fornitore preferenziale : 
- ' ' - considera tutti i record presenti nell'archivio BRARES0F.
- 1   - esclude tutti i fornitori con il campo priorità non impostato.
- 2   - si comporta come il valore 1, ma nella lista per selezione vengono  presentati anche i fornitori con il campo priorità non impostato.
Nel ritorno dell'ente (sia singolo sia in scansione) le opzioni '1' e '2' sono equivalenti.
Ricordiamo che a pari priorità viene tornato l'ente con codice più basso.
 :  : FLD T$BR1P **Visualizzatore su articoli**
È un valore V2SI/NO :  se impostato viene attivata la gestione variabile 'a visualizzatori' dell'anagrafico articoli, tramite la forma di presentazione specificata nella tabella del tipo articolo. Se lasciato bianco, resta attiva la gestione base 'fissa'.
 :  : FLD T$BR1Q **Forma presentazione**
È significativo se è stato impostato in questa tabella il flag di visualizzatore su articoli e se è assente il campo corrispondente a livello di tipo articolo (tabella BRA).
È un elemento della tabella B£Q in cui si indica il programma di visualizzazione utilizzato per gli articoli.
 :  : FLD T$BR1R **Suffisso Pgm Aggiustamento**
È significativo se è assente il campo corrispondente a livello di tipo articolo (tabella BRA).
_9_Se utilizzata versione 1 gestione articoli (senza visualizzatore)
È il suffisso del pgm BRAR01D_x :  permette di gestire controlli e impostazioni personalizzate durante la gestione dell'anagrafico articoli (Es. BRAR01D_Z).
_9_Se utilizzata versione 2 gestione articoli (con visualizzatore)
È il suffisso del pgm BRAR02C_x :  permette di modificare la tipologia degli oggetti dei campi presenti nel tracciato (per esempio vedi BRAR02C_A).
 :  : FLD T$BR1S **Unità Memorizzazione su Cicli di lavorazione**
Serve per definire l'unità di misura con cui vengono scritti i tempi del ciclo nel file.
Se non impostato assume 'SS' secondi.
È utile in caso di valori elevati di pezzi/ora, per memorizzare in unità di misura più piccole (decimi, centesimi ...)
 :  : FLD T$BR1U **Cambio Tipo Articolo**
Se impostato, è posssibile modificare il tipo articolo nella videata di dettaglio dell'articolo.
Vengono eseguiti i seguenti controlli : 
1) Contenitore note;
2) Categoria parametri;
3) Parametri impliciti;
4) Tipo date implicite;

1) _Se il Contenitore note del tipo articolo nuovo è uguale al contenitore note del tipo articolo vecchio, la modifica viene effettuata.
    _Se il Contenitore note del tipo articolo nuovo è diverso dal contenitore note del tipo articolo vecchio, la modifica viene effettuata solo se per quell'articolo non esistono commenti.
2) _Se la categoria parametri del tipo articolo nuovo è uguale alla categoria parametri del tipo articolo vecchio, la modifica viene effettuata.
    _Se la categoria parametri del tipo articolo nuovo è diversa dalla categoria parametri del tipo articolo vecchio, la modifica viene effettuata solo se non esistono parametri esterni per quella categoria/articolo.
3) _Se i parametri impliciti del tipo articolo nuovo sono uguali ai parametri impliciti del tipo articolo vecchio, la modifica viene effettuata.
    _Se i parametri impliciti del tipo articolo nuovo sono diversi dai parametri impliciti del tipo articolo vecchio, la modifica viene effettuata solo se non esistono parametri impliciti legati a quell'articolo.
4) _Se il tipo data implicita del tipo articolo nuovo è uguale al tipo data implicita del tipo articolo vecchio, la modifica viene effettuata.
    _Se il tipo data implicita del tipo articolo nuovo è diversa dal tipo data implicita del tipo articolo vecchio, la modifica viene effettuata solo se non esistono date legate a quell'articolo.
 :  : FLD T$BR1W **Alternative ciclo multiple**
Se impostato, è attivata dalla lista cicli la gestione delle alternative multiple (che si sviluppano in serie su più percorsi).
Se lasciato in bianco, è invece attivata la gestione alternative base, in cui si possono impostare soltanto alternative tra fasi parallele.
E' consigliata l'impostazione delle alternative multiple, in quanto più versatile di quella base.
 :  : FLD T$BR1V **Lead time variabile in lead time cumulato**
Se impostato, nel lead time cumulato viene considerato, nel tempo di approvvigionamento totale, anche il tempo di approvvigionamento variabile (oltre a quello fisso)
 :  : FLD T$BR1X **Lead time rettifica in lead time cumulato**
Se impostato, nel lead time cumulato viene considerato, nel tempo di approvvigionamento totale, anche il tempo di approvvigionamento di rettifica (oltre a quello fisso)
 :  : FLD T$BR1Y **Tipo coda**
Definisce il tipo coda che viene assunto se non impostato il valore nel gruppo risorsa (tabella BRM). Se anche il valore nella presente tabella viene lasciato in bianco, si assume il valore 'A' (coda in giorni).
 :  : FLD T$BR1Z **Forza data scansione**
Se impostato, nell'esplosione di produzione di distinta e ciclo, se l'assieme è un articolo e se la data passata è inferiore alla data di creazione dell'articolo stesso, viene assunta quest'ultima. Questo comportamento è necessarion nel caso di distinte e cicli di gruppo, con data di validità iniziale sui legami presente alla nascita del codice (per gestirne l'evoluzione da un codice precedente non intercambiabile).
 :  : FLD T$BR11 **Suff.agg.interf.art.**
E' possibile attivare un programma per il completamento/modifica dei campi del BRARTI0F nella routine £IAR.
Il campo è il suffisso del programma B£IARUx ed è lanciato dal programma B£IAR_SM (interfaccia articoli SMEUP), è lanciato nella routine di completamento (GEPART) ed è utile se si vuole personalizzare campi del BRARTI0F, per un esempio vedere il sorgente B£IARUA.
 :  : FLD T$BR12 **Tipo matricola modificabile**
Se impostato, in gestione, il campo tipo matricola è modificabile, anche se è stato ricevuto.
Ciò consente, tra l'altro, di poter inserire una matricola di tipo diverso quando il programma di guida della gestione matricole viene richiamato dal menu del modulo matricole di Loocup.
 :  : FLD T$BR13 **Dichiarazioni di intento, flusso aggiornamento anagrafica ente**
Se impostato, in gestione di inserimento, modifica e cancellazione delle dichiarazioni di intento,
verranno aggiornate le informazioni sull'anagrafica enti.
In particolare verranno aggiornati : 
- Data Validità Esenzione
- Dichiarazione di Untento
- Data Dichiarazione di Intento
