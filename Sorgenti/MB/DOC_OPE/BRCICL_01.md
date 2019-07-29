# Introduzione

L'obiettivo delle nuove navigazioni è quello di rendere la consultazione dei cicli di lavoro __agevole__ dal punto di vista della raggiungibilità, e __semplice__ dal punto di vista della comprensione.
Dal punto di vista della raggiungibilità, queste schede possono essere richiamate direttamente dal modulo BRCICL, mentre dal punto di vista della comprensione queste sono semplici perchè ripropongo l'ormai nota struttura a tre sezioni.
Ciascuna sezione ha una funzione ben precisa : 
**1.** la prima verticale a sinistra, dedicata al menù :  questa riporta tutte le azioni e navigazioni più importanti relative ai cicli di lavoro
**2.** la seconda orizzontale, nella parte alta, dedicata ai filtri e alla loro impostazione
**3.** la terza, che occupa tutta la restante parte, destinata a contenere il risultato della ricerca.


![BRCICL_001](http://localhost:3000/immagini/MBDOC_OPE-BRCICL_01/BRCICL_001.png)

Come già accade per molti altri oggetti di Sme.UP, anche i cicli sono organizzati per tipologia.
La consultazione dei dati avviene per tipologie omogenee e questo significa che, come prima cosa, occorre scegliere quale tipo ciclo si intende consultare. Questa scelta può essere sempre modificata grazie alla voce "Cambio ciclo" prensente nell'Hypermenù del modulo.

![BRCICL_003](http://localhost:3000/immagini/MBDOC_OPE-BRCICL_01/BRCICL_003.png)

# Il dashboard del modulo

La prima voce di menù ci permette di accedere al cruscotto del modulo, ovvero una scheda puramente statistica che permette di visionare quanti cicli  di un certo tipo sono presenti nel sistema.
Oltre a questa informazione, si può visionare anche lo stato di utilizzo e le impostazioni di tutte le altre tipologie di ciclo attraverso la scheda "situazione generale cicli".

![BRCICL_004](http://localhost:3000/immagini/MBDOC_OPE-BRCICL_01/BRCICL_004.png)
# Le navigazioni :  il SURF dei cicli

A differenza di molti altri moduli in cui ha senso avere la possibilità di consultare i dati da punti di vista diversi, per quanto riguarda i cicli, esiste una sola forma di interrogazione.
Questa interrogazione può essere raggiunta o direttamente dall'Hypermenù del modulo BRCICL o, dove presente, dal FLY "Brec.UP Basic Records - Interrogazione cicli".
All'apertura, la scheda si presenta strutturata, come già ricordato sopra, con le tre sezioni.
La prima cosa da fare è impostare le modalità di esplorazione specifiche che per i cicli possono essere : 

![BRCICL_002](http://localhost:3000/immagini/MBDOC_OPE-BRCICL_01/BRCICL_002.png)
L'esplorazione dei cicli può essere fatta in 3 modalità differenti a seconda di quello che si vuole ottenere. Per comprendere meglio le logiche di esplorazione, ricordiamo che un ciclo è l'elenco di tutte le operazioni che devono essere compiute da un esecutore (sia esso una macchina, un uomo, o una qualsiasi altra risorsa) per ottenere un dato prodotto. Se si pensa a questa definizione allora si ha che : 
1. L'IMPLOSIONE permette di visualizzare tutte le operazioni che possono essere eseguite da una specifica risorsa, indipendentemente dal ciclo specifico di cui fanno parte.
2. L'ESPLOSIONE permette invece di visualizzare, dato un oggetto, quali sono le sole operazioni necessarie alla sua realizzazione.
3. Esplorazione SCHEDULATA (al più presto o al più tardi) che permette di vedere, su una risorsa, quali sono le operazioni che deve svolgere in sequenza a capacità infinita.
Per maggiori informazioni sulla schedulazione a capacità infinita si rimanda alla documentazione specifica : 
- [Schedulazione a Capacità Infinita](Sorgenti/MB/DOC/S5_001)

Guardiamo ora nel dettaglio le diverse tipologie di esplorazione dei cicli : 
** __11= Esplosione tecnica__  :  è l'esplorazione che permette di visualizzare tutte le fasi del ciclo di lavoro che servono per realizzare un singolo prodotto. Questa esplosione non è sensibile alla data di validità delle fasi e permette di consultare il ciclo così come definito a livello teorico.
** __12= Esplosione di produzione__ : è l'esplorazione che permette di visualizzare tutte le fasi del ciclo di lavoro che servono per realizzare un singolo prodotto. Questa è sensibile alla data di validità delle fasi :  verranno visualizzate solo le fasi che sono valide rispetto alla data impostata nel filtro. Se omessa, come data limite verrà assunta la data del giorno.
** __21= Implosione tecnica__ :  è l'esplorazione che permette di visualizzare tutte le fasi dei cicli tecnici che possono essere svolte da una precisa risorsa. Come il metodo 11, anche in questo caso la data di validità non viene presa in considerazione.
** __22= Implosione di produzione__ : è l'esplorazione che permette di visualizzare tutte le fasi dei cicli tecnici che possono essere svolte da una precisa risorsa e che sono compatibili con la data di validità impostatata nel filtro. Se omessa, viene assunta come data di validità limite quella del giorno.
** __31= Schedulata al più presto__ :  permette di visualizzare le fasi di un ciclo in modo che queste vengano svolte il prima possibile (schedulate cioè al più presto) sulle macchine.
** __32= Schedulata al più tardi__ :  permette di visualizzare le fasi di un ciclo pianificate al più tardi sulle varie risorse.
Nelle esplorazioni con schedulazione, è possibile visualizzare anche il gant che mostra, per ciascuna fase, l'occupazione in termini di tempo della risorsa abbinata a ogni singola fase. Tale occupazione dipende in modo proporzionale dalla quantità di prodotto da realizzare e dalla durata della singola operazione.

A seconda di quello che si sceglie come modalità di esplorazione, sia essa implosione o esplosione, si avrà la possibilità di impostare alcuni filtri piuttosto che altri.
**1.**Con una scansione __tecnica** possiamo impostare le informazioni di base legate ai cicli.
In questo caso i filtri su cui è possibile agire sono : 
** Ciclo :  è un campo di fondamentale importanza per quei cicli per i quali è stato impostato il prefisso e la gestione tramite testata;
** Quantità :  funge da moltiplicatore e serve per vedere i tempi del ciclo moltiplicati per la quantità qui inserita.
** Stato legami :  per filtrare le fasi che sono in uno stato particolare.
** Ums :  per convertire i valori da una unità di misura a un'altra.
** CCar :  codice di carico, usato nella determinazione dei tempi e dei costi.
** Schema :  per cambiare le colonne delle informazioni che vengono caricate nella sezione centrale della scheda.
**2.** Con una scansione __di produzione** possiamo eventualmente scegliere di vedere anche altri campi oltre a quelli appena citati.
Esempi di questi filtri aggiuntivi sono : 
**Logistica :  è un flag che permette di visualizzare per ogni fase, tutti i materiali a essa abbinati.
**Esponente di modifica e Configurazione :  sono informazioni legate all'articolo.

Ciascuno di questi filtri è dotato di una documentazione che ne spiega il significato, l'utilità e lo scopo. A questa si può accedere premendo il tasto funzionale F1 con il cursore del mouse posizionato sul filtro specifico : 

![BRCICL_005](http://localhost:3000/immagini/MBDOC_OPE-BRCICL_01/BRCICL_005.png)

