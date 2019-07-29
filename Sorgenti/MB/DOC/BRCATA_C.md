# Dove memorizzare i dati.

File BRCATA0F


Il catalogo è caratterizzato dalla tabella BSD tipo catalogo che modella il significato dei campi
del record. In particolare, con questa tabella si può definire : 

*    Tipo ente produttore
*    Tipo ente distributore
*    Parametri impliciti (C£I)
*    Metodo ricezione(programma)
*    Metodo invio(programma)
*    Metodo codifica(programma)
*    Metodo aggiornamento(programma)


Il file ha come chiave principale, il tipo catalogo, il tipo ente di produzione, l'ente di produzione e il codice articolo fornitore.

Ogni record di catalogo ha un suo IDOJ che lo rende univoco e facilmente individuabile, una serie di
campi tipizzati in base alla tabella BSD e una parte di dati variabili inseriti in formato XML nel campo finale a lunghezza variabile.


Un'esigenza particolare di questa gestione è l'utilizzo di campi chiave(riferimenti del fornitore),
 lunghi almeno 35 byte.


|  R="99" |
| 
| .COL Txt="Campo" LunAut=" " A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" Lun="25" A="L" |
| 
| .COL Txt="Tipo" LunAut=" " A="L" |
| 
| .COL Txt="T" LunAut=" " A="L" |
| 
| .COL Txt="Lungh De " LunAut=" " A="L" |
| 
| .COL Txt="B.da" LunAut=" " A="L" |
| 
| .COL Txt="B.a" LunAut="1" A="L" |
| C§IDOJ    |ID Oggetto                  |                     |A|   10    |   1  | 10 |
| C§TICT    |Tipo Catalogo               |TABSD                |A|    3    |  11  | 13 |
| C§COCT    |Codice Catalogo             |                     |A|   30    |  14  | 43 |
| C§LIVE    |Livello                     |TAB£W00              |A|    1    |  44  | 44 |
| C§STAT    |Stato                       |                     |A|    2    |  45  | 46 |
| C§TCDP    |Tipo ente produzione        |OG                   |A|   12    |  47  | 58 |
| C§CODP    |Ente produzione             |                     |A|   15    |  59  | 73 |
| C§TCDD    |Tipo ente distribuzione     |OG                   |A|   12    |  74  | 85 |
| C§CODP    |Ente distribuzione          |                     |A|   15    |  86  |100 |
| C§ARCF    |Codice articolo fornitore   |                     |A|   30    | 101  |130 |
| C§MARC    |Marchio                     |                     |A|   30    | 131  |160 |
| C§RIF1    |Riferimento oggetto 1       |                     |A|   30    | 161  |190 |
| C§RIF2    |Riferimento oggetto 2       |                     |A|   30    | 191  |220 |
| C§RIF3    |Riferimento oggetto 3       |                     |A|   30    | 221  |250 |
| C§DESE    |Descrizione estesa          |                     |A|  200    | 251  |450 |
| C§ARTI    |Codice Articolo             |AR                   |A|   15    | 451  |465 |
| C§DESA    |Descrizione codificata      |                     |A|   70    | 466  |535 |
| C§CLMA    |Classe materiale            |TACLS                |A|    5    | 536  |540 |
| C§UNMS    |Unità di misura gestione    |TAUMS                |A|    2    | 541  |542 |
| C§PESO    |Peso                        |                     |P|   12  5 | 543  |549 |
| C§VOLU    |Volume                      |                     |P|   12  5 | 550  |556 |
| C§DINV    |Data inizio validità        |D8*YYMD              |P|    8  0 | 557  |561 |
| C§AFSE    |Data fine serie             |D8*YYMD              |P|    8  0 | 562  |566 |
| C§IDMT    |Riferimento IDOJ Master     |                     |A|   10    | 567  |576 |
| C§QRIF    |Quantita' Rif Master        |                     |P|   11  3 | 577  |582 |
| C§VALU    |Codice valuta               |TAVAL                |A|    4    | 583  |586 |
| C§PRZA    |Prezzo                      |NR                   |P|   21  6 | 587  |597 |
| C§PRZB    |Prezzo                      |NR                   |P|   21  6 | 598  |608 |
| C§PRZC    |Prezzo                      |NR                   |P|   21  6 | 609  |619 |
| C§PRZD    |Prezzo                      |NR                   |P|   21  6 | 620  |630 |
| C§PRZE    |Prezzo                      |NR                   |P|   21  6 | 631  |641 |
| C§QRIV    |Quantita'                   |                     |P|   11  3 | 642  |647 |
| C§BARC    |Barcode                     |                     |A|   15    | 648  |662 |
| C§CL01    |Codice 1                    |                     |A|   15    | 663  |677 |
| C§CL02    |Codice 2                    |                     |A|   15    | 678  |692 |
| C§CL03    |Codice 3                    |                     |A|   15    | 693  |707 |
| C§CL04    |Codice 4                    |                     |A|   15    | 708  |722 |
| C§CL05    |Codice 5                    |                     |A|   15    | 723  |737 |
| C§CL06    |Codice 6                    |                     |A|   15    | 738  |752 |
| C§CL07    |Codice 7                    |                     |A|   15    | 753  |767 |
| C§CL08    |Codice 8                    |                     |A|   15    | 768  |782 |
| C§CL09    |Codice 9                    |                     |A|   15    | 783  |797 |
| C§CL10    |Codice 10                   |                     |A|   15    | 798  |812 |
| C§NU01    |Numero 1                    |NR                   |P|   15  5 | 813  |820 |
| C§NU02    |Numero 2                    |NR                   |P|   15  5 | 821  |828 |
| C§NU03    |Numero 3                    |NR                   |P|   15  5 | 829  |836 |
| C§NU04    |Numero 4                    |NR                   |P|   15  5 | 837  |844 |
| C§NU05    |Numero 5                    |NR                   |P|   15  5 | 845  |852 |
| C§NU06    |Numero 6                    |NR                   |P|   15  5 | 853  |860 |
| C§NU07    |Numero 7                    |NR                   |P|   15  5 | 861  |868 |
| C§NU08    |Numero 8                    |NR                   |P|   15  5 | 869  |876 |
| C§NU09    |Numero 9                    |NR                   |P|   15  5 | 877  |884 |
| C§NU10    |Numero 10                   |NR                   |P|   15  5 | 885  |892 |
| C§DT01    |Data libera  1              |D8*YYMD              |P|    8  0 | 893  |897 |
| C§DT02    |Data libera  2              |D8*YYMD              |P|    8  0 | 898  |902 |
| C§DT03    |Data libera  3              |D8*YYMD              |P|    8  0 | 903  |907 |
| C§DT04    |Data libera  4              |D8*YYMD              |P|    8  0 | 908  |912 |
| C§DT05    |Data libera  5              |D8*YYMD              |P|    8  0 | 913  |917 |
| C§DT06    |Data libera  6              |D8*YYMD              |P|    8  0 | 918  |922 |
| C§DT07    |Data libera  7              |D8*YYMD              |P|    8  0 | 923  |927 |
| C§DT08    |Data libera  8              |D8*YYMD              |P|    8  0 | 928  |932 |
| C§DT09    |Data libera  9              |D8*YYMD              |P|    8  0 | 933  |937 |
| C§DT10    |Data libera 10              |D8*YYMD              |P|    8  0 | 938  |942 |
| C§FL01    |Flag                        |FLBRCATA0F01         |A|    2    | 943  |944 |
| C§FL02    |Flag                        |FLBRCATA0F02         |A|    2    | 945  |946 |
| C§FL03    |Flag                        |FLBRCATA0F03         |A|    2    | 947  |948 |
| C§FL04    |Flag                        |FLBRCATA0F04         |A|    2    | 949  |950 |
| C§FL05    |Flag                        |FLBRCATA0F05         |A|    2    | 951  |952 |
| C§FL06    |Flag                        |FLBRCATA0F06         |A|    2    | 953  |954 |
| C§FL07    |Flag                        |FLBRCATA0F07         |A|    2    | 955  |956 |
| C§FL08    |Flag                        |FLBRCATA0F08         |A|    2    | 957  |958 |
| C§FL09    |Flag                        |FLBRCATA0F09         |A|    2    | 959  |960 |
| C§FL10    |Flag                        |FLBRCATA0F10         |A|    2    | 961  |962 |
| C§FL11    |Flag                        |FLBRCATA0F11         |A|    2    | 963  |964 |
| C§FL12    |Flag                        |FLBRCATA0F12         |A|    2    | 965  |966 |
| C§FL13    |Flag                        |FLBRCATA0F13         |A|    2    | 967  |968 |
| C§FL14    |Flag                        |FLBRCATA0F14         |A|    2    | 969  |970 |
| C§FL15    |Flag                        |FLBRCATA0F15         |A|    2    | 971  |972 |
| C§FL16    |Flag                        |FLBRCATA0F16         |A|    2    | 973  |974 |
| C§FL17    |Flag                        |FLBRCATA0F17         |A|    2    | 975  |976 |
| C§FL18    |Flag                        |FLBRCATA0F18         |A|    2    | 977  |978 |
| C§FL19    |Flag                        |FLBRCATA0F19         |A|    2    | 979  |980 |
| C§FL20    |Flag                        |FLBRCATA0F20         |A|    2    | 981  |982 |
| C§FL21    |Flag                        |FLBRCATA0F21         |A|    2    | 983  |984 |
| C§FL22    |Flag                        |FLBRCATA0F22         |A|    2    | 985  |986 |
| C§FL23    |Flag                        |FLBRCATA0F23         |A|    2    | 987  |988 |
| C§FL24    |Flag                        |FLBRCATA0F24         |A|    2    | 989  |990 |
| C§FL25    |Flag                        |FLBRCATA0F25         |A|    2    | 991  |992 |
| C§FL26    |Flag                        |FLBRCATA0F26         |A|    2    | 993  |994 |
| C§FL27    |Flag                        |FLBRCATA0F27         |A|    2    | 995  |996 |
| C§FL28    |Flag                        |FLBRCATA0F28         |A|    2    | 997  |998 |
| C§FL29    |Flag                        |FLBRCATA0F29         |A|    2    | 999  |1000 |
| C§FL30    |Flag                        |FLBRCATA0F30         |A|    2    |1001  |1002 |
| C§FL31    |Flag                        |FLBRCATA0F31         |A|    2    |1003  |1004 |
| C§FL32    |Flag                        |FLBRCATA0F32         |A|    2    |1005  |1006 |
| C§FL33    |Flag                        |FLBRCATA0F33         |A|    2    |1007  |1008 |
| C§FL34    |Flag                        |FLBRCATA0F34         |A|    2    |1009  |1010 |
| C§FL35    |Flag                        |FLBRCATA0F35         |A|    2    |1011  |1012 |
| C§FL36    |Flag                        |FLBRCATA0F36         |A|    2    |1013  |1014 |
| C§FL37    |Flag                        |FLBRCATA0F37         |A|    2    |1015  |1016 |
| C§FL38    |Flag                        |FLBRCATA0F38         |A|    2    |1017  |1018 |
| C§FL39    |Flag                        |FLBRCATA0F39         |A|    2    |1019  |1020 |
| C§FL40    |Flag                        |FLBRCATA0F40         |A|    2    |1021  |1022 |
| C§DTIN    |Data inserimento            |D8*YYMD              |P|    8  0 |1023  |1027 |
| C§USIN    |Utente inserimento          |UP                   |A|   10    |1028  |1037 |
| C§PRIN    |Programma inserimento       |                     |A|   10    |1038  |1047 |
| C§DTAG    |Data aggiornamento          |D8*YYMD              |P|    8  0 |1048  |1052 |
| C§USAG    |Utente aggiornamento        |UP                   |A|   10    |1053  |1062 |
| C§PRAG    |Programma aggiornamento     |                     |A|   10    |1063  |1072 |
| C§DATI    |Dati                        |                     |A|30002    |1073  |31074 |
| 





### Dubbi.
Alcuni dati dovranno essere ripetuti, per esempio i dati relativi a codice a barre, dimensioni, pesi e volumi sono ripetuti più volte per articolo/fornitore. (Si pensa di usare i parametri)
Caricamento massivo :  questi cataloghi vengono importati periodicamente per aggiornare i prezzi, le caratteristiche del prodotto, e per caricare nuovi articoli. Se un prodotto esce dal catalogo fornitore bisognerebbe toglierlo anche dal nostro catalogo??(si)
Non si vorrebbe oggettizare il catalogo per non dover gestire la cancellazione di oggetti legati a questo oggetto(es. note e listini, probabilmente non si riuscirà a farlo)
Se un fornitore mi passa un listino che entra in vigore più avanti nel tempo.....come faccio a gestire due record dello stesso articolo/fornitore (doppio idoj???) Risolto con un tipo catalogo provvisorio. Si gestira lo spostamento da un catalogo ad un altro.
Nello STD elettrico, in base ai campi famiglia del fornitore, 18byte + 18byte si costruiscono gli sconti di acquisto dell'articolo e si reperisce la classe gestionale, che ne determina poi la scontistica in vendita. (Alias)
