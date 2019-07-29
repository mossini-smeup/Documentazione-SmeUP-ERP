# Organizzazione dei Menù Sme.up
Le funzioni Sme.up sono attivabili attraverso elementi della tabella MEA dove è scritto il programma di lancio ed i parametri di controllo dell'azione.
Le funzioni sono raggruppate in menù secondo diverse modalità; anche i menù sono elementi della MEA in cui il campo "Tipo azione" è "M".

I diversi criteri di organizzazione delle azioni (diverse tipologie di menù) sono identificati dal campo "Programma azione" : 

***AP "Applicazione"**
Si tratta della impostazione con cui viene fornito il sistema. I menù di tipo applicazione corrispondono esattamente ai sottosettori della tabella MEA e le voci che li compongono non sono altro che gli elementi della MEA del sottosettore corrispondente. Ad esempio tutti gli elementi della MEA che sono presenti nel sottosettore BR sono del modulo Brec.up, il menù che li richiama ha "BR" nel campo "Parametro".

Normalmente con questa impostazione si usano degli elementi di "titolo" per raggruppare azioni omogenee, questi elementi di titolo hanno "T" nel campo Tipo azione. In Looc.up le azioni raggruppate da titolo vengono presentate come cartelle, esiste un metodo per visualizzare in Looc.up le cartelle e le sotto cartelle :  quando il Tipo azione è T se il campo programma azione ha una "L" seguita da un numero (es. 03) tutte le azioni successive fino al prossimo titolo, vengono presentate in una sottocartella al livello 3, se il titolo successivo ha un livello diverso (es. 01) tutte le azioni successive vengono presentate in una sottocartella a livello 1.

***UL "User List"**
Con questo metodo l'utente si può creare il proprio menù raggruppando tutte le azioni di suo interesse. Tecnicamente viene creata una MDV (ambiente = B£MENU e utente = **nome) dove "nome" è il nome dato dall'utente in fase di costruzione del menù.
_R_Modalità di creazione dei menù *UL
    -- Nel campo Opzione a sinistra delle azioni si inserisce un "+" (più) per selezionare, se si vuole deselezionare un'azione inserire un "-" (meno). Confermare la scelta con -INVIO-
    -- Per vedere la lista delle azioni selezionate premere F7  dalla lista si possono ancora escludere le azioni dalla selezione
    -- Con F6 si apre una finestra dove associare il nome al gruppo creato. Nel campo "Gruppo" inserire "*UL" e nel campo "Menù" digitare il nome scelto
    -- Confermare l'inserimento con F6.

_1_ATTENZIONE
Ogni volta che si conferma con F6 si perdono tutte le impostazioni confermate in precedenza :  restano valide solo le ultime

_r_Casi Particolari
***USER** (è una MDV memorizzata con nome -*)
***LAST** (è una MDV memorizzata con nome .*)
***MAIN** (Carica tuttii i tipi di menù esistenti)

 :  : INI Gestione MDV
 :  : CMD CALL B£MDV0
 :  : FIN

**Elementi Tabella B£NME (Parametri variabili)**
Questo metodo serve per creare menù associati ad uno degli oggetti Sme.up, tipicamente gli oggetti interessati possono essere :  il dipendente, il reparto, la risorsa, un elemento di una tabella, .....
Per la costruzione dei menù bisogna far riferire questi oggetti a dei parametri multipli creati nel sottosettore "ME" della tabella "B£N". Nella tabella MEA il parametro creato deve essere messo nel campo "Programma/Azione", mentre nel campo "Parametro" si inserisce il valore dell'oggetto a cui si vogliono associare le azioni sottostanti il menù.
Ad esempio, se voglio creare dei menù per reparto : 
- se manca la tabella reparti ne creo una (es. XRP con elementi 001 = Uff. Tecnico, 002 = Uff. Acquisti, ...)
- creo un elemento della tab. B£N_ME di tipo :  oggetto,  facoltativo, multiplo, riferito alla tabella XRP (es. REP)
- per il menù delle azioni di competenza dell'Uff. Tecnico creo un elemento della MEA con Tipo azione = M, Programma/Azione = REP, Parametro = 001
- in tutte le azioni che voglio dare anche all'Uff. Tecnico devo andare sui parametri dell'elemento mea (F10, 11) ed inserire 001 nel parametro REP
- per il menù Acquisti stesso procedimento :  creo una MEA con parametro 002 e a tutte le azioni degli Acquisti inserisco 002 nel parametro REP

Un metodo alternativo all'inserimento manuale dei parametri REP nelle azioni è quello visto in precedenza di selezionare le azioni con + <ENTER>, visualizzare con F7, con F6 aprire la finestra dove inserire Gruppo = REP, Menù = 001 (Uff. Tecn.) 002 (Uff. Acq.), .....

_1_ ATTENZIONE
Ogni volta che si conferma con F6 si perdono tutte le impostazioni confermate in precedenza :  restano valide solo le ultime

 :  : DEC T(ST) P() K(B£NME) I(_9_Gestione elementi Tabella B£NME >>)
 :  : DEC T(TA) P(C£E) K(MEA) I(_9_Gestione elemento MEA Tabella C£E  >>)

 :  : INI Gestione parametri Categoria MEA
 :  : CMD CALL C£CR01G PARM('MEA')
 :  : FIN

In Looc.up i menu creati con il metodo B£N compaiono sotto una cartella specifica con la descrizione dell'elemento della B£N (es. REPARTO).

**Funzioni utili**
_r_F09 Il comando fa avanzare la lista delle azioni al gruppo successivo (es. se sono presentate le azioni di un reparto con F9 vengono presentate le azioni del reparto successivo) In pratica si scorrono tutti i valori del primo campo in alto a sinistra.

_r_F10 Il comando fa avanzare la lista delle azioni di un gruppo al menù successivo (es. se sono presentate le azioni BR con F10 si passa alle azioni C£) In pratica si scorrono tutti i valori del secondo campo in alto a sinistra.

_r_F16 Il comando porta al menù principale delle applicazioni (*AP 00).

# Generazione dei menù
Per generare le voci di menù standard è sufficiente lanciare l'esecuzione del pgm B£MNU0 il quale cancellerà e riscriverà tutti i sottosettori della tabella MEA corrispondenti agli elementi della tabella B£A (in questa rigenerazione solo le voci con codice alfabetico che vengono riconosciute come personalizzazioni non vengono toccate). Il pgm può anche essere richiamato passando la singola applicazione

Esiste inoltre il programma B£IN32 che permette di ricavare le azioni da formati video preesistenti (per esempio dei menù ACG).

 :  : DEC T(ST) P() K(B£A) I(_9_Applicazioni)
 :  : INI Chiamata B£MNU0
 :  : CMD CALL B£MNU0
 :  : FIN
 :  : INI Chiamata B£IN32
 :  : CMD CALL B£IN32
 :  : FIN

# Documentazione oggetti da Menù
Dalle voci menù è inoltre possibile richiamare i link di documentazione esterna legati al sottosettore della tabella MEA indicati nella tabella B§T. Per richiamarne l'elenco è sufficiente mettere l'opzione **D** su una qualsiasi voce di menù.

 :  : DEC T(ST) P() K(B§T)

# Modalità di esecuzione
## Da ambiente
Se trovato viene caricato il menù richiesto, altrimenti vengono caricati tutti i gruppi esistenti.

## Riga comando
A seconda del metodo di chiamata si attivano i seguenti comportamenti.

## Ultimo menù
Richiamato senza passare nessun parametro. Non viene permesso l'abbandono dei menù.
  CALL B£MNU


### Menù applicativo
E' il sottosettore della tabella MEA. Se trovato viene caricato il menù richiesto, altrimenti si comporta come "Ultimo menù"  Viene permesso l'abbandono dei menù.
  CALL B£MENU PARM('00')

Non viene permesso l'abbandono dei menù.
  CALL B£MENU PARM('00' 'X')

### Menù Sme_up
Se trovato viene caricato il menù richiesto, altrimenti vengono caricati tutti i gruppi esistenti. Non viene permesso l'abbandono dei menù.
  CALL B£MENU PARM('00' 'X' '*AP')

# Eccezioni in ambiente Looc.up
Non sono caricati i menu di tipo
**A** Acg
**C** Comando AS/400

Non sono caricate le seguenti azioni
**K** Menù Acg
**C** Comando AS/400

E' possibile la sola navigazione e non la gestione.
