# CQS - Tipo strumento di misura
 :  : DEC T(ST) K(CQS)
## OBIETTIVO
Stabilire le relazioni di calcolo della classe di precisione.
Descrivere i rilievi definibili dall'utente, fissandone l'obbligatorietà e l'unità di misura.
## CONTENUTO DEI CAMPI
 :  : FLD T$SDQU **Tipo misurazione**
Descrive il tipo di misura che esegue lo strumento. È un campo controllato dalla tabella 'CQ*TM' (Tipo misura).
_9_Esempio
VA   Variabili
AT   Attributi
EN   Ente di controllo
 :  : FLD T$TPCO **Tipo controllo**
Campo controllato nella tabella 'CQ*VT' (Valori tipo strumento), stabilisce le modalità di calcolo della classe di precisione, in funzione delle quote rilevate. Può assumere i seguenti valori : 
A   non esegue il calcolo della classe di precisione.
T   esegue il calcolo della classe di precisione riferendosi solo al valore del fondoscala.
V   esegue il calcolo della classe di precisione riferendosi al valore dell'ampiezza della scala.
P   strumento certificato esternamente.
 :  : FLD T$DES1 **Descrizione 1/5**
Descrizione di 5 rilievi definibili dall'utente. Sono utilizzati nella gestione strumenti misura semplificata.
 :  : FLD T$CON1 **Tipo controllo 1/5**
Questo campo viene utilizzato nella gestione strumenti di misura semplificata. Il campo può assumere i valori : 
' '  Il rilievo è facoltativo
'O'  Il rilievo e la successiva dichiarazione vengono rese obbligatorie.
 :  : FLD T$MUN1 **Unità di misura 1/5**
Unità di misura del rilievo descritto nel campo libero 'Descrizione 1/5'. Anche questo campo viene utilizzato nella gestione strumenti di misura semplificata. Questo campo è controllato dalla tabella 'CQH' (Unità di misura).
 :  : FLD T$COMP **Strumento Composto**
Questo campo indica se lo strumento è composto da altri strumenti semplici. Il campo può assumere i valori : 
' '  Lo strumento è semplice
'X'  Lo strumento è composto.
