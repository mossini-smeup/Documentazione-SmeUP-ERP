# Analisi per BCD di sola interrogazione

## Tabella B§G
In tabella B§G si aggiunge un campo di 2 caratteri (tabellarlo in una *CN/xx?). Definisce il campo di analisi :  ad esempio due Fine.UP diverse ciascuna con più B§G, ad esempio con PAR_SCP diversi.

## Archivio
Nuovo archivio :  B£BCDM0F

Ambiente  2 (non servirebbe perché derivabile dalla B§G ma utile per ricerche
B§G   3
N.ro Sessione   15.0 (generale, da un numeratore)
Tipo record  10
N.ro progressivo 10.0 (all'interno di un tipo record)
Memorizzazione 5000 (varchar)

Logico 1
Ambiente/B§G/N.ro Sessione/Tipo Record/N.ro progressivo


## Lanciatore
Richiesta dati :  occorre un nuovo lanciatore B£BCD08.

Il lanciatore può ricevere o meno un parametro.
Se lo riceve è del tipo : 
"AMB_XX" dove XX è l'ambiente
"TAB_YYY" dove YYY è l'elemento di B§G. In questo caso è come se ricevesse anche l'ambiente, in quanto lo legge dalla tabella.

Il tipo record individua cosa c'è memorizzato nel campo lungo
Ha questi valori

### Generali

ED Elemento di distinzione del gruppo :  vedremo dopo a cosa serve

£BCDW1
£BCDW2
£BCDS1
£BCDS2
£BCDD1
£BCDD2

NB :  B§G è contenuta in £BCDD1

 :  : T04 Specifici Fine.UP
S5X Contenuto di S5X (parametri di lancio)
S5B Contenuto tabella S5B
DSIRIS
DSDEGR
ecc...

Supponiamo di avere questa memorizzazione (riportiamo solo il record ED)

Amb. B§G N.Sessione Record di ED :  formattato?
A1 XX1 1  zzzzzzzzzzzzzzzzzzzzzzzz
A1 XX1 3  aaaaaaaaaaaaaaaa
A1 XX2 4  llllllllllllllll
A2 YY1 2  eeeeeeeeeeeeee
A2 YY1 5  wwwwwwwwwwwwwwww
A3 ZZ1 6  ppppppp

Il programma di innesco deve scegliere una sessione.

Se non riceve niente presenta una matrice come la precedente da cui scegliere una riga

Se riceve AMB_A1 presenta
B§G N.Sessione Record di ED :  formattato?
XX1 1  zzzzzzzzzzzzzzzzzzzzzzzz
XX2 3  aaaaaaaaaaaaaaaa
XX3 4  llllllllllllllll

Se riceve uno di questi valori : 
AMB_A3, TAB_XX2, TAB_ZZ1 fa vedere solo una riga e poi fa proseguire in quanto la sessione è univoca (potrebbe essere anche cieco?).

Se riceve TAB_XX1 presenta
N.Sessione Record di ED :  formattato?
1  zzzzzzzzzzzzzzzzzzzzzzzz
3  aaaaaaaaaaaaaaaa

Da qui si sceglie la sessione come nel modo precedente.


Riferirsi all'altro documento per vedere le modalità del richiamo.


## Script INT
Lo script INT va modificato in questo senso
All'inizio, prima di ogni altra istruzione (compresa la pulizia delle variabili) si testa se il flag è a '1'
Se è così si esegue il programma di caricamento delle memorie della sessione ricevuta nel file, si lancia S5SMES_D3 e si va a fine.
Questo programma va modificato nel senso di impedire le azioni (rischedulazione, salvataggio).
Inoltre, nella finestrina a destra dove si vedono le azioni fatte, metterei la visualizzazione di S5X, vale a dire i campi di lancio.
Capire poi come questo pgm va a fine :  ritorna all'inizio, esce del tutto, distinguere il caso di una sola memorizzazione selezionabile (e quindi finisce e basta) o più memorizzazioni, nel qual caso ritorna all'inizio per poter sceglierne un'altra.
Si dovrà poi modificare S5SMES_D4 per far sì che in interrogazione (il flag gli è disponibile) non possa andare in modifica, e poi in qualche modo segnare lo stato di avanzamento attuale :  agganciando S5IRIS che potrebbe non esserci più.

Alla fine della BCD, dopo aver aggiornato S5IRIS, scrivere su disco le memorie. Per provare potrebbe essere inizialmente la exit finale del S5SMES_25.

Questo programma può avere o meno riempito il campo n.ro sessione.
Se non ce l'ha, bisogna capire se deve andare in sostituzione di una situazione già memorizzata.
Forse si potrebbe procedere così.
Si riserva un tipo record all'elemento di distinzione del gruppo che, senza exit, è uguale a S5X, ma lo si può cambiare (con exit). Si vede se ce n'è già uno uguale :  se sì acquisisce il numero di sessione e la si pulisce, altrimenti ricava una nuova sessione con la £CRN e lo mette nel primo numero della nuova schiera (NB :  verrà anch'esso memorizzato, ma quando la BCD di interrogazione lo legge, subito dopo gli sovrappone quello appena acquisito nell'innesco).  Tra i record che scrive c'è l'elemento di distinzione. Ad esempio, se non si vuol controllare la data massima, nel record ED la si pulisce con la exit, mentre resta in quello S1 (in pratica resta sempre l'ultimo). Oppure se varia l'ora di lancio e non interessa, si fa la stessa cosa.
Se c'è il numero vuoi dire che, nella sessione, si è già fatto un salvataggio. In questo caso cancella tutti i record della sessione e li riscrive (alcuni potrebbero essere buoni, ma per sicurezza è meglio pulire tutto).

L'idea è che per una sessione si memorizza, al massimo, l'ultima situazione salvata. È una condizione troppo restrittiva?

# Problemi
I programmi mongolfiera, che hanno memorie private (ad esempio i materiali, i batch, le multipostazioni e le risorse secondarie), devono avere due funzioni in più :  memorizzazione e ripresa.
La memorizzazione è richiamata dopo la memorizzazione normale (S5SMES_25) la ripresa nel nuovo programma di costruzione memorie.
Aggiungerei una exit a entrambi i programmi, con funzioni MEM e RIP, che a sua volta chiama le mongolfiere personali con la stessa funzione, per fare la stessa cosa delle mongolfiere standard. Questo è da fare naturalmente se interessa riportare a video informazioni contenute nelle memorie delle mongolfiere.

Per colloquiare con l'archivio di memorizzazione vedere le procedure di cui ho abbozzato i prototipi e l'utilizzo in SRC_INT di P_BCD.
Sono due copy :  una di lettura e una di scrittura.
Sarebbe da aggiungere una /Copy del File (farlo sempre in aggiornamento così va bene per entrambe :  infatti nelle mongolfiere si deve scrivere e leggere nello stesso programma).

Ho fatto una prova :  il pgm OCC_01 in W_GALGUI e va benissimo :  si copia da/a un elemento di OCCUR in un campo lungo uguale (non fa una piega anche con i packed). Quindi, ad esempio, se si sta salvando DSIRIS, si copia l'occorrenza X in un campo molto più lungo (così vale per tutte le DS :  vedere quello che ha fatto Arrighini nelle exit dell'analisi disponibilità per controllare la lunghezza massima), e lo si passa alla routine.




