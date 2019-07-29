# SFS - Sequenza di ottimizzazione
 :  : DEC T(ST) K(SFS)
## OBIETTIVO
Permette di rendere flessibile la sequenza con cui vengono eseguiti i passi di ottimizzazione.
## UTILIZZO
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM CODICE
 :  : FLD T$DESC DESCRIZIONE
 :  : FLD T$P,01 PASSO 01
Si deve indicare la sequenza dei passi (quindi dei programmi e relative condizioni) da richiamare, per ottenere l'ordinamento delle operazioni su un centro.
 :  : FLD T$P,02.T$P,01 PASSO 02
 :  : FLD T$P,03.T$P,01 PASSO 03
 :  : FLD T$P,04.T$P,01 PASSO 04
 :  : FLD T$P,05.T$P,01 PASSO 05
 :  : FLD T$P,06.T$P,01 PASSO 06
 :  : FLD T$P,07.T$P,01 PASSO 07
 :  : FLD T$P,08.T$P,01 PASSO 08
 :  : FLD T$P,09.T$P,01 PASSO 09
 :  : FLD T$P,10.T$P,01 PASSO 10
