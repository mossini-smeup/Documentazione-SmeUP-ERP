# Gestione delle figure di documentazione

## Cos'è una figura
Una figura di documentazione è un oggetto V3 F.**MODULO** dove **MODULO** è un oggetto di tipo TAB£AMO.
Essa è costituita da un file immagine di tipo PNG che è stato associato alla documentazione di un modulo.
Per "battezzare" un file immagine come figura di documentazione vanno quindi identificate le due dimensioni : 

- un file PNG
- un modulo alla cui documentazione assegnare la figura


## I file PNG
Il tipo PNG è il tipo di file immagine "ufficiale" per Looc.UP.
A tali file PNG ci si deve ricondurre per entrare nella procedura di assegnazione alla documentazione di un modulo.

## La documentazione di un modulo
Ogni modulo può possedere, dei file di documentazione. All'interno di questi file di documentazione, tramite la specifica  :  : FIG, si può fare riferimento alle figure della documentazione.
Tale figure devono essere elencate nel membro **MODULO**_FIG per poter essere ricercate come oggetti V3 F.**MODULO**.
Tale membro "di indice" delle figure della documentazione del modulo vengono gestiti tramite la scheda B£DOCU_FI.

## Come trasformo un file immagine in figura
### Ricondursi ad un file PNG
All'interno di Looc.UP esistono differenti strade per giungere ad un file PNG : 

- Selezionare specificatamente un file PNG prodotto esternamente
-- Attraverso il modulo di ricerca degli oggetti è possibile selezionare un file PNG come oggetto J1 PATHFILE, una volta selezionato si apre la scheda e da lì si accede alla funzione di "trasformazione" in figura della documentazione di un modulo
- Copiare un immagine nella clipboard di sistema
-- Da Loocup, è possibile generare lo screenshot della finestra che si ha di fronte o di alcune partei di essa
- Generare uno screenshot da Looc.UP di : 
-- Ogni scheda ha nel suo menù di finestra la voce Strumenti --> Screenshot della scheda che genera un file PNG immagine della scheda e ne apre la scheda di gestione
-- Ogni sezione di scheda ha nel suo popup la voce Screenshot della Sezione che genera un file PNG immagine della sezione e ne apre la scheda di gestione
-- Alcuni moduli prevedono di generare il proprio screenshot e mettono a disposizone la funzione per farlo tramite bottone nella bottoniera

