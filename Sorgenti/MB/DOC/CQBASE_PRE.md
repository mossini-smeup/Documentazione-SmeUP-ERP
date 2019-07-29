# Installazioni NON Sme.up
Nel caso l'installazione avvenga in un contesto differente, è necessario scrivere alcuni programmi definiti d'interfaccia destinati a relazionarsi con il sistema gestionale.
Per alcuni dei principali gestionali i drivers necessari sono già previsti(ACG, GIPROS, MAPICS,ecc.) e sono disponibili nelle librerie Sme.up standard.(appositi file sorgente SRC_xx)
I driver utilizzati dall' applicazione sono : 
 * **Indispensabili**
 ** Articoli
 ** Clienti
 ** Fornitori
 ** Cicli di Lavoro
 ** Centri di Costo
 ** Centri di Lavoro
 ** Dipendenti

 * **Consigliati/obbligatori per alcuni moduli**
 ** Aliquote orarie/Costi
 ** Distinta base
 ** Ordini Fornitori
 ** Ordini Produzione
 ** Ordini Clienti
 ** Cespiti

## File indispensabili
  :  : DEC T(OJ) P(*FILE) K(CQPIAN0F)
#  Riprendere se opportuno da ambiente modelli
 :  : INI Piani di campionamento (Archivio CQPIAN0F) >>
 :  : CMD ?CPYF SMEMOD/CQPIAN &LIBDAT/CQPIAN0F MBROPT(COMPLETA)
 :  : FIN
  :  : DEC T(OJ) P(*FILE) K(IGLEGA0F)
#  Riprendere se opportuno da ambiente modelli
 :  : INI Legami logici calcolo indici (Archivio IGLEGA0F) >>
 :  : CMD ?CPYF SMEMOD/IGLEGA &LIBDAT/IGLEGA0F MBROPT(COMPLETA)
 :  : FIN
  :  : DEC T(OJ) P(*FILE) K(IGFORM0F)
#  Riprendere se opportuno da ambiente modelli
 :  : INI Archivio Formule (Archivio IGFORM0F) >>
 :  : CMD ?CPYF SMEMOD/IGFORM &LIBDAT/IGFORM0F MBROPT(COMPLETA)
 :  : FIN

## Tabelle indispensabili
**Tabelle Personalizzazione**
 :  : DEC T(TA) P(B£1) K(*)
 :  : DEC T(TA) P(CQ1) K(*)

## Programmi indispensabili
 :  : DEC T(OJ) P(*PGM) K(CQNC01D_A)
