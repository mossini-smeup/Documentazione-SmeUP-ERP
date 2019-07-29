# MMX - Stato impianto
## OBIETTIVO
Permettere di differenziare il comportamento, in funzione dello stato impianto. Se lo stato ha una X nel campo GESTIONE MANUTENZIONE, non vengono estratti gli interventi di quell'impianto con uguale stato
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC DESCRIZIONE
Descrizione del codice
 :  : FLD T$ELEM CODICE
Tipo di stato (es. attivo, obsoleto, sospeso...)
 :  : FLD T$GEST __GESTIONE MANUTENZIONE__
Con blank lascia estrarre gli interventi, con X non permette di estrarli.

