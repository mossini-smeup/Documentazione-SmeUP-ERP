# JA1 - Parametri java
## OBIETTIVO
Permettere la personalizzazione del collegamento a JAVA
## CONTENUTO DEI CAMPI
 :  : FLD T$JA1A __Utente default__
Si imposta il profilo utente che verrà utilizzato all'atto della connessione da JAVA. È opportuno creare un utente apposito, con le seguenti caratteristiche : 
_7_INLMNU(*SIGNOFF)
PWDEXPITV(*NOMAX)
INLPGM(*NONE)
In questo modo si impedisce che questo utente possa collegarsi dalla mappa di collegamento. Inoltre la password non ha scadenza, quindi essa non segue l'impostazione della variazione della password definita a livello di sistema.
**IMPORTANTE** :  Questo Utente viene utilizzato come utente FTP di AS400 nella funzione FTP dello SMENS (£G53).
In particolare è indispensabile per la fase di creazione cubi (CUBE_UP)
 :  : FLD T$JA1B __Password__
È la password dell'utente definito in precedenza, utilizzata anch'essa all'atto della connessione da JAVA. Per ragioni di riservatezza, è presentata non visualizzata.
 :  : FLD T$JA1C __Log comunicazioni JA__
Consente di scrivere un log delle varie comunicazioni effettuate, mediante l'uso della routine £jac. I valori possibili sono : 
- ' ' nessuna registrazione di log;
- '1' viene registrato un evento per ogni chiamata all'AS400;
- '2' Vengono aggiornati i campi della tabella jau con delle informazioni riguardanti i collegamenti;
- '3' entrambe le opzioni '1' '2' contemporaneamente.
 :  : FLD T$JA1F __Attivazione LOG__
Se impostato, attiva la gestione della scrittura log per la comunicazione Looc.UP / Web.UP
Sono previsti i seguenti valori : 
' ' = Nessun log attivo
'1' = Log attivo in base a quanto definito in tabella JAL
'2' = Attivo solo per errori
'3' = Attivo per info collegamento ed errori
'9' = Attivo per tutte le info
 :  : FLD T$JA1H __Password protezione PDF con £G53__
Se impostata, viene utilizzata come password master di default nella protezione dei PDF creati con la £G53.
Viene sostituita solo se gestita a livello di creazione del singolo documento (£G53MP).
 :  : FLD T$JA1I __Path Specifico £G53__
Questo è il campo che definisce la cartella dell'IFS da cui vengono eseguiti lo Smens e lo Smedg.
Se tale campo è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/Smeup**
Se tale campo non è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/xxxxx/Smeup**
dove xxxxx è il contenuto del campo.
 :  : FLD T$JA1J __Exit JAJAC0_SM (SV)__
Questo campo permette di impostare il suffisso del programma di exit del JAJAC0_SM.
Il nome del programma di exit sarà JAJAC0_SM + il suffisso.
