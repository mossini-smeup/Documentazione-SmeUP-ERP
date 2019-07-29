# Componente IMD - Immagine Dinamica

Questo componente non ha interfaccia grafica :  si tratta di un componente che genera un'immagine dinamica.
A fronte di una funzione F(IMD;....) il componente richiamerà il servizio con in parametri presenti nella fun, e con l'XML restituito costruirà un'immagine, depositandola in una cartella.
Verrà restiuito l'XML di un albero. Nel codice dell'oggetto presente sarà indicato il path completo.

Questo componente è utilizzabile solamente in LoocUp.
Genera immagini per il componente WFD.

Il setup che è in grado di gestire è definito nel tag G.SET.IMD

##  OBIETTIVO PRIMARIO
Realizzare un componente di Looc.up che generi immagini di oggetti in modo dinamico.
Il componente deve essere in grado a fronte di un setup e dei dati di creare un'immagine composta da un'immagine di sfondo, un testo e 4 immagini (opzionali) una per ogni angolo.


##  OBIETTIVI SECONDARI
1) Acquisire conoscenza sulle API delle librerie JAVA 2D che consentono la manipolazione delle immaggini
2) Definire un formato XML e la sintassi FUN per richiamare e configurare il componente, che possa essere
preso come standard (soprattutto per la parte Setup)
3) Consolidare una metodologia di gestione di un progetto (pianificazione, documentazione, strumenti) e del suo ciclo di vita

##  VINCOLI
- XML Matrice
- Funzionamento in Looc.up


##  PARTECIPANTI
- Silvano Lancini (C.P.)
- Dario Foresti
- Federico Fortini

##  OGGETTI COIVOLTI
- J1/GRA/IMD
- TA/B&AMO/LOCIMD
- J5/EDT_SCH/G.SET.IMD
