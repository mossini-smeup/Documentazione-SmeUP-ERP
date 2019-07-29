# Componente Spotlight

## Abstract

Lo spotlight è un componente grafico che permette di gestire la digitazione di una stringa di caratteri che può poi essere utilizzata al fine di scatenare una certa funzionalità.


## Funzionalità
- [Eseguire comandi o ricerche](Sorgenti/MB/DOC/LOCSPL_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCSPL_F02)
- [Suggerimenti](Sorgenti/MB/DOC/LOCSPL_F03)
- [Personalizzazioni grafiche](Sorgenti/MB/DOC/LOCSPL_F04)

## Introduzione
Lo spotlight è un componente grafico che permette di gestire la digitazione di una stringa di caratteri che può poi essere utilizzata al fine di scatenare una certa funzionalità.
I due usi più tipici sono l'esecuzione di un comando o l'impostazione di un filtro testuale, ma nulla vieta altri utilizzi.

E' importante notare che se non viene specificato alcuni dinamismo la sezione spotlight applicherà la stringa indicata ai comandi previsti dal sezione fissa in alto alla schermata (si veda il sorgente ALIAS di SCP_CLO ed i suoi utilizzi).

Le funzionalità si possono poi scatenare al semplice invio o tramite visualizzazione di bottoni specifici.

A tale stringa possono agganciarsi funzionalità di questo tipo : 
* Un testo watermark che dia indicazione di cosa può scrivere
* Un testo precompilato

## Formato dati
Tipo di XML utilizzato :  Xml di matrice.

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.SPL))) L(1)

## Schede di esempio
Gli esempi del componente spotlight sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

