# Trasferimenti giacenze negative MFP
Il programma, controlla le giacenze negative e cerca di pareggiarle, a parità di ubicazione/fase con giacenze positive di altri contenitori
### Formato di lancio
![P5PMFP_22](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP84/P5PMFP_22.png)La distribuzione può avvenire per : 
 * Ordine, si cerca di eseguire i bilanciamenti all'interno dello stesso ordine MFP
 * Articolo, i bilanciamenti avvengono indipendentemente dall'ordine
### Formato di lista
![P5PMFP_23](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP84/P5PMFP_23.png)In questo esempio il programma ha trovato due giacenze negative : 
 * contenitore C1100012, ubicazione CDL03_P, fase 0010, con una quantità negativa di 25
 ** la bilancia con il contenitore C1100010 che ha una giacenza positiva di 70; dopo il bilanciamento su questo contenitore resta un residuo positivo di 45
 * contenitore C1100012, ubicazione CDL03_P, fase 0040, con una quantità negativa di 50
 ** la bilancia con il contenitore C1100009 che ha una giacenza positiva di 17; dopo il bilanciamento il contenitore si azzera e su quello di partenza resta un residuo negativo di 33
 ** la bilancia con il contenitore C1100010 che ha una giacenza positiva di 17; dopo il bilanciamento il contenitore si azzera e su quello di partenza resta un residuo negativo di 16
 ** la bilancia con il contenitore C1100011 che ha una giacenza positiva di 71; dopo il bilanciamento su questo contenitore resta un residuo positivo di 55

Il comando funzione F6 esegue i bilanciamenti suggeriti.
Il comando funzione F17 permette di impostare il contenuto della lista.
