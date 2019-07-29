# Modifiche tracciato B£SLOT

A partire dall'esigenza di aggiungere una serie di nuove caratteristiche alla definizione degli attributi, si rende necessaria una revisione del tracciato del B£SLOT0F.

## Nuovi campi necessari alla £K89
 * B£CAMF  = Campo File  :  campo del file corrispondente all'oav  (lunghezza 10)
 * B£AOGG  = Oggetto Dinamico :  tipizzazione dinamica             (lunghezza 20)
 * B£LUNG  = Lunghezza
 * B£DECI  = Decimali  (numerico? come distinguiamo decimali 0 o no decimali? dall'oggetto?)
 * B£OBBL  = Obbligatorio                   (Valore O)
 * B£NCTP  = Non controllare tipo           (Valore 1)
 * B£NCCO  = Non controllare consistenza    (Valore 1)
 * B£INOU  = Input/Output                   (Valori B/O/H)
 * B£CASE  = Case sensitiv                  (Valori LC / UC )
 * B£TEFI  = Testo fisso                    (Valore 1)
 * B£LUGR  = Lunghezza Grafica
 * B£LOGM  = Log di modifica
 ** ' '    = Se attivo log o notifica da oggetto
 ** '1'    = Si, sempre
 ** '2'    = Si, sempre con notifica
 ** '3'    = No, mai anche se attivo su oggetto
 ** '4'    = No notifica, mai anche se attiv.su oggetto

