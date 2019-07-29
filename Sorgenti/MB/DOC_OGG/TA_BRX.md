# BRX - Rapporto fiscale
 :  : DEC T(ST) K(BRX)
## CONTENUTO DEI CAMPI
 :  : FLD T$BRXA **Persona fisica**
I valori possibili sono i seguenti : 
1.   Persona Fisica :  sono richiesti e gestiti dati specifici quali luogo di nascita      residenza ecc.
2.   Persona Fisica :  i dati non sono obbligatori.
' '. Persona Giuridica.
 :  : FLD T$BRXB **Controllo partita IVA-Codice fiscale-Partita IVA CEE**
0.   Dato facoltativo (Default)
1.   Dato obbligatorio e valido
2.   Come 1 ma accetta la forzatura **
3.   Dato non gestito (deve essere blank)
4.   Come 1 ma con univocità dati di identificazione.
5.   Come 2 ma con univocità dati di identificazione.
6.   Come 4, storicamente aveva un significato differente, ma ad oggi è identico al 4.
7.   Come 1 ma con forzatura codice bianco.
_7_Note
A)   Se richiesta univocità ed esistono altri codici della stessa tipologia con uguale valore , i programmi di gestione li presentano a video.
B)   Per i valori non previsti si assume 1.
C)   Nota tecnica :  per le verifiche tecniche fare riferimento alla funzione G12 dell'applicazione B£.
 :  : FLD T$BRXC.T$BRXB **Controllo partita IVA-Codice fiscale-Partita IVA CEE**
 :  : FLD T$BRXD.T$BRXB **Controllo partita IVA-Codice fiscale-Partita IVA CEE**
 :  : FLD T$BRXE **Percipiente**
Se impostato, indica che saranno richiesti e gestiti i dati specifici del percipiente, quali :  codice tributo, percentuali, ecc.
 :  : FLD T$BRXF **Dogana**
Indica un soggetto utilizzato per identificare una particolare dogana.
