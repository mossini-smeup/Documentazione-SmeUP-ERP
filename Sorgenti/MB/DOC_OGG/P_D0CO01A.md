# Calcolo costo interattivo di un oggetto
Dato un oggetto il programma ne calcola il costo, presenta in una lista il risultato e, se opportunamente impostato, può memorizzare il costo calcolato.

## Formato di input
![D0BASE_51](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01A/D0BASE_51.png)Sono possibili le seguenti impostazioni : 
 * **Contesto**; è il tipo di oggetto di cui si vuole calcolare il costo, al momento sono previsti AR, DR, OP, CM
 * **Tipo costo**; è il tipo costo che sarà memorizzato
 * **Data**; è la data a fronte della quale sarà eseguita la memorizzazione, la stessa data viene utilizzata nelle eventuali scansioni distinta e ciclo
 * **Oggetto**; dipende dal contesto, è l'istanza di cui eseguire il calcolo costo, la descrizione del campo varia dinamicamente in funzione del contesto scelto
 * **Tipo costo**; hhhh
 * **Quantità calcolo**; se impostata una quantità i vari elementi di costo vengono calcolati anche per la qtà indicata
 * **Quantità lotto**; hhhhhhhh
 * **Politiche %**; se il contesto è articolo è possibile indicare una distribuzione di poltiche anche mista, in assenza si utilizzano le politiche di pianificazione
 * **Esplosione distinta**; se il contesto è un articolo è possibile eseguire il ricalcolo dei costi dei componenti di distita, oppure per i componenti, se ci sono si possono usare i costi letti senza ricalcolo, se si è chiesto il ricalcolo costo dei componenti è possibile scegliere di memorizzarlo. Valori previsti :  Blank = non ricalcolare i costi dei componenti di distinta, 1 = ricalcolare senza memorizzare, 2= ricalcolare e memorizzare i costi
 * **Tipo di calcolo**; Blank = Tutti (vengono ricalcolati tutti i costi), M = solo mancanti (si ricalcolano solo i costi mancanti), P = solo presenti (si ricalcolano solo i costi presenti)
 * **Impostazioni**; contiene le impostazioni del calcolo (vedi paragrafo successivo). **Nota**, se questo campo non è blank, con il bottone laterale è possibile interrogare le impostazioni presenti nell'apposito formato, se invece questo campo è blank, si può accedere con possibilità di modifica alle impostazioni del calcolo

Sul piede del formato ci sono dei comandi funzione con il significato seguente : 
 * **F06 = Conferma**, lancia l'elaborazione
 * **F07 = Dati programmazione**, attiva/disattiva la visione dei dati tecnici
 * **F14 = Autorizzazioni**, apre la gestione autorizzazioni per la classe = ABILITA e la funzione = D0CO01A che regolano la possibilità per l'utente di utilizzare il programma
 * **F15 = Memorizza Impostazioni**, permette di salvare le impostazioni eseguite nell'apposito formato con il nome indicato in questo campo.

# Impostazioni di calcolo costo
## Formato impostazioni del calcolo
![D0BASE_52](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01I/D0BASE_52.png) * **Estrazione oggetti**
 ** __Programma__; per il contesto articolo è possibile far eseguire il ricalcolo del low level code, indicando il tipo esplosione distinta da utilizzare nel ricalcolo. Se attivata questa modalità il ricalcolo sarà eseguito prima della elaborazione vera e propria del calcolo costi
 ** __Exit__; permette di indicare un suffisso del programma XXXXXXX_x come exit nell'estrazione oggetti
 * **Calcolo costo**
 ** __Programma__; qui si sceglie il programma da utilizzare per l'elaborazione e le relative impostazioni di elaborazione (vedi formato impostazioni calcolo costo successivo)
 ** __Exit__; permette di indicare un suffisso del programma XXXXXXX_x come exit nel calcolo costo
 * **Completamento costi**
 ** __Struttura__; qui si sceglie il programma da utilizzare per il completamento dei costi di struttura e le relative impostazioni di elaborazione (vedi formato impostazioni completamento costi struttura successivo)
 ** __Ricariche__; qui si sceglie il programma da utilizzare per il completamento dei costi ricariche e le relative impostazioni di elaborazione (vedi formato impostazioni completamento costi ricariche successivo)
 * **Documentazione errori**
 ** __Exit__; permette di indicare un suffisso del programma XXXXXXX_x come exit nella documentazione errori
 * **Memorizzazioni**
 ** __Costi__; questa impostazione è relativa alle modalità di memorizzazione del costo oggetto, valori possibili : 
 *** >Blank, nessuna memorizzazione
 *** >N, nessuna memorizzazione e cancellazione dei costi attualmente presenti
 *** >C, memorizzazione solo se non ci sono errori
 *** >V, memorizzazione solo se ci sono valori
 *** >T, memorizzazione di tutti i codici (inidpendente da errori e anche per valori = 0)
 ** __Documentazione__; questa impostazione è relativa alle modalità di memorizzazione della documentazione del calcolo costo, valori possibili : 
 *** >Blank, nessuna memorizzazione
 *** >1, viene memorizzata la documentazione del calcolo costo al primo livello
 *** >2, viene memorizzata per data la documentazione del calcolo costo a tutti i livelli
 * **Flussi**
 ** __Pre / Post__; si possono indicare elementi della tabella B£H che descrivono flussi di elaborazione da eseguire prima o dopo del calcolo

### Formato impostazioni di calcolo costo
![D0BASE_53](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01I/D0BASE_53.png) * **Costo aliquote**; indicare il tipo costo da utilizzare per le aliquote orarie
 * **Costo lavorazione esterna pieno**; indicare il tipo costo da utilizzare per le lavorazioni esterne in caso di conto lavoro pieno
 * **Costo lavorazione esterna fase**; indicare il tipo costo da utilizzare per le lavorazioni esterne in caso di conto lavoro di fase
 * **Costo materiale acquisto**; indicare il tipo costo da utilizzare per i componenti che sono di acquisto
 * **Costo componente produzione**; indicare il tipo costo da utilizzare per i componenti che sono di produzione
 * **Politiche costi**; indicare l'elemento della tabella C£V dove trovare le politiche (produzione, acquisto, lavorazione) da utilizzare nel calcolo costo
 * **Metodo lettura aliquote**; blank = solo dal centro di costo, 1 = dalla risorsa presente nel ciclo (es. aliquote da centro di lavoro), 2 = dalla risorsa del ciclo con risalita al centro di costo
 * **Costo Fase per Operazione**; SI/NO hhhhh
 * **Configurazione di calcolo**; se indicata si utilizza la configurazione per le esplosioni distinta e ciclo
 * **Scrittura costo a totalizzaizone £Q**; SI/NO hhhhh
 * **Costo operazione esterna ciclo 09**; indicare con quale modalità reperire il costo delle operazioni esterne, valori possibili :  blank =  costo recuperato solo dal tipo costo, 1 = costo recuperato dal tipo costo con risalita al costo del ciclo (valore inserito nel campo 09 del ciclo  - R§TE09 di BRRICI0F), 2 = costo recuperato dal ciclo con risalita al costo del tipo costo
 * **Aliquota alla data ciclo**; SI/NO hhhhh
 * **Ciclo master**
 ** __Tipo ciclo__; hhhhh
 * **Risalita a ciclo in TCO**; SI/NO hhhhh
 * **Distinta master**
 ** __Tipo distinta__; hhhhh
 * **Risalita a distinta in TCO**; SI/NO hhhhh
 * **Tipo costo del componente**; hhhhh

### Formato impostazioni di completamento costi struttura
![D0BASE_54](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01I/D0BASE_54.png) * **Nuova gestione livello inferiore IGI**;  SI/NO hhhhh
 * **Suffisso programma per exit di calcolo costi indiretti**; hhhhh
 * **Attivazione exit di calcolo**
 ** __Materiale acquisto__;  SI/NO hhhhh
 ** __Lavorazione esterna__;  SI/NO hhhhh
 ** __Lavorazione interna__;  SI/NO hhhhh
 ** __Ricarica materiale acquisto__;  SI/NO hhhhh
 ** __Ricarica lavorazione esterna__;  SI/NO hhhhh
 ** __Ricarica oggetto__;  SI/NO hhhhh

### Formato impostazioni di completamento costi ricariche
![D0BASE_55](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01I/D0BASE_55.png) * **Sottosettore ricariche**;  hhhhh
 * **Sottosettore metodo attribuzione %**;  hhhhh
