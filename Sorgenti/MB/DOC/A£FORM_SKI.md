 :  : HEA RESP(MR) STAT(10) USAG(MR) DTAG(20120612) RELS(V3R2) AMBT(AP)

## Finalità della metodologia : 

- Verificare la propria competenza/Skill
- Verificare l'efficacia di un corso di addestramento
- Creare una banca data degli skill utile per individuare le persone capaci di compiere una funzione

## A chi è indirizzato ?

- Agli studenti dei corsi, onde si capacitino delle proprie competenze prima e dopo il corso
- Agli analisti e responsabili dei sistemi informativi per verificare la propria conoscenza degli strumenti informatici
- Agli installatori dei sistemi informativi per individuare capacità e mancanze
- Ai gestori del personale per individuare le aree di grossa mancanza di conoscenza ed indirizzare il piano formativo

## Che competenze copre ?

- Tutte le competenze riguardanti gli applicativi NEGOZIANDO e SMEUP
- Tutte le competenze riguardanti il supporto hardware relativo al funzionamento degli applicativi suddetti
- Tutte le competenze trasversali, quelle che riguardano i comportamenti relazionali e relativi al lavoro di gruppo

## A cosa si agganciano le competenze ?

Le competenze si agganciano ai moduli di Smeup, ossia agli elementi della tabella B£AMO. Questo significa che probabilmente debbono essere creati dei moduli ad hoc per appenderci le competenze. Ad esempio, la competenza necessaria per installare un server, farà riferimento ad un modulo creato specificatamente per questo motivo.


## Come si compone la metodologia?

La metodologia si compone di due fasi : 

- Creazione di un questionario di domande chiuse, con risposte numeriche che vanno dall'1 al 6 (1 = mai o nulla, 6 = sempre o tutto). Il questionario viene compilato (ed aggiornato, incrementato) dal responsabile del modulo il quale ha la comptenza per immaginare tutte le domande che verificano la conoscenza. Le domande possono avere anche un peso (importanza)
- Registrazione delle risposte di autovalutazione del soggetto, per data di autovalutazione.

## Come si crea il questionario?

Dalla scheda del modulo oggetto del questionario, nel menu a sinistra (LOA12) si clicca su Formazione/Skill e compare nella sezione di destra la gestione del questionario. Cliccare su "Modifica voci del contenitore", ed inserire nella matrice di aggiornamento sia la domanda che la risposta.
La domanda del questionario può essere classificata aggiungendo nell'alias la caratterizzazione stessa. In presenza di più classificazioni le stesse devono essere separate dal carattere punto e virgola (;)
Si rende noto che la classificazione è case sensitive per cui Com e COM sono considerate due classificazioni diverse.



## Chi sono i soggetti che eseguono l'autovalutazione ?

I soggetti sono identificati nel parametro stesso della valutazione.
Tendenzialmente l'Utente o il Collaboratore.

## Modalità di analisi dei dati consuntivi

I dati saranno analizzati secondo le seguenti aggregazioni : 
- Per persona che risponde all'autovalutazione e data di risposta
- Per modulo e periodo, mediando le risposte delle persone
- Per singola voce e periodo, mediando le risposte delle persone.

I valori sui moduli saranno aggregati in modalità lineare (somma semplice) ed ottendeno la percentuale rispetto al totale teorico (numero di domande * 6), evitando di pesare le risposte in quanto la comprensione del grado di conoscenza ha più senso farla rispetto alla media dei valori delle altre persone, o rispetto al valore che una persona ha ottenuto in diverse date, per comprendere se il trend è in miglioramento.

## Modalità di compilazione dello Skill
La modalità di compilazione avviene attraverso una matrice in cui verrà esposta la domanda e richiesta una valutazione da 1 a 6.
La richiesta si riferisce sempre all'anno in corso, se non espresso diversamente.
La richiesta si riferisce sempre al proprio utente, se non espresso diversamente.
I valori assumono il seguente significato : 
 :  : PAR L(TAB)
Valore|Significato
1|Non so o non capisco domanda
2|So alcune cose
3|So molte cose ma tanti dubbi
4|So ma ho dubbi
5|So ma ho qualche dubbio
6|So tutto e son sicuro


## Modalità di compilazione dei video
La modalità di compilazione avviene attraverso una matrice in cui sono elencati i video.
La richiesta si riferisce sempre all'anno in corso, se non espresso diversamente.
La richiesta si riferisce sempre al proprio utente, se non espresso diversamente.
I valori assumono il seguente significato : 
### Piace/Non piace
 :  : PAR L(TAB)
Valore|Significato
1|Non mi piace
2|Mi piace

### Fatto
 :  : PAR L(TAB)
Valore|Significato
1|Fatto

### Pessimo/Ottimo
 :  : PAR L(TAB)
Valore|Significato
1|Gravemente insufficiente
2|Insufficiente
3|Sufficiente
4|Buono
5|Ottimo
6|Eccellente


## Modalità di compilazione della salute aziendale
La modalità di compilazione avviene attraverso una matrice.
La richiesta si riferisce sempre all'anno in corso, se non espresso diversamente.
La richiesta si riferisce sempre a un'identificativo di sessione non riconducibile all'utente.
I valori assumono il seguente significato : 

### Verita
 :  : PAR L(TAB)
Valore|Significato
1|Vero raramente
2|Vero qualche volta
3|Normalmente vero
4|Sempre vero


## Come realizzare un nuovo questionario
Vengono ora elencati i passaggi neccessari per la creazione di un nuovo questionario.

 :  : PAR L(TAB)
Passo|Descrizione|Nota
1|Creare il questionario|Il questionario deve essere creato come voce.
 ||Creare un nuovo oggetto "MBDOC_VOC" e aggiungere le domande tramite il tag  :  : VOC
 ||Utilizzare il wizard per la documentazione del tag.
2|Creare il reposoty per la risposta alla domanda|La risposta viene memorizzata nei parametri £OG.
 ||Creare o riutilizzare un parametro nella tabella B£NOG compatibile con l'ogetto intestatatio del questionario.
 ||Nel tipo oggetto inserire l'oggetto intestatario del questionario
 ||Nell'unità di misura, il range disponibile per la domanda (Riferirsi ai valori descritti nel'oggetto V2B£VAL.
 ||Limitare il valore superiore come da descrizione del valore V2B£VAL
 ||La struttura di memorizzazione è la sequente : 
 ||Codice 1 - Questionario
 ||Codice 2 - Domanda
 ||Oggetto del parametro - Oggetto intestatatario
 ||Valore  del parametro - Risposta alla domanda
3|Gestione del questionario|Non esiste una gestione standar del questionario, per questa ragione bisogna creare una propria scheda di utilizzo.
 ||Richiamre la seguente scheda passando i parametri necessari alla gestione del questionario
 ||F(EXD;*SCO;) 1(VO;.1.;) 2(2(MB;SCP_SCH;C£CONR_VA) 4(;;GES) P(NUMP_EL(.2.) USER(.3.) RND(.4.))
 ||Significato dei parametri : 
 ||.1. = Nome del questionario
 ||.2. = Nome del parametro
 ||.3. = Identificativo del questionario
 ||.4. = Numero di domande da mostrare, scelte casualmente dal questionario

L'oggetto intestatario ".3." è facoltativo nei seguenti casi : 
 :  : PAR L(TAB)
Oggetto|Descrizione
OJ*USRPRF|Utente sistema
UT|Utente sistema
TAB£U|Utente applicativo
UP|Utente applicativo
CNCOL|Collaboratore derivato dall'utente
<**>|Oggetto univoco, Creato in automatico dal sistema

Se il questionario finisce con la sigla "_SKI" allora sarà presentata la sola domanda V21.
