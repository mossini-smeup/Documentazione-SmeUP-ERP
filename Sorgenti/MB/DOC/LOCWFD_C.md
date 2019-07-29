# Esecuzione dei test

## Cosa il componente è in grado di rappresentare
Il componente può rappresentare diagrammi di Workflow oppure di Ordini.
Questo significa che se all'interno di Loocup mi trovo su un oggetto di tipo TA WFA oppure di un oggetto F1 posso visualizzare la relativa scheda e utilizzare il componente grafico WFD.


## Prerequisiti all'utilizzo del componente

- Loocup V2R3M091109 (onde rosse)
- Upgrade dal 18/02/2010

## Ambienti e script

Nell'ambiente SVI, dalla scheda utente, selezionare "Workflow", poi "Inserimento".
Tasto destro su uno dei processi e aprire la sua scheda.

Nel primo pannello ci sono i pulsanti per paragonare la visualizzazione del diagramma del processo nella versione vecchia e nuova.
Nel pannello "script" posso editare lo script sia con l'editor che con la modalità grafica nuova.

Se invece si vuole consultare un processo già iniziato si può utilizzare la scheda "Workflow" poi "Ordini" :  doppio click su un ordine e sulla scheda relativa selezionare il tab "Situazione Ordine".
In questo modo è possibile consultare il diagramma dell'ordine sia nella vecchia modalità con il componente GRP che con il nuovo componente WFD.

Per eseguire dei test sulla funzionalità dell'appilcazione WF è stato predisposto l'ambiente D29.


## Script di test

 :  : VAR Name="Tgfre" Des="vew"
 :  : VAR Name="fer1" Des="fvwe"
 :  : VAR Name="dd1" Des="vewgfwerg"

-Commento
 :  : 

 :  : TRA Name="T03" Cce="**" PosY="406" PosX="862" Des="Tipo parte 1"
    :  : REQ.EXT.C Con="&AWF.OMS%I/09=1"
    :  : FROM
   -Commento
    :  : LUO Name="L03" PosY="197" PosX="880" Des="Intermedio 2"
    :  : TO
      -Commento
       :  : LUO Name="L20" PosY="399" PosX="1253" Des="Intermedio 20"
       :  : LUO Name="L04" PosY="721" PosX="877" Des="Intermedio 4"
 :  : TRA Name="T4" PosY="732" PosX="1235"
    :  : FROM
      -Commento
       :  : LUO Name="L20" PosY="399" PosX="1253" Des="Intermedio 20"
    :  : TO
       :  : LUO Name="L04" PosY="721" PosX="877" Des="Intermedio 4"
 :  : TRA Name="T01" Dic="1" Cle="1" Cce="**" PosY="206" Pad="1" PosX="712" Azg="B" Des="Modifica articolo"
    :  : DIC.FUN Fun="A(WFAZB _02;GES;02) 3(AR;;&AWF.OMS)" Des="Modifica articolo"
    :  : FROM
       :  : LUO Name="L01" PosY="107" PosX="725" Tip="I" Des="Partenza"
    :  : TO
       :  : LUO Name="L03" PosY="197" PosX="880" Des="Intermedio 2"
       :  : LUO Name="L02" PosY="200" PosX="578" Des="Intermedio 1"
-Commento
 :  : TRA Name="T02" Cce="**" PosY="406" PosX="562" Des="Unit  misura NR"
    :  : REQ.EXT.C Con="&AWF.OMS%I/07=NR"
    :  : FROM
       :  : LUO Name="L02" PosY="200" PosX="578" Des="Intermedio 1"
    :  : TO Tip="C"
       :  : WHN Con="1" Des="Chiudi articolo"
          :  : LUO Name="L0S4" PosY="721" PosX="877" Des="Intermedio 4"
       :  : WHN Con="2" Des="Chiudi articolo"
          :  : LUO Name="L" PosY="505" PosX="445" Des="Idio 3"
       :  : OTH Des="Lascia l'articolo aperto"
          :  : LUO Name="L05" PosY="764" PosX="578" Tip="F" Des="Finale"



## Funzione di esempio

Lanciare questa funzione : 
F(WFD;*EDTLET;) 1(MB;SCP_WFA;ESE_NEW)



# Testing release 1.0
Vanno verificate le funzioni di Editing, sia modificando frammenti di script che aggiungendone di nuovi.
Vanno inoltre contemporaneamente testate le funzioni di visualizzazione e sul formato in cui uno script viene salvato.


## Operatività
Copiare il file SCP_WFA nella propria W e poi utilizzare l'ambiente SVIU.
Appuntarsi quale test è stato compiuto e l'esito ed eventuali condizioni particolari di test.
Se si è impossibilitati a compiere un test per problemi tecnici di "ambiente" o di competenze, annotare i motivi.


## Elenco di test da compiere

### Test di stress

- posizionare le transizioni con X o Y molto grandi (oltre le dimensioni dello schermo), negative, nulle o a zero.
- verificare il comportamento quando ho più transizioni o luoghi sovrapposti, sia in visualizzazione che in modifica grafica
- verificare il comportamento di diagrammi complessi in visualizzazione e modifica quando ho : 
-- molte transizioni (almeno 50)
-- molti luoghi (almeno 50)
-- molti collegamenti anche con condizionati (almeno 50)
-- posizionare molte transizioni e luoghi allineati sull'asse X e poi allineati sull'asse Y, superando i limiti di visualizzazione dello schermo
- verificare salvataggio ed esportazione di script grandi e con molti attributi (modificare le transizioni con l'editor di testo)
- verificare il comportamento quando Loocup non è massimizzato


### Test sulla robustezza

- validare funzioni di salvataggio o esportazione
- verificare il comportamento quando modifico un luogo o transizione con l'editor di testo e compio le seguenti operazioni : 
-- scambio codice a due o più transizioni
-- scambio codice a due o più luoghi
-- scambio codice tra luoghi e transizioni
-- assegno lo stesso codice a più di un elemento
-- mix delle operazioni sopra elencate
- con l'editor di testo provare a spostare blocchi di script o singole righe a caso e poi utilizzare l'editor grafico.
- con l'editor di testo creare transizioni che utilizzino tutti i tag poi verificare : 
-- salvataggio
-- rivisualizzazione
-- esportazione
- provare ad includere più script differenti in un unico script
- provare ad aggiungere attributi non validi
- provare a creare script con sintassi non valide, ad esempio : 
-- 3 " : "  prima di un tag
-- più tag validi sulla stessa riga
-- posizionare "-"
--- all'inizio di una riga di commento a metà e alla fine
--- prima di un tag valido



###  Test sulla formattazione

Dopo ogni salvataggio va verificata la forma in cui lo script è stato scritto su AS400



###  Test sulla visualizzazione

Entrare nell'ambiente D29 e provare a creare un ordine, poi, passo dopo passo, va controllata la visualizzazione dello stato.
Si può anche controllare lo stato degli ordini già creati. Questi sono visibili nell'ambiente SVI, scheda Workflow, Ordini.



## Esito test

### Esito Test di stress
 :  : PAR L(TAB)
- Descrizione|OK|KO|Non eseguito|Note
- posizionare le transizioni con X o Y molto grandi (oltre le dimensioni dello schermo), negative, nulle o a zero.||||
- verificare il comportamento quando ho più transizioni o luoghi sovrapposti, sia in visualizzazione che in modifica grafica||||
- verificare il comportamento di diagrammi complessi in visualizzazione e modifica quando ho : ||||
-- molte transizioni (almeno 50)||||
-- molti luoghi (almeno 50)||||
-- molti collegamenti anche con condizionati (almeno 50)||||
-- posizionare molte transizioni e luoghi allineati sull'asse X e poi allineati sull'asse Y, superando i limiti di visualizzazione dello schermo||||
- verificare salvataggio ed esportazione di script grandi e con molti attributi (modificare le transizioni con l'editor di testo)||||
- verificare il comportamento quando Loocup non è massimizzato||||


### Esito Test sulla robustezza
 :  : PAR L(TAB)
- Descrizione|OK|KO|Non eseguito|Note
- validare funzioni di salvataggio o esportazione||||
- verificare il comportamento quando modifico un luogo o transizione con l'editor di testo e compio le seguenti operazioni : ||||
-- scambio codice a due o più transizioni||||
-- scambio codice a due o più luoghi||||
-- scambio codice tra luoghi e transizion||||i
-- assegno lo stesso codice a più di un elemento||||
-- mix delle operazioni sopra elencate||||
- con l'editor di testo provare a spostare blocchi di script o singole righe a caso e poi utilizzare l'editor grafico.||||
- con l'editor di testo creare transizioni che utilizzino tutti i tag poi verificare : ||||
-- salvataggio||||
-- rivisualizzazione||||
-- esportazione||||
- provare ad includere più script differenti in un unico script||||
- provare ad aggiungere attributi non validi||||
- provare a creare script con sintassi non valide, ad esempio : ||||
-- 3 " : "  prima di un tag||||
-- più tag validi sulla stessa riga||||
-- posizionare "-"||||
--- all'inizio di una riga di commento a metà e alla fine||||
--- prima di un tag valido||||



###  Test sulla formattazione
 :  : PAR L(TAB)
- Descrizione|OK|KO|Non eseguito|Note
- Dopo ogni salvataggio va verificata la forma in cui lo script è stato scritto su AS400||||



###  Test sulla visualizzazione
 :  : PAR L(TAB)
- Descrizione|OK|KO|Non eseguito|Note
- Entrare nell'ambiente D29 e provare a creare un ordine, poi, passo dopo passo, va controllata la visualizzazione dello stato.||||
- Controllare lo stato degli ordini già creati. Questi sono visibili nell'ambiente SVI, scheda Workflow, Ordini.||||

