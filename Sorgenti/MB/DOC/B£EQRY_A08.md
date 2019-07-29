# Generalità

Al fine di poter interagire in modo trasparente anche con altre applicazioni, gli oggetti smeup possono essere deviati su archivi/interfacce differenti da quelle standard.

# Struttura

In smeup l'accesso ai dati delle istanze avviene essenzialmente in due modi : 
* Attraverso la specifica /COPY di interfaccia che viene predisposta nello standard per ogni classe
* Attraverso l'identificazione sul database che è stata fissata per ogni classe (qualora le istanze della classe appartengano ad un archivio)
Per deviare un oggetto standard occorre quindi intervenire su entrambi i punti (anche se il secondo è in realtà necessario solo per gli oggetti che appartengono ad un archivio)

Per il primo punto l'intervento è specializzato per la singola classe. Pur essendo poi l'operatività simile, l'intervento va effettuato in base alla funzionalità della /COPY di interfaccia della singola classe. L'approfondimento di questi aspetti, per ogni classe, può avvenire attraverso la scheda della classe (oggetto OG,,codiceclasse) nella quale è indicata la /COPY attraverso cui si accede all'oggetto.
Va inoltre precisato, che qualora per l'oggetto sia necessario gestire esclusivamente le funzioni di decodifica/scansione l'oggetto può essere deviato attraverso la configurazione della tabella B£O**. Tramite questa tabella è infatti possibile deviare qualsiasi oggetto, genericamente. In tale casistica per tale oggetto saranno però disponibili solo le informazioni di codice e descrizione.

Per il secondo punto invece l'intervento è lo stesso per tutte le classi :  va inserito l'elemento della B§O avente come codice il codice della classe ed all'interno del quale possono essere indicate le informazioni che permettono di indentificare le modalità di accesso al database necessarie per l'oggetto in questione.

 :  : DEC T(ST) K(B§O) L(1)
 :  : DEC T(ST) K(B£O**) L(1)

# Exit della £IVD
Nell'accesso sql all'archivio corrispondente ad un oggetto è inoltre possibile applicare delle proprie considerazioni (es. filtri impliciti basati su autorizzazioni). Il suo effetto si manifesta attraverso la /COPY £IVD, sulla base della quale, vengono fondati tutti gli accessi SQL di un oggetto.
Al momento tale funzionalità ha lo svantaggio di essere applicabile esclusivamente agli accessi SQL. Va quindi applicata tenendo conto di questa considerazione.

 :  : DEC T(MB) P(QILEGEN) K(£IVD) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£IVD0_U) L(1)



