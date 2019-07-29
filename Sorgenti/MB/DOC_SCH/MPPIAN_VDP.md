# Scheda MPS Visualizzazione Vista Piano
Questa scheda è deputata all'analisi di una vista, appartente ad un piano, selezionata nella scheda MPPIAN di provenienza, sono possibili le seguenti azioni : 

 * _2_Sintesi dettaglio
 * _2_Contenuto dettaglio
 * _2_Modifica vista
 * _2_Statistiche della vista
 * _2_Comparazione
 * _2_Analisi nel tempo
 * _2_Analisi tabellare
 * _2_Analisi tabellare con periodo

## Sintesi dettaglio
Permette di andare alla scheda MPPIAN_RVP di gestione di una riga della vista piano. Quindi la prima sezione serve per selezionare Oggetto 1 e Oggetto 2 in modo da individuare la riga, di questa sezione sono possibili 2 visualizzazioni : 
 * _2_Standard, presenta in forma di matrice l'oggetto 1 e l'oggetto 2, ordinata per oggetto 1
 * _2_Completa, come la precedente ma raggruppata e totalizzata per oggetto 1

![MPPIAN_080](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_080.png)
## Contenuto dettaglio
Questa sezione presenta l'intero contenuto della vista piano con tutti i valori di tutti i periodi.

![MPPIAN_081](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_081.png)
## Modifica vista
Come la precedente ma in forma di matrice modificabile in modo da poter cambiare direttamente i valori (nota, la manutenzione è soggetta al controllo di autorizzazione per classe MPGP01 e funzione = vista piano come nella manutenzione vista piano dell'emulazione 5250).
In questa matrice sono predisposti diversi set-up di visualizzazione : 
 * _2_Standard
 * _2_Raggruppato per oggetto 1
 * _2_Raggruppato per oggetto 2

![MPPIAN_082](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_082.png)
## Statistiche della vista
Per ogni riga della vista presenta una serie di indici statistici : 
 * _2_Numero di elementi
 * _2_Totale
 * _2_Media
 * _2_Varianza
 * _2_Deviazione standard
 * _2_MAD (Mean Absolute Deviation)
 * _2_MSD (Mean Square Deviation)
 * _2_Numero di elementi diversi da zero
 * _2_Totale elementi diversi da zero
 * _2_Media elementi diversi da zero
 * _2_Varianza elementi diversi da zero
 * _2_Deviazione standard elementi diversi da zero
 * _2_MAD elementi diversi da zero
 * _2_MSD elementi diversi da zero
 * _2_Numero di elementi eliminando il massimo e il minimo
 * _2_Totale elementi eliminando il massimo e il minimo
 * _2_Media elementi eliminando il massimo e il minimo
 * _2_Varianza elementi eliminando il massimo e il minimo
 * _2_Deviazione standard elementi eliminando il massimo e il minimo
 * _2_MAD elementi eliminando il massimo e il minimo
 * _2_MSD elementi eliminando il massimo e il minimo
 * _2_Numero di elementi compresi tra stremi non zero
 * _2_Totale elementi compresi tra stremi non zero
 * _2_Media elementi compresi tra stremi non zero
 * _2_Varianza elementi compresi tra stremi non zero
 * _2_Deviazione standard elementi compresi tra stremi non zero
 * _2_MAD elementi compresi tra stremi non zero
 * _2_MSD elementi compresi tra stremi non zero
 * _2_Primo elemento non a zero
 * _2_Ultimo elemento non a zero
 * _2_Mediana
 * _2_% di errore, calcolata come (deviazione standard / media) * 100

![MPPIAN_083](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_083.png)
_3_Nota 1, selezionando le impostazioni di visualizzazione _2_Base o _2_Completa si possono vedere un set ridotto di indici oppure tutti

_3_Nota 2, per il significato e le formule di calcolo degli indici presentati fare riferimento alla documentazione della routine di calcolo funzioni matematiche £G56
- [Test statistiche](Sorgenti/MB/DOC_OGG/P_TSTG56)

## Comparazione
Permette di confrontare i dati della vista di partenza con un'altra vista, sono previste una comparazione in forma sintetica, una comparazione in forma estesa ed una manutenzione in matrice modificabile della vista con confronto con un'altra vista di riferimento.

![MPPIAN_084](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_084.png)
![MPPIAN_085](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_085.png)
![MPPIAN_086](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_086.png)
## Analisi nel tempo
Analizza i dati della vista piano attraverso il componente standard LOA02

![MPPIAN_087](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_087.png)
## Analisi tabellare
Analizza i dati della vista piano attraverso il componente standard LOA03

![MPPIAN_088](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_088.png)
## Analisi tabellare con periodo
Come la precedente con in più la possibilità di selezionare il periodo

![MPPIAN_089](http://localhost:3000/immagini/MBDOC_SCH-MPPIAN_VDP/MPPIAN_089.png)