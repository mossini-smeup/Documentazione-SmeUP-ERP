# Calcolo costo "Wip" Oggetto


_7_Introduzione
Il costo WIP è un costo relativo agli ordini di produzione.
E' costruito sui tempi rilevati dalla dichiarazioni di attivià e sulle
quantità prelevate dal magazzino.
Il calcolo del costo è diviso in due parte : 
- costruzione di un ciclo e di una distinta wip
- calcolo del costo base sul ciclo e sulla distinta wip.

_7_COSTRUZIONE CICLO WIP
Partendo da un ordine di produzione vengono lette tutte le sue
dichiarazioni di attività.
Le dichiarazioni sono totalizzate per ciclo e fase dichiarata,
Per ogni fase sono totalizzati i tempi e calcolate le seguenti quantità
. 01 Quantità Ordine
     è la quantità dell'ordine di produzione
. 02 Quantità Buona
     è la quantità buona delle dichiarazioni di attività
. 03 Quantità Scarto
     è la quantità scarti delle dichiarazioni di attività
. 04 Quantità Versata
     è la quantità dei movimenti di versamento magazzino
. 05 Quantità Calcolo
     è la quantità utilizzata per il calcolo del ciclo tra : 
     02=Buona, 02+03=Buona+Scarto, 04=Versata
. 06 Coefficiente Quantità Versata
     è la quantità buona delle dichiarazioni di attività sulla fase
     fase origine effettiva del ciclo
. 07 Quantità Lorda Versamenti Fase Successiva
     è la quantità buona + scarti delle dichiarazioni di attività della
     fase successiva,
     se ultima fase è la quantità buona delle sue dichiarazioni di
     attività
. 08 Coefficiente Quantità Lorda Fase Successiva
     è la quantità calcolata dalla formula : 
     =07/06*02
     =QtàLordaVersamentiFaseSuccessiva/CoefficienteQtàVersata*QtàBuona
. 09 Quantità Netta
     è la quantità calcolata dalla formula : 
     =02-08
     =QtàBuona-CoefficienteQtàLordaFaseSuccessiva
. 10 Quantità Lorda
     =09-03
     =QtàNetta-QtàScarti
E' possibile decidere su quale quantità i tempi vengono poi
riportati unitari nella memorizzazione del ciclo.
La scelta può essere tra quantità Buona o Buona+Scarti.
La quantità utilizzata viene memorizzata nella quantità "05" indicata
come "Quantità calcolo"
Tutte le quantità indicate sono rispettivamente memorizzate nei
10 campi numerici del ciclo.

_7_COSTRUZIONE DISTINTA WIP
Partendo da un ordine di produzione vengono letti tutti i versamenti e
per ciasun componente totalizzati tutti i suoi prelievi.
Dal ciclo Wip vengono rirese tutte le fasi con la rispettiva quantità
"05" di calcolo ciclo
Per ogni componente viene riproporzionata la sua quantità totale
di prelievo con la quantità di ciclo con fase prelievo = fase ciclo
Se la fase di prelievo e la fase di ciclo non corrispondono
si considera coma fasi di ciclo la precedente a qualla di prelievo.
Nel caso di prima fase non corrispondente si assume la prima di ciclo

_7_CALCOLO COSTI
Il calcolo costi è un calcolo base.
Dove nella definizione del Wip si definisce su quale quantità
sarà costruito il costo tra quantità di ciclo Buona o Buona+Scarti
La quantità del ciclo utilizzata nel costo sarà riproporzionata
con la quantità utilizzata nella costruzione del ciclo.
Il cofficiente di distinta utilizzata nel costo sarà riproporzionata
con la quantità utilizzata nella costruzione del ciclo. Mentra la
quantità di disitinta sarà sempre la quantità totale rispetto alla
quantità di calcolo del ciclo
