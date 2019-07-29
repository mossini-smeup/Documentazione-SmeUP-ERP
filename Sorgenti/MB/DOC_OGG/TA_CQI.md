# CQI - Classi di importanza caratteristica
 :  : DEC T(ST) K(CQI)
## OBIETTIVO
Assegnare, in funzione dell'importanza della caratteristica da controllare, il livello L.Q.A. accettazione del lotto.
## CONTENUTO DEI CAMPI
 :  : FLD T$LQAP **Livello L.Q.A. Prop**.
Valore del Livello di Qualità Accettabile per la CLASSE della caratteristica in esame o percentuale massima di campioni non conformi, in accordo con la normativa UNI 4842-75
 :  : FLD T$LMIN **Valore Minimo Accettato**
Valore minimo di L.Q.A. che l'utente può utilizzare alla fase del ciclo di collaudo, assegnata per la classe della caratteristica.
 :  : FLD T$LMAX **Valore Massimo Accettato**
Valore massimo di L.Q.A. che l'utente può utilizzare alla fase del ciclo di collaudo, assegnata per la classe della caratteristica.
 :  : FLD T$RIPQ **Richiesta Azione su Lotto Successivo**
Campo forzatura 'Azione su Lotto Successivo' al lotto in cui è stata rilevata la non conformità.
' '  Non esegue nessun collegamento per la dichiarazione o la modifica dell'azione da eseguire sul successivo lotto in consegna.
'X'  Al termine della dichiarazione dei dati contenuti nella Gestione dei non Conformi, si collega al Lotto, nella 'Gestione Lotti', in modo da permettere la dichiarazione o la modifica della definizione delle azioni da eseguire sulla consegna successiva.
