# Scenario
## Autorizzazioni su dati scenario
Gli scenari modificabili da una sessione sono tutti quelli che hanno i primi due caratteri corrispondenti all'azienda della B£2, se questa non è indicata sono tutti modificabili. Se uno scenario non è modificabile i suoi dati sono comunque visualizzabili. Se si vogliono applicare differenti criteri per la determinazione della modificabilità, basarsi sull'exit attivabile tramite la BR2.

Se invece un utente non risulta autorizzato allo scenario, per lui lo scenario è come se non esistesse.

## Utilizzo dello scenario nelle interfacce
 * si ha in chiave lo scenario
 ** lo scenario non viene passato, che sia passato o meno non cambia molto, l'unica cosa che cambia è la porzione di scenario che si va ad utilizzare ...
 *** 1) non si gestisce lo scenario --> nessun problema
 *** 2) lo scenario è l'azienda --> posizionamento --> si calcola lo scenario e si fissano sia azienda che scenario in chiave --> scansione --> si tiene lo scenario/azienda calcolato nella scansione
 *** 3) lo scenario è l'azienda + qualcos'altro --> posizionamento --> si calcola lo scenario e si fissano sia azienda che scenario in chiave --> scansione --> se lo scenario che viene ritornato è solo l'azienda, si deve continuare a saltare se il codice si ripete
 *** 4) lo scenario è l'azienda oppure l'azienda + qualcos'altro --> posizionamento --> si calcola lo scenario e si fissano sia azienda che scenario in chiave --> scansione --> si tiene lo scenario/azienda calcolato nella scansione
 ** lo scenario viene passato
 *** 1 non si gestisce lo scenario
 *** 2 lo scenario è l'azienda
 *** 3 lo scenario è l'azienda + qualcos'altro
 *** 4 lo scenario è l'azienda oppure l'azienda + qualcos'altro
 * non si ha in chiave lo scenario
 ** lo scenario non viene passato
 *** 1 non si gestisce lo scenario
 *** 2 lo scenario è l'azienda
 *** 3 lo scenario è l'azienda + qualcos'altro
 *** 4 lo scenario è l'azienda oppure l'azienda + qualcos'altro
 ** lo scenario viene passato
 *** 1 non si gestisce lo scenario
 *** 2 lo scenario è l'azienda
 *** 3 lo scenario è l'azienda + qualcos'altro
 *** 4 lo scenario è l'azienda oppure l'azienda + qualcos'altro
