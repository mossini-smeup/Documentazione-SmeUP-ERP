## OBIETTIVO
Definisce le caratteristiche delle fonti future (ordini, impegni) nelle analisi di pianificazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice della fonte.
 :  : FLD T$DESC Descrizione
 :  : FLD T$M5FA __Origine Fonte__
È un elemento V2/M5OFF che definisce la natura della fonte.
 :  : FLD T$M5FB __Parametro 1/2/3/4 Fonte__

I parametri 1/2/3/4 della fonte assumono un significato diverso in funzione dell'origine fonte : 

- [&-x2a; M5F - AP - Altra applicazione](Sorgenti/MB/DOC_OGG/TA_M5F_AP)
- [&-x2a; M5F - BL - Bilanciata](Sorgenti/MB/DOC_OGG/TA_M5F_BL)
- [&-x2a; M5F - CM - Commessa](Sorgenti/MB/DOC_OGG/TA_M5F_CM)
- [&-x2a; M5F - DL - Disponib.libera](Sorgenti/MB/DOC_OGG/TA_M5F_DL)
- [&-x2a; M5F - DV - Deviaz.altro ambiente](Sorgenti/MB/DOC_OGG/TA_M5F_DV)
- [&-x2a; M5F - FF - Fonte fotografata](Sorgenti/MB/DOC_OGG/TA_M5F_FF)
- [&-x2a; M5F - FG - Fabbisogno giornaliero](Sorgenti/MB/DOC_OGG/TA_M5F_FG)
- [&-x2a; M5F - IM - Impegno](Sorgenti/MB/DOC_OGG/TA_M5F_IM)
- [&-x2a; M5F - IP - Impegno pianificato](Sorgenti/MB/DOC_OGG/TA_M5F_IP)
- [&-x2a; M5F - IR - Impegno provvisorio](Sorgenti/MB/DOC_OGG/TA_M5F_IR)
- [&-x2a; M5F - IT - Impegno di trasferimento](Sorgenti/MB/DOC_OGG/TA_M5F_IT)
- [&-x2a; M5F - JM - Fabbisogno primari JMRP](Sorgenti/MB/DOC_OGG/TA_M5F_JM)
- [&-x2a; M5F - MP - Vista MPS](Sorgenti/MB/DOC_OGG/TA_M5F_MP)
- [&-x2a; M5F - OP - Ordine di produzione](Sorgenti/MB/DOC_OGG/TA_M5F_OP)
- [&-x2a; M5F - PM - Parametri](Sorgenti/MB/DOC_OGG/TA_M5F_PM)
- [&-x2a; M5F - PN - Ordine pianificato](Sorgenti/MB/DOC_OGG/TA_M5F_PN)
- [&-x2a; M5F - QE - Quantità eccedente](Sorgenti/MB/DOC_OGG/TA_M5F_QE)
- [&-x2a; M5F - QG - Quantità giornaliera](Sorgenti/MB/DOC_OGG/TA_M5F_QG)
- [&-x2a; M5F - RA - Richiesta d acquisto](Sorgenti/MB/DOC_OGG/TA_M5F_RA)
- [&-x2a; M5F - RM - Richiesta di movimentazione](Sorgenti/MB/DOC_OGG/TA_M5F_RM)
- [&-x2a; M5F - SD - Scorta datata](Sorgenti/MB/DOC_OGG/TA_M5F_SD)
- [&-x2a; M5F - UT - Definizione utente](Sorgenti/MB/DOC_OGG/TA_M5F_UT)
- [&-x2a; M5F - VT - Documento di trasferimento](Sorgenti/MB/DOC_OGG/TA_M5F_VT)
- [&-x2a; M5F - V5 - Documento di ciclo esterno](Sorgenti/MB/DOC_OGG/TA_M5F_V5)
 :  : FLD T$M5FJ __Segno fonte neutra__
Significativo solo se Azione Fonte = N.
Definisce il segno della quantità neutra e consente di suddividere la stessa in Entrate/Uscita. Se impostato al valore '-', la quantità neutra verrà presentata con il segno invertito. L'impostazione di questo campo NON condizionerà in alcun modo la disponibilità dell'articolo, in quanto la quantità neutra NON verrà considerata in nessun modo nel calcolo della quantità disponibile.
 :  : FLD T$M5FD __Ordinamento fonte__
È un carattere che stabilisce, a pari data, nell'ambito delle fonti future, la posizione di questa fonte.
 :  : FLD T$M5FE.T$M5FB
 :  : FLD T$M5FF __Parametro suggerimento__
Contiene le informazioni che guidano l'applicazione del suggerimento collegato a questa fonte, nel caso in cui si voglia dar corso al suggerimento stesso. L'assenza di questa informazione sta a significare che non si vuole attivare questa funzionalità.
I primi 10 caratteri contengono il programma di applicazione, (controllato nella tabella M5*/*P), i restanti sono ulteriori condizioni, specifici di ogni fonte.
Per le fonti SME_UP è attiva la seguente impostazione : 
-    L'ultimo carattere a destra, se impostato, definisce il suffisso del programma di aggiustamento, che viene lanciato prima della scrittura del suggerimento stesso.
Il programma deve chiamarsi nel modo seguente :  xxxxxx_SMy, dove xxxxxx_SM è il programma SME_UP di rilascio, ed y è il suffisso codificato in questa tabella.
Sempre per le fonti SME_UP, nelle posizioni 11-14 si inserisce un oggetto che guida il rilascio e dipende dal tipo dell'ordine : 
-    Se il rilascio è verso un ordine di produzione, si inserisce un elemento della tabella M5P, con cui si impostano le caratteristiche del rilascio (se si chiede il tipo ordine, se si imposta un tipo ordine specifico). È un campo opzionale.
_B_Programma standard di rilascio M5PNP5_SM.
- Se il rilascio è verso una richiesta d'acquisto, si inserisce il tipo richieste (elemento della tabella GAR). È un campo opzionale
_B_Programma standard di rilascio M5PNRA_SM.
-    Se il rilascio è verso una riga di documento esterno, si inserisce invece un elemento della tabella M5V, che contiene gli estremi del documento da generare (tipologia, causale, ...). È un campo obbligatorio
_B_Programma standard di rilascio M5PNV5_SM.
-    Se il rilascio è verso una riga di documento esterno, se è presente il codice dell'ente o verso una richiesta d'acquisto e se il codice ente non è impostato, vengono richiesti un elemento della tabella M5V (da inserire a partire dall'undicesimo carattere) e un elemento della tabella GAR (da inserire a partire dal quattordicesimo carattere. Il significato di questi due parametri è il medesimo di quello descritto nei punti precedenti. È un campo obbligatorio.
_B_Programma standard di rilascio M5PNVR_SM.
Il parametro del suggerimento può essere codificato anche nel caso di fonti già in corso (ordini di produzione, acquisto rilascati, ecc..) :  in tal caso il programma che si inserisce (che è lo stesso del rilascio verso la fonte oggetto di suggerimento), agisce in modalità variazione o annullamento, in modo che esegua l'eventuale suggerimento di annullamento oppure di variazione quantità e/o data collegato a questa fonte.
 :  : FLD T$M5FG __Descrizione ridotta__
È la descrizione che viene usata nel caso di rappresentazioni compatte (ad esempio nelle visualizzazioni e stampe JMRP).
 :  : FLD T$M5FH __Classe fonte JMRP__
È un elemento V2/CFJM, che serve a JMRP per riconoscere le fonti di questa classe.
 :  : FLD T$M5FI __Raggruppamento per data__
Se impostato, verrà tornata una riga cumulativa per tutte le fonti di questo tipo, che si verificano nella stessa data.
In questo caso tutti i campi dell'elemento (commessa, ente, configurazione, ecc..) sono lasciati in bianco. Unica eccezione è il numero documento, in cui viene forzato il campo '>>', che individua una fonte raggruppata.
Se la fonte è raggruppata, ma in una data c'è un solo elemento, vengono ritornati tutti i campi, come se la fonte non fosse raggruppata.
 :  : FLD T$M5FL __Livello__
È un elemento della tabella B£W00 :  se impostato, verranno considerate le sole fonti con questo livello, se lasciato in bianco verranno considerate le fonti con livello '2'.
 :  : FLD T$M5FM __Separazione per codice di rottura__
Questa impostazione è significativa se è presente, per questa fonte, il raggruppamento per data. Se impostato, all'interno di ogni data, verranno ritornate le quantità divise per il codice di rottura della pianificazione (impostato nella tabella M51).
_9_Esempio :  se è stata impostata la pianificazione per commessa, e questa fonte tratta gli impegni pianificati, verrà ritornata, all'interno della stessa data,  una riga di impegno per ogni commessa.
**Attenzione** :  nel caso di impegni pianificati, come elemento di separazione, viene considerato il campo specifico dell'archivio (commessa, configurazione, ente...) e non il codice di rottura.
Ciò significa che la separazione non dipende dal fatto che il codice sia pianificato a rottura o meno (nel qual caso, mentre il campo specifico è valorizzato, il codice di rottura è in bianco).
Questa opzione è utile quando questa fonte è presente nel gruppo fonti di pianificazione, e l'articolo, gestito a rottura, presenta un gran numero di impegni, per cui si è scelto di  raggrupparli per data. Se non si tenessero separati per codice di rottura, esso risulterebbe in bianco (a meno che in una data ci sia un solo impegno), in quanto nelle fonti raggruppate tutti i campi della fonte (commessa, configurazione, ente, ...) sono lasciati in bianco.
 :  : FLD T$M5FN __Suffisso programma aggiustamento__
Se impostato, è il suffisso x del programma M5M5D0G_x, che viene lanciato all'atto della scrittura delle fonti di questo tipo, per modificarne il comportamento.
 :  : FLD T$M5FW __Filtro plant di competenza__
Questo campo è utilizzato solo in ambienti multiplant.
Se vale 1, questa fonte verrà ritornata solo in scansione del plant di competenza.
Se vale 2, verrà invece ritornata in scansione degli altri plant.
Se la si lascia vuota, verrà sempre ritornata.
 :  : FLD T$M5FO __Stato minimo__
Sono significativi per le fonti interne per le quali è impostato lo stato. Se inseriti (se non impostato lo stato massimo viene assunto '99') sono un'ulteriore parzializzazione per fonti di questo tipo.
 :  : FLD T$M5FZ __Origine se fonte utente__
È un elemento V2/M5OFF che, se impostato, viene ritornato nel campo "origine fonte", nel caso di fonte utente.
Può essere utile se la fonte utente è in realtà una fonte "standard" ma elaborata con programmi utente (ad esempio righe di ciclo esterno sia dell'articolo in esame sia dei suoi alternativi), nel qual caso i camp della fonte sono di documenti V5, e quindi, impostando l'origine fonte V5 si ottengono i vantaggi di caratterizzazione.
E' cura di chi implementa il programma di ritorno della fonte utente, garantire la congruenza dei campi di caratterizzazione, con il valore inserito in questo campo.
 :  : FLD T$M5FP.T$M5FO __Stato massimo__
 :  : FLD T$M5FQ __Fonte 'fissa'__
È un campo trattato nella pianificazione materiali. È significativo per le coperture (fonti positive).
Può assumere i seguenti valori : 
- _7_'1'  : 
- Non vengono emessi suggerimenti di riduzione, ma di eccedenza.
    - Non vengono emessi suggerimenti di eliminazione, ma di eccedenza.
    - Non vengono emessi suggerimenti di anticipo, ma nuovi ordini.
- _7_'2' : 
 - Non vengono emessi suggerimenti di riduzione, ma di eccedenza.
    - Non vengono emessi suggerimenti di eliminazione, ma di eccedenza.
    - Vengono emessi suggerimenti di anticipo.
- _7_'3' : 
 - Non vengono emessi suggerimenti di riduzione, ma di eccedenza.
    - Vengono emessi suggerimenti di eliminazione.
    - Vengono emessi suggerimenti di anticipo.
Può venire utilizzata, ad esempio, in caso di ordini emessi a fornitori e terzisti con condizioni vantaggiose (economiche e/o di termini di consegna), a patto che non vengano modificati :  quindi non possono essere nè anticipati nè stornati (parzialmente o totalmente). Il suggerimento di ritardo viene comunque emesso perchè rappresenta un'informazione che può rimanere all'interno dell'azienda, senza essere comunicata al fornitore.
Un altro utilizzo è quello di non perturbare gli ordini di produzione in corso, con suggerimenti di modifica.
 :  : FLD T$M5FR __Riclassifica__
È un elemento della tabella 'M5*RF' :  viene usato nell'analisi pianificazione e disponibilità riepilogate. Per maggiori dettagli fare riferimento alla documentazione del campo corrispondente nella tabella M5E (fonti esistenti).
 :  : FLD T$M5FS __Ordinamento riclassifica__
È usato nelle analisi riepilogate. Per maggiori dettagli riferirsi alla documentazione del campo corrispondente nella tabella M5E (fonti esistenti).
 :  : FLD T$M5FK __Gestione flag esclusione__
Definisce il trattamento del flag di esclusione da analisi disponibilità, impostato nell'oggetto della fonte.
Attualmente il flag di esclusione è gestito nelle fonti di origine V5, attraverso il flag 28 delle righe documento. Se questo campo NON è impostato, il flag di esclusione impostato sulla riga del documento verrà ignorato.
 :  : FLD T$M5FT.T$M5FB
 :  : FLD T$M5FU.T$M5FB
