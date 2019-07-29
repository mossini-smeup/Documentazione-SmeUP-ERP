Per la consultazione utilizzare il **"Set and play"** relativo al modulo.

## Note specifiche per tabelle

### Numeratori
Al numeratore definito dalla tabella CRNBR, si aggiungono i numeratori del protocollo delle lettere ricevute/emesse che hanno un codice dinamico costruito nel seguente modo : 
"NR1."+anno+"."+azienda per le emesse
"NR2."+anno+"."+azienda per le ricevute.
Per maggiori dettagli vedere s'n'p dei numeratori contabili.

 :  : INI   Set'n play numeratori contabili
 :  : CMD CALL C5N000G PARM('OF' 'O I' 'AZ')
 :  : FIN

### Parametri azienda

Indicare il contenitore note delle dichiarazioni e natura giuridica dell'azienda ed i riferimenti del rappresentante legale

 :  : INI   Anagrafica azienda
 :  : CMD CALL BREN01G PARM('AZI')
 :  : FIN
