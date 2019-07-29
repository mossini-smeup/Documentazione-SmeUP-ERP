## SERVIZI AS400
Nel menù servizi è compresa la voce 'Servizi AS400', che comprende alcune funzionalità di accesso all'AS400 in forma grafica.
Tali funzionalità sono : 
 * Cambio password
 * Gestione stampanti
 * Spool di stampa
 * Lista lavori
 * Messaggi di sistema

Non avendo ancora una gestione delle stampe AS400 nativa di Looc.UP, temporanamente ci appoggiamo a questi tool grafici, che sono però nativi del Client Access (IBM iSeries Access per Windows).
L'installazione minimale è descritta in : 
 :  : DEC T(MB) P(DOC) K(LOBASE_12F)
Inoltre, per non incorrere in errori, è necessario ricostruire i seguenti presupposti : 
La versione del Client Access installata non può essere inferiore a quella dell'AS400.
__ Verificare questa condizione__
Andare in START, PROGRAMMI, IBM iSeries Access per Windows, Proprietà iSeries Access per Windows.
Nel caso sia inferiore sarà necessario aggiornarla. Per farlo è possibile utilizzare quella disponibile sull'AS400 in iSeries Navigator, File System, IFS, Root, QIBM, ProdData/CA400, Express, Install, Image, SETUP.EXE
(compatibile con la versione dell'OS400 installato, ma non è detto che sia l'ultima), oppure installare la versione più recente del Client Access.
L'ultima versione rilasciata (09/12/2005) è la V5R3M0 SP spSI20055.
L'ultima versione disponibile sul ns. server è V5R2M0 SP spSI18400.

Fare riferimento al sito IBM per ogni dettaglio : 
[http://www-03.ibm.com/servers/eserver/iseries/access/casp.html](http://www-03.ibm.com/servers/eserver/iseries/access/casp.html)
pagina dettagli)

__Verificare che sia installato l'AFP Workbench per Windows - Wiewer__
Andare in Start, Programmi, IBM iSeries Access per Windows, installazione selettiva :  verranno indicati tutti i prodotti Client Access installati.
Nel caso AFP Workbench per Windows - Wiewer vada comunque in errore nella visualizzazione di una stampa, scaricare l'ultima versione rilasciata dall'IBM (1.71.03.00) al sito FTP : 
 :  : DEC T(J1) P(PATHFILE) K(ftp : //ftp.software.ibm.com/as400/products/clientaccess/win32/afpviewer/ftd17103/) I(link per download)

##
