# UI1 - Main User Interface
## OBIETTIVI
Definisce i parametri generali relativi all'esecuzione di Looc.up.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$UI1A __Ambiente__
 :  : FLD T$UI1B __Coda lavoro__
Coda lavori in cui vengono immessi i lavori di Looc.up.
 :  : FLD T$UI1C __Timeout code (sec.)__
Mediante questo campo è possibile impostare il tempo di attesa di ricezione dati dopo il quale viene considerata
persa la connessione con il client.
Valori possibili : 
- ' ' :  timeout di 500 secondi
- 'A' :  timeout di 120 secondi
- 'B' :  timeout di 2000 secondi
- 'C' :  timeout di 30000 secondi
- 'D' :  timeout infinito (no timeout)
 :  : FLD T$UI1D __Modo Emulatore__
Mediante questo campo è possibile attivare le funzionalità avanzate di emulazione quali : 
- £G08 in formato scheda
 :  : FLD T$UI1E __Exit JACFG1__
Se si desidera utilizzare un programma particolare di caricamento per le configurazioni iniziali
di LoocUp,è possibile specificare il suffisso del programma da richiamare.
Viene lanciato il programma di aggiustamento 'JACFG1_x'. Per maggiori informazione sulla modalità
di utilizzo del programma,leggere le note riportate nel sorgente del programma prototipo (JACFG1_x).
 :  : FLD T$UI1H __Chiusura Job Emulat.__
