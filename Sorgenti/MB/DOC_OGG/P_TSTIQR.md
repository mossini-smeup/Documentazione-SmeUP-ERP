# OBIETTIVO
Gestire le operazioni di query su oggetti applicativi.

# FUNZIONI E METODI

## SEL - Selezione
La Funzione SEL è dedicata alla costruzione di una selezione di record tramite una query esplicitandola in un formato di output.

### INZ  - Inizializzazione
Di fondamentale importanza è l'esecuzione con metodo INZ. Tramite questo metodo vengono fissati i parametri tramite i quali verrà costruita la seleezione. Questi i parametri previsti (salvo specificato diversamente i parametri sono facoltativi) : 
* **£IQROG** :  oggetto di riferimento (obbligatorio)
* **£IQRQR** :  codice query (obbligatorio)
* **£IQRSC** :  schema
* **£IQROR** :  ordinamento
* **£IQRIN** :  parametri di input (in formato codiceparametro(valoreparametro))
** **JAXCP** :  codice componente, obbligatorio. Deve indicare il codice componente con il quale si vuole risolvere la selezione
** **JAXSC** :  codice coda, obbligatorio quando si voglio far eseguire funzioni di invio xml
** **QRNRE** :  numero di righe della prima pagina. Per ogni pagina successiva, questo numero verrà moltiplicato per 2.
** **PAG** :  indica che si è in fase di paginazione su una selezione già costruita
** **PAG_NRI** :  se si è in fase di paginazione indica il numero preciso di righe caricate sino a quel momento
** **Q2PAR** :  parametri dello schema. Questo parametro è a sua volta composto dai seguenti parametri : 
*** Context :  è la stringa di riferimento per la memorizzazione dei setup dello schema. Viene passata nel caso il pgm di risoluzione dello schema ne possa fare utilizzo.
*** **Id** :  se valorizzato a Yes indica che nello schema dovrà esiste una colonna avente per contenuto l'identificativo dell'oggetto e per codice colonna ID_LI. Se assente verrà automaticamente aggiunta allo schema.
*** **Tp** :  se valorizzato a Yes indica che nello schema dovrà esiste una colonna avente per contenuto il tipo oggetto di riferimento e per codice colonna ID_TP. Se assente verrà automaticamente aggiunta allo schema.
*** **SchPar** :  se previsto possono essere passati una serie di parametri aggiuntivi che saranno poi trattati dal pgm di schema specifico.
*** **Opz** :  può essere valorizzata a Yes o con un qualsiasi istanza dell'oggetto VOCOD_VER. Se valorizzata in questo modo verrà automaticamente aggiunta come colonna sulla sinistra una colonna avente le seguenti caratteristiche : 
**** Codice colonna $OP
**** Intestazione colonna Op
**** Tipo Oggetto Colonna VOCOD_VER
**** Valore colonna :  il contenuto del parametro Opz se diverso da Yes, 000102 e Yes
*** **Det** :  può essere valorizzata a Yes verrà automaticamente aggiunta come colonna sulla sinistra ****** Codice colonna $DET
**** Intestazione colonna Det. o il valore del parametro IntDet
**** Tipo Oggetto Colonna VOCOD_VER
**** Valore colonna :  000103 (Vai a dettaglio)
*** **CndDet** :  deve essere valorizzato con un codice attributo dell'oggetto di riferimento :  solo le righe per cui per questo attributo risulta un valore presenteranno la cella valorizzata.
**** Codice colonna $KD
**** Intestazione colonna Det. o il valore del parametro IntDet
**** Tipo Oggetto Colonna VOCOD_VER
**** Valore colonna :  000103 (Vai a dettaglio)
*** **IntDet** :  permette di indicare l'intestazione da applicare alle colonne create dai parametri Det o CndDet.
** **QRFRM** :  stringa SQL utilizzabile per il FROM. Questa stringa verrà applicata alla query per forzare un particolare archivio di partenza.
** **Q3FLT** :  in questo parametro possono essere passati i valori di applicare al filtro previsto da query. Il formato è campofiltro(valorecampofiltro), ad eccezione dei campi che prevedono un operatore di range, per questi è previsto che i parametri siano due, con la seguente codifica campofiltro_I(valorelimiteiniziale) campofiltro_F(valorelimitefinale).
** **QRPAG** :  valore di paginazione tramite esso verrà applicato un filtro aggiuntivo (normalmente corrispondente al valore delle chiavi di ordinamento) alla query necessario per posizionarsi alla riga voluta.
** **WHRQ3** :  stringa SQL utilizzabile per una WHERE. Questa stringa verrà applicata alla query per forzare un particolare filtro SQL.
** **Q3JOB** :  se valorizzata a Yes, verrà applicata alla query anche l'eventuale filtro di job dell'oggetto (E/*JOB)
** **Q3FST** :  stringa di filtro per codice/descrizione. La stringa passata in questo parametro verrà ricerca sia nel codice che nella descrizione dell'oggetto. Solo se la stringa verrà trovata in almeno uno dei due valori, la riga verrà considerata valida.
** **Q3FSA** :  stringa di filtro avanzata (si veda l'api £K41).
** **Q3LIS** :  filtro per lista. Definizione di una LISTA, la cui WHERE corrispondente va ad aggiungersi alla WHERE dell'oggetto, la struttura per questo campo è la seguente :  LI(TipoOggetto;NomeLista;NomeCampoFile)
** **Q3DDWN** :  Parametro di Drill Down con la struttura prevista dal B£SER_83
- FLDn(Nome Campo) VALn(Valore) OPEn(Operazione). Solo se previsto filtro di job.
** **Q4STR** :  stringa SQL utilizzabile per l'ORDER BY. Questa stringa verrà applicata alla query per forzare un particolare ordinamento.

### GRI  - Ritorno Griglia
Se il componente di output ha un forma matrice, tramite questa funzione vien restituito l'xml della griglia di matrice.

### ARIG  - Invia Righe
Viene eseguito internamente il ciclo delle righe selezionate dall'elaborazione per il numero di righe previsto dalla paginazione, con l'invio diretto dei dati sulla coda.
NOTA BENE :  in caso di forma matriciale, la £JAX_ARIG_I e la £JAX_ARIG_F devono essere rispettivamente eseguite prima e dopo questo tipo di chiamata.

### APOP  - Invia Popup
Viene eseguito internamente il ciclo delle righe selezionate dall'elaborazione per il numero di righe previsto dalla paginazione, con l'invio diretto dei dati sulla coda.
NOTA BENE :  la £JAX_APOP_I e la £JAX_APOP_F devono essere rispettivamente eseguite prima e dopo questo tipo di chiamata, inoltre per poter compilare correttamente il popup di paginazione dovrà essere passata come INPUT la £UIBDS della servizio che si sta eseguendo. A tale funzione verranno accodati i parmetri : 
* PAG :  valorizzato a YES per indicare che è attiva la paginazione
* PAG_NRI :  con il numero di righe caricate sino a quel momento (sulla base del quale verranno calcolati il numero di righe della paginazione seguente.
* QRPAR :  con il alore di riferimento per eseguire il corretto riposizionamento sulle righe

### SET  - Ritorno Setup
Ritorna il setup del componente da aggiungere all'invio dell'xml della funzione

### SQL  - Ritorno SQL per Apertura Cursore
Ritorna l'intera stringa di select sql utilizzata per risolvere la selezione (se è stato utilizzata una scansione sql)

### SQLERR  - Ritorno Messaggio Errore su Apertura Cursore SQL
Ritorna l'eventuale messaggio di errore nel caso in cui, prevedendolo, l'apertura del cursore non sia avvenuta correttamente.

### STA  - Ritorno Dati Statistichi
Vengono ritornati in forma parametrica alcuni dati statistici sull'ultima esecuzione.

## DEC - Decodifica
Esegue le funzioni di decodifica per gli oggetti base coinvolti Q1/Q2/Q3/Q4/Q5.
Il codice oggetto da decodificare deve essere passato nel campo £IQRIK.
Rappresenta l'interfaccia comune per la /COPY £DEC

## INZ - Inizializzazione

In sequenza le operazione eseguite dalla funzione : 

1. Inizializza la query caricando le impostazioni dal programma di fonte o da file di script.

2. Se non valorizzati £IQRSC/£IQRFL/£IQROR vengono impostati i default della query.

3. Vengono eseguite le routine di caricamento campi : 
   Schema      £IQ2(CAR : SCH)
   Filtro      £IQ3(CAR : FLT)
   Ordinamento £IQ4(CAR : ORD)
  Nota : 
   I campi schema/filtro/ordinamento possono assumere il valore '**' che indica al motore di query
   l'impostazione da programma chiamante delle definizioni; non verranno quindi eseguite le routine di caricamento.
   Questa opzione risulta utile nell'utilizzo da programma RPG per cablare determinate impostazioni.

4. Viene eseguita l'inizializzazione del programma di fonte B£IQR_xx(INZ : )

5. Vengono eseguite le routine di caricamento valori e completamento delle definizioni campi : 
   Schema      £IQ2(CMP : SCH)
   Filtro      £IQ3(CMP : FLT)
   Ordinamento £IQ4(CMP : ORD)

   Il completamento delle definizioni campi si basa sul tipo tracciato degli oggetti Q2/Q3/Q4.
   Questa operazione avviene qualora il programma di fonte non abbia già provveduto.

   Se lo schema risulta vuoto, il motore di query provvede a impostarne uno di default Codice/Descrizione,
   valorizzandolo tramite £IQROK e £DEC(£IQROG : £IQROK).

6. Vengono eseguite le routine di caricamento valori : 
   Filtro      £IQ3(CAR : VAL) £IQ3IN(FLT() CFG())

   Se passato il parametro FLT() in £IQRIN, vengono caricati i valori di filtro secondo la sintassi : 
   FLT(£IQR3I(x)(valore_x))
   Se passato il parametro Q3_CFG([MEIDOJ]) in £IQRIN, vengono caricati i valori di filtro dalla configurazione.
   Se passato il parametro Q3_CFG(*USER) in £IQRIN, viene ricercata la configurazione del filtro utente.

   In questa fase vengono estratti i campi di schema/filtro con valore dinamico.                     .
   La valorizzazione di questi campi e la conseguente applicazione del filtro verrà eseguita dal motore di
   query qualora risulti necessario, ovvero £IQ2DDI/£IQ3DDI = '1' per un qualsiasi campo di schema/filtro.
   E' compito del programma di fonte valorizzare correttamente questi campi che per defaut assumono valore ='1'.

## SLC - Selezione

In sequenza le operazione eseguite dalla funzione : 

1. Viene eseguita la selezione dei records con chiamata al programma di fonte B£IQR_xx(SLC : )
   Il campo £IQRIN potrebbe contenere il parametro PAG() indicante il numero di pagina da cui eseguire la
   selezione dei records. La valorizzazione di questo campo dipende dalla chiamata B£IQR_xx(NXT : PAG)
   Il campo £IQRIN potrebbe contenere il parametro NRE() il numero elementi richiesti oppure *ALL indicante
   il caricamento completo.

## NXT - Avanzamento record

In sequenza le operazione eseguite dalla funzione : 

1. Viene eseguita la scansione dei records con chiamata al programma di fonte B£IQR_xx(NXT : )
   Al ritorno di questa chiamata la schiera £IQR2V contiene il valore dei campi dello schema, che saranno
   eventualmente completati e filtrati dal motore di query.
   L'eventuale parzializzazione dei records avviene tramite chiamata £IQ3(CHK : FLT).
   L'eventuale completamento del record avviene tramite chiamata £IQ2(CMP : VAL).

## NXT : PAG - Avanzamento pagina

In sequenza le operazione eseguite dalla funzione : 

1. Viene richiesto il valore di paginazione da passare per la successiva selezione tramite la chiamata B£IQR_xx(NXT : PAG).
   Il valore di ritorno del campo £IQROU verrà ritornato nella successiva chiamata paginata B£IQR_xx(NXT : ) PAG(£IQROU).
