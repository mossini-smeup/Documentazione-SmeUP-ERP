 :  : HEA RESP(TA) STAT(10)
# OBIETTIVO
Attraverso questo servizio è possibile lanciare le elaborazioni previste relative ai colli. Esse
si articolano nel seguente modo : 
## PCK Packing List
Funzioni relative alla packing list
### . LIS - Richieste
Elenco dei colli collegati ad una richiesta di movimentazione, un documento o un viaggio.
### . PRE - Lista di preparazione
Dettaglio della lista di preparazione colli di una richiesa di movimentazione, un documento o un
viaggio
 :  : PRO.SER Cod="PCK.LIS.1" Tit="Packing List. Lista Colli" Fun="F(EXB;GMSER_06;PCK.LIS) 1(DM;;-(O;;DM;))"

 :  : PRO.SER Cod="PCK.PRE.2" Tit="Packing List. Lista Preparazione" Fun="F(EXB;GMSER_06;PCK.PRE)" Ref="PCK.LIS.1"

