## OBIETTIVO

Registrare i tempi di avvio del client LoocUp

## ATTIVAZIONE

 * Da riga di comando, aggiungendo il parametro **--startdbg**
 * Tramite file di configurazione :  all'interno della cartella di installazione LOOCUP_LOG va creato/modificato un file con nome "startup.properties". All'interno di esso andranno scritte le seguenti righe : 
-abilito il log dello startup
log_startup=true
-abilito la loggatura nella cartella di installazione sottocartella LOOCUP_LOG\STARTUP
log_startup_in_install_folder=true

## GESTIONE DATI DEL LOG

Il log contiene le informazioni sul tempo che intercorre tra l'avvio di Loocup e la visualizzazione della prima schermata.

 * Log di valutazione di tempi di avvio (STARTUP)
 ** Nome del file :  <numero_univoco>.log
 ** Locazione : 
 *** <cartella_installazione_loocup>/LOOCUP_LOG/STARTUP
 *** in locale, nella cartella dei file di log di LoocUp, sottocartella STARTUP,
 ** Descrizione :  registra i tempi di avvio di loocup
 ** Contenuto : 
 *** Data
 *** Ora
 *** Tipo dato (TIM o ENV)
 *** Codice valore
 *** Descrizione
 *** Valore 1 (il significato dipende dal tipo dato)
 *** Valore 2 (il significato dipende dal tipo dato)

Questo file viene copiato nell'IFS. Esistono appositi servizi che li elaborano.
