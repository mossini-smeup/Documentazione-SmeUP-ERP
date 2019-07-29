# Figure e immagini
Le figure della documentazione sono immagini (quindi dei file) legate al modulo di appartenenza e hanno consistenza tramite l'oggetto V3F.<Modulo>
Il file è l'immagine. La figura è l'associazione dell'immagine al modulo.
Nella documentazione si possono inserire figure e non immagini.
L'unica estensione consentita per le immagini è PNG

# Dove si trovano
Le immagini (i file) sono depositate sul server definito nella variabile SME.IMG (Immagini distribuite) e PER.IMG (Immagini presenti solo nell'installato), all'interno del server specificato sono suddivise per applicazione e modulo.
Le figure sono catalogate in appositi membri.

# Scheda di gestione
Per associare una nuova immagine al modulo (e quindi creare una figura) bisogna eseguire le seguenti operazioni : 
## Immagine generata in Looc.UP
Attraverso lo "Screenshot della scheda" si acquisisce l'immagine in formato PNG, attraverso questa operazione si viene  automaticamente indirizzati alla scheda dell'immagine PNG da cui si procede all'associazione al modulo, tramite apposita scelta da menù.
Una volta selezionato il modulo in cui depositare l'immagine e confermato il suo nome l'immagine verrà automaticamente salvata sul server e verrà automaticamente creata la figura.
## Da un'Immagine
L'immagine deve essere in formato PNG, a questo punto aprendo la scheda dell'immagine (J7), possiamo procedere all'assegnazione nella medesima modalità dello "Screenshot"
## Dal modulo
Attraverso il menù della documentazione e successivamente attraverso il tag gestire figure, scegliamo la cartella che contiene l'immagine da associare (che deve essere in formato PNG)  e confermiamo il suo nome, l'immagine verrà automaticamente salvata sul server.

# Come installare l'archivio figure dei moduli standard
Le immagini sono distribuite in un file compresso reperibile sul sito di Smeup nella sezione dei download.
## Il download
Dal sito Smeup è possibile scaricare un file (in formato zip) contenente tutte le immagini.
Accedere all'area Download del sito Smeup, posizionarsi su "Download Sme.UP ERP" e successivamente nella sezione "Immagini e documentazione". Il file è SmeImg.zip.
[http://www.smeup.com](http://www.smeup.com)
## La configurazione
Nella variabile SME.IMG è definito il  percorso dove vengono cercate (da visualizzatori o generatori di documentazione) le immagini delle figure della documentazione. Tale variabile deve avere un valore che rappresenti il percorso di una cartella raggiungibile da Looc.UP / Sme.UP Provider.
Nell'impostazione standard essa eredita il proprio valore  dalla variabile SME.HOM (a partire dalla quale si definiscono i vari archivi di risorse esterne). Quindi, se si vuole mantenere l'impostazione standard si dovrebbe modificare SME.HOM ed ottenere di conseguenza la modifica  della variabile SME.IMG. Occorre fare attenzione però che così facendo si ottiene come effetto la modifica di TUTTE le variabili che ereditano il valore di SME.HOM. Diversamente si può modificare SOLO il valore di SME.IMG. Per identificare da quale script SCP_CLO vengono caricate le variabili fare riferimento alla scheda delle variabili a cui si accede dal menù Servizi --> Variabili
Una volta impostata la variabile va riavviato Looc.UP / Sme.UP Provider perché la modifica venga recepita.
## Il ripristino
L'archivio in formato zip va scompattato, ottenendo così la cartella SmeImg.
La cartella così ottenuta deve essere posizionata in maniera da coincidere con il percorso ottenuto dalla variabile SME.IMG
