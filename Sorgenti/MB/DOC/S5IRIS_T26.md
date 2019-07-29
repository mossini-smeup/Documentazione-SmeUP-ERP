
# Costruzione Alternative

La costruzione delle alternative (DSALTE) e della schiera di puntamento (XIPNAL con numero elementi XINRAL) su DSIRIS, presenta varie particolarità.
Se è presente una risorsa forzata (impegno iniziato, forzato o congelato), viene scritta solo l'alternativa con questa risorsa.
Se è assente la risorsa forzata le alternative possono derivare da tutte le risorse specifiche o solo da quelle di filtro, in base a quanto impostato nello script : 
Se non impostato flag nello script o nessuna risorsa specifica in S5IRSE vengono assunte tutte le risorse specifiche.
Se impostato flag nello script e presenti risorse specifiche in S5IRSE vengono assunte solo quelle.
Inoltre la schiera XIPNAL viene, nel caso di risorsa forzata, completata nelle posizioni successive al puntatore XINRAL (obbligatoriamente pari a uno) con le eventuali risorse specifiche su cui si può spostare. Questi campi sono utilizzati nel Gantt di dettaglio, nel popup di spostamento risorsa e nel controllo di ammissibilità spostamento.


Per chiarire il procedimento, segue questo esempio con i quattro casi possibili (con e senza risorsa forzata, ciascuno con e senza risorse in S5IRSE) esaminati nei due casi di assenza e presenza del flag di utilizzo delle risorse specifiche di S5IRSE.

I dati di input sono i seguenti : 
Risorsa principale P01 ha le Risorse secondarie S01 S02 e S03
Impegno 1 ha la Risorsa forzata S01 e le Risorse in S5IRSE assenti
Impegno 2 ha la Risorsa forzata assente e le Risorse in S5IRSE assenti
Impegno 3 ha la Risorsa forzata S01 e le Risorse in S5IRSE - S01 e S03
Impegno 4 ha la Risorsa forzata assente e le Risorse in S5IRSE - S02 e S03

La costruzione di DSALTE e dei campi in DSIRIS (XINRAL - numero alternative e XIPNAL - puntatori alla alternative) viene effettuata nel programma S5SMES_01K

NB :  nel seguito nella schiera XIPNAL la sigla A(XXX) individua il puntatore all'alternativa XXX, la sigla R(YYY) individua il puntatore alla risorsa YYY.

Si assume che non ci siano anomalie (ad esempio risorsa forzata non appartenente alla risorsa principale) :  vengono tutte eliminate con messaggio di segnalazione nel programma S5SMES_01K.

Caso A :  flag posizione 10 bianco (non considerare le risorse in S5IRSE)

Impegno 1 - XINRAL = 1 - XIPNAL = A(S01)
Impegno 2 - XINRAL = 3 - XIPNAL = A(S01) A(S02) A(S03)
Impegno 3 - XINRAL = 1 -XIPNAL = A(S01)
Impegno 4 - XINRAL = 3 - XIPNAL = A(S01) A(S02) A(S03)

Questa situazione non viene integrata con le risorse possibili, in quanto non è previsto il filtro sulle risorse di S5IRSE

Caso B :  flag posizione 10 valorizzato (considerare le risorse in S5IRSE)

Impegno 1 - XINRAL = 1 - XIPNAL = A(S01)
Impegno 2 - XINRAL = 3 - XIPNAL = A(S01) A(S02) A(S03)
Impegno 3 - XINRAL = 1 - XIPNAL = A(S01)
Impegno 4 - XINRAL = 2 - XIPNAL = A(S02) A(S03)

Questa situazione, per gli impegni forzati (ma non iniziati) viene integrata con le risorse possibili, in quanto è previsto il filtro sulle risorse di S5IRSE, e viene eseguita nel programma S5SMES_02K, che registra tutte le risorse se non sono presenti filtri di risorse su S5IRSE.

Impegno 1 - XINRAL = 1 - XIPNAL = A(S01) R(S01) R(S02) R(S03)
Impegno 3 - XINRAL = 1 - XIPNAL = A(S01) R(S01) R(S03)


Nel programma di gestione dettaglio (S5SMES_D4), si passa al componente Gantt, come filtro generale, la schiera delle risorse specifiche di ogni gruppo.
Si passa inoltre, come filtro specifico, la schiera delle risorse specifiche ammesse.
Se ci sono valori non a zero in XIPNAL oltre XINRAL questa parte è direttamente il filtro risorse specifiche.
In caso contrario, se XINRAL è minore del numero di risorse del gruppo, vuol dire che XIPNAL è un filtro, e quindi si carica il filtro delle risorse scorrendo DSALTE.
Se infine XINRAL è uguale al numero delle risorse del gruppo, non si passa nessun filtro specifico, dato che esso coincide con il filtro generale :  vuol dire che :  o non è attivo il filtro sulle risorse di S5IRSE, oppure sono state inserite, in S5IRSE, tutte le risorse specifiche.
Si passa inoltre l'informazione di ammissibilità degli spostamenti, in base a quanto impostato in posizione 31 della stringa dei parametri di impostazione.



# Costruzione dei dettagli a partire dalle alternative.

Questa funzione viene eseguita nel programma S5SMES_05 che crea anche la DSGRUP.
In particolare, vengono valorizzati i flag di DSDEGR in questo modo : 

Ricordo che il flag di DSALTE XATFAS (Tipo fase) è attualmente lasciato in bianco (riservato per le alternative di fase).

Il flag di DSDEGR XGTFAS, normalmente lasciato bianco (in quanto copiato da XATFAS), assume il valore 'O' (obbligatorio) nel caso di impegno iniziato, forzato o congelato (quando la risorsa forzata è valorizzata). Questa informazione è comunque ridondante, in quanto in questi casi c'è una sola alternativa, e quindi un solo dettaglio.

Nella selezione del miglior dettaglio (S5SMES_11E) vengono esclusi i dettagli con questo campo valorizzato ad 'E' (esclusi), anche se attualmente questo valore non è assegnato dal sistema, in quanto non vengono scritti i dettagli esclusi se ce n'è uno obbligatorio, ma è modificabile da exit, per ridurre l'insieme delle risorse di un impegno in competizione. Può essere attivato nell'exit S5SMX_01x, di completamento schedulazione, in cui si rende pronto l'impegno successivo a quello di cui si sta schedulando il dettaglio (si scorrono i dettagli di questo impegno, e si aggiornano con questo flag quelli che si intendono escludere). Un motivo di tale esclusione (eseguita in corso d'opera) presumibilmente dipende dalla risorsa del dettaglio appena schedulato (per permettere solo dettagli successivi limitrofi). Questa esclusione è, diversamente dalla sospensione, definitiva, in quanto una volta escluso un dettaglio esso non viene più riattivato (lo si potrebbe fare con arzigogoli informatici ma non risulta chiaro il motivo) mentre la sospensione di un impegno deve obbligatoriamente essere temporanea (pena l'incompletezza della schedulazione)

Riassumendo : 
un impegno si sospende (dinamicamente ad ogni loop)
un dettaglio si esclude (staticamente una volta per tutte)





