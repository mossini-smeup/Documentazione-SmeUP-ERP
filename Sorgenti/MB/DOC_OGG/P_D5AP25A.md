## Attività preliminari

- Controllare in modo preciso la corrispondenza tra causali e tipi movimento utilizzati negli incassi/pagamenti, verificando che ci sia corrispondenza fra descrizioni e tipi movimento. Se è necessario intervenire sulle causali è poi possibile utilizzare il pgm C5UT49A per adeguare i dati esistenti.
    HD*   - Confrontare parole descrizioni con relativi tipi movimento
    HD*     - Per tutte le causali legate a C5D con tipo movimento 05 / 06 vanno
    HD*       attribuite causali con tipo movimento 05 o 17
    HD*     - Per tutte le causali di perdita su crediti vanno attribuiti tipi movimento 08
    HD*     - Per tutte le causali di insoluto/protesto vanno attribuiti tipi movimento 04 / 09
    HD*     - Per tutte le causali di abbuono/sopravvenienze vanno attributi tipi movimento 06
    HD*     - Per tutte le causali di sconto finanziario vanno attributi tipi movimento 11
    HD*
    HD* - Liste conti interessi : 
    HD*   - Servono per identificare nelle fatture le contropartite relative all'addebito
    HD*     di interessi dovuti a ritardi di pagamento
    HD*
    HD* - Liste conti di sconto cassa : 
    HD*   - Servono per identificare nelle fatture le contropartite relative all'applicazione
    HD*     di sconti di in fattura
