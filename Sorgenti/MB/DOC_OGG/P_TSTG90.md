# OBIETTIVO
Rendere più semplici le funzioni di lettura e scrittura dei paragrafi.
Per paragrafo si intente una stringa che può estendersi su più righe del sorgente unite fra loro tramite il carattere **+**.
## Metodi di lettura
Attraverso questa API si possono eseguire le operazioni di lettura dei seguenti documenti : 
* Sorgente
* Note
* Help di programma
* Help di tabella
* Documenti x oggetto
* Help di scheda
* Help di archivio
## Metodi di scrittura
Attraverso questa API si possono eseguire le operazioni di scrittura dei seguenti documenti : 
* Sorgente
## Modalità di comunicazione
Gli attributi vengono passati all'api attraverso il buffer di comunicazione (G90SO)

Elenco degli attributi in modalità**Sorgente** : 
 :  : PAR L(TAB)
**Attributo** | **Descrizione**             | **Dove si attiva**
Lib       | Nome della libreria     | Lettura e Scrittura
Fil       | Nome del file           | Lettura e Scrittura
Mem       | Nome del membro         | Lettura e Scrittura
Sec       | Sezione                 | Lettura
SAt       | Attributo               | Lettura
SeE       | Attributo fine          | Lettura
SAM       | Conversione in maiuscolo| Lettura
TMe       | Tipo membro             | Scrittura
DMe       | Descrizione membro      | Scrittura
BefTag    | Tag Originale           | Scrittura
BefImg    | Paragrafo Originale     | Scrittura
AftTag    | Nuovo Tag               | Scrittura
AftImg    | Nuovo Paragrafo         | Scrittura


Elenco degli attributi in modalità**Note** : 
 :  : PAR L(TAB)
Attributo || Descrizione             || Dove si attiva
NCo       | Contenitore             | Lettura
NK1       | Chiave 1                | Lettura
NK2       | Chiave 2                | Lettura
NK3       | Chiave 2                | Lettura
NCi       | Capitolo iniziale       | Lettura
NCf       | Capitolo finale         | Lettura


Elenco degli attributi in modalità**Help di programma** : 
 :  : PAR L(TAB)
Attributo | Descrizione             | Dove si attiva
Lib       | Nome della libreria     | Lettura
Fil       | Nome del file           | Lettura
HPg       | Nome del membro         | Lettura
Con       | Contesto                | Lettura


Elenco degli attributi in modalità**Help di tabella** : 
 :  : PAR L(TAB)
Attributo | Descrizione             | Dove si attiva
Set       | Settore                 | Lettura
Cam       | Campo                   | Lettura


Elenco degli attributi in modalità**Documenti oggetto** : 
 :  : PAR L(TAB)
Attributo | Descrizione             | Dove si attiva
DT1       | Tipo 1                  | Lettura
DK1       | Oggetto 1               | Lettura
DT2       | Tipo 2                  | Lettura
DK2       | Oggetto 2               | Lettura
DTd       | Documento               | Lettura


Elenco degli attributi in modalità**Help di scheda** : 
 :  : PAR L(TAB)
Attributo | Descrizione             | Dove si attiva
Lib       | Nome della libreria     | Lettura
Fil       | Nome del file           | Lettura
HSc       | Nome del membro         | Lettura
Sec       | Sezione                 | Lettura
SAt       | Attributo               | Lettura
SeE       | Attributo fine          | Lettura
SAM       | Conversione in maiuscolo| Lettura


Elenco degli attributi in modalità**Help di archivio** : 
 :  : PAR L(TAB)
Attributo | Descrizione             | Dove si attiva
Arc       | Settore                 | Lettura
Cam       | Campo                   | Lettura

## Opzioni
Sono attivabili le seguenti opzioni in fase di**lettura** : 
 :  : PAR L(TAB)
Opzione   | Descrizione
G90TB     | Trascura paragrafi vuoti
G90ST     | Solo paragrafi con TAG
G90II     | Leggi anche le include come se fossero parte del membro in lettura
G90TV     | Restituisci il testo del paragrafo con la variabile**TXT**

Sono attivabili le seguenti opzioni in fase di**Estrazioni delle costantoi** : 
 :  : PAR L(TAB)
Opzione   | Descrizione
G90ES     | Elimina caratteri speciali

Sono attivabili le seguenti opzioni in fase di**Aggiornamento** : 
 :  : PAR L(TAB)
Opzione   | Descrizione
G90IP     | Identificativo del paragrafo da gestire, inteso come numero progressivo nel sorgente.

## Gestione dei paragrafi
Per poter gestire in maniera corretta i paragrafi bisogna tener presente le seguenti regole : 
* Se si richiede l'aggiunta di un paragrafo, questo sarà aggiunto popo il paragrafo di riferimento (G90IP)
* Se di richiede la modifica o la cancellazione di un paragrafo, questo deve essere passato nel paragrafo di   riperimento (G90IP)
* Se viene passato l'immagine originale, verrà rieseguita la lettura del paragrafo per controllarne l'integrità.
