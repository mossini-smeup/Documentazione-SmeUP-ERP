# Struttura movimenti magazzino a fronte di documenti
## Tipo movimento di magazzino (V2/GMTMO)
 * **PP**, prelievo pianificato (P5)
 * **VP**, versamento pianificato (P5)
 * **DO**, documento ciclo esterno (V5)
 * **PE**, prelievo esterno (V5)

I campi assumono il seguente significato : 
 * **PP**, prelievo pianificato (P5)
 ** __Tipo ordine 1__, tipo impegno (TA P5I)
 ** __Numero ordine 1__, numero ordine di produzione
 ** __Data ordine 1__, data previsto prelievo. Se "Scarico Visualizzato" mette data inizio ordine
 ** __Riga/Sequenza 1__, 4 (sequenza precedente) + 4 (sequenza successiva). Se modo "Scarico Visualizzato" (Scarico secondo distinta) non lo fa
 * **VP**, versamento pianificato (P5)
 ** __Tipo ordine 1__, blank
 ** __Numero ordine 1__, numero ordine di produzione
 ** __Data ordine 1__, data previsto versamento
 ** __Riga/Sequenza 1__, blank
 * **DO**, documento ciclo esterno (V5)
 ** __Tipo ordine 1__, tipo documento (TA V5D)
 ** __Numero ordine 1__, numero documento
 ** __Data ordine 1__, data prevista consegna
 ** __Riga/Sequenza 1__, numero riga documento (primi 4 caratteri)
 * **PE**, prelievo esterno (V5)
 ** __Tipo ordine 1__, tipo documento (TA V5D)
 ** __Numero ordine 1__, numero documento
 ** __Data ordine 1__, data previsto prelievo
 ** __Riga/Sequenza 1__, numero riga documento (primi 4 caratteri)
 ** __Operazione__, numero sequenza (primi 6 caratteri) dell'articolo (se articolo / fase)
