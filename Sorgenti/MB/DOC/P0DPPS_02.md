## Dati generali
I dati della società, i responsabili del trattamento dati, della sicurezza dei sistemi informativi e l'incaricato alla custodia delle parole chiavi e codici identificativi sono nei parametri dell'azienda.
Anche  gli incaricati al trattamento dei dati sensibili e giudiziari sono parametri.
 :  : DEC T(CN) P(AZI) K(01)

_NOTA :  La categoria di questi parametri  è AZI ed il sottosettore della B£N è AZ (è diversa dalla categoria standard dei parametri aziendali che è £CA, in quanto gli automatismi di aggiornamento di quest'ultima per la fasatura fiscale delle informazioni legate alla contabilità sconsigliava l'utilizzo della stessa....)

 :  : DEC T(ST) K(B£N) (AZ)

Dei dati generali fanno parte : 

### Sede
### Titolare trattamento
Il dato viene letto nella categoria dei parametri AZI+ codice azienda, parametro X0 .
### Responsabili

- responsabile trattamento : 
il dato viene letto nella categoria dei parametri AZI+ codice azienda, parametro X1.
- responsabile della sicurezza e dei Sistemi informativi : 
il dato viene letto nella categoria dei parametri AZI+ codice azienda, parametro X2 .
- incaricato alla custodia delle parole chiave e codici identificativi :  il dato viene letto nella categoria dei parametri AZI+ codice azienda, parametro X3 .
- incaricati al trattamento dati personali e comuni : 
Gli incaricati al trattamento dei dati personali e comuni sono i contatti di tipo COL, opportunamente filtrati con una loro caratteristica (in SME.up è lo stato minore di 15)
- incaricati al trattamento dei dati sensibili e giudiziari : 
il dato viene letto nella categoria dei parametri AZI+ codice azienda, nel parametro X4 .
- terzi che trattano dati della società, non appartenenti in maniera diretta alla società stessa : 
Si tratta di tutti i contatti di tipo COL che hanno Stato=2 e Livello=13/14/15 e che hanno inserita in anagrafica Zona=EXT;
inoltre vengono letti anche i parametri AZI+ codice azienda X6 (fornitori esterni) 	

 :  : DEC T(CN) K(COL)
La stessa lista dei collaboratori ma con un filtro più ristretto viene utilizzata per catalogare i Terzi che trattano dati.
La lista dei locali dove vengono trattati i dati è nel parametro X5 dell'azienda. I locali sono codificati nella tabella delle ubicazioni dei cespiti.

## Misure fisiche
il dato viene letto nella categoria dei parametri AZI+ codice azienda, nel parametro X5  (TA P0*MA);
a questo punto il filtro passa sulla Categoria A5E parametro B1.
I metodi di accesso sono codificati nella tabella P0*MA
 :  : DEC T(ST) K(P0*MA)

## Server e sistemi aziendali
I computers, i servers ed i sistemi di collegamento con l'esterno sono codificati nei cespiti aziendali. Tramite la tabella A5D sono identificati (campo chiamato raggruppamento implicito del cespite) ed i sistemi di protezione sono caratterizzati nei parametri dell'elemento A5D.
Vengono scansionati i cespiti relativi alla categoria fiscale "Macchine uff.elet. ed elettro." tramite la £ICE filtrando su quelli con classe implicita=A3/A5 ;
le caratteristiche vengono lette nella categoria dei parametri A5D+ classe implicita=A3/A5, nel parametro C1.
Nb :  la categoria fiscale viene letta dalla tabella P01 campo T$P01B!
 :  : DEC T(ST) K(A5E)
 :  : DEC T(CE) K()
 :  : DEC T(ST) K(A5D)

## Elaboratori e apparecchiature
Vengono scansionati i cespiti relativi alla categoria fiscale "Macchine uff.elet. ed elettro." tramite la £ICE filtrando su quelli con classe implicita=A2 ;
le caratteristiche vengono lette nella categoria dei parametri A5D+ classe implicita=A2, nel parametro C1.
Nb :  la categoria fiscale è cablata nel servizio!!!

## Dispositivi di connessione esterna
Vengono scansionati i cespiti relativi alla categoria fiscale "Macchine uff.elet. ed elettro." tramite la £ICE filtrando su quelli con classe implicita=A4 ;
le caratteristiche vengono lette nella categoria dei parametri A5D+ classe implicita=A4, nel parametro C1 .
Nb :  la categoria fiscale è cablata nel servizio!!!

## Censimento banche dati
Archivi cartacei : 
Gli archivi vengono letti dalla tabella TA P0H, nella quale sono presenti anche tutte le informazioni necessarie :  dati trattati, locale di collocamento, tipo di custodia, persona/e con accesso, metodo di accesso e trattamento dati.
La persona di accesso è un parametro che viene letto nella categoria P0H definito come A10;
Gli Archivi Cartacei sono codificati nella tabella P0H.
 :  : DEC T(ST) K(P0H)
Archivi informatici : 
Gli Archivi informatici sono codificati nella tabella P0G :  notare che in tale tabella c'è anche la classe/funzione di protezione di Smeup per tali archivi. Questo permette di ottenere automaticamente la lista degli utenti (B£U) che sono autorizzati a creare, modificare, visualizzare, stampare tali archivi.
 :  : DEC T(ST) K(P0G)
Autorizzazioni : 
Vengono passati i codici Classe e Funzione letti dalla tabella TA P0G per l'archivio, e viene quindi eseguita la £AUA per ogni utente azienda presente nella TA B£U per il reperimento delle autorizzazioni.

## Sezione documenti
Il resto del documento non è stato strutturato e viene proposto in modalità testo.
Le lettere informative da spedire a clienti, fornitori, collaboratori, vengono generate usando la G69 e la lista degli enti.

Chiamata al servizio JATRE_34C (VIS) puntando ai membro di documentazione DPPS08_00  DPPS17_08 (file DOC_DPPS/SMEDEV)
Tali membri contengono delle variabili individuabili tramite il prefisso & che vengono poi tradotte.

Documentazione Servizio
Presente in DOC_SER riferita al servizio B£SER_14;
Si accede tramite la Scheda di LoocUp Documentazione/documentazione servizi/B£SER_14.

Lista Clienti
 :  : DEC T(CN) K(CLI)

Lista Fornitori
 :  : DEC T(CN) K(FORI)

