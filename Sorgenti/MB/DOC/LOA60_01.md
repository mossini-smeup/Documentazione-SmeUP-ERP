Attraverso i seguenti parametri viene costruito il comando SQL che permette la generazione delle notifiche.
Parametri : 
 :  : PAR L(TAB)

| .COL Txt="Key" |
| 
| .COL Txt="SubKey" |
| ---|----|
| 
| .COL Txt="Valori" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Nota" |
| Cos|||Costruttore|01=Comandi SQL |
| Par|||Parameteri del costruttotre|Contiene tutti i parametri del costruttore |
| Par|Ogg||Oggetto|Attraverso l'oggetto utilizzando l'api IVD viene costruito l'sql e identificato il campo di database in cui è contenuto l'oggetto applicativo |
| Par|Whr||Where|Permette di selezionare i soli oggetti inerenti alla notifica |
| Par|Res||Responsabile|E' ammessa la notifica ad un solo responsabile |
| Par|Res|<valore>|Valore fisso|Scrivendo un valore fisso di responsabilità |
| Par|Res|<OAV>|Attributo|Attraverso un attributo eseguito sull'oggettoi applicativo |
| Par|Fre||Campo di responmsabilita|Campo del file contenente il responsabile. |
| Par|Ore||Campo di oggetto|Tipo e parametro dell oggetto applicativo su cui eseguire l'oav del responsabile derivandolo dal campo di database |
| Par|Kre||Campo di codice oggetto|Codice dell oggetto applicativo su cui eseguire l'oav del responsabile derivandolo dal campo di database |
|  |
| Il dettaglio della notifica è dinamico esso verrà proposto utilizzando il comando SQL rigenerato al momento della richiesta. |
| 