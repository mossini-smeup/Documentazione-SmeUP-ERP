# Tabelle

Creare i numeratori all'interno della tabella CRNBR (elementi NR1.AA.XX per le dichiarazioni ricevute nell'anno AA dall'azienda XX e NR2.AA.XX per le dichiarazioni emesse nell'anno AA dall'azienda XX)
  :  : DEC T(TA) P(CRNBR)  D(Tabella CRNBR)

Creare all'interno della tabella BRX il rapporto fiscale Dogana e associare questa tipologia di rapporto ai fornitori dogana
  :  : DEC T(TA) P(BRX)  D(Tabella BRX)

Riprendere da modello la tabella BR*CL  dei codici carica
  :  : DEC T(TA) P(BR*CL)  D(Tabella BR*CL)

Creare elemento NST (contenitore note) con le seguenti caratteristiche : 
* Tutte e tre i codici impostati ad **
* Capitolo / Tipo Note a NOT
  :  : DEC T(ST) P()  D(NST)
Tale codice andrà poi indicato nell'apposito campo dei parametri fissi azienda (vedi sotto il il titolo "varie").

# Autorizzazioni
Abilitare la classe BRIN01G

