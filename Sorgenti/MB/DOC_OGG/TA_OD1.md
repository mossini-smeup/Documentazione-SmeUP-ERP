# OD1 - Impostazioni base documentale
 :  : DEC T(ST) K(OD1)
## OBIETTIVO
Definisce i parametri generali relativi al Modulo Documentale.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$OD1A
E' il nome della coda di comunicazione con Loocup Server.
Per Invio si intende dal Server al Client.
La coda deve esistere nella libreria SMEUPUIDQ. Se non esiste è creata dinamicamente al primo richiamo al server Loocup
 :  : FLD T$OD1B
E' il nome della coda di comunicazione con Loocup Server. Client to server
Per Invio si intende dal Client al Server.
La coda deve esistere nella libreria SMEUPUIDQ. Se non esiste è creata dinamicamente al primo richiamo al server Loocup
 :  : FLD T$OD1C
E' il nome del Documentale su cui verranno archiviati i documenti
 :  : FLD T$OD1D
E' il tipo documento del documentale relativo alla fatturazione attiva
