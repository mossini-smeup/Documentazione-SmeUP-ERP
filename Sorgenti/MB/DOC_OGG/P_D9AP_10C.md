# 10 D9AP_10C - Estrattore da COSAR00F
Estrae dall'archivio COSAR00F, relativo ai costi di un articolo


_2_Parametri origine

- Tutti i costi? :  determina se calcolare tutti i tipo costo presenti (opz 1) o solo quelli selezionati sotto (opz 2)
- Tipo costo 1,2,3,4,5,6 :  tabella TCO permette di selezionare un tipo costo se 1 la voce precedente fino ad un max di 6
- Tipo livello :  se indicato calcola i costi del tipo livello indicato
- Livello costo :  se indicato calcola i costi del livello indicato

_2_Oggetti origine

- Articolo
- Tipo costo (tabella TCO)
- Fase ciclo (oggetto FA)
- Data calcolo dei costi (data a 6)	

_2_Oggetti aggiuntivi piatti
Non gestiti

_2_Valori origine
Sono fissi : 

- Costo :  indica il costo dell'articolo
- Nr. fasi :  è un contatore delle fasi per articolo
- Varia.Materiale, Lav.Esterne mat var, Lav.Ìnterne mat var, Macchina mat var, Fissi Materiale, Lav.Esterne mat fis, Lav.Ìnterne mat fis, Macchina, mat fis, Ausiliari 01, Ausiliari 02, Ausiliari 03, Ausiliari 04, Ausiliari 05, Ausiliari 06, Ausiliari 07, Ausiliari 08, Ausiliari 09

_2_Parametri dinamici
Se compilato il campo nella D9B relativo ai parametri dinamici prima del lancio si potrà indicare un'intervallo alfabetico degli articoli che si vogliono estrarre.

_2_NOTE
Attenzione, ricordarsi di selezionare un solo tipo costo per volta o vederli affiancati, altrimenuti si rischia di vedere un costo articolo somma di più tipi costo. Stesso discorso per le fasi di ciclo, verificare con il Nr fasi se il processo è monofase o no.
