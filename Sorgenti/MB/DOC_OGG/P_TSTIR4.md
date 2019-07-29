# OBIETTIVO
 Ritornare il tipo oggetto di un campo.

# PREREQUISITI
 D/COPY QILEGEN,£IR4DS
 D/COPY QILEGEN,£B£EQRY_TC

# PARAMETRI
## PARAMETRI DI INPUT
 - Funzione :  **£IR4FU**
  **INZ**Prepara il tracciato
       Riceve il tracciato **£IR4K1**
  **CAR**Carica valori del tracciato
       Riceve il campo e il valore da caricare **£IR4NC, £IR4VC**
  **FIN**Fine preparazine
       Nessun parametro
  **RIT**Ritorna oggetto del campo
       Riceve il campo**£IR4NC**, ritorna la sua descrizione ed il suo oggetto.**£IR4DC,£IR4OC**

 - Metodo :  **£IR4ME**
   Nessuno

## PARAMETRI DI OUTPUT
 Descrizione del capo richiesto **£IR4DC**
 Oggetto     del capo richiesto **£IR4OC**
 Errore                         **£IR435, *IN35**

# ESEMPI DI CHIAMATA
# NOTE
