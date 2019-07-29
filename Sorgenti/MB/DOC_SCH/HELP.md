# Help
## Cosa riceve la scheda di help contestuale

Sono possibili 3 casi : 

### Configurazione di questionari RE Q- o RE L-

Oggetto 1 :  il questionario da cui è stata invocata.
From :  da quale componente è giunta la richiesta
Sect :  la sezione contenente la domanda
Posi :  la domanda di cui si richiede l'help


### Configurazione di tag di script
Oggetto 1 :  il questionario da cui è stato estratto il questionario associato al tag
From :  vale UIG30TagDialog
Sect :  è il nome del tag che si sta configurando
Posi :  la domanda di cui si chiede l'help


### Configurazione di parametri di servizi

Se la richiesta è giunta da un questionario di configurazione di un parametro di un servizio si ha che : 
l'oggetto 1 è il servizio
From ha il valore "Dialog"
Sect è la funzione.metodo del servizio
Posi è la domanda. Nel caso di parametri posizionali il codice della domanda è QST_xx dove xx è un progressivo.
