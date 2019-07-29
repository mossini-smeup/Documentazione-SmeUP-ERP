## OBIETTIVO

 * registrare alcune informazioni sul pc dove si sta eseguendo LoocUp
 * valutare le prestazioni della rete
 * controllare i prerequisiti

## ATTIVAZIONE

 * Da file di configurazione (netlog.properties), posizionato nella cartella di installazione di Loocup, sottocartella LOOCUP_LOG
 * da riga di comando (parametro --netstat).

NOTA :  se un file con nome <IP_MACCHINA>_<UTENTE>_<AS400>.log è già presente nella cartella di loggattura, non viene sovrascritto.

## GESTIONE DATI DEL LOG

 * Log di valutazione compatibilità e prestazioni del sistema  (NETSTAT)
 ** Nome del file :  <IP_MACCHINA>_<UTENTE>_<AS400>.log
 ** Locazione :  <cartella_installazione_loocup>/LOOCUP_LOG/NETSTAT
 ** Contenuto (campi separati da |) : 
 *** Data
 *** Ora
 *** Tipo dato (ENV, DAT, VER)
 *** Codice valore
 *** Descrizione
 *** Valore 1 (il significato dipende dal tipo dato)
 *** Valore 2 (il significato dipende dal tipo dato)
 *** Valore 3 (il significato dipende dal tipo dato)
 *** Tipo valore 1

Dettagli in
- [Controllo prerequisiti Looc.Up](Sorgenti/MB/DOC/LOBASE_038)
