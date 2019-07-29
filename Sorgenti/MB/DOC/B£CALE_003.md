# Modalità del reperimento calendario
La funzione di reperimento del calendario riceve : 

- un tipo risorsa (elemento della tabella TRG, nel seguito T1)
- una risorsa (oggetto del tipo e parametro definito nel tipo risorsa), nel seguito R1
- due date (se assente l'inferiore viene assunto oggi, se assente la superiore viene assunta l'inferiore)

e ritorna, per ciascuna data compresa tra le due date ricevute : 

- il codice dell'orario (in bianco se chiusura totale)
- il numero di risorse
- la percentuale di utilizzo
- il numero di ore lavorative

In questo documento viene esposta la modalità di reperimento di queste informazioni, che può anche essere molto articolata, qualora si abbia la necessità di inserire le informazioni a livelli più alti rispetto alla singola risorsa.

## Lettura calendario annuale
Legge il calendario annuale di T1.
Se non trovato ed è impostato in tabella TRG il tipo risorsa superiore legge il calendario annuale di questo tipo risorsa.
Se non trovato scrive il calendario annuale di T1, eventualmente copiandolo (se impostato in T1 il flag di calendario base) dal calendario base dell'anno 3000 (della (del tipo) risorsa base se impostata in T1, oppure, se a blanks, di T1 stesso).
Il calendario annuale serve per definire : 

- i giorni di chiusura completa (codice F)
- i giorni particolari (codici 1-5), ad esempio semi-festività, il cui codice orario è contenuto nel calendario base.

### Nota
Se impostato in T1 il flag di calendario base, anche in inserimento manuale del calendario annuale (sia in modo esplicito con l'opzione  01, sia passando tramite il tasto roll-up o roll-down ad un anno inesistente in archivio), vengono proposte le informazioni del calendario base dell'anno 3000 (del tipo risorsa del calendario base se presente, altrimenti di T1).
In questo modo è possibile fissare, una volta per tutte, i giorni comuni a tutti gli anni (ad esempio le chiusure complete per festività civili e religiose fisse).

## Lettura calendario base
Si legge il calendario base, in cui si definiscono gli orari della settimana standard e quelli per le eccezioni 1-5 definite nel calendario annuale, con la seguente risalita, tenendo presente che essa termina al primo record valido (vale a dire con il codice orario del lunedì valorizzato) :  (R1 è l'oggetto del calendario e T1 il tipo risorsa a cui appartiene).

-  Calendario di R1 di tipo T1,
-  Se impostato in T1 il tipo risorsa deviata D1 e l'OAV di deviazione, il calendario dell'OAV di R1 (se non blanks) di tipo D1
-  Se presente nel calendario base di R1 la risorsa collegata, il calendario della risorsa collegata di tipo T1 (Vedi NOTA di seguito per compilazione)
-  Il calendario  della risorsa ** di tipo T1.
-  Se impostato in T1 il tipo risorsa deviata D1 il calendario della risorsa ** di tipo D1.

Se non viene trovato nessun calendario base valido, la funzione termina con la segnalazione di errore.
### Nota
Perché sia assunta la risorsa collegata è necessario scriverla nel record di R1 senza specificarvi gli orari.
Nel calendario settimanale è obbligatorio inserire la risorsa collegata oppure tutti gli orari. (settimanali e giorni speciali). Se si inseriscono entrambi, la risorsa collegata sarà utilizzata nel reperimento delle eccezioni.

## Lettura eccezioni (modalità di risalita)
E' possibile definire, per un tipo risorsa, una risorsa, un mese ed un anno, per ogni giorno del mese, il codice orario che, se impostato, si sovrappone a quello determinato dal calendario base.
Sono possibili varie modalità di risalita, in funzione di quanto impostato nel campo  eccezioni comuni  di T1.
Viene assunto, per ogni giorno del mese, il primo codice orario valorizzato, nella seguente scaletta : 

### Eccezioni comuni = blanks : 

-  Risorsa
-  Risorsa deviata (se impostato in T1 l'OAV per deviazione)
-  Risorsa collegata (se impostata nel calendario base di R1)
-  Risorsa **


### Eccezioni comuni = 1

-  Risorsa dell'anno
-  Risorsa deviata dell'anno (se impostato in T1 l'OAV per deviazione)
-  Risorsa collegata dell'anno (se impostata nel calendario base di R1)
-  Risorsa ** dell'anno.
-  Risorsa dell'anno 3000
-  Risorsa deviata dell'anno 3000 (se impostato in T1 l'OAV per deviazione)
-  Risorsa collegata dell'anno  3000 (se impostata nel calendario base di R1)
-  Risorsa ** dell'anno 3000


### Eccezioni comuni = 2

-  Risorsa dell'anno
-  Risorsa dell'anno 3000
-  Risorsa deviata dell'anno (se impostato in T1 l'OAV per deviazione)
-  Risorsa deviata dell'anno 3000 (se impostato in T1 l'OAV per deviazione)
-  Risorsa collegata dell'anno (se impostata nel calendario base di R1)
-  Risorsa collegata dell'anno  3000 (se impostata nel calendario base di R1)
-  Risorsa ** dell'anno
-  Risorsa ** dell'anno 3000

### Note

- Impostando il flag  eccezioni comuni  è possibile definire un'eccezione valida per tutti gli anni. Ad esempio, se un cliente è sempre chiuso in agosto, è sufficiente inserire questa eccezione per l'anno 3000.
- L'orario di eccezione si sovrappone non solo al codice orario base, ma anche alla chiusura completa (definita a livello di calendario annuale).
- L'esposizione precedente, relativa alla determinazione del codice orario, si applica nello stesso modo al numero risorse e alla percentuale di utilizzo (valori del calendario base sovrapposti da quelli della prima eccezione significativa).
- Significato dell'origine del dato nelle interrogazioni


| 
| .COL Txt="Codice" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| A | GENERALE - CHIUSURA COMPLETA |
| B | GENERALE - CHIUSURA COMPLETA RIS.SUPER. |
| C | RISORSA ASSUNTA |
| D | RISORSA COLLEGATA |
| E | RISORSA DEVIATA |
| F | RISORSA |
| G | ECCEZIONE COMUNE RISORSA ASSUNTA |
| H | ECCEZIONE RISORSA ASSUNTA |
| I |  ECCEZIONE COMUNE RISORSA COLLEGATA COMUNE |
| J | ECCEZIONE RISORSA COLLEGATA |
| K | ECCEZIONE COMUNE RISORSA DEVIATA |
| L | ECCEZIONE RISORSA DEVIATA |
| M |  ECCEZIONE COMUNE RISORSA |
| N | ECCEZIONE RISORSA |
| 

 C(*CONT)
- Errori segnalati nelle interrogazioni


| 
| .COL Txt="Codice" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| A | Trovati troppi codici orario nelle tabelle OLG. Possono essere gestiti al massimo 98 codici orario |
| B | Nell'anagrafico risorse non è stata trovata la risorsa di default (**), oppure è priva di codici orari |
| C | Nel calendario annuale non è stato trovato l'anno richiesto, per il tipo di risorsa |
| D | Il periodo richiesto supera la capacità del calendario. (Possono essere gestiti al massimo 999 giorni.) |
| E | Nell'anagrafico risorse o nelle eccezioni è stato trovato un codice orario non valido |
| 

