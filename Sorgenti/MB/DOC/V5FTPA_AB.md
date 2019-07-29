# Note su Webservice Abletech

## Link per il test delle API

Ambiente Reale
https://ixapi.arxivar.it/Invoice/swagger/ui/index-!

Ambiente Test
https://ixapidemo.arxivar.it/Invoice/swagger/ui/index-!

## Script LOA38
Gli script LOA38 impiegati per la comunicazione con albletech sono : 
* LOA38_61 per servizi generali e di invio
* LOA38_82 per l'aggiornamento degli esiti delle fatture (notifiche)

## Utility per ottenere token X-Authorization
In un ambiente in cui siano stati configurati correttamente i dati di accesso ad abletech (tramite l'estensione dei dati azienda £56), è possibile lanciare il pgm V5AB08, al fine di ottenere una stampa in cui viene riportato il token X-Authorization, valido in quel dato momento.

