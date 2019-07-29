## Obiettivo
Questo componente si propone di gestire un raccoglitore di funzioni. Le funzioni sono lette da tutti gli SCRIPT di SCP_SET aventi un prefisso indicato come parametro.
Gli SCRIPT e il loro contenuto potrànno facilmente essere estesi dall'utente e nello stesso tempo LOOC.up tratterà tali argomenti in modo univoco e quindi standard. Come per tutti i costruttori in futuro potranno essere implementate nuove funzionalità operative.

## Definizioni

- Elemento
Una qualsiasi funzione richiamabile in LOOC.up

- Subsezione
Insieme di elementi. La subsezione ha associato : 
-- Attributi. Utilizzati come codici di ricerca e parzializzazione
-- Note esplicative

- Sezione
Insieme di subsezioni
- Gruppo
Insieme di sezioni descritte in un membro di SCRIPT. I gruppi sono numerati da 01 a 99 e il numero viene usato come progressivo nella costruzione del nome dopo il prefisso ricevuto.


## Convenzioni

- I gruppi sono definiti secondo la codifica xxxxnn dove xxxx è il prefisso ricevuto e nn è un progressivo da 01 a 99


## Modalità di utilizzo ed esempi

- Definisco come prefisso LOA07_OD per l'organizzazione della documentazione
- Definisco un gruppo per destinatario
- Organizzo sezioni e subsezioni a piacere
- Definisco attributi (esempio importanza, ubicazione, stato ecc) per tutte le subsezioni
- Inserisco note interpretative per ogni sottosezione
- Inserisco le funzioni tipiche di ogni subsezione
-- Chiavi di menù
-- Schede
-- Documenti
-- Cartelle del file system
-- Ecc.


 :  : DEC T(MB) P(DOC_VOC) K(L_EDT_SET)
