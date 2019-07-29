## OBIETTIVO
 :  : FIG

Tracciare le azioni applicative eseguire da un utente in ambiente grafico.

## ATTIVAZIONE

Questo log è sempre attivo.

NOTA BENE :  esiste anche un log di cronologia tecnica, gestita dal client. Con questo log, il client traccia tutte le funzioni eseguite dal client. Rispetto alla cronologia che è presa in considerazione in questo documento, sussistono queste differenze : 
* La cronologia client, salva puramente la funzione, senza informazioni aggiuntive. Non prevede quindi, il salvataggio di una descrizione del client e non prevede alcuna icona
* La cronologia client, traccia tutte le funzioni eseguite dal client, mentre questa salva solo le funzioni che hanno un significato applicativo/operativo per l'utente (le varie forme di menù, le azioni di popup, le azioni lanciate dalla barra comandi, dai preferiti e dalla cronologia stessa)
* La cronologia client, viene salvata sul pc del singolo utente, mentre questa salva i dati sul server e permette quindi anche di interrogare i dati di tutti gli utenti

## GESTIONE DATI DEL LOG

I dati della cronologia, letti e gestiti attraverso la /COPY £K08. Tramite essai i dati vengono salvati nel file B£MEDE con queste chiavi : 
* METIPA :  'CRONO'
* MECODI :  Codice Ambiente
* MECOD1 :  Utente
* MECOD2 :  Data
* MECOD3 :  Ora

Nel campo MEDATI vengono salvati : 
* Nei primi 50 caratteri, il codice dell'icona (se previsto)
* Nei successivi 256 caratteri, sono dedicati alla descrizione dell'azione
* Tutti i caratteri restanti sono dedicati alla memorizzazione della funzione tracciata.

## DURATA DEI LOG

I log vengono mantenuti per 15 giorni. I dati precedenti vengono cancellati al primo accesso giornaliero da parte dell'utente.
