  In questo modo io posso impostare una scheda e chiamare come funzione qualsiasi dettaglio
  Esempio Scheda di un messaggio
  - Presenta
    . Immagine
    . Pagina
    . Pagina dell'autore ecc.

# Socialmailer
## Mastering del dato
Sme.UP ERP è il master dei seguenti oggetti/entità di dominio applicativo : 
- account
- referenti
- campagne
- liste

Socialmailer è il master dei seguenti oggetti/entità di dominio applicativo : 
- template newsletter;
- statistiche :  aperture e click

Alcuni dati degli oggetti master si trovano su entrambi :  es. disiscrizione da invio newsletter, l'informazione rimane su socialmailer (per evitare di inviare nuove comunicazioni), ma deve essere riportata sulla scheda del referente.
x


## Funzionalità tecniche

### Premessa

A. Vale sempre il principio di simmetria :  per i link, per download, per le richieste di funzioni
B. Trasferimento dati :  protocollo di comunicazione web service e xml
C. il protocollo è definito dal chiamato

Tipi di integrazione : 
1. login a socialmailer
- attraverso digitazione delle credenziali
- diretto con passaggio automatico delle credenziali

2. Link :  accesso a socialmailer tramite link/URL (che verrà embeddata nel client/server) cui verranno passati i parametri (funzione/pagina che voglio richiamare e parametri relativi all'oggetto es. codice referente)
3. Download
4. Richiesta di dati da presentare all'utente


## Funzionalità applicative

Potremo parlare di integrazione quando : 
- in Sme.UP avremo : 
1. almeno 10 punti che denotano collegamenti con Socialmailer (link)
2. modulo di documentazione video ecc
- in socialmailer : 
1. almeno 10 punti che denotano collegamenti con Sme.UP (link)
2. attivando delle funzionalità di Sme.UP, sarà possibile visualizzare delle voci (es. visualizzazione scheda referente Web.UP )

### Da Sme.UP ERP attraverso Looc.UP : 
- dalla scheda del referente Looc.UP
- voglio avere accesso web (con/senza login?) e consultare in Socialmailer
- pagina del referente
- pagina delle campagne in cui il referente è coinvolto
- pagina delle statistiche del referente/campagne
- voglio avere una matrice di Looc.UP valorizzata con (Interfaccia dati)
- le campagne in cui il referente è coinvolto
- le statistiche del referente/campagne
- dalla gestione dei referenti in Looc.UP (inserimento/modifica/elimina) voglio che ci sia : 
- la possibilità di un aggiornamento sincrono (a run-time) dei referenti in socialmailer
- la possibilità di un aggiornamento asincrono, massivo ma con possibilità di filtro dei referenti in socialmailer

### Da Socialmailer
- voglio poter impostare la connessione verso Sme.UP ERP
- server di riferimento (smeup providere e iseries) utente, password, ambiente

- dalla scheda del contatto (referente)
- voglio arrivare alla scheda del referente presente in web.UP (attraverso link e aperta in un tab del browser)
- voglio avere una sezione/tab/scheda (in socialmailer) che mi presenti le informazioni presenti in Sme.UP ERP ma non gestite/presenti in socialmailer


## Modello di campagna (richiesta di Baroni)
- dalla scheda del referente Looc.UP
- voglio avere accesso web (con
