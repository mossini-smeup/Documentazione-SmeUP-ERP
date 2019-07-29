# LO1 - Configurazione Loocup
 :  : DEC T(ST) K(LO1)
## CONTENUTO DEI CAMPI
 :  : FLD T$LO1A  **Interfisso lib LOA15**
È un codice di 3 caratteri che rappresenta il gruppo di aziende a cui l'azienda presente in B£2 appartiene.
Viene utilizzato per comporre il nome della libreria dati non in linea in cui vengono scritti i file generati dal costruttore LOA15.

La composizione del nome della libreria avviene nel seguente modo : 
**SBI_yyyxxT**
dove _7_yyy è il valore presente nel campo T$LO1A, _7_xx è il codice azienda presente in B£2 (££B£2A) e il carattere T viene aggiunto qualora sia valorizzato il flag ambiente di test in B£2 (££B£2Z).

Quindi qualora T$LO1A sia valorizzato a G001 e l'azienda in B£2 a 01 avremmo come libreria dati del LOA15 **SBI_G00101** per l'ambiente di produzione e **SBI_G00101T** per l'ambiente di test.

Qualora >non sia valorizzato T$LO1Ala composizione del nome della libreria avviene nel modo : 
**SMEUPBIxxT**
dove  _7_xx è il codice azienda presente in B£2 (££B£2A) e il carattere T viene aggiunto qualora sia valorizzato il flag ambiente di test in B£2 (££B£2Z).

_9_N.B. :  Spetta all'installatore verificare attentamente che il nome della libreria dati _9_risultante sia univoco sulla stessa macchina.

 :  : FLD T$LO1C  **Exit Menù**
Permette di attivare l'exit LOA12_SE_x (dove x è il valore del campo).

Tramite questa exit sarà possibile intervenire sui menù standard di oggetti, aggiungendo, modificando o togliendo le istruzioni costruite dallo standard.

