
# Obiettivo

Gestire la produzione del file e dei modelli relativi alla comunicazione liquidazione periodica IVA.

# Parametri
 * Anno :  Indicare l'anno per il quale si vuole fare la comunicazione.
 * Trimestre :  indicare il trimestre per il quale si vuole fare la comunicazione.    Per chi esegue la liquidazione iva trimestralmente bisogna tenere conto : 
   ** i trimestrali "speciali" (distributori di carburante/autotrasportatori) con riferimento    alla comunicazione del quarto trimestre indicano "4" nel campo trimestre
   ** i trimestrali "normali" devono presentare la comunicazione anche per il quarto trimestre    indicando "5" nel campo trimestre
 * Liquidazione Gruppo :  da impostare qualora si stia facendo una liquidazione del gruppo.    In questo caso bisogna fare attenzione ad impostare correttamente il parametro aziendale che     indica l'elenco delle aziende di gruppo (parametro AAF).    (PREREQUISITO :  il file delle dichiarazioni C5CUNI deve essere in comune a tutti i sistemi)
 * Azione : 
 ** **Estrazione** :  permette di estrapolare i dati.       In particolare per le operazioni attive/passive verranno lette tutte le operazioni del periodo,    mentre per le altre voci verranno ripresi i valori stampati periodicamente in liquidazione.     Si sottolinea che non viene presa in considerazione la voce     LQ15 Variazioni di imposta Debiti.     Nel totale delle operazioni attive non va ricompreso l'ammontare degli acquisti     di beni/servizi assoggettati a reverse charge, annotati nel registro delle fatture emesse.     I campi invece non gestiti in fase di estrazione, ma che è possibile compilare manualmente     sono : 
     *** Subforniture :  contribuente che si è avvalso delle agevolazioni previste per i contratti        di subfornitura
     *** Eventi Eccezionali :  soggetti che hanno usufruito delle agevolazioni fiscali previste a         seguito di calamità naturali / eventi eccezionali
     *** Versamenti AUTO UE :  Vanno indicati i versamenti relativi all'imposta dovuta per la prima        cessione interna di veicoli in precedenza oggetto di acquisti intraUE.
     *** Altri casi non gestiti sono i contribuenti con contabilità separata e periodicità     diversa (sia mensile che trimestrale).
 ** **Manutenzione Manuale** :  mi permette di manutenere i dati estratti
 ** **Trasmissione e stampa modelli** :  mi permette di produrre il file da trasmettere all'agenzia delle entrate ed i modelli da conservare.

_2_NOTA BENE :  in ognuna delle azioni, premendo il tasto funzione F2 e successivamente il tasto funzione F1 è possibile accedere alla documentazione specifica della funzione.

