 :  : HEA RESP(LS) STAT(00)
# Obiettivo
Chiedere ad un servizio di costruire/completare la gliglia/colonna ricevuta mediante XML.
Ad esempio posso leggere un file CSV mediante il componente DBM e chiedere di riassegnare testo, oggetto, IO, ecc di una colonna derivandolo eventualmente da uno SCRIPT fornito.
Ogni colonna viene passata a questo servizio per il completamento.
In particolare viene chiamato dal servizio JA_00_19 che ottiene una griglia contenente la colonna che deve essere riassegnata.

# Funzioni/Metodi
- GRI = Tutte le colonne di una tabella passata
- COL = Permette di modificare il contenuto di una colonna nella lettura di database esterni.
- SET = Setup associati all'esterno per la tabella letta

# Input/Ouput
## Input
- T5/P5/K5 = Membro da cui leggere le assegnazioni
  - Assume MB SCP_SET SMA_SER_33
  - La sezione *DEFAULT è sempre aggiunta come prototipo definito all'interno del programma stesso
- K6 = Nome della sezione dello script (rappresenta di fatto il tracciato della tabella)
  - Assume il contenuto del campo TABLE dell'INPUT
  - Assume la sezione bianca se manca la sezioni indicata
- INPUT
  - TABLE = Nome della tabella
  - COD   = Codice della colonna
  - TXT   = Testo

## Ouput
Griglia standard di LOOC.up che contiene una sola colonna da sostituire alla colonna in elaborazione

### Comportamento del servizio
1. Carico lo script opportuno (Assumo SCP_SET/SMA_SER_33 e aggiungo la sezione *DEFAULT)
2. Determino la sezione da elaborare (assumo la sezione bianca all'interno dello script e *DEFAULT)
3. Scandisco i campi
   - Se trovo COD corrispondente ne derivo tutti e soli gli attributi trovati sostituendoli
   - Se manca COD e trovo TXT procedo come sopra
4. Alla griglia associo comunque i setup eventualmente presenti
