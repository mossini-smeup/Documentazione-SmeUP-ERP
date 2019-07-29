# V§N - Nazioni codici ISO / tabella A
 :  : DEC T(ST) K(V§N)
## OBIETTIVO
Lo scopo della V§N è quello di dare una tabella standard che contenga tutti i codici ISO. Lo
scopo è quello di non creare dubbi nella scelta della nazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
Elemento che indica il Codice ISO delle Nazioni. È lo standard internazionale. Utilizzare il codice ISO 3166 a 2 caratteri.
 :  : FLD T$DESC Definizione
Campo descrittivo della Nazione .
 :  : FLD T§V§NA __Codice ISO (3)__
È il codice ISO 3166 che utuilizza 3 caratteri.
Per ogni codice alfanumerico di 2 caratteri della nazione, corrisponde il relativo codice numerico lungo 3.
_9_Esempio :  AD Andorra - 020 , AM Armenia - 051, .. ecc..
 :  : FLD T$V§NB __Aggregazione di Appartenenza__
Campo che definisce l'appartenenza della nazione in esame, al gruppo così definito : 
"_7_C" - Paesi appartenenti alla CEE; serve per attivare il controllo della Partita Iva così definita  :  Cod.ISO Nazione + blanks + Partita Iva (esempio)  DE 14256789524.
"_7_I" - Italia.
"_7_O" - Paesi appartenenti all'OCSE.
"_7_R" - Resto del mondo.
Tutti gli elementi in aggiunta devono essere gestiti
 :  : FLD T$V§NC __Codici se Nazione CEE__
Elemento della tabella V§*IA , utilizzato solo nel caso in cui sia necessario codificare un codice diverso da quello ISO per una nazione CEE.
 :  : FLD T$V§ND __Codice Comune Capitale__
Indica il C.A.P. della Nazione.
 :  : FLD T$V§NE __Prefisso telefonico Nazione__
Indica il prefisso telefonico della Nazione (campo non controllato).
 :  : FLD T$V§NF __Codice Divisa__
Elemento della tabella V§*DI , indica il codice ISO per la codifica delle Divise.
 :  : FLD T$V§NG __Codice Corrispondente Esterno (NAZ)__
Elemento della tabella NAZ che chiude la congruenza tra le tabelle SMEUP V§N e NAZ con l'eventuale tab.NAZ dell'applicazione contabile (ACG,.. ... .). In questo caso la V§N deve contenere l'elemento della NAZ, la quale è deviata sulla contabilità.
 :  : FLD T$V§NN __Code page Client windows__
È la code page utilizzata nel trattamento dei flussi di dati verso i client, basati su sistema operativo Windows.
Viene utilizzato ad esempio durante il trasferimento dati mediante £PCT, gestito dagli stampatori di applicazione.
In particolare, gli stream file creati tramite le routine £PCT e £G80 verranno creati con la code page indicata in questo campo (se non specificata verrà utilizzata la code page del job). (Vedi anche campo Code pafe output).
 :  : FLD T$V§NJ __Code page IN/OUTput__
È la code page utilizzata nei campi "stringa" dei programmi. Le routine £PCT e £G80 utilizzeranno questa code page come code page delle stringhe che verranno scritte (o lette) da stream file.
Questo valore è necessario in quanto tutti i lavori di Sme_up utilizzano come CCSID predefinito il valore 280. Di conseguenza, se si utilizza Sme_up in una lingua diversa da quella italiana, eventuali caratteri non appartenenti alla serie di caratteri Latin I, non verrebbero convertiti correttamente. La code page specificata in questo campo permette di "forzare" una code page diversa da quella del job per le operazioni di scrittura/lettura, effettuate dalle due routine
precedenti. Se questo valore non è specificato verrà utilizzata la code page del job.
