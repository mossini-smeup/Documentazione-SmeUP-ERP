
## Obiettivo
Il modulo A39 è un'intefaccia che permette di pubblicare webservice, pertanto è un costruttore che permette di rendere pubbliche delle funzioni Sme.UP, eseguibili dall'esterno.

Il costruttore A39 è costituto da 3 entità : 
* una scheda :  LOA39
* una servizio base :  LOA39_SE
* script SCP_SET specifici Sme.UP o utente :  LOA39_xx

## Funzionamento
Lo Sme.UP Provider tramite il servizio LOA39_SE, interpreta gli script di interfaccia alle funzioni Sme.UP attribuendo un nome al webservice, che identifica univocamente una funzione.

Negli script vengono definite le istanze della classe SESUB.A39 nel formato xx.yyy.zzz : 
* xx è il gruppo, corrisponde al nome dello script LOA39_xx
* yyy è la sezione definita all'interno dello script
* zzz è la subsezione definita all'interno dello script

All'interno dello script vengono pertanto indicate le funzioni pubblicate come web service e le relative variabili di input, che possono essere trasformate dal provider, come definito nella pre trasformazione. L'output restituito al provider è il risultato della funzione stessa e può essere dal provider trasformato come definito nella post trasformazione.

## Definizione nello script SCP_SET
Nel dettaglio questi sono i tag previsti nello script ed i relativi attributi principali : 


| 
| .COL Cod="COL001" Txt="Tag" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="Descrizione" LunAut="1" |
| SEZ       |nell'attributo Cod viene indicata la sezione |
| SUB       |nell'attributo Cod viene indicata la subsezione |
| A39.SUBMET|l'attributo Name indica il nome attribuito alla funzione |
| A39.SUBFUN|l'attributo Value contiene la funzione che deve essere eseguita |
| A39.PRETRS|l'attributo Value contiene la classe che si occupa della pre trasformazione |
| A39.PREVAR|l'attributo Name contiene la relativa variabile prevista e Value il relativo valore |
| A39.PSTTRS|l'attributo Value contiene la classe per si occupa della post trasformazione |
| A39.PSTVAR|l'attributo Name contiene la relativa variabile prevista e Value il relativo valore |
| 

E' infine possibile tramite il tag A39.VAR definire delle variabili di contesto G91 (&CO.xxx..).

## Autenticazione/Ambienti/Autorizzazioni

TODO
