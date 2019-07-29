# CQF - Classi difetto
 :  : DEC T(ST) K(CQF)
## OBIETTIVO
Stabilire in funzione della classe di difetto il valore di demerito o parametro di danneggiamento che influenza l'indice di qualità del lotto.
## CONTENUTO DEI CAMPI
 :  : FLD T$CQFA **Valore difetto**
Valore che indica il livello di gravità del difetto. Deve essere inteso come un demerito :  più è alto, più è grave.
_9_Esempi : 
DIFETTO CRITICO
Difetto tale da portare al mancato funzionamento del prodotto o creare grossi rischi per il veicolo o l'impianto di installazione del cliente.
Può portare ad un rifiuto del prodotto da parte del cliente.
Valore di demerito elevato (100).
DIFETTO IMPORTANTE
Difetto tale da ridurre notevolmente la funzionalità del prodotto o creare un certo grado di rischio per il mezzo del cliente.
Difetto da riparare per un regolare funzionamento del prodotto.
Valore di demerito medio (50).
DIFETTO MINORE
Difetto tale da ridurre parzialmente la funzionalità del prodotto, pur non creando condizioni di rischio per il cliente o problemi di installazione.
Difetto che può richiedere interventi di riparazione e che, comunque, riduce la soddisfazione del cliente.
Valore di demerito basso (20).
DIFETTO SECONDARIO
Difetto tale da non incidere sulla funzionalità del prodotto :  non richiede riparazioni e non comporta rischi.
Questo difetto può comunque incidere negativamente sull'immagine dell'Azienda e sulle aspettative del cliente.
Valore di demerito molto basso (2).
 :  : FLD T$CQFB **Richiesta Azione Lotto Successivo**
Campo forzatura 'Azione su Lotto Successivo' al lotto in cui è stata rilevata la non conformità.
' '  Non esegue nessun collegamento per la dichiarazione o la modifica dell'azione, da eseguire sul successivo lotto in consegna.
'X'  Al termine della dichiarazione dei dati contenuti nella Gestione dei non Conformi si collega, nella 'Gestione Lotti', al Lotto in modo da permettere la dichiarazione o la modifica della definizione delle azioni da eseguire sulla consegna successiva.
