# PARAMETRI ESTESI - ESTENSIONI OGGETTO

### Introduzione :  i parametri

Attraverso i parametri è possibile aggiungere facilmente ad uno, due o tre oggetti applicativi Sme.UP altre informazioni, ciascuna delle quali può a sua volta essere un oggetto Sme.UP oppure un numero o un testo generico.
Si possono anche gestire informazioni multiple o informazioni diverse per data di validità.
Questa struttura è guidata configurando le tabelle C£E (Categoria parametri) e B£N (Parametri variabili).
La Categoria parametri determina gli oggetti di riferimento, l'archivio in cui i parametri vengono scritti e gli elementi di B£N che vi appartengono.
Gli elementi di B£N definiscono le caratteristiche del singolo parametro.

### I parametri estesi

E' stata implementata la possibilità di gestire parametri estesi collegati a una griglia di oggetti.

Questo permette in particolare di gestire : 

- valori **alfanumerici fino a 30000 caratteri**, come ad esempio link web, percorsi di file e cartelle, note
- valori **numerici con precisione 30 e scala 9**
- fino a **3 chiavi** della griglia di oggetti (rispetto alle 2 chiavi gestite dai parametri non estesi)
- numero di **sequenza** dei record (consente l'ordinamento di parametri multipli e dei paragrafi di note che superino i 30000 caratteri)


### Esempi di utilizzo

Nei parametri estesi è possibile salvare : 

- **Commenti** (salvando in ogni record un testo fino a 30000 caratteri). Tramite una integrazione con il costruttore **LOA37** è possibile ascoltare una casella e-mail e inserire le mail come commenti collegati a un oggetto.
- **Note**  (impostando un parametro multiplo è possibile gestire testi lunghi a piacere in cui ciascuna riga contiene un paragrafo ordinati in base al numero di sequenza).
- **Attività collegate**
- **Tag** (per facilitare la ricercabilità)
- **Hash, link, indirizzi web**
- **Percorsi di file e cartelle** collegati ad un oggetto (ad esempio un cliente, un fornitore o un referente)


Inoltre, definendo l'oggetto del parametro come un **J5** è possibile utilizzare il parametro esteso come una struttura definibile tramite gli script di SCP_CFG. (Ad esempio con la descrizione di una attività svolta, una data, un numero di ore e un codice utente).

Tramite i J5 i parametri estesi possono così trovare una varietà di utilizzi mettendo in correlazione più informazioni (delle quali è possibile definire obbligatorietà, oggettizzazione, valori di default, lunghezza ecc)


### Dettagli implementativi

Al fine di non introdurre discontinuità con il passato il file C£CONR0F non è stato modificato, quindi i parametri in esso definiti continuano a funzionare esattamente come prima.

Si è proceduto invece alla creazione di un nuovo file C£ESO00F (e relative copie) nel vengono quale memorizzati i parametri estesi.

Alla definizione di un parametro in tabella B£N sono stati aggiunti i seguenti campi : 

- Flag **Parametro esteso** che identifica i parametri che saranno scritti su C£ESO
- **Lunghezza** del campo codice (alfa)  :  se assente assume 15 se valore non esteso e 256 se valore esteso; impostabile fino a 30000 per i parametri estesi
- **Lunghezza** (precisione) e **Decimali** (scala) del campo valore (numerico)  :  se assente risale alla dimensione massima, 30 9 per parametri estesi e 15 5 per parametri non estesi

In questo modo è possibile gestire parametri di tipo eterogeneo nella stessa categoria (elemento di tabella C£E).

La categoria determina l'archivio in cui vengono scritti i parametri che vi appartengono. I parametri estesi finiscono nel file C£ESOx0F (dove _x_ è la lettera presente nel campo "File di appartenenza" impostato sulla categoria), mentre i parametri non estesi nel file C£CONx0F. Se il campo "File di appartenenza" è vuoto viene assunto C£ESO00F per parametri estesi e C£CONR0F per parametri non estesi. Quindi i parametri di una stessa categoria possono trovarsi nel C£ESO e nel C£CON a seconda del fatto che siano definiti o meno come estesi.


### Accesso tramite OAV

I parametri estesi sono accessibili tramite £OAV come attributi di tipo K/ (differenziandosi quindi dai parametri non estesi P/ ). La £OAV è però limitata a due soli oggetti come chiavi e alla restituzione di un output numerico di precisione 15 e scala 5 nel campo £OAVON. Il campo codice viene restituito nel campo £OAVO_VAES (valore esteso), che viene sempre riempito dall'API.


### API di interfaccia

E' stata realizzata una nuova API di interfaccia £C£F che consente lettura , scrittura, modifica ed eliminazione di parametri, indipendentemente dal fatto che siano definiti come estesi o meno (nel qual caso viene richiamata la £C£E in modo trasparente all'utilizzatore).

La £C£F consente inoltre di accedere ai parametri estesi a 3 chiavi (a differenza della £OAV che gestisce gli attributi K/ con un massimo di 2 chiavi) e restituisce valori numerici con precisione 30 e scala 9.
