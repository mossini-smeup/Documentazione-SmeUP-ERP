# Generalità
In Sme.up ad un oggetto applicativo si possono associare, oltre alle informazioni normalmente contenute nell'archivio anagrafico di riferimento, anche tutta una serie di altre informazioni chepossono essere derivate da programmi standard (es. tutti i parametri oppure per un articolo i dati di pianificazione), inoltre si possono associare anche informazioni di tipo dinamico calcolate direttamente da programmi utente (es. la temperatura di cottura di una vernice se l'umidità è > 50%).

Tutte le informazioni di un oggetto, siano esse : 

- contenute nell'archivio
- contenute in altri archivi (es. parametri)
- derivate
- calcolate da un programma (dinamiche)

vengono definite OAV (acronimo di Oggetto Attributo Valore) di un oggetto e possono essere richiamate in qualsiasi punto di Sme.up quando si gestisce un oggetto qualsiasi.

# Codifica
Convenzionalmente gli attributi di un oggetto sono codificati nel seguente modo : 

- attributi 'I/', sono quelli di tipo 'Interno' cioè contenuti nell'archivio anagrafico dell'oggetto
- attributi 'P/', sono quelli di tipo 'Parametro' cioè contenuti nell'archivio parametri (C£CONR0F) ed associati all'oggetto
- attributi 'J/', sono quelli di tipo 'Derivato' cioè contenuti in archivi vari diversi dall'anagrafico ma riconducibili all'oggetto
- attributi 'U/', sono quelli di tipo 'Utente' cioè calcolati da un programma specifico


# Interrogazione
Gli attributi di un oggetto possono essere visualizzati con l'opzione '7' lanciabile dalle funzioni di un oggetto (tasto F10 dal formato di gestione di dettaglio dell'oggetto) : 

![B£_06_01](http://localhost:3000/immagini/MBDOC_OPE-B£_OAV/BX_06_01.png)
Oppure utilizzando la funzione generale di lancio dell'interrogazione (programma B£OAV2L che può essere lanciato con il comando breve 'UP OAV') : 

![B£_06_02](http://localhost:3000/immagini/MBDOC_OPE-B£_OAV/BX_06_02.png)

Con  'Scelta' = 1 dato un oggetto (Tipo + Parametro) si possono vedere tutti i suoi OAV, eventualmente filtrando per codice.

Con  'Scelta' = 2 dato un oggetto specifico (Tipo + Parametro + Codice) si possono vedere tutti i suoi OAV ed i relativi valori : 

![B£_06_03](http://localhost:3000/immagini/MBDOC_OPE-B£_OAV/BX_06_03.png)
# Informazioni tecniche
## Costruzione OAV
Per essere utilizzati gli OAV devono essere 'costruiti' cioè devono essere presenti nel file B£SLOT0F dove sono inserite tutte le definizioni degli attributi attivi per gli oggetti Sme.up.

La costruzione/ricostruzione del file può essere lanciata dal programma TSTOAV, utilizzando le funzioni / metodo opportune : 

![B£_06_04](http://localhost:3000/immagini/MBDOC_OPE-B£_OAV/BX_06_04.png)
## Inclusione OAV negli schemi
Gli OAV rappresentano informazioni associate agli oggetti, quindi risulta naturale poter presentare anche queste informazioni nelle liste che si possono ottenere in Sme.up, cioè includere gli OAV negli schemi informazione.
- [Schemi di visualizzazione e stampa](Sorgenti/MB/DOC_OPE/B£_SCH)

Per far ciò bisogna inserire degli elementi nella tabella INT (sottosettore specifico) corrispondente allo schema di stampa che si vuole ampliare.

### Convenzioni di codifica e descrizione
Il codice dell'elemento deve avere la convenzione di scrittura seguente : 

- da 001 a 100 per valori alfanumerici
- da 101 a 199 per valori numerici

La descrizione deve avere la struttura seguente : 
_2_&nnn*TT*PPP >CCC

dove : 
 * _2_ &, fisso per indicare che si tratta di un valore derivato da un OAV
 * _2_ nn, numero dell'elemento della tabella INT che richiama l'oggetto di cui si vuole inserire nello schema l'OAV decurtato del primo 0. (es. nella tabella degli schemi analisi disponibilità INT_AD se voglio aggiungere un OAV dell' ente sarà nnn = 10)
 * _2_ *TT, è il tipo oggetto (es. se si parla di ente sarà *TT = *CN)
 * _2_ *PPP, può essere : 
 ** _3_blank, quando l'oggetto non pretende il parametro oggetto (es. per gli articoli può essere sufficiente TT = AR se si vuole un OAV comune a tutti gli articoli)
 ** _3_*PPP, dove PPP è il parametro oggetto quando questo è predefinito (es. per una causale di movimentazione sarà *TT = *TA e *PPP = *GMC)
 **_3_&nnn, dove il parametro oggetto viene preso da un altro campo della tabella INT (es. nella tabella schemi analisi disponibilità INT_AD se voglio aggiungere un OAV di un ente prendendo un OAV dipendente dal tipo ente dovrò scrivere *PPP = &09 per derivare il tipo ente dalla tabella INT_AD)
 * _2_  >CCC, può essere : 
 ** _3_blank, nello schema sarà aggiunta la descrizione
 ** _3_>>, nello schema sarà aggiunta la descrizione
 ** _3_>CCC, in questo caso CCC è il codice dell'OAV (es. >U/001 aggiunge alo schema un OAV di tipo utente e che ha codice U/001)

Esempio : 

![B£_06_05](http://localhost:3000/immagini/MBDOC_OPE-B£_OAV/BX_06_05.png)
questo elemento della tabella INT_AD aggiunge agli schemi dell'analisi disponibilità l'OAV I/03 (indirizzo) di un ente il cui codice è nell'elemento 010 della tabella ed il cui tipo è nell'elemento 009 della tabella.

- [Autorizzazioni attributi di un oggetto](Sorgenti/MB/DOC_OPE/B£_OAV1)
