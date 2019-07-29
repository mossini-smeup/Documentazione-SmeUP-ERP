# PHU - Slave/Unità logiche TTS
 :  : DEC T(ST) K(PHU)
## OBIETTIVO
Catalogare gli slave di ogni master. Definire come sono configurati e quali azioni vengono
eseguite con i dati rilevati.
## CONTENUTO DEI CAMPI
 :  : FLD T$PHU3  __Config. Unità Logica__
 :  : FLD T$PHU4  __Blocco Unità Logica__
 :  : FLD T$PHU5  __Setup Unità Logica__
 :  : FLD T$PHU6  __Unità non esistente__
 :  : FLD T$H,01  __01° Tipo__
 :  : FLD T$H,02  __02° Tipo__
 :  : FLD T$H,03  __03° "   __
 :  : FLD T$H,04  __04° "   __
 :  : FLD T$H,05  __05° "   __
 :  : FLD T$H,06  __06° "   __
 :  : FLD T$H,07  __07° "   __
 :  : FLD T$H,08  __08° "   __
 :  : FLD T$H,09  __09° "   __
 :  : FLD T$H,10  __10° "   __
 :  : FLD T$PHU0  __Stringa testo(+=Ges)__
 :  : FLD T$PHU1  __Configurazione__
 :  : FLD T$PHU8  __Gruppo azioni ricez.__
 :  : FLD T$PHU7  __Metodo a ricezione__
E' il programma di struttura TTS che elabora i dati ricevuti dal master.
 :  : FLD T$PHU9  __Metodo a fine conf__
E' un programma di struttura TTS lanciato quando il master ha finito di configurare uno
slave. Viene quindi lanciato ogni qualvolta uno slave va online.
 :  : FLD T$PHUA  __No gestione OK Conf.__
Se impostato questo campo, l'applicazione TTS AS400 (PHMAN0) inizia ad elaborare le
informazioni ricevute dal master anche se non e' stato ricevuto da questo il messaggio
di slave configurato
