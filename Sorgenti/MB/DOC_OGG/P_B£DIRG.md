# Obiettivo
Conn questa funzione è possibile gestire il numero di risorse (componenti della squadra) disponibili nei vari intrevalli orari del giorno.

Un esempio può essere quando abbiamo un certo numero di operai che lavorano su due turni (mattina  pomeriggio) mentre altri fanno il turno normale, in questi casi la mattina presto, fino alle ore 08,00 abbiamo meno persone presenti rispetto all'intervallo 08,00 - 17,00  quando abbiamo la piena presenza e torniamo ad avere una rpesenza ridotta dopo le ore 17,00.

# Formato di lancio
La funzione viene lanciata da formato seguente : 

![B£DIRG_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIRG/BXDIRG_01.png)
 * **Tipo risorsa**, è un elemento della tabella TRG, il tipo risorsa deve prevedere lo sviluppo per squadre (campo di TRG)
 * **Tipo oggetto**, può essere una data specifica (quando vogliamo gestire il numero di risorse della squadra in un particolare giorno), un giorno della settimana (es. Martedì) quando vogliamo gestire il numero risorse di uno specifico giorno della settimana, "**" quando vogliamo gestiore il numero risorse valido per tutti i giorni (default)

# Formato dettaglio

![B£DIRG_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIRG/BXDIRG_02.png)
in questo formato si possono inserire fino a 6 intervalli di ore/frazioni, non consecutivi, e per ogni intervallo si inserisce il numero di risorse presenti.

## Tabelle utilizzate
- [OLG - Orari di lavoro giornalieri](Sorgenti/MB/DOC_OGG/TA_OLG)
