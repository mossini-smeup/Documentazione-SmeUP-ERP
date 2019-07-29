# CQB - Esito controllo collaudo
 :  : DEC T(ST) K(CQB)
## OBIETTIVO
1. Assegnare ad ogni causale di accettazione un peso di riferimento per l'analisi statistica.
2. Rendere obbligatorie le dichiarazioni delle non conformità e dei valori rilevati nei casi opportuni.
3. Attivare la registrazione a magazzino del lotto.
4. Raggruppare gli esiti di collaudo in sottoclassi.
## CONTENUTO DEI CAMPI
 :  : FLD T$CMEP **Coeff. media pesata**
Coefficiente di valutazione del lotto. È un numero compreso tra 0 e 100.
_9_Esempio : 
100  Lotto accettato conforme.
40   Lotto accettato in deroga.
5    Lotto scartato.
 :  : FLD T$RAGE **Tipo Accettazione**
Campo controllato dalla tabella CQ*TA. Esso definisce il raggruppamento per categoria delle causali di accettazione.
(Tipo Accettazione Lotto).
 :  : FLD T$ODCO **Obbligo dichiarazione NC**
Obbligo della dichiarazione della/delle non conformità.
' '  Dichiarazione non obbligatoria.
'1'  Dichiarazione obbligatoria. In questo caso il programma si collegherà direttamente con il modulo della gestione non conformi.
 :  : FLD T$OVAL **Obbligo dichiarazione valori**
Obbligo della dichiarazione dei valori di riferimento misurati sul lotto in entrata.
' '  Dichiarazione non obbligatoria.
'1'  Dichiarazione obbligatoria. In questo caso il programma si collegherà direttamente con il modulo della gestione dei valori misurati sul lotto in entrata (variabili ed attributi).
 :  : FLD T$CQBA **Obbligo registrazione note**
Obbligo di inserimento di almeno una nota di collaudo.
' '  Registrazione non obbligatoria.
'1'  Registrazione obbligatoria.
 :  : FLD T$RMAG **Reg. magazzino Coll.**
Registrazione delle quantità dichiarate del Lotto nei magazzini di competenza definiti nella tabella 'CQL' (Tipo Lotti).
' '  Non attiva la registrazione del movimento magazzino.
'1'  Attiva la registrazione del movimento magazzino attraverso l'opportuna interfaccia.
 :  : FLD T$IRRE **Declassa P.d.C.**
Declassa il Piano Di Campionamento sul prossimo Lotto in entrata da parte dello stesso Fornitore.
' '  Non attiva il declassamento del Piano di Campionamento sul prossimo lotto in consegna dallo stesso Ente.
'1'  Attiva il declassamento del P.d.C. variandolo ad un Piano più gravoso secondo quanto è stato indicato nella tabella CQR (Regole di commutazione P.d.C.).
Tale variazione diventa prioritaria rispetto alla normale gestione delle regole di commutazione del lotto.
 :  : FLD T$FLG5 **Azione prossima consegna**
Valore da impostare automaticamente in fase di dichiarazione di collaudo di un lotto nel campo azione prossima consegna.
 :  : FLD T$CRI1 **Riclassifica 1/2/3**
Campi di riclassifica controllati dalla tabella 'CQ*CR' (Riclassifica Causali N.C./Acc.). Tali campi sono usati per eseguire riclassifiche nelle analisi statistiche.
 :  : FLD T$CRI2.T$CRI1 **Riclassifica 1/2/3**
 :  : FLD T$CRI3.T$CRI1 **Riclassifica 1/2/3**
