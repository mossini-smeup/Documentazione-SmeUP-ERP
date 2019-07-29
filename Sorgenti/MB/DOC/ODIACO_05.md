# Manutenzione documenti conservati
## Controlli pre conservazione
Prima dell'avvio della fase di conservazione gestita dal documentale vengono avviati i controlli gestionali relativi ai documenti sottoposti a conservazione. Tali controlli sono di due tipi :  relativi al lotto che si sta conservando e relativi ai lotti già conservati
### Controlli all'interno del lotto di conservazione
Quando si procede alla conservazione di un lotto di documenti vengono effettuati dal programma ODSER_06 dei controlli sul fatto che le fatture che si stanno conservando abbiano i protocolli consecutivi e senza buchi. Se il controllo non ha successo la conservazione si interrompe. Se il controllo è superato con successo la conservazione procede passando il controllo delle operazioni a Comped Document Filing Manager. Che opera sui documenti elettronici. Una volta che quest'ultima fase ha successo viene presa nota dell'ultimo documento conservato per ogni protocollo coinvolto nella conservazione.
### Controlli di consequenzialità fra lotti successivi
Superato il controllo di cui al punto precedente relativo al contenuto del lotto, parte una fase di controllo per far sì che non si creino buchi nella numerazione dei documenti conservati fra due differenti lotti. Quindi ad esempio se si sta per conservare un lotto di documenti relativi al protocollo V1 e il primo documento del lotto in esame ha numero 000118, verrà controllato che l'ultimo documento conservato, relativamente al protocollo V1, abbia numero 000117.

## A conservazione avvenuta
Una volta che il singolo documento è conservato esso è immodificabile per il resto della sua esistenza.

### Procedure di forzatura degli indicatori di conservazione
Qualora per qualche motivo, ovviamente entrando in un ambito che non è ammissibile dalle normative al momento vigenti, ma comunque applicabile nelle fasi di test dell'applicazione, sia necessario rendere nuovamente archiviabile o conservabile un documento si può procedere nel seguente modo


- call xv5078
-- inserire il numero di protocollo del documento da sbloccare
-- inserire il numero fattura del documento da sbloccare
-- INVIO


E' altresì possibile modificare gli indicatori di controllo della consequenzialità fra loti di conservazione

- up par
-- categoria parametri £d2
-- inserire Tipo Documento e Parametro Documento
-- INVIO
-- inserire il numero di documento desiderato


### Ultima nota per testing
Per stampare una fattura in PDF con archiviazione : 

- call v5fa01a
- mettere a 1 sia _3_Tipo Output Fattura sia _3_Archiviazione
- inserire il documento desiderato (per il numero di fattura nel v5fa01a +=nr fattura)
- F6

