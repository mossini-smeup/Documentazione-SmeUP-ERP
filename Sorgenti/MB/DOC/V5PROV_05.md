# Generalità
Al fine di poter attribuire i costi, nonchè i contributi in funzione del loro periodo di competenza (e non in funzione della registrazione della fattura agente) sono state introdotte delle funzioni di contabilizzazione apposite.

Le contabilizzazioni previste sono : 
 * Contabilizzazione Provvigioni, suddivisa fra : 
 ** Costo (contabilizza i costi provvigioni in funzione della loro competenza)
 ** Liquidato (contabilizza le fatture da ricevere per le provvigioni liquidate in un periodo)

 * Contabilizzazione Contributi, suddivisa fra : 
 ** Enasarco
 ** FIRR
 ** ISC

La contabilizzazione di Enasarco FIRR viene "flaggata" separatamente sul record del piano contributi (D5COSO0F), in modo da essere trattata al momento della contabilizzazione della fattura agente.

Questi programi di contabilizzazione utilizzano la tecnica delle registrazioni automatiche (tab. C5U) e, in particolare : 
 * Costo
 ** COPRO   Costo Provvigioni :  definisce conto/tipo registrazione/causale da utilizzare per imputare il costo. L'elemento può avere come desinenza il tipo provvigione.
 ** COAGE   Contributo Provvigioni :  definisce il conto da utilizzare come contropartita
 * Liquidato
 ** PRPRO   Costo Provvigioni :  definisce conto/tipo registrazione/causale da utilizzare per imputare l'attesa fatture.
 ** PRAGE   Liquidato per Agente :  definisce il conto da utilizzare come contropartita (normalmente coincide con il COAGE)

Per la contabilizzazione dei contributi si utilizzano questi elementi : 
 * Contributi
 ** ENAAZ   Enasarco azienda :  definisce tipo registrazione/causale da utilizzare per la contabilizzazione dell'enasarco, nonchè il conto da utilizzare per imputare l'enasarco a carico azienda
 ** ENAAC   Enasarco azienda :  definisce il conto da utilizzare per la contropartita dell'enasarco azienda
 ** ENAAN   Anticipo enasarco :  definisce il conto da utilizzare per l'enasarco anticipato dall'azienda
 ** ENACN   Contropartita Anticipo enasarco :  definisce il conto da utilizzare come contropartita dell'enasarco azienda
 ** ENASA   Enasarco :  definisce il conto da utilizzare per l'imputazione dell'enasarco a carico dell'agente
 ** ENACO   Contropartita Enasarco :   definisce il conto da utilizzare come contropartita dell'enasarco. Tale conto verrà stornato alla contabilizzazione della fattura.
 ** FIRR    Firr :  definisce conto/tipo registrazione da utilizzare per l'imputazione del FIRR
 ** FIRC    Contropartita Firr :   definisce il conto da utilizzare come contropartita del FIRR

# Elementi C5U
 :  : DEC T(TA) P(C5U&AZ) K(COPRO) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(COAGE) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(PRPRO) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(PRAGE) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENAAZ) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENAAC) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENAAN) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENACN) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENASA) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(ENACO) I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(FIRR)  I(>>)
 :  : DEC T(TA) P(C5U&AZ) K(FIRC)  I(>>)

# Programmi di contabilizzazione
## PGM Contabilizzazione Provvigioni
 :  : INI
 :  : CMD CALL V5PR20G
 :  : FIN
## PGM Contabilizzazione Contributi
 :  : INI
 :  : CMD CALL V5PR21G
 :  : FIN

Per ognuna delle contabilizzazioni è prevista una Exit per il completamento delle righe di analitica.
## Esempi : 
### Exit contabilizzazione costi
 :  : INI .
 :  : CMD CALL B£VED0 PARM('V5PR20A_A' '' '' '' '0')
 :  : FIN
### Exit contabilizzazione liquidato
 :  : INI .
 :  : CMD CALL B£VED0 PARM('V5PR20B_A' '' '' '' '0')
 :  : FIN
### Exit contabilizzazione contributi
 :  : INI .
 :  : CMD CALL B£VED0 PARM('V5PR21E_A' '' '' '' '0')
 :  : FIN
