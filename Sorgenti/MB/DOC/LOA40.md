## Obiettivo
 Importare in modo controllato dati su AS400 da un file esterno

## Variabili
Tutte le varibili sono definite nell script gestito nel set'n play
* "ImFlDr"  Driver file import, E'  il tipo di driver usato per l'import. Esistono 3 tipi di driver : 
** 01 Funzione Java
** 02 Specifico per biglitti da visita (file BSCARD)
** 03 con £G80 solo per file in IFS
* "ImFlCa" Cartella file origine, E' la cartella dove riesiedono i file da importare. Nella fase di import vengono presentati tutti i file della cartella e si può scegliere quale file importare.
* "ImFlFi" File origine. E' il file che si vuole imporare. Deve essere in formato CSV.
* "ImDaLi" Libreira dati. E' la libreria AS00 dove importare il file di WORK, Di defaut si assume "SMEUPWXX" dove XX è l'azienda
* "ImDaFi" File dati. E' il file di WORK dove viene importato il file origine. Di default si assume "IXX_YYYYYY" dove XX è "ImFlDr" e YYYYYY sono i primi 6 caratteri dell'utente AS400. Se si mette "*AUT" verrà attribuito un nome progressivo IXXYYZZKKK dove XX è lo script, YY la sezione, ZZ il gruppo e KKK un progressivo alfanumerico..
* "ImDaDr" Driver dati. E' il driver specifico di import dati. Gestisce l'import comtrollato dei dati nel gestionale. A stadard sono proposti una serie di driver per alcuni file tra i più importanti. Esempio "01" per il file BRARTI0F
* "ImDaAl" Alias Dati. E' un ON/OFF (ON  valore "1"). Ogni dato viene normalizzato dal suo alias
* "ImDaFl" Campi dati. E' possibile decidere quali campi far gestire al driver. I lfile origine potrebbe contenere colonne che non si vogliono aggiornare. In questo caso basta elencare le colonne separate dal carattere "|"
* "ImDaEx" Exit dati. E' una exit lanciata dal driver dove è possibile gestire eseigenze specifiche


## IMPORT FILE

il file esterno deve essere un formato CSV.
De essere nella cartella Smeup/XXYYYYY del proprio desktop, dove XX è l'oggetto e YYYYYY il parametro (Per esempio Smeup/AR articoli, Smeup/CNCLI Clienti)

Le colonne devono contenere il loro nome nella prima riga.  Il nome della colonna diventerà il nome del campo del tracciato record del file importato su AS400. Oltre al nome è possibile inidicare altre informazioni relative alla colonna :  oggetto, lunghezza. La nomenclatura deve essere la stessa che viene usata dagli export su excel da loocup :  Descrizione(NomeCampo|Oggetto|Lunghezza)

Nella scheda è possibile gestire i file nella relativa cartella.

E' necessario eseguire l'import del file su AS400.
L'import crea il file XXX_YYYYYY nella libreria SMEUPBI10, dove XXX è un valore fisso per ogni pgm specifico e YYYYYYY è l'utente AS400.
Per esempio ART_BELPAO è articoli dell'utente BELPAO, REF_LANSTE sono i referenti dell'utente LANSTE

PROBLEMI
Se definisco un campo NR l'import standard da CSV non mi carica i valori e mi trovo su aS400 la colonna con tutti "null".Ho dovuto definire il campo "**". Dove però ho poi problemi di controllo sull'oggetto
Da verificare quindi numeri. Da testare anche le date


## SIGNIFICATO COLONNE CAMPI
*Numero colonna, è il numero della colonna del file csv
*Nome, è il nome del campi del DBA a cui fa riferimento la cononna del fil CSV
*Intestazione, è descrizione della colonna
*Oggetto, è l'oggetto Smeup della colonna
*Oggetto dinamico, indica se l'oggetto è dinamico, in questo caso deve essere risolto nel programma specifico (routine NOR_CAM)
*Lunghezza, è la lungheza del campo della colonna
*Obbligatorio, indica se la colonna è obbilgatoria per poter eseguire una qualsiasi funzione
*Key risalita, indica in quale passo si risalita è stata trovato il record corripondente (esempio negli enti se non ho nel file origine il codice ma la p.iva e la ragione sociale, prima cerca se esiste con uente con la P.iva indicata, se non esiste prova con la ragione sociale)
*Key, indica i campi chiave
*Key immissione, indica i campi chave che non devono essere controllati in immissione
*Numero lotto, indica il campo che definisce una gestione di import per lotti
*Riga lotto. indica la riga di ordinamento all'interno all'interno dello stesso lotto

## AGGIORNAMENTO DATI

 I programmi di import gestiscono l'immissione o l'aggiornamento di un record in funzione della presenza del record di input sul gestionale
 Per gli aggiornamenti viene presentato il record attuale sul gestionale e segnalati tutti i campi in aggiornamento.
Per ogni campo viene eseguito il controllo dell'oggetto e segnalto l'ventuale errore.

E possibile eseguire l'azione di immissione/modifica per ongi singolo record o eseguire di massa su tutto il file

Per ogni campo di ciascuna riga è possibile caricare una serie di messaggi di errori. L'errore pu essere di riga e/o di lotto.
Solo gli errori di lotto inibiscono le azioni di immissione e/o aggiornamento
