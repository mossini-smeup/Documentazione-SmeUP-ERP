# CFV - Valori del configuratore
 :  : DEC T(ST) K(CFV)
## OBIETTIVO
Questa tabella è pensata per contenere i possibili valori di risposta di una domanda.
Quando definisco una domanda posso specificare nei campi "Filtro risposta" e "Parametro Filtro" rispettivamenten "TA" e "CFVxx". Così facendo l'utente che deve rispondere a questa domanda ha la possibilità di scegliere un elemento del sottosettore CFVxx.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM  **Codice**
Codice del valore
 :  : FLD T$DESC  **Descrizione**
Il valore della possibile risposta
 :  : FLD T$CFVA  **Regola validazione**
Per ora non gestito.
È pensato per inserire una regola che stabilisca se questo valore deve essere mostrato all'utente che compila il questionario oppure no.
