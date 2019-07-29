# MMF - Tipo frequenza intervento
## OBIETTIVO
Codificare le varie metodologie utilizzate per la determinazione delle previsioni di intervento.
_9_Esempi : 
- L'intervento alla data deve essere eseguito con una certa regolarità, con data fissata (es. :  ogni fine trimestre si esegue la pulizia dei filtri di un impianto);
- L'intervento a consumo deve essere eseguito a fronte di un esaurimento graduale (es. :  tagliando di controllo per aver raggiunto un certo chilometraggio);
- L'intervento con frequenza deve essere eseguito con una certa frequenza, cioè dopo un certo numero di giorni lavorativi (es. :  ogni 10 giorni si devono sostituire le matrici di estrusione).
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM TIPO FREQUENZA
Codice
 :  : FLD T$DESC DESCRIZIONE
Campo descrittivo
 :  : FLD T$MMF1 __PROGRAMMA CALCOLO__
È possibile utilizzare una Exit per influenzare il calcolo della data da proporre.
_9_Esempio :  MMEC11_CA/GG/CI/GS/OC/.. ..
In questo modo si possono costruire tipologie di intervento specifiche.
 :  : FLD T$PAR1 __PARAMETRI PGM__
Nel caso si utilizzino exit specifiche, c'è la possibilità di impostare un parametro. Questo consente di fare programmi con diverse funzioni
di calcolo frequenza.
 :  : FLD T$MMF0 __INTESTESTAZIONE FREQ.__
Intestazione del tipo frequenza che viene utilizzata nel pgm di gestione dell'intervento
 :  : FLD T$MMF2 __DATA__
Inserendo '1' in questo campo, viene permessa la formattazione del campo della frequenza, come tipo campo data. È da inserire '1' quando la
frequenza è "ALLA DATA".
