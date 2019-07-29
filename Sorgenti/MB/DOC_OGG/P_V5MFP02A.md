# Distribuzione a rientro da C/Lavoro
Il programma disitribuisce i colli dichiarati in ingresso su : 

- colli in giacenza dal terzista
- ordini di produzione
- ordini di conto lavoro


In questo modo le righe del documento entrata merci vengono adeguate alla  movimentazione da eseguire.

Le righe ricevute vengono portate a livello/stato 9/90, e vengono create tante nuove righe quante quelle derivate dalla distribuzione.

Nella tabella di lancio B£JXX è ncessario impostare nel campo "param.aggiuntivi" : 
 * Tipo documento ordini C/lavoro
 * Forma presentazione C/lavoro Fase
 * Suffisso pgm calcolo priorità ordini
 * Suffisso pgm calcolo priorità giacenza
 * Suffisso pgm calcolo priorità distribuzione
 * SS.B£J passi tipi righe
 * B£J Tipo riga 1
 * B£J Tipo riga 2
 * B£J Tipo riga 3
 * B£J Tipo riga 4
 * B£J Tipo riga 5
 * B£J Tipo riga 6
 * B£J Tipo riga 7
 * B£J Tipo riga 8
 * B£J Tipo riga 9

Il programma può trattare nello stesso documento tipologie diverse di fornitura, per questo deve avere delle associazioni tra i tipi riga scritti in precedenza con il flusso R/F e i controlli e le righe che dovrà eseguire/generare nella fase di distribuzione, questi abbinamenti vengono impostati attraverso altri elementi di tabella B£J presenti in un proprio sottosettore, nel parametro esteso si questo elemento è indicato il sottosettore e gli elementi di B£J da utilizzare internamente all'elaborazione. Per ogni elemento della B£J tipo riga è necessario impostare i suoi paramentri aggiuntivi sul pgm "V5MFP02B".

## Funzione/Metodo nella tabella di lancio B£J_XX
 * Funzione
 ** 'CIE' = Cieca. No Visualizzazione. No Richiesta conferma
 ** 'CNF' = Conferma. No Visualizzazione. Si Richiesta conferma
 ** 'blanks' = Visualizz. Si Visualizzazione. Si Richiesta conferma

### Formato lista
Se la funzione non è in modalità "CIE" il sistema presenta nella lista segente il dettagli dell'elaborazione (righe origine, ordini ci C/Lavoro, giacenza c/o terzista, risultato della distribuzione) : 
![P5PMFP_61](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP02A/P5PMFP_61.png)![P5PMFP_62](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP02A/P5PMFP_62.png)### Opzioni della lista
Nella lista sono possibile le seguenti opzioni : 
![P5PMFP_63](http://localhost:3000/immagini/MBDOC_OGG-P_V5MFP02A/P5PMFP_63.png)