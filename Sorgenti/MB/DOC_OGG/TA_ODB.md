# ODB - Documentale COMPED
 :  : DEC T(ST) K(ODB)
## OBIETTIVO
Definisce i parametri generali relativi al Documentale COMPED.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
Rappresenta il nome del documentale
 :  : FLD T$ODBA
Codice del Server richiamato. Il codice viene assegnato negli script di configurazione di Loocup presenti nel file SCP_CLO
 :  : FLD T$ODBB
Utente di collegamento configurato nel Documentale
 :  : FLD T$ODBC
Password dell'utente sopraindicato (è case-sensitive)
 :  : FLD T$ODBD
E'la sorgente dati (Database Source Name) configurata. Ad esempio in Comped è il nome della sorgente dati residente su SQL Server su cui Comped ha costruito il suo database.
