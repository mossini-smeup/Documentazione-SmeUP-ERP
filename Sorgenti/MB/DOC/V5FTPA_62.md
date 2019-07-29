# Risoluzione dei problemi

## Cosa controllare in caso di problemi di configurazione
* Se aprendo la scheda _Cruscotto Invio Fatture_ in alto compaiono le scritte in rosso vuol dire che la configurazione della FE presenta degli errori/warning.
* Dalla scheda _Cruscotto Invio Fatture_, verificare gli errori nel tab _Controlli   di Sistema.
** Errore su programa di invio :  controllare tabella V50, campo T$V50O "Pgm invio ft a SdI".
** Verifica Parametri di Comunicazione :  mancano gli elementi della tabella EDC, potrebbe non essere stato fatto girare il programma di allineamento V5UTX29.
** Controlli di congruenza :  Ambiente e elementi nella EDC non sono allineati. Se nella tabella B£2 è specificato "ambiente di test" e nella EDC ci sono elementi collegati allo smartkit, viene indicato un warning. E viceversa.
** Congruenza elementi EDC :  alcuni elementi della tabella EDC puntano al webservice reale, altri al webservice di test. Allineare le tabelle EDC.
** Controllo Provider :  controllare che lo smartkit specificato in V50 sia attivo e che le code dello smartkit siano attive nella libreria SMEUPUIDQ
** Controllo User e Password :  controllare la presenza dell'estensione £56 sull'azienda
** Controllo AooiD :  cliccare sul pulsante "Richiedi Aooid", dopo aver inserito user e password.

## Cosa controllare in caso di problemi di Richiesta AooiD
* Prima di tutto verificare che collegandosi sul sito https://ix.arxivar.it/  con le credenziali del cliente si riesca ad accedere
** poi verficare che sia attiva la sezione Elenco Aoos dopo essere entrati in "Vai al portale IXFE" (se non è presente l'elenco Aoos è probabile che non sia ancora stata ultimata l'attivazione del contratto da parte di Abletech)
* I problemi relativi alla richiesta AooiD sono per lo più relativi allo smartkit.
* Dalla scheda _Cruscotto Invio Fatture_, verificare nel tab _Scheda Provider_ nella scheda relativa ai LOA38 che l'albero non sia vuoto
* Qualora fosse vuoto occorre verificare che lo smartkit acceda ad un ambiente con in linea le modifiche della Fatturazione Elettronica.
* Controllare la presenza degli script LOA38_61 e LOA38_82 nel file SCP_SET in linea sull'ambiente in cui è avviato lo smartkit.
* In caso siano state fatte delle modifiche a programmi o tabelle potrebbe essere necessario riavviare lo smartkit. Contattare chi lo gestisce.
* Qualora non venissero caricati ancora correttamente il LOA38 controllare di aver riportato correttamente tutte le modifiche al membro EDT_SET (contenente i tag A38) nel file SCP_CFG .

## Cosa controllare in caso di errore nella creazione dell'XML
* Dalla scheda _Cruscotto Invio Fatture_, nel tab _Invio_ scegliere Tipo selezione "1"   (XML Errato).
* Nella matrice risultante, accanto a ciascuna fattura è presente l'icona di una lente, cliccando sulla quale viene aperta una scheda che mostra informazioni di dettaglio della fattura.
* Cliccando sull'icona della lente nelle righe con Nome tracciato EDFEIT08 è possibile consultare i log contententi errori e warning in merito alla fattura.
* Le stesse informazioni sono contenute in uno spool generato per ciascun lotto di estrazione.
* Qualora venisse generato un XML con più righe identiche, il problema potrebbe essere la mancanza del settore ED della tabella CRN, oppure del Numeratore della CRN ED £FEV6. In caso rilanciare il programma V5UTX29.

## Cosa controllare in caso di errore nell'invio
* Dalla scheda _Cruscotto Invio Fatture_, verificare quanto presente nel tab _Controlli   di Sistema.
* Controlli sulla singola fattura
** Dalla scheda _Cruscotto Invio Fatture_, nel tab _Invio_ scegliere Tipo selezione "4"   (Errore nell'invio).
** Nella matrice risultante, accanto a ciascuna fattura è presente l'icona di una lente, cliccando   sulla quale viene aperta una scheda che mostra informazioni di dettaglio della fattura.
** Cliccando sull'icona della lente nelle righe con Nome tracciato EDFEIT08 è possibile consultare   i log contententi errori e warning in merito alla fattura.
* Controllare i log di comunicazione con il webservice
** Dalla scheda _Cruscotto Invio Fatture_ , nel tab _Log integrazione con webservice_  consultare i log della £K11 verificando la presenza di messaggi di errore.
** In caso non siano presenti messaggi di errore è possibile attivare un log di maggior dettaglio   impostando il campo Log dell'elemento B£K11G della tabella PGM. In questo modo verrà loggato   tutto quello che viene ricevuto sulla coda dalla £K11 (consultabile dalla stessa interrogazione   del punto precedente). Ricordarsi di spegnere il log di dettaglio sulla tabella PGM quando non più necessario, in quanto comporta la scrittura di una notevole quantità di dati.
* Controlli Provider / Smart Kit
** Dalla scheda _Cruscotto Invio Fatture_, nel tab _Scheda provider_ controllare lo stato del provider nell'apposita voce di menù.
** Dalla scheda _Cruscotto Invio Fatture_, nel tab _Scheda provider_ controllare che la scheda del LOA38, selezionabile da menù, carichi correttamente lo script LOA38_61. Se non viene caricata controllare che sia in linea lo script SCP_SET/LOA38_61 e la versione aggiornata dello script SCP_CFG/EDT_SET (contenente i tag A38).
** Recuperare i log sulla macchina del Provider (dalla versione 1.0.9 dello Smart Kit è possibile scaricarli dalla pagina di debug (accessibile tramite http://ip provider/debug).
