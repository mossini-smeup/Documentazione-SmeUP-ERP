# Come trovare la documentazione di Sme.up
La documentazione si può reperire direttamente dall'interno dell'applicazione :  in ambiente grafico, attraverso Looc.up, possiamo visualizzare sia la documentazione interna i cui i testi sono scritti su archivi AS/400 che la documentazione esterna (internet o cartelle windows), purché il sistema sia configurato per l'accesso all'esterno.

# Documentazione completa - dal menù a tendina di Looc.up
>My Loocup > Documentazione > Completa
si apre la scheda della documentazione di Sme.up, che permette di accedere ai documenti dei vari moduli / applicazioni : 


![T001B](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001B.png)questa è la scheda della documentazione del modulo >B£DOCU,  relativo alla gestione della documentazione.

La scheda di questo modulo è organizzata in varie sottoschede : 
## Tutta la documentazione
Mostra la documentazione del modulo >B£DOCU e, in coda, il capitolo >"Documentazione Applicazioni", che può essere esploso per visualizzare tutti i documenti presenti e collegati ad un'applicazione o a un modulo : 


![T001A](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001A.png)
## Organizzazione della documentazione
Ne descrive la classificazione : 


![T001U](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001U.png)
## I documenti
Questa sottoscheda ha una prima sezione divisa a sua volta in ulteriori sottoschede, ognuna personalizzata a una tipologia di documenti, le cui caratteristiche sono presentate  in forma di matrice : 

- >documentazione attiva, si tratta degli stessi documenti visualizzati nella sottoscheda >"Tutta la documentazione";
- >documentazione degli oggetti, sono i documenti associati a :  Programmi, Archivi, Help di tabella, Valori fissi Sme.up;
- >documentazione dei servizi,
- >documentazione dei modelli, documenti di presentazione o spiegazione dei modelli di installazione o di dimostrazione;
- >domande e risposte;
- >glossario, dei termini caratteristici utilizzati.

nella parte destra della sottoscheda viene presentato il documento selezionato : 


![T001M](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001M.png)
## I manuali
Permette di accedere al link internet, dove sono presenti i book di Sme.up : 


![T001C](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001C.png)
## Le News e le Note Tecniche
Questa scheda permette di accedere al link internet contenente le News di Sme.up : 


![T001N](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001N.png)
## Ricerca contenuto
Data una libreria e un file, questa scheda permette di recuperare tutti i documenti che soddisfanoi criteri di ricerca (es. :  documenti che contengono una parola o un gruppo di parole nel titolo o nel contenuto) : 


![T001O](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001O.png)
## Gli script
Presenta un albero di librerie e file contenenti degli script.
Selezionando un file, viene mostrata la matrice dei membri >SCP_xxx, che si possono visualizzare e analizzare in diverse modalità : 


![T001P](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001P.png)
# Ricerca documentazione per contenuto - dal menù a tendina di Looc.up
>My Loocup > Documentazione > Ricerca contenuto
si apre la stessa scheda "Ricerca contenuto" descritta in precedenza.

## Documentazione applicazione - dal menù a tendina di Looc.up
>My Loocup > Applicazioni > <selezionare l'applicazione>

Si apre la _2_Scheda dell'applicazione, in cui molte sezioni sono dedicate alla comprensione e quindi alla documentazione della corrispondente applicazione : 


![T001H](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001H.png)
Abbiamo : 

- >Navigazione; presenta tutte le funzioni previste dall'applicazione ed organizzate secondo il menu standard.
- >Documentazione applicazione; permette di accedere alla documentazione attiva dell'applicazione
- >Modelli dinamici; rimanda alla scheda del modello dinamico dell'applicazione (vedi anche il paragrafo successivo relativo alla documentazione dinamica)
- >Set'n play; visualizza gli oggetti significativi dell'applicazione (oggetti applicativi, oggetti di sistema, tabelle e sottosettori, ...) e le API. _2_Nota, quello che viene visualizzato dalla scheda è presente in una schiera contenuta nel programma B£AR18 a cui si rimanda.
- >Servizi e azioni; presenta la lista dei servizi, delle azioni e ancora della API previste per l'applicazione
- >Dati; elenca gli archivi di cui l'applicazione è proprietaria e per ogni archivio è possibile lanciare la relativa scheda oggetto
- >Documenti; permette di accedere a diverse tipologie di documenti che possono essere collegati con l'oggetto (es. se l'oggetto è un cliente si potrebbe accedere alle e.mail a lui riferite), nel caso dell'applicazione tra i documenti accessibili ci sono le cartelle contenenti i i documenti commerciali e quelle contenenti le immagini.

>NB. : 
Selezionando un singolo modulo dal tab. Navigazione, ne viene proposta la scheda, contenente una parte delle funzioni viste per l'intera applicazione.

## Reperire la documentazione (modalità emulazione 5250)

>My Loocup > Applicazioni > <selezionare l'applicazione> <lanciare la funzione "Documentazione applicativa"
Questa funzione è la medesima utilizzabile in ambiente non grafico da terminali nativi AS/400 o da Client/Access.
Viene aperto il menù delle varie tipologie di documentazione per applicazione : 


![T001Q](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001Q.png)
## Archivi utilizzati
La documentazione è scritta fisicamente in membri AS/400 del file DOC, i vari membri sono organizzati su più livelli :  i documenti di dettaglio sono a livello modulo mentre quelli più generali sono a livello applicazione (ad esempio un'istruzione operativa normalmente si trova a livello modulo, e un documento visione si trova a livello applicazione).

### Casi particolari
_2_Documenti di carattere generale (es. :  la visione architetturale di Sme.up) che sono al di sopra dell'applicazione vengono posti nell'applicazione B£ (Funzioni di base).

_2_Documenti di carattere tecnico (es. :  gli standard di programmazione) sono posti nell'applicazione A£ (Funzioni tecniche)

I documenti degli oggetti sono presenti su file specifici ed hanno delle convenzioni di denominazione : 

- _3_Help di tabelle, sono nel file DOC_OGG ed hanno un nome che inizia per TA_
- _3_Programmi, sono nel file DOC_OGG ed hanno un nome che inizia per P_
- _3_Archivi, sono nel file DOC_OGG ed hanno un nome che inizia per F_
- _3_Valori fissi Sme.up, sono nel file DOC_OGG ed hanno un nome che inizia per V2_
- _3_Servizi, sono nel file DOC_SER ed hanno un nome che inizia con il codice applicazione a cui il servizio è riferito
- _3_Help delle schede, sono scritti direttamente in fondo al membro di script della scheda :  il sistema interpreta il testo presente in corripondenza del primo tag titolo (T01, T02, T03) e tutte le righe successive come documentazione di help della scheda.


_2_Documenti specifici del cliente di norma vengono posti nell'applicazione convenzionale X1 (Personalizzazioni)

### Immagini
I documenti possono includere delle immagini (schemi, figure, printscreen, ecc...) queste immaginisono visibili solo quando si consulta la documentazione via Looc.up
Le immagini devono stare in ambiente windows in un percorso codificato la cui parte finale è :   \TAB£A\aa\mmmm (dove aa = applicazione e mmmm = modulo) mentre la radice è denominata [SME.IMG] ed è risolta dalle impostazioni di setup di Loocup che sono presenti come script nel file SCP_CLO da una istruzione di tipo C.VAR, vedi esempio seguente : 

_1_C.VAR Cod="SME.IMG" Txt="Immagini" Value="\\server\dati\immagini loocup" TVal="J1" PVal="PATHDIR"
(_3_Nota :  l'istruzione C.VAR, come tutte le istruzioni degli script di Loocup, deve essere preceduta da 2 caratteri duepunti " : ")

Le impostazioni di setup possono essere a livello di : 

- default (il membro ha nome :  DEFAULT)
- ambiente (il membro ha nome :  A_xxx dove xxx è il codice ambiente)
- gruppo utenti (il membro ha nome :  G_xxx dove xxx è il codice del gruppo utenti)
- utente (il membro ha nome :  xxxxxx dove xxxxxx è il profilo con cui l'utente si collega all'AS/400)

nel ricercare le impostazioni C.VAR si esegue la risalita dal dettaglio massimo (utente) al livello più generale (default).

## Stampare i documenti
I documenti possono essere stampati attraverso le opzioni di Loocup che creano un file di tipo PDF che può essere salvato o stampato.
Questa funzione si lancia dal menù contestuale al documento (tasto destro dal tab della sottoscheda), voce "Stampa della sezione" : 

![T001R](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001R.png)
viene emessa una finestra che contiene le impostazioni di stampa : 


![T001S](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001S.png)
dopo aver compilato i parametri di impostazione, con il tasto ENTER si lancia la creazione del PDF.

## Dove trovare la documentazione dinamica
La parte preponderante della documentazione dinamica è il modello dinamico dell'impresa, cioè il risultato della customizzazione applicata all'implementazione, a questo scopo sono state create le funzioni associate ai modelli dinamici con le quali, attraversando gli oggetti di un'applicazione si può creare ed analizzare il modello di cui esiste la scheda nell'applicazione C£, modulo C£MODI : 

![T001T](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001T.png)
Altri punti di esplorazione di questa documentazione sono i seguenti : 

- _2_Dall'elemento di tabella, di ogni elemento di tabella si può operare il "drill down" che evidenzia la distinta degli impieghi in altre tabelle, sia in visualizzazione che in stampa.

_3_Scheda tabella, un altro modo per accedere alla documentazione è rappresentato dalla "scheda" :  aprendo la scheda tabella si possono interrogare : 
-- "drill down"
-- "documentazione della tabella"
-- "documentazione dell'elemento di tabella" (se presente, è una documentazione specifica dell'implementazione e si trova nelle note di tabella)


![T001F](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001F.png)

- _2_Dall'oggetto applicativo, si possono stampare tutti i metodi e le proprietà degli oggetti, esplodendo sulle diverse classi dell'oggetto.

_3_Oggetti particolari, determinati tipi di oggetti (archivi, programmi, elementi di tabella) hanno schede particolari nelle cui sezioni è prevista anche la documentazione. Dell'elemento di tabella abbiamo appena trattato, se l'oggetto è un programma la relativa scheda è quella visualizzata in uno dei paragrafi seguenti, se l'oggetto è un file la scheda che si apre prevede : 
-- "documentazione testuale"
-- "elenco logici collegati e relative chiavi"
-- "tracciato record"


![T001G](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001G.png)

- _2_Dalla documentazione di applicazione, si possono intervistare con metodi di accesso diversi le impostazioni dei modelli.

_3_Scheda applicazione, questa scheda permette di analizzare l'applicazione interrogando : 
-- "documentazione"
-- "servizi"
-- "archivi"
-- "modelli dinamici"
-- ecc....
a loro volta, per gli oggetti che vengono visualizzati si può accedere alla relativa scheda e quindi documentazione.


![T001H](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001H.png)

- _2_Tasto destro del mouse sull'icona server, in alto a destra delle mappe video, selezionando "Scheda Programma" : 


![T001D](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001D.png)
Il sistema presenta la scheda dell'oggetto programma dalla quale si può accedere sia alla documentazione applicativa che a quella tecnica : 

![T001E](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001E.png)

- _2_Dal formato guida dell'emulazione, attivando la "Funzione" (click sull'icona schermo oppure F2) e successivamente cliccando F1 si apre l'help di funzione.


![T001I](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001I.png)

![T001L](http://localhost:3000/immagini/MBDOC_OPE-B£DOCU20OL/T001L.png)