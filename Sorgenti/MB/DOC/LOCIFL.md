# Obiettivo
L'obiettivo del componente IFL è consentire l'esecuzione di flusso, cioè una serie di funzioni in modo sequenziale.
IFL è il componente supportato da Web.UP. In Looc.UP IFL viene deviato automanticamente sul componente FLU.
Il componente riceve un xml di albero ed esegue le funzioni presenti nella proprietà Exec di ciascun nodo, nell'ordine in cui i nodi sono emessi.
Un flusso può essere nidificato :  è possibile indicare tra le funzioni da eseguire una funzione con componente IFL che a sua volta restituisce un ulteriore flusso tramite un albero di funzioni.
Questo consente quindi di ottenere un flusso dinamico, eseguendo una prima funzione e poi richiamando una seconda funzione con  componente IFL che valuta cosa fare e restituisce la funzione successiva.
