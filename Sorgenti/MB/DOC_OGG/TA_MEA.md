# MEA - Menù - azioni SME_up
## ELEMENTO STANDARD
Attraverso l'elemento standard si vuol distribuire una struttura di menù non modificabile definita in laboratorio. L'elemento standard possiede le seguenti caratteristiche : 
* é numerico
* il sotto settore dell'elemento è un'applicazione
L'unico campo ammesso alla modifica è lo__User Level__

## ATTENZIONE
_1_NOTE SU UTILIZZO CAMPO LIBERO
Per la tabella MEA a differenza di quello che avviene normalmente per le tabelle il campo libero è stato riservato dallo standard.

In funzione di quanto definito nei campi "Tipo azione" e "Programma/Azione", vanno indicati i parametri da utilizzare per eseguire l'azione.
**NB** :  nel caso di menu Sme.up (tipo richiamo 'M'), se nel campo 'Programma/Azione' è inserito '*AP', nel campo in esame va inserito il codice del menù (sottosettore MEA). Al contrario, se non è inserito '*AP', va inserito il codice del parametro della tabella (B£NME) e nel campo in esame il contenuto del parametro. Da notare in quest'ultimo caso che il contenuto delcampo può assumere i valori sotto indicati : 
- _4_&OAooppppppppaaaaaaaaaa;
- _4_&PGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.;
- _4_&UG;
Dove : 
- **&OA** indica al programma che il contenuto del parametro sarà variabile e recuperato, tramite un attributo dell'utente che richiede il richiamo del menu;
- **oo**  indica l'oggetto con cui si identifica l'attributo dell'oggetto (es. UT oppure OJ*USRPRF oppure TA);
- **ppp** indica il parametro dell'oggetto dell'attributo (nell' esempio di oggetto TA sarà B£U);
- **aaa** è il codice dell'attributo (esempio I/T$B£UA nel caso di gruppo utente della tabella B£U);
- **&PG** indica al programma che il contenuto del parametro sarà variabile ed impostato tramiteil richiamo del pgm utente B£MENU_U;
- **&UG** indica che il parametro da utilizzare è il gruppo utente della tabella B£U;

_r_ Documentazione generale del modulo B£MENU
- [Menù Sme.up](Sorgenti/MB/DOC/B£MENU)

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Codice__
Indica il codice della voce di MEA.
 :  : FLD T$MEAE __Tipo azione__
Questo elemento viene gestito dal pgm specifico della tabella (B£TMEA). Può assumere i seguenti valori : 
- **" "=Chiamata ad un programma** :  Chiamata interattiva di un pgm
- **"S"=Immissione in batch di un pgm** :  permette di lanciare il pgm attraverso la £GPE;
- **"A"=Azione ACG (1=Azione 2=Sis.Inf.)** :  permette di eseguire un'azione ACG;
- **"M"=Menù di SME_up** :  richiama un altro menù della tabella MEA;
- **"G"=Menù AS/400** :  è l'equivalente del comando AS GO;
- **"K"=Menù Modulo base ACG** :  richiama un menù di tabella;
- **"T"=Titolo** :  non compie nessuna azione, ha valore solo come titolo;
- **"C"=Comando AS400** :  permette di eseguire un comando AS;
- **"J"=Funzione grafica client** :  permette di eseguire una funzione grafica del modulo Looc.up;
- **"D"=Scheda del modulo** :  permette di eseguire la scheda del modulo impostato (che in questo
       caso è un campo obbligatorio).
       In 5250 questa voce si comporta come se fosse un titolo di primo livello (campo
       Programma/Azione riempito con il valore "L01").
       La descrizione di questa azione viene impostata in automatico derivandola dal modulo,
       all'aggiornamento dell'elemento di tabella.
      **Nota interna laboratorio : **
       All'aggiornamento dell'elemento viene inoltre memorizzata la F di richiamo nella parte utente
       della tabella, in modo che il comportamento sia uguale alle azioni di tipo 'J'.
       Ogni sera viene eseguita la generazione dello script del menu standard, in questa fase le
       descrizioni delle azioni della scheda del modulo verranno riaggiornate derivandole
       dal modulo (B£UT53S)
 :  : FLD T$MEAA __Programma/Azione__
Questo campo è significativo se il tipo azione è : 
' ' (programma) Si imposta il nome del programma. I parametri vanno invece impostati nel campo
                libero.
'T' (titolo)    Si imposta "Lnn" per indicare il livello del sottomenù.
                Nella gestione loocup e nella gestione ad albero rappresenta il livello di apertura
                della tendina. Le azioni sottostanti, fino ad una nuova azione 'T', appartengono
                allo stesso sottomenu (tendina).
'M' (menù)      Si imposta il primo codice di definizione del menù (tipicamente *AP)

Ricordiamo che in caso di azione 'J' o 'D' si imposta la funzione nel campo libero (per l'azione 'D'
questo viene fatto in modo automatico dal gestore di tabella).
In caso di azione 'J', si possono inserire i singoli campi (servizio, funzione, oggetti, ecc..)
oppure scrivere la F e popolare i campi sovrastanti con F21.
In caso di azione 'M', si indica invece la seconda parte del codice del menù (tipicamente il
codice del sottosettore della MEA)

 :  : FLD T$MEAC __Categoria di protezione__
Configurando opportunamente la tabelle *CNME e B£SME, è possibile raggruppare le voci di menù in modo da renderle oggetto di autorizzazione.

Nel caso delle voci di menù derivate dalla tabella MEA il tema non è quello di una "autorizzazione a ..." bensì di una "esclusione da ...". In questo senso, attraverso la gestione autorizzazioni (UP AUT) i valori ammessi SI/NO sono da intendersi rispettivamente come ESCLUSO DALLA VOCE MENU/AMMESSO ALLA VOCE MENU, con una logica quindi opposta rispetto al normale concetto delle autorizzazioni.

 :  : FLD T$MEAD.T$MEAC __Codice di protezione__
 :  : FLD T$MEAF __Richiesta di conferma__
_4_Attiva solo in modalità 5250
È un elemento V2SI/NO. Se impostato, prima delle esecuzione dell'azione verrà sempre esplosa una finestra di conferma.
 :  : FLD T$MEAG __Gruppo grafico__
_4_Attiva solo in modalità 5250
Se si imposta un attributo video, viene modificato il colorfe della voce.
 :  : FLD T$MEAL __Modulo Appartenenza__
È un elemento della tabella B£AMO e rappresenta il modulo di appartenenza dell'azione. Se non
impostato viene considerata una azione di Applicazione.
Attraverso la sua presenza si attivano i seguenti effetti : 
* L'azione sarà soggetta alle autorizzazioni previste per il modulo di appartenza
* L'azione in ambiente loocup, verrà utilizzata nel modulo di appartenenza, altrimenti
  verrà visualizzata non nel menù di ingresso.
Questo campo è obbligatorio nei seguenti casi : 
* Azioni standard
* Azioni specifiche di sottosettori (applicazioni) standard. Questa obbligatorietà può essere
  forzata impostando 'N' nel campo "No modulo su std".
* Tipi azioni 'D' (indipendentemente dal valore impostato nel campo "No modulo su std").
Viene controllato che il modulo appartenga al sottosettore (applicazione della MEA), ad eccezione
delle voci 'D'. Esse infatti non indicano il modulo di appartenenza ma il modulo di esecuzione, in
quanto vengono esposte sempre al primo livello del menu (a destra). E'quindi possibile inserire
moduli di applicazioni diverse da quella del sottosettore in corso (ad esempio nelle vendite, V5,
si inseriscono i listini).
Il modulo è quindi facoltativo, senza ulteriori forzature, in azioni di sottosettori
(applicazioni) specifiche, che, a loro volta, possono essere solo azioni specifiche.
Anche in questo caso, il modulo, se impostato, deve esistere in tabella.
Il significato del diverso comportamento in applicazioni standard e specifiche, è di rendere
naturale l'assegnazione di tutte le azioni a moduli, in caso di applicazioni standard, mentre
per le applicazioni specifiche è lasciata la massima libertà.
 :  : FLD T$MEAM __User Level__
Fissa un livello corrispondente alla classe d'autorizzazione USRLVL, tramite cui la voce sarà visibile solo agli utenti che hanno un livello di autorizzazione maggiore o uguale a quello indicato in questo campo.
Nella fasatura tramite PTF XX99999B viene mantenuto lo Usrlvl dell'ambiente cliente a meno che non sia un elemento che passa da in sviluppo ad un altro usrlvl.
**Attenzione : ** l'UP FTB non fa queste considerazioni.
**Attenzione 2 : ** se la voce presenta l'indicazione di un modulo, la voce eredita lo userlevel del modulo e/o dell'applicazione di appartenenza del modulo, qualora uno dei due sia superiore (più restrittivo) allo userlevel della voce.
 :  : FLD T$MEAN __Parametro Tipo Oggetto__
_4_Attiva solo in modalità Loocup
Questo campo viene utilizzato solo se il campo "Modulo Appartenenza" è valorizzato.
In questo caso, se il modulo è parametrato (vale a dire il suo oggetto master ha il parametro
obbligatorio, ad esempio gli Enti, i documenti V5, ecc...), e l'azione è una CALL, nel presente
campo si indica in quale parametro verrà inserito il parametro attualmente attivo.
Ad esempio, se si è nel modulo BRENTI1, il parametro attivo è CLI, l'azione è
"CALL PGM(xxxx)", impostando nel presente campo "1", l'azione diventerà : 
"CALL PGM(xxxx) PARM('CLI')"
Il parametro può andare anche in sostituzione, sovrascivendo la parm corrispondente : 
Ad esempio, l'azione "CALL PGM(xxxx) PARM('xx' 'yy' 'bb'), impostando a "2" il presente campo,
diventerà "CALL PGM(xxxx) PARM('xx' 'CLI' 'bb').
Per quanto riguarda il parametro attivo dei moduli parametrati, per le funzioni grafiche, è invece possibile indicare l'utilizzo delle variabili "&" disponibili anche nelle schede. In merito al campo parametro, questo è normalmente contenuto nella variabile &IN.PMK.
 :  : FLD T$MEAO __Esegui sempre__
_4_Attiva solo in modalità Loocup
Se impostato, l'azione verrà eseguita ad ogni selezione, non tenendo conto della cache presente.
 :  : FLD T$MEAI __Emulaz./Looc.UP__
E'possibile impostare se la voce è visualizzata solo in un ambiente : 
* 1  :  5250
* 2  :  Loocup
* N  :  La voce sarà valida solo per altri device (es. Phone/Tablet)
Alcune voci sono implicitamente di un ambiente, in base a quanto impostato nel campo "Tipo Azione"
* "A" Azione ACG                    Solo 5250
* "G" Menu AS400                    Solo 5250
* "K" Menu modulo base ACG          Solo 5250
* "C" Comando AS400                 Solo 5250
* "J" Funzione grafica Client       Solo Loocup
 :  : FLD T$MEAP __No modulo su std__
Questo campo è significativo unicamente in caso di azioni non standard in applicazioni
standard.
Se lo si imposta a 'N' si ha l'effetto che il modulo deve essere obbligatoriamente bianco, e qundi
l'azione viene visualizzata al primo livello dell'applicazione (sottosettore) in cui è inserita.
Nelle azioni standard è vuoto, nelle azioni non standard di applicazioni non standard il modulo è
facoltativo indipendentemente dal presente campo.
Per la descrizione degli effetti provocati dalla compliazione del campo modulo, si rimanda alla
documentazione specifica di questo campo.
 :  : FLD T$MEAQ __Grafica azione menù__
_4_Attiva solo in modalità Loocup
Questo campo è utilizzato solo per azioni del menù di ingresso degli utenti, dall'ambiente loocup e solo qualora queste azioni richiamino a loro volta un altro menù.
Tramite il presente campo è possibile indicare se il menù richiamato verrà esposto con una forma grafica di albero o di image list. NOTA BENE :  questa seconda modalità (IML) può essere applicata solo il menù richiamato è monolivello.
Tramite il valore "E" invece il menù di secondo livello verrà esploso direttamente nel menù di primo livello.
 :  : FLD T$MEAR __Surf__
_4_Attiva solo in modalità Loocup
Questo campo viene utilizzato se il campo "Modulo Appartenenza" è valorizzato ed il campo
ed il campo "Utilizzo modulo" è lasciato in bianco.
Normalmente la voce viene riportata tra le "ACTIONS" del modulo :  se si imposta il presente campo essa verrà riportata nei "SURF" (dopo gli eventuali Surf standard).
In tal modo si possono riportare interrogazioni dei dati del modulo nella loro posizione naturale.
Vi sono alcune azioni standard che hanno valorizzato il presente campo :  sono surf che non sono stati costruiti con la funzione standard (£G46) e che saranno eliminati quando verrà realizzata quest'ultima funzione.
Indicando il valore "2", oltre a quanto sinora descritto, si ha inoltre l'effetto di rendere disponibile tale funzione nelle ricerche dell'oggetto corrispondente al modulo (si veda funzione/metodo OGG.MOC della £K01).

 :  : FLD T$MEAS __Ordinamento__
Questo campo permette di emettere il menù nella sequenza ritenuta più opportuna. L'ordinamento
è dato dalla concatenazione di Ordinamento e Codice elemento. Quindi nel caso non venga compilato
alcun Ordinamento nel sottosettore la sequenza è determinata dal Codice.

 :  : FLD T$MEAT __Tipo Icona__
Il valore impostato determina il tipo e parametro dell'oggetto dell'icona da associare
all'elemento nei menù in Loocup.

 :  : FLD T$MEAU __Codice Icona__
E' il codice dell'oggetto dell'icona da associare all'elemento nei menù in Loocup. Deve essere
compilato in relazione al campo Tipo Icona

 :  : FLD T$MEAV __Voce dinamica__
Indica che i sottomenù della voce di menù vengono generati utilizzando la funzione presente nel
campo Parametro/Funzione. Questo campo ha significato solo per i sottosettori £S e £L .

 :  : FLD T$MEAW **Phone**
Se impostato attiva una funzione J o D su un Device di Tipo Phone

 :  : FLD T$MEAZ **Tablet**
Se impostato attiva una funzione J o D su un Device di Tipo Tablet

 :  : FLD T$MEAY **Livello di modifica**
Campo che, se opportunamente impostato, permette di non far apparire la voce nel menù di competenza. Questo flag può assumere i seguenti significati : 
- ' '=Attiva :  la voce è visibile;
- '1'=In sviluppo :  la voce di menù non è visibile perchè è ancora in fase di sviluppo;
- '2'=Sospesa :  la voce non è visibile perchè momentaneamente non attiva;
- '3'=Obsoleta :  la voce non è visibile perchè superata da altre voci o perchè non più supportata;
