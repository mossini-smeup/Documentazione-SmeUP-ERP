# Rientro MFP da C/Lavoro - controllo operazione
Il programma verifica se le righe del documento V5 del flusso hanno tutte la fase (la fase è necessaria per lo smistamento eseguito nel passo successivo del flusso) e, se manca cerca di aggiungerla.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "parametri aggiuntivi" : 
 * Tipo righe bolla
 * Tipo ordine
 * Tipo riga ordine

## Logica di elaborazione
Si scorrono tutte le righe del documento, vengono saltate le righe diverse dal "Tipo riga bolla" o che hanno già il campo fase valorizzato. Per le restanti viene cercata una riga ordine chje abbia : 
 * tipo documento / tipo riga da parametri aggiuntivi B£J
 * stesso fornitore della testata
 * livello attivo ("2")
 *quantità residua
Se si trova una sola riga ordine viene eseguito direttamente l'aggiornamento delle righe documento con la fase copiata dall'ordine, altrimenti viene proposta la lista di selezione dove la scelta è manuale.

### Formato di selezione
![P5PMFP_59](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP02Z/P5PMFP_59.png)
Con "X" si aggiorna la fase sulla riga

### Opzioni su lista
![P5PMFP_60](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP02Z/P5PMFP_60.png)