# CSJ - Azioni eseguibili da interrog.
 :  : DEC T(ST) K(CSJ)
## OBIETTIVO
Permettere all'utente di definire e/o attivare le azioni che possono essere eseguite a fronte, quando si presenta la richiesta azione nel formato di visualizzazione dei costi.
## CARATTERISTICHE
Le azioni che possono essere richiamate possono essere di due tipi : 
1.   Modalità di aggregazione e/o confronto di dati.
2.   Accesso ad altre funzioni / programmi.
All'installazione, la tabella contiene i valori di base e può essere modificata e/o integrata dall'utente.
## CONTENUTO DEI CAMPI
 :  : FLD T$CJFS **Forma di sintesi**
La presenza di questo campo indica trattarsi della condizione.
1. Il valore immesso può esistere nella tabella CSS. Se non è presente in tale tabella, dovrebbe essere una delle forme di sintesi standard implicite nell'applicazione.
 :  : FLD T$CJNP **Nome del programma da richiamare**
La presenza di questo campo indica trattarsi della condizione.
2. Alcuni programmi sono forniti con l'applicazione, altri potrebbero essere scritti dall'utente.
 :  : FLD T$CJP1 **Parametro 1/2**
- A. Se programma
Specifica eventuali parametri che devono essere passati come condizionamento al programma chiamato.
- B. Se forma di sintesi
Parametro 1 = PRO indica che i valori devono essere rappresentati nella forma progressiva.
Parametro 2 = PRO indica che le percentuali devono essere rappresentati nella forma progressiva.
 :  : FLD T$CJP2.T$CJP2 Parametro 1/2
