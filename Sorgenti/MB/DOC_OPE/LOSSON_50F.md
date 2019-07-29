
## PREMESSA
Nella release V3R1 di Loocup è presente la possibilità di eseguire l'accesso a SmeUp in SSO. Questa funzionalità non è presente in release precedenti.


## COSA SIGNIFICA SSO
Single Sign On è una tecnologia che permette ad un utente di autenticarsi una sola volta (in dominio) e di accedere alle risorse informatiche alle quali è abilitato (es. 5250, Looc.Up, Web.Up).
Per una panoramica generale consulatare il documento
 :  : DEC T(MB) P(DOC) K(LOBASE_50P)
per approfondimenti  consulatare il documento
 :  : DEC T(MB) P(DOC) K(LOBASE_50G)


## PREREQUISITI
Installando la versione V3R1 di Loocup non può accedere in SSO a qualunque iSeries automaticamente.
E' necessaria un'opportuna configurazione di tutti gli attori in gioco ( server di dominio, iSeries, PC).
I dettagli di questa configurazione esulano lo scopo del documento. Si rimanda alla documentazione specifica oppure a prendere contatto con gli amministratori di sistema.

Vediamo il dettaglio dei prerequisiti : 

 - PC deve essere associato ad un dominio Windows.
 - Il server di dominio deve essere raggiungibile.
 - Il PC deve aver installato un sistema operativo Windows XP Professional SP2/SP3, oppure Windows 7 Professional o superiore. **Le versioni Home non supportano l'SSO con kerberos.**
 - Abilitazione supporto kerberos (vedi appendice A)


**NOTA BENE** : 
L'SSO non può funzionare se il collegamento all'iSeries viene effettuato via IP pubblico (es. se mi collego da casa).
Se si desidera utilizzare comunque l'autenticazione in SSO è necessario collegarsi attraverso il client VPN SSL, al dominio aziendale, per poter usufruire poi delle policy di dominio.


## COME AUTENTICARSI ATTRAVERSO SSO

Seguire  i seguenti passi : 
 * Creare un collegamento a Loocup (Loocup_w.exe o Loocup.exe )
 * Modificare l'attributo "Proprietà" del collegamento :   dopo Loocup.exe, aggiungere uno spazio poi il nome dell'iSeries

![LOBASE_168](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50F/LOBASE_168.png)

- Avviare Loocup


![LOBASE_169](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50F/LOBASE_169.png)

- Nella finestra di signon, spuntare il campo SSO, poi cliccare su OK.


Da questo momento in poi tutti gli accessi che utilizzando il collegamento così configurato non richiederanno l'inserimento della password e avremo diretto accesso a Loocup o alla scelta dell'ambiente.
Nel caso di insuccesso verrà riproposta la finestra di login che richiederà nuovamente le credenziali (va tolto però il segno di spunta dal campo SSO).

### DISABILITARE  L'ACCESSO IN SSO

Aprire la finestra di "About" e togliere il flag di spunta relativo al checkbox "Attiva SSO" : 

![LOBASE_170](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50F/LOBASE_170.png)

## COME ACCEDERE CON UTENTI DIFFERENTI

L'accesso tramite SSO utilizza le credenziali dell'utente iSeries associato all'utente di dominio windows  (utilizzato per accedere al Pc). Tramite SSO si può pertanto accedere con un solo profilo iSeries.

Per autenticarsi attraverso altro profilo, quindi non attraverso SSO, è necessario predisporre un collegamento nel quale o manca il nome dell'iSeries (collegamento generico), oppure si indica un utente.

![LOBASE_171](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50F/LOBASE_171.png)
## SSO ABILITAZIONE ALTERNATIVA

Questa soluzione consente di attivare e disattivare SSO attraverso gli attributi presenti nella riga di collegamento.

 - Creare un collegamento a Loocup (Loocup_w.exe o Loocup.exe )
 - Modificare l'attributo Proprietà del collegamento :   dopo Loocup.exe, aggiungere  uno spazio poi il nome dell'iSeries, un altro spazio ed infine  *SSO
 - Cliccare su OK

![LOBASE_172](http://localhost:3000/immagini/MBDOC_OPE-LOSSON_50F/LOBASE_172.png)
L'utente *SSO è una convenzione adottata da Loocup per indicare la modalità di accesso in SSO.
L'accesso tramite SSO utilizza le credenziali dell'utente iSeries associato all'utente di dominio windows  (utilizzato per accedere al Pc). Tramite SSO si può pertanto accedere con un solo profilo iSeries.
Nel caso in cui si voglia accedere con un utente differente riferirsi al paragrafo precedente.

### DISABILITARE L'ACCESSO IN SSO

SSO da collegamento (link) a Loocup.exe; Modificare un link verso Loocup.exe togliendo il parametro "*SSO"

## TABELLA RIEPILOGATIVA DELLE MODALITA' DI ATTIVAZIONE

|  Nam="Modalità attivazione" |
| 
| .COL Txt="Tipo  utente" LunAut="1" |
| ---|----|
| 
| .COL Txt="Istante Tempo 0 (attivazione SSO)" LunAut="1" |
| 
| .COL Txt="Istante Tempo 1 (effetto)" LunAut="1" |
| 
| .COL Txt="Limiti" LunAut="1" |
| 
| .COL Txt="Per disattivare" LunAut="1" |
| Utente | Imposto SSO in finestra accesso | Accesso diretto | Non posso modificare l'utente d'accesso a meno di disattivare SSO e quindi avere riproposta la maschera di login | About dentro Looc.Up (togli flag) |
| Sviluppatore | *SSO nel link | Accesso diretto | Posso modificare l'utente d'accesso togliendo  *SSO prima di lanciare l'esecuzione | Rimuovere *SSO dal link |
| Sviluppatore | Utente nel link | Richiesta Password | Per attivare SSO devo rifarmi alle condizioni sopra indicate | Niente (a meno che SSO non sia attivo) |
| 



## NOTE

L'accesso all'iSeries tramite SSO avviene con l'utente iSeries associato al profilo di Windows (utente di dominio).
Per accedere con un'utente differente va creato un altro link a Loocup che riporti dopo il nome dell'iSeries il nome dell'utente.
Se si avvia Loocup con questo collegamento e si seleziona il campo SSO, verrà mostrato un avviso in cui si propone di togliere l'utente dal collegamento.
Basterà spuntare il flag "Non mostrare più".
Il link così configurato sarà polivalente :  selezionando il campo SSO avverrà l'accesso in SSO, si potrà comunque indicare la password o cambiare utente.


## APPENDICE  A - Abilitare l'autenticazione kerberos (solo per utenti con privilegi si amministratore)

Fare riferimento al manuale
 :  : DEC T(MB) P(DOC) K(LOBASE_50D)


