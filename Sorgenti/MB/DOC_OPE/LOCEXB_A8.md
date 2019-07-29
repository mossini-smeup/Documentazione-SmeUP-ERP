## La copertina di una Matrice
### Cosa è La Copertina?
La copertina è la prima pagina del pdf del report.

### Come posso vederla?
Cliccando col tasto destro sull'etichetta di una matrice e scegliendo Visualizza come Report.
Le matrici che hanno la copertina si riconoscono da una piccola icona rossa nell'etichetta.

### Posso vedere le informazioni della copertina prima di creare il pdf?
Sì, le informazioni vengono visualizzate cliccando sull'icona rossa nell'etichetta della matrice.

### Quali informazioni posso gestire in una copertina?
Titolo 1
Titolo 2
Titolo 3
Titolo 4
Immagine di sfondo
Logo dell'azienda in alto a Dx
10 attributi non oggettizzati in cui posso scegliere sia il nome che il valore

### Quanto sono lunghi i campi?
Ogni campo (titolo, nome dell'attributo, valore attributo) è lungo 100 caratteri.

### Come posso gestire queste informazioni?
Ci sono due modi per gestire queste informazioni : 
nello script della scheda
nel servizio

Nello script della scheda bisogna valorizzare, al momento della chiamata della funzione, il campo Input come segue
T01(Titolo uno) T02(Titolo due) T03(Titolo tre) T04(Titolo quattro) Img([IMG : VO;COD_SEL;COV_001]) Log([IMG : VO;COD_SEL;LGO_001]) R01(AttribEst1|A1) R02(AttribEst2|A2) R03(AttribEst3|A3)

Nel servizio si devono valorizzare i campi della copy
      £JaxT01 TITOLO 1
      £JaxT02 TITOLO 2
      £JaxT03 TITOLO 3
      £JaxT04 TITOLO 4
      £JaxImg SFONDO
      £JaxLgo LOGO
      £JaxAtt    DIM(10) NOMI ATTRIBUTI
      £JaxVaL   DIM(10) VALORI ATTRIBUTI

### Casi particolari
In caso di doppia valorizzazione, sia il campo Input nella scheda che i campi della copy nel servizio, vincono i campi della copy.
Nel caso in cui sia inclusa la copertina ma i valori non vengano passati, il servizio che costruisce la copertina genera dei valori standard
