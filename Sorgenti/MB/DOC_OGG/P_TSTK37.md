
 # Obiettivo
 Leggere dati da un Json.

 # Prerequisiti
 Necessita di avere in linea la libreria specifica per il parsing Json, copyright di Scott C.  Klement. Per ulteriori dettagli vedere qui : 
- [Parsing Json](Sorgenti/MB/DOC/WSBASE_01)

 ## Funzione GET metodo ATR. Reperisci attributo.
 Permette di reperire il valore di un attributo.

 Nel campo £K37I_PF va impostato il percorso IFS dove è presente il file Json.

 Nel campo £K37I_PA va impostato il percorso dell'attributo da reperire in questa modalità : 
 Nodo1\Nodo2\Array1(7)\Nodo3\Array2(5)\Attributo
 Il separatore è il "\" e la differenza tra il nodo e l'elemento array è l'indice tra parentesi  quadre.

 In output nel campo £K37O_TA è presente il tipo di attributo : 
 S - Stringa
 B - Booleano
 N - Numerico
 * - null (indica il valore null per qualsiasi dei 3 tipi precedenti)

 Per il tipo Stringa e Booleano il valore verrà restituito nel campo £K37O_AL. Il campo £K37O_M5  puà contenere il valore CONT per indicare che il valore continua, è pertanto rieseguire l'API  con gli stessi parametri per avere il resto del valore, se invece il campo £K37O_MS contiene FINE  è stato letto tutto il valore.
 Per il tipo Numerico il valore verrà restituito nel campo £K37O_NU

 ## Funzione CLO. Chiudi json.
 Chiude il Json liberando l'area di memoria allocata. E' SEMPRE NECESSARIO eseguire questa funzione
 al termine dell'utilizzo di questa API per non lasciare impegnata memoria inutilmente.ù
