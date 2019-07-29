# DIP - Dipendente
## OBIETTIVO
Definire in maniera univoca e sistematica la "codifica e la descrizione" del personale.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$SCOL Scolarità
è un campo tabellato CQ*DC che permette di indicare il livello di scolarità del dipendente che costituisce la principale discriminante nell'assegnazione dell'impiego e del trattamento economico (diplomato ragioniere, diplomato perito industriale, laureato in Economia e Commercio, laureato in Ingegneria ecc.)
 :  : FLD T$LING Lingua straniera
è un campo tabellato CQ*DF che stabilisce se in funzione della conoscenza linguistica si può decidere di assegnare al dipendente ruoli che comportano relazioni con l'estero
 :  : FLD T$AREA Area di provenienza
è un campo tabellato CQ*DG che consente di indicare da che area di provenienza (cementizio, manifatturiero, meccanico, servizi ecc) deriva il dipendente assunto. Anche questo dato contribuisce ad individuare il tipo di impiego più consono alle caratteristiche del dipendente
 :  : FLD T$QUAL Qualifica precedente
è un campo tabellato CQ*DH che indica il livello di qualifica raggiunto dal dipendente nelle occupazioni precedenti (apprendista, funzionario, dirigente impiegato, operaio, quadro ecc.)
 :  : FLD T$TIDI Posizione precedente
è un campo tabellato CQ*DA che specifica quale ruolo è stato svolto dal dipendente in occupazioni precedenti (collaudatore, progettista, contabile, programmatore software ecc.)
 :  : FLD T$REDI Reparto
(Archivio) Individua il settore, la Funzione a cui è stato assegnato il dipendente in base alle referenze emerse dalle caratteristiche precedenti
 :  : FLD T$STAT Stato di assunzione
è un campo tabellato CQ*DI che indica la condizione in cui si trova il dipendente al momento (dimesso, in forza, licenziato, pensionato ecc)
