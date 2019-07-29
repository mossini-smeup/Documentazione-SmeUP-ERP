# Come popolare un MPS con dati provenienti da Excel

## Introduzione
Tramite queste istruzioni sarà possibile : 
 * popolare una semplice anagrafica articoli in **BRARTI0F**
 * generare le giacenze in **GMQUAN0F**
 * popolare i costi in **D5COSO0F**
 * popolare un piano MPS con serie storica di 24 periodi mensili in una vista di **MPPIAN0F**
 * popolare vista XMT (per MiniTab) in **MPPIAN0F**

## Prerequisiti
 * __Sme.Up V3R1__ o successivi con __Looc.UP Graphics interface module__ aggiornato.

## Specifiche
I dati esterni devono essere resi disponibili in un file Excel (**MPWEB00F.xls**) con un unico formato record che riporti tutte le informazioni legate al singolo articolo.

La periodicità assunta è di 24 mesi storici e 12 previsionali.

La procedura popola anagrafica Articoli, Costi e Giacenze nel rispetto degli standard Sme.UP.

Gli articoli aventi giacenza ma privi di serie storiche contribuiscono al calcolo della previsione.

## Tracciato
**DATI PERIODICI (MPWEB00F)**
__DATI SOCIETA'__
 * Codice Azienda			A(6)
 * Ragione sociale Azienda		A(30)
__DATI PLANT__
 * Codice Plant				A(3)
 * Descrizione Plant			A(30)
__DATI ARTICOLI__
 * Codice Articolo			A(15)
 * Descrizione Articolo			A(15)
 * Data Uscita Articolo			P(8,0)
 * Codice Articolo Entrante		A(15)
 * Unità di Misura			A(35)
 * Classe Articolo			A(5)
 * Descrizione Classe Articolo		A(30)
 * Unità di Misura			A(3)
 * Giacenza				P(11,3) GMQUAN
 * Costo Unitario			P(20,6) D5COSO
__DATI PERIODO__
 * Data Inizio Periodicità		P(8,0)
 * Serie Storica (da 001 a 024)		P(11,2) MPPIAN
 * Serie Previsionali (da 001 a 036)	P(11,2) MPPIAN

## Tabelle
Le tabelle da implementare sono le seguenti : 
 * **MP2** Parametri previsione HW
 * **XDP** Classe previsionale
 * **A£Q** Periodicità
 * **UMS** Unità di Misura

## Piani
**HWaamm** Piano mensile di 36 periodi, 24 storici e 12 previsionali.
Il prefisso **HW** è seguito da **aa** e **mm** che identificano anno e mese di inizio.

## Viste
 * **STO** Serie storica (generalmente si utilizzano le quantità Ordinate).
 * **HW1** Serie previsionale, nei primi 24 periodi si può evidenziare l'aderenza della previsione rispetto alla storia.
 * **Z00** ad uso del grafico dell'Indice di Prestazione del Modello.
 * **Z01** ad uso del grafico dell'Indice di Prestazione del Modello.
 * **Z02** ad uso del grafico dell'Indice di Prestazione del Modello.
 * **XMT** Vista di output per esportazione risultati.
 * **DIF** Vista per le Differenze.

## Flussi

Verificare la scrittura della scorta minima in **D5COSO0F** da calcolo Holt Winters.

## Schede
La scheda utilizzata da Looc.UP si chiama **ANA_OR_PR** e comprende anche le seguenti informazioni
 * Indice di Prestazione del Modello (Cart del modello)
 * Indicatore di Programmabilità (Si-No)

## Programmi e servizi
Programmi e servzi interessati sono i seguenti : 
 * **XDPSER10** DPHW Servizio per ANA_OR_PR
 * **XMPPIAN1** DPHW Crea MPPIAN-VEN da GMQUAN se non esiste
 * **XMPPIAN2** DPHW Crea MPPIAN-Znn per rappresentazione grafica
 * **XMPPIAN3** DPHW Crea Indice di Prestazione del Modello
 * **XMPPIAN4** DPHW Elimina DIF da settimana 25 a 120
 * **XMPPIAN5** DPHW Calcolo Indicatore di Programmabilità

