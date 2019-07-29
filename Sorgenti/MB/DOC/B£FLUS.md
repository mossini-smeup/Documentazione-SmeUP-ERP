# Generalità
Uno dei problemi nelle installazioni di sistemi gestionali è la necessità da parte del cliente di dover supportare procedure complesse, molto spesso specifiche dell'ambiente del cliente o del settore produttivo.
In Sme.up la risposta risiede nella scomposizione delle proceure complesse in sequenze di funzionielementari, dette "azioni" e nella possibilità di lanciare flussi in cui eseguire le azioni in sequenza. Le azioni vengono ricombinate nelle sequenze volute, in modo da costituire le procedure complesse richieste dal cliente.
Un'azione è un programma normalizzato (dove la struttura dell'input e dell'output è definita secondo lo standard Sme.up, in modo da poter essere inserita nel flusso di azioni).
Dall'impostazione della sequenza e dalla definizione dei parametri di esecuzione associati all'azione si ottengono le procedure complesse richieste dal cliente.

# Tipi di flusso
Tutti i flussi di azioni sono definiti nella tabella B£H.
Esistono 5 tipi di flusso : 


- flussi batch, che prevedono la possibilità di lanciare in sequenza più azioni elementari. In questo tipo di flussi le azioni non richiedono parametri passati esternamente (possono essere solo usati parametri interni definiti nell'azione, cioè in tabella B£J), come tutte le azioni richiamate negli altri tipi di flusso.
Il programma che lancia questi tipi di flusso è il >B£GFP10.

- fllussi avanzati, che permettono l'esecuzione in sequenza di un gruppo di azioni definite nella tabella B£H. L'esecuzione interattiva e ogni azione vengono proposte al termine della precedente e, all'interno della sequenza, le azioni possono essere obbligatorie (se non eseguita, viene chiesta esplicitamente la rinuncia), ripetibili (al termine del flusso viene proposta una finestra per la scelta delle azioni ripetibili), non obbligatorie (al termine del flusso, nella finestra per la scelta delle azioni ripetibili, sono proposte anche le azioni facoltative).
Un esempio di questi tipi di flusso sono i flussi di ricevimento merci a fronte di ordini acquisto, dove ci sono azioni per la selezione del fornitore e l'impostazione della testata della BEM, azioni successive di selezione delle righe di BEM (dagli ordini acquisto aperti), azioni per la revisione della BEM, azioni per ulteriori selezioni di righe, azioni per il confezionamento, azioni per il collegamento del documento, ecc....
Il programma che lancia questi tipi di flusso per i documenti è il >V5AT10A, che si appoggia sulla tabella V5G per determinare i gruppi di attività (e i conseguenti flussi B£H) da lanciare.

- flussi di collegamento (nello standard Sme.up una delle caratteristiche dell'oggetto è quella di avere la possibilità di lanciare automaticamente flussi di azioni nelle varie fasi della sua vita :  inserimento, copia, modifica, cancellazione, ecc...)
Un esempio di azioni richiamabili in questi tipi di flusso può essere l'apertura automatica della gestione parametri, oppure l'invio di una e-mail alla Logistica durante l'inserimento di un articolo da parte dell'Uff. Tecnico.

- flussi di scelta, che prevedono la possibilità di definire una serie di azioni selezionabili manualmente e inizializzabili singolarmente, attraverso l'attivazione delle funzioni di un oggetto (>F10 oppure >UP FUN).
Un esempio di azioni richiamabili può essere l'apertura della gestione parametri oppure l'interrogazione della distinta base di un articolo.

- flussi di esecuzione, che permettono l'esecuzione di una specifica azione per un determinato oggetto (caratterizzato da tipo e parametro), selezionabile tra quelle previste nell'elemento di tabella B£H costruito in modo >"E-OOPPP", dove >OO è il tipo oggetto e >PPP è il parametro associato. L'azione lanciata si applica al solo oggetto in input.
Il programma che lancia questi tipi di flusso è il >B£AR30.
Un esempio di azioni richiamabili in questi tipi di flusso è l'assegnazione (prenotazione di una giacenza disponibile) delle righe delle richieste di movimentazione appartenenti alla testata in input.


## Flussi associati ad un oggetto
Ad un oggetto possono essere associati flussi di collegamento, lanciati automaticamente nelle varie fasi della vita dell'oggetto : 

- inserimento (flussi I-);
- copia (flussi C-);
- modifica (pre modifica flussi :  F-, post modifica flussi :  M-);
- cancellazione (pre eliminazione flussi :  P-, post eliminazione flussi :  D-);


Ciascuno di questi flussi è identificato da un elemento della tabella B£H avente come lettera iniziale la caratteristica dell'evento scatenante (I = immissione, C= copia, ...) seguita dal trattino ("-") e dall'oggetto a cui si applica (AR articoli, DR righe documenti, OR, ordini di produzione, ....).
Oltre ai flussi precedenti, all'oggetto è anche associato il flusso di scelta (flusso A-), che permette di definire un gruppo di azioni, eseguibili manualmente tramite la gestione delle funzioni per oggetto (F10).

NB. : 
Un metodo comodo per visualizzare i flussi attivi per un determinato oggetto, in gestione dell'oggetto, è di aprire le funzioni per oggetto (F10) e selezionare le funzioni generali per oggetto (Opzione 3), in seguito a cui una videata mostrerà i flussi di azione presenti e quelli mancanti.

![B£FLUS_01](http://localhost:3000/immagini/B£FLUS/BXFLUS_01.png)
selezionando il flusso voluto, con un carattere qualsiasi, si aprirà una seconda finestra con l'elenco delle azioni previste : 

![B£FLUS_02](http://localhost:3000/immagini/B£FLUS/BXFLUS_02.png)
# Azioni
L'azione è un'operazione elementare all'interno di un flusso di azioni, eseguita da un programma specifico, che viene costruito basandosi su una definizione standard della struttura di input e di output.
Tutte le azioni sono descritte negli elementi interni ai vari sottosettori della tabella B£J. Ogni flusso (B£H) punta ad un sottosettore specifico.

## Azioni associate ad un flusso
Compilando opportunamente la tabella B£H, si definisce il sottosettore della tabella B£J da cui selezionare le azioni da associare al flusso e la regola di selezione da adottare : 
Esempio : 

![B£FLUS_03](http://localhost:3000/immagini/B£FLUS/BXFLUS_03.png)
In questo esempio le azioni richiamate sono quelle che iniziano per I0 e sono presenti nella tabella B£J sottosettore AR.

## Azioni disponibili
Ogni azione è un programma che esegue una attività elementare e che può essere sviluppato sul momento, sulla base delle richieste utente, oppure  scelto all'interno della libreria delle azioni elementari, messe a disposizione nello standard Sme.up.
Per verificare quali siano le azioni standard disponibili esistono 2 metodi : 

- dalla tabella B£J, nel campo "Nome Programma", inserire un carattere di ricerca (! o ?), selezionare l'applicazione e proseguire, agendo sulle varie selezioni richieste;
- lanciare l'utility "UP AZI", inserire il codice applicazione, selezionare il contesto e proseguire nelle selezioni, come nel caso precedente.


_2_Azioni Disponibili - Esempio 1

>Ricerca da tabella B£J : 
![B£FLUS_04](http://localhost:3000/immagini/B£FLUS/BXFLUS_04.png)selezionare l'applicazione, es. BR : 
![B£FLUS_05](http://localhost:3000/immagini/B£FLUS/BXFLUS_05.png)
_2_Azioni Disponibili - Esempio 2

>Ricerca via UP AZI : 
![B£FLUS_06](http://localhost:3000/immagini/B£FLUS/BXFLUS_06.png)