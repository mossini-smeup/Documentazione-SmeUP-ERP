## Oggetti remoti

In uno script di Oggetti remoti dovrà essere presente : 
- una sezione SEZ Cod="LIS"
- una sezione SEZ Cod="DEC"
- nessuna, una o più sezioni SEZ Cod="OAV" nel caso in cui si vogliano definire OAV remoti di oggetti remoti

Per la definizione degli OAV remoti si rimanda alla seguente documentazione : 
- [OAV remoti](Sorgenti/MB/DOC/WSREOB_02)

Questo è un estratto dello script dell'oggetto remoto V5GDR (File di Google Drive).

 :  : SEZ Cod="LIS"
 :  : AUT Sub="GO.A01.001" Var="Content-Type(application/x-www-form-urlencoded)" Pay="client_secret=xxx&grant_type=refresh_token&refresh_token=xxxx" Ind="access_token" Ind="access_token"

 :  : DAT Sub="GO.A07.001" Var="Authorization(Bearer &AUT) Accept(application/json) IdFolder(xxx)"
 :  : COD Ind="files(*)\id" Hsh="1"
 :  : DES Ind="files(*)\name"

 :  : SEZ Cod="DEC"
 :  : AUT Sub="GO.A01.001" Var="Content-Type(application/x-www-form-urlencoded)" Pay="client_secret=xxx&grant_type=refresh_token&refresh_token=xxxx" Ind="access_token" Ind="access_token"

 :  : DAT Sub="GO.A03.001" Var="Authorization(Bearer &AUT) Accept(application/json) FileId(&CO.CD) Hsh="FileId"
 :  : COD Ind="id" Hsh="1"
 :  : DES Ind="name"

La sezione Cod="LIS" indica come recuperare la lista delle istanze degli oggetti remoti.
La sezione Cod="DEC" indica come recuperare la DEC di un singolo oggetto remoto.

Entrambe le sezioni necessitano di un tag  :  : DAT nel quale sono scritte le configurazioni del webservice da interrogare. Tramite l'attributo Var è possibile passare variabili al webservice. Se il webservice necessita di autenticazione è necessario aggiungere un tag  :  : AUT. Il relativo token ottenuto potrà essere utilizzato nello script attraverso la variabile &AUT.

I tag  :  : COD e  :  : DES indicano rispettivamente come recuperare dal json restituito dal webservice il valore di codice e descrizione dell'oggetto.

Il tag Hsh è utile quando l'identificativo dell'oggetto nel webservice esterno ha una lunghezza maggiore di 15. In questo caso viene codificato con un hash. La variabile &CO.CD viene comunque de-hashizzata e quindi il codice è ripristinato ad una lunghezza maggiore di 15 nella chiamata al webservice di DEC.






