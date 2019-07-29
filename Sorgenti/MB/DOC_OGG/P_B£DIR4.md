# OBIETTIVO
Visualizzare la disponibilità di una risorsa in un determinato periodo :  numero di risorse, codice dell'orario di lavoro e sua rappresentazione grafica nell'arco della giornata.
Il programma consente inoltre di ottenere, per ogni giornata, un formato di dettaglio con le informazioni circa l'origine dei dati di disponibilità, ossia da quali archivi sono stati ricavati.
In tal modo è più facile capire quali priorità sono state adottate dalla funzione di preparazione del calendario, e quindi come si devono modificare gli archivi se il calendario ottenuto non corrisponde a quello che ci si aspettava.
# DETTAGLIO FORMATI
# Formato guida

![B£DIR4_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR4/BXDIR4_01.png)
## Tipo risorsa gestita
Codice controllato sulla tabella TRG.
## Codice risorsa
Viene controllato sull'anagrafico opportuno, in funzione del tipo di risorsa. I codici che iniziano con '**' non vengono controllati.
## Data inizio / Data fine
Delimitano il periodo da visualizzare.
# Formato visualizzazione

![B£DIR4_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR4/BXDIR4_02.png)
## Abbreviazioni

- S = scelta. Permette di passare ad un formato che presenta in dettaglio tutti i dati del giorno.
- Ori Ris = origine del numero di risorse
- Num Ris = numero di risorse
- Ori Cod = origine del codice orario di lavoro
- Co Or = codice orario di lavoro


## Grafico
Ogni riga rappresenta la disponibilità della risorsa in una giornata. Ogni colonna rappresenta mezz'ora.
# TABELLE COLLEGATE

- TRG  =    Tipo risorsa gestita
- OLG  =    Orari lavorativi

# MODALITA' DI COSTRUZIONE DEL CALENDARIO
Il calendario di una risorsa viene costruito leggendo i tre archivi

- anagrafico risorse
- calendario annuale
- eccezioni per periodo


## Sequenza operativa
### Lettura anagrafico risorse
Permette di ottenere i valori settimanali e particolari per codici orari, numero risorse disponibili e percentuali di utilizzo. Questi dati vengono assunti dalla prima risorsa trovata che contiene dei codici orari non in bianco. La ricerca procede utilizzando in cascata i codici risorsa : 

- della risorsa interessata
- della risorsa collegata, se indicata per la risorsa
- della risorsa di default '**'

### Lettura anagrafico risorse
Permette di ottenere i valori settimanali e particolari per codici orari, numero risorse disponibili e percentuali di utilizzo. Questi dati vengono assunti dalla prima risorsa trovata che contiene dei codici orari non in bianco. La ricerca procede utilizzando in cascata i codici risorsa : 

- della risorsa interessata
- della risorsa collegata, se indicata per la risorsa
- della risorsa di default '**'

NB :  l'anagrafico della risorsa di default deve sempre esistere ed avere impostati tutti i codici orari.

### Lettura calendario annuale del tipo risorsa interessata
Permette di ottenere i codici tipo giorno.
### Costruzione calendario
I dati relativi ad ogni giornata vengono impostati utilizzando i valori 'settimanali' o 'particolari' letti dall'anagrafico risorse, in funzione del codice 'tipo giorno' letto nel calendario annuale : 

- ' ' fa assumere i valori di quel giorno della settimana (ad esempio, del martedì)
- '1'-'5' fanno assumere i valori del corrispondente giorno particolare numero 1 - 5
- 'F' forza una 'chiusura totale', ponendo a zero il numero di ore lavorative.


### Ricerca eccezioni della risorsa di default o collegata
Se i dati anagrafici utilizzati nella fase precedente (letti nella prima fase), sono quelli della risorsa di default, si cercano le eccezioni della risorsa di default. In caso contrario, se nell'anagrafico della risorsa è indicata la risorsa collegata, si cercano le eccezioni della risorsa collegata.
Se vengono trovate, ogni valore non vuoto viene forzato nel corrispondente dato nel calendario (qualunque fosse il suo contenuto precedente).
### Ricerca eccezioni della risorsa
Se vengono trovate, ogni valore non vuoto viene forzato nel corrispondente dato nel calendario (qualunque fosse il suo contenuto precedente).
## Errori segnalati
Gli eventuali errori rilevati durante la costruzione del calendario vengono segnalati con dei codici, indicati nella seguente tabella : 

 - _2_A; trovati troppi codici orario nelle tabelle OLG. Possono essere gestiti al massimo 98 codici orario.
 - _2_B; nell'anagrafico risorse non è stata trovata la risorsa di default (**), oppure è priva di codici orari.
 - _2_C; nel calendario annuale non è stato trovato l'anno richiesto, per il tipo di risorsa.
 - _2_D; il periodo richiesto supera la capacità del calendario. Possono essere gestiti al massimo 999 giorni.
 - _2_E; nell'anagrafico risorse o nelle eccezioni è stato trovato un codice orario non valido.

