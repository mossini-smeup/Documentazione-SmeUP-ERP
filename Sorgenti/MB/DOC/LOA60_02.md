Attraverso i seguenti parametri vengomo lette le fonti della reportistica permettono la generazione delle notifiche.
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
| Cos|||Costruttore|02=Reportistica |
| Par|||Parameteri del costruttotre|Contiene tutti i parametri del costruttore |
| Par|A15||Nome fonte|Nome fonte da analizzare |
| Par|Res||Responsabile|E' ammessa la notifica ad un solo responsabile |
| Par|Res|<valore>|Valore fisso|Scrivendo un valore fisso di responsabilità |
| Par|Res|<OAV>|Attributo|Attraverso un attributo eseguito sull'oggettoi applicativo |
| Par|Ore||Campo di oggetto|Tipo e parametro dell oggetto applicativo su cui eseguire l'oav del responsabile derivandolo dal campo di database |
| Par|Kre||Campo di codice oggetto|Codice dell oggetto applicativo su cui eseguire l'oav del responsabile derivandolo dal campo di database |
| Par|Whr||Where|Permette di selezionare i soli oggetti inerenti alla notifica |
|  |
| Il dettaglio della notifica è statico, essendo la reportistica stessa. |
| 