# Oggetti J1 FIL_SIF
## Significato
L'acronimo SIF sta per Smeup Index File e rappresentano dei file residenti su PC, quindi il codice coincide con un percorso file.
## Cosa sono
Il file SIF è a tutti gli effetti un file Xml con un formato compatibile agli Xml prodotti da Smeup per la documentazione.
### Il contenuto
L'Xml contenuto è in tutto e per tutto quello prodotto dai servizi come il B£SER_22. Tale servizio produce infatti l'xml compatibile con in motori di tarttamento della documentazione in Loocup.
Il file SIF rappresenta contiene tale Xml a cui sono stati tolti i dati all'interno del CDATA nel nodo contenuto ed al cui interno è stato messo il riferimento al file in cui tali dati sono stati riversati.
All'interno del file SIF quindi restano le informazioni relative alla funzione (nodo Service) ed i vari Setup.
### L'utilizzo
Il file SIF può essere processato tramite la funzione F(INT;JA_00_00;XML.RUN)1(J1;PATHFILE;PATH_TO_SIF). Si rimanda alla documentazione del servizio JA_00_00 per maggiori informazioni

