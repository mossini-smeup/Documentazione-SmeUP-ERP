# Descrizioni di un oggetto

Per ogni oggetto sono stati creati due tipi di descrizioni : 
- Descrizione Base  (OAV G/12)
- Descrizione Completa (OAV G/40)
Entrambe queste descrizioni possono essere ricavate grazie alla /COPY £DEC, rispettivamente ai campi £DECDE e £DECO_DESC.
La descrizione completa è generata in base alle specifiche visibili nella /COPY £IVD, nel campo
£IVDID.

Oltre a queste due descrizioni è possibile forzare una nuova descrizione che viene scritta nell'archivio C£LING0F con le seguenti chiavi : 
T§TIPO :  oggetto (Es. CNCLI)
T§CODI :  codice oggetto di cui si vuole forzare la descrizione
T§LING :  lingua derivata dalla tabella B£2

Infine è possibile comporre una descrizione "Normalizzata" creata automaticamente secondo le regole della /COPY £K40, la cui costruzione può essere schedulata o lanciata manualmente dalla scheda "Controllo parole ricerca naturale", e viene salvata nel file C£ALIA0F con le seguenti chiavi : 
E$TIP1 :  oggetto (Es. OG)
E$COD1 :  codice oggetto (Es. CNCLI)
E$TIP2 :  '**'
E$COD2 :  Codice elemento codice oggetto (Es. codice cliente)
E$ALIA :  '£DE'
E$SCD2 :  codice Azienda

Infine è possibile fare un test di ricerca per ogni singola parola chiave relativa all'oggetto, in modo tale da vedere quanti sarebbero gli elementi visualizzati ricercandola all'interno del
specifico.

