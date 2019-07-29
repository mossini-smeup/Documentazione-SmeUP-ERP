# Comportamento dello standard

La funzionalità delle combo, in smeup è fissata per classe, attraverso la /COPY £K04. Tendenzialmente si è seguito questo criterio : 
* Per gli oggetti dei moduli anagrafici (BR, come articoli, contatti, commesse) è stata predisposta la combo tramite ricerca, essendo le istanze di questi oggetti molto numerose
* Per le tabelle o gli oggetti fissi (es. V2) è stata predisposta la combo con elenco completo.

Per l'operatività delle combo standard si rimanda al documento specifico.

- [La Funzione di Ricerca Tramite Combo-Box](Sorgenti/MB/DOC/B£EQRYA02B)

Si ricorda inoltre qui che attraverso le funzioni di analisi degli accessi del modulo B£EQRY, è possibile verificare l'elenco completo, mentre dalla singola classe (oggetto OG) controllando lo specifico attributo è possibile verificare la funzionalità della singola classe.

# Modificare il Comportamento dello standard

Il comportamento standard può però essere, forzato su altre classi o al contrario disattivato per le classi previste dallo standard, sia genericamente che localmente.

Genericamente, attraverso l'exit della /COPY £K04 è possibile modificare il comportamento previsto dallo standard per ogni classe. Tale exit ha nome fisso B£K04G_U e viene automaticamente attivata nel momento in cui viene compilato l'oggetto.

 :  : DEC T(MB) P(QILEGEN) K(£K04) L(1)
 :  : DEC T(MB) P(SMESRC) K(B£K04G_U) L(1)

Localmente, nel singolo servizio d'aggiornamento, è possibile : 
* Disattivare la combo su una classe prevista dallo standard, indicando nella griglia della matrice, l'attributo di input/output "b"
* Attivare la combo su una classe non prevista dallo standard indicando nella griglia della matrice, l'attributo di input/output "C" per attivare l'icona di combo su elenco completo o l'attributo di input/output "E" per attivare l'icona di combo per ricerca.
* Sia che la funzione di combo sia fissata dallo standard che sia stata forzata localmente è inoltre possibile forzare una funzione di risoluzione della combo differente rispetto a quella prevista dallo standard (si veda il documento operativo specifico relativo alle combo). Per fare questo vanno compilata la schiera £JayComLst secondo la struttura prevista dalla ds £JayDSCom. In tali schiere per campo potranno essere indicati o l'elenco preciso dei valori possibili o la funzione da eseguire per lo svolgimento della stessa. Va sottolineato che nel caso si voglia indicare una funzione, in tale funzione possono essere impiegate le seguenti variabili di loocup : 
** T1, P1, K1 :  che conterranno rispettivamente, il tipo oggetto, il parametro oggetto, il contenuto del campo, sul quale viene eseguita la funzione di combo
** A patto che venga applicato un dinamismo "LostFocus" sul'input panel, tutte le variabili corrispondenti ai nomi degli altri campi della matrice.

Queste funzionalità sono inoltre implementabili anche nelle funzionalità di richiesta standard UIR, attraverso l'exit del costruttore A08 (si veda la risoluzione della funzione SET_COM)
 :  : DEC T(V2) P(LOCOS) K(A08) L(1)
 :  : DEC T(MB) P(JASRC) K(LOA08_ES) L(1)
