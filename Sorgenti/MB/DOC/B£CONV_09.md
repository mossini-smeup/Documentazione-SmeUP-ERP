## Importazione File Excel

### Importazione File Excel

L'importazione di dati presenti all'interno di fogli excel e la scrittura di file fisici con i dati presenti all'interno di questi file è facilitata dall'utilizzo della scheda dell'oggetto File Excel.
Per richiamarla è sufficiente indicare come Tipo oggetto J1, Parametro FIL_XLS e quindi indicare nel campo XLS files il percorso del file da importare : 
![B£CONV_001](http://localhost:3000/immagini/B£CONV_09/BXCONV_001.png)La scheda del file riporterà nella prima sezione di sinistra l'elenco dei fogli presenti all'interno del file excel; selezionando il foglio di interesse il suo contenuto verrà visualizzato nella sezione di sinistra : 
![B£CONV_002](http://localhost:3000/immagini/B£CONV_09/BXCONV_002.png)![B£CONV_003](http://localhost:3000/immagini/B£CONV_09/BXCONV_003.png)Cliccando sul pulsante 'Esportazione' verrà richiesta la libreria all'interno della quale importare il file. Il default presentato è la libreria *USER : 
![B£CONV_004](http://localhost:3000/immagini/B£CONV_09/BXCONV_004.png)Confermando la libreria verrà eseguita l'importazione dei dati al cui termine verrà emesso un messaggio di conferma : 
![B£CONV_005](http://localhost:3000/immagini/B£CONV_09/BXCONV_005.png)L'esportazione genera all'interno della libreria indicata un file e un membro entrambi con nome corrispondente al nome del foglio importato. Quindi nel nostro esempio avremo file Foglio1 e membro Foglio1.
Il tracciato del file sarà determinato in funzione dell'intestazione e del contenuto delle colonne. In particolare, le colonne che all'interno del fiel excel contengono numeri verranno tradotte in campi numerici di lunghezza 15 mentre le altre colonne verranno tradotte in file alfanumerici di lunghezza 255 : 
![B£CONV_006](http://localhost:3000/immagini/B£CONV_09/BXCONV_006.png)Ottenuto il file sarà possibile inserirne i record all'interno di un altro file del database attraverso un'istruzione di INSERT.
Si riporta a titolo di esempio l'istruzione utilizzata nel caso in esame : 

 :  : PAR F(03)
INSERT INTO **LIB/brenti0f**
 (**E§TRAG**, **E§CRAG**, **E§IDOJ**, **E§GRUP,**E§RAGS**, **E§INDI**, **E§INDA**, **E§TELE**, **E§TFAX**, **E§TELX**, **E§IEMA**, **E§PECO**, **E§CNAZ**, **E§LOCA**, **E§PROV**, **E§CAPA**, **E§LING**, **E§VALU**, **E§TSOG**, **E§CPAI**, **E§COFI**, **E§CTA1**)
select
  substr ( **EXTRAG**, 1, 3),
  substr (DIGITS( **EXCRAG**), 7, 4),
  substr(DIGITS( **EXIDOJ**), 1, 10),
  substr ( **EXGRUP**, 1, 3),
  substr ( **EXRAGS**, 1, 35),
  substr ( **EXINDI**, 1, 35),
  substr ( **EXINDA**, 1, 35),
  substr ( **EXTELE**, 1, 20),
  substr ( **EXTFAX**, 1, 20),
  substr ( **EXTELX**, 1, 20),
  substr ( **EXIEMA**, 1, 132),
  substr ( **EXPECO**, 1, 20),
  substr ( **EXCNAZ**, 1, 6),
  substr ( **EXLOCA**, 1, 35),
  substr ( **EXPROV**, 1, 10),
  substr(DIGITS( **EXCAPA**), 6, 5),
  substr ( **EXLING**, 1, 2),
  substr ( **EXVALU**, 1, 3),
  substr ( **EXTSOG**, 1, 1),
  substr ( **EXCPAI**, 1, 30),
  substr ( **EXCOFI**, 1, 20),
  substr(DIGITS( **EXCTA1**), 9, 2)
from  **W_BSI/FOGLIO1**
where  **EXTRAG**<>' '

