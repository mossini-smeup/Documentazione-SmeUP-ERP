# Descrizione
Attualmente il sistema non supporta un driver specifico JDBC, ma si appoggia direttamente
a quello utilizzato dal componente database  :  : DEC T(TA) P(B£AMO) K(MUDBMS)
Ad un accesso diretto tramite JDBC sono da preferire le API specifiche dei plugin db.core,
db.syntax, in modo da garantire il corretto parsing delle istruzioni e alcune cache di
memoria (grafo metadati del database)
