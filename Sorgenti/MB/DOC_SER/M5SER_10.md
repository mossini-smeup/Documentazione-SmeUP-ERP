 :  : HEA RESP(GR) STAT(15)
# OBIETTIVO
Questo servizio fornisce funzionalità per l'applicazione di massa di suggerimenti MRP da Looc.up.

# FUNZIONI
## Applicazione di una lista di suggerimenti (APP.LIS)
Riceve in ingresso una lista di suggerimenti, nella forma (sugg;sugg;sugg;...), di massimo 1800 elementi.
Per ogni suggerimento chiama un'azione standard (es. AP) oppure un programma/funzione/metodo specifico.

## Bottone applicazione suggerimento (BTN)
Restituisce un bottone (sensibile alle lingue) con la descrizione di un'azione di applicazione di suggerimento.

 :  : PRO.SER Cod="APP.L.1" Tit="Applicazione di una lista di suggeriment. " Fun="F(EMU;M5SER_10;APP.L) P( LIS(-(F;;;Lista di suggerimenti)) AZI(-(F;;;Azione di applicazione)) PGM(-(F;;;Programma da chiamare)) FUN(-(F;;;Funzione programma)) MET(-(F;;;Metodo programma)))"

 :  : PRO.SER Cod="BTN.2" Tit="Bottone descrizione azione. " Fun="F(TRE;M5SER_10;BTN) P( AZI(-(F;;;Azione di applicazione)))"

