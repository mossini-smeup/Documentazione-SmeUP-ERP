# Dati di Input

* Tipi Oggetto Previsti : 
** LI
** Qualsiasi altro oggetto viene convertito ad una lista virtuale che ha come unico elemento l'oggetto stesso

* Parametri (P ed INPUT)
** Tp2 :  Tipo Oggetto Aggiuntivo (viene utilizzato nel relativo campo della G40)
** Cd2 :  Cod. Oggetto Aggiuntivo (viene utilizzato nel relativo campo della G40)
** Context : 

** WHR :  Stringa WHERE SQL libera che va ad aggiungersi alla WHERE dell'oggettp
** LI :  Definizione di una LISTA, la cui WHERE corrispondente va ad aggiungersi alla WHERE dell'oggetto, la struttura per questo campo è la seguente :  LI(TipoOggetto;NomeLista;NomeCampoFile)

# CONTEXT

* Composto da : 
** B£SER_84
** £UIBME
** Nome file
** Campo
** Nome Tracciato
** Eventuale stringa passata con il parametro Context

# Determinazione Schema di Default

* Viene assunto cercando in risalita questi schemi : 
** Q/DFT
** T/DFT
** *FIL/*ALL se l'oggetto corrisponde ad un file
** *TAB/*ALL se l'oggetto corrisponde è una tabella
** Codice/Descrizione

