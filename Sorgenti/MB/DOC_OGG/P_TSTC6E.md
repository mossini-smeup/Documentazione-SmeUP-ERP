# OBIETTIVI

Questa /COPY permette di gestire tutte le funzionalità relative alla gestione del fido promiscuo.
NOTA BENE :  perchè le funzioni diano un risultato è prerequisito aver attivato la gestione del fido promiscuo nella tabella C55.

# EXIT
Attraverso la tabella C55 è possibile attivare un exit che poi intervenga sulle logiche standard.
L'exit può essere implementata copiando direttamente il pgm standard C5C6E0.

# FUNZIONI/METODI
**CAR Caricamento struttura Gruppo Affidamento**
Dati di input : 
* Azienda (£C6EI_AZ)
* Banca (£C6EI_BA)
* Gruppo Affidamento (£C6EI_GA)
* Data di riferimento (£C6EI_DF)

Elaborazione : 
* Viene controllata l'esistenza del gruppo di affidamento corrispondente ai dati di input ed in caso affermativo ne viene ritornata la struttura

Dati di output : 
* Indicatore 35 acceso se non esiste il gruppo
* Campo di output del gruppo di affidamento (£C6EO_GA)
* N° di rapporti che compongono il gruppo (£C6EO_NR)
* Schiera rapporti del gruppo (£C6EO_RB)
* Schiera dei tipi rapporti del gruppo (corrispondenti alla precedente schiera) (£C6EO_TR)
* Schiera degli eventuali importi limite al fido (£C6EO_LI)

**CHK Controllo se Rapporto in Gruppo Affidamento**
Dati di input : 
* Azienda (£C6EI_AZ)
* Rapporto (£C6EI_RA)
* Data di riferimento (£C6EI_DF)

Elaborazione : 
* Viene controllato se alla data di riferimento il rapporto risulta inserito in un gruppo di affidamento. Cioè in un gruppo di rapporti per cui è previsto un fido promiscuo comune.

Dati di output : 
* Indicatore 35 acceso se il rapporto non appartiene ad un gruppo di affidamento
* Eventuale limite al fido promiscuo ritornato nel primo elemento della schiera di output (£C6EO_LI)
* Il codice della tabella del gruppo di affidamento (£C6EO_GA)

**CAL Calcolo distribuzione**
Dati di input : 
* Azienda (£C6EI_AZ)
* Banca (£C6EI_BA)
* Gruppo Affidamento (£C6EI_GA)
* Data di riferimento (£C6EI_DF)
* Schiera dei rapporti del gruppo (£C6EI_RB)
* Schiera dei tipi rapporti del gruppo (£C6EI_TR)
* Schiera degli eventuali importi limite del fido per ogni rapporto (£C6EI_LI)
* Schiera dei saldi di ogni rapporto del gruppo (£C6EI_SA)

Elaborazione : 
* Tramite i dati passati in input viene recuperato dai dati anagrafici il valore del fido promiscuo valido alla data e poi sulla base della seguente logica viene applicata la distribuzione di tale importo : 
** In prima battuta il fido totale viene attribuito ai rapporti con saldo negativo :  a tali rapporti viene attribuito un importo tale per cui o viene coperto il saldo negativo o viene raggiunto il limite massimo attribuibile al rapporto.
** Eseguita l'elaborazione precedente viene preso il residuo del fido totale, suddiviso per il numero di rapporti che non hanno raggiunto il limite (se è previsto) e questa quota viene attribuita ad ogni rapporto. Nel caso in cui la somma delle quote per effetto della suddivisione non corrisponda essattamente alla sommatoria del fido, la differenza viene attribuita al primo rapporto.
** NOTA BENE :  se in questa fase uno dei rapporti raggiunge il limite avviene questo : 
*** a tale rapporto viene attribuito l'importo limite, a tutti gli altri rapporti viene attribuita la quota prevista
*** al termine del ciclo per effetto del fatto che su uno o più rapporti non è stata attribuita la quota prevista, ci sarà un residuo. Su tale residuo verrà ripetuto il ciclo :  l'importo residuo verrà suddiviso per il numero di rapporti che non hanno raggiunto il limite ed ad essi applicato.

Questo un esempio della logica : 
* Dato di input : 
** Fido di gruppo totale 100.000
** Due rapporti per il gruppo
** Il 1° rapporto ha 30.000 come saldo e nessun limite di affidamento
** Il 2° rapporto ha 70.000- come saldo e un limte di affidamento di 80.000
** Il pgm innanzitutto attribuisce 70.000 al secondo rapporto per coprire il saldo negativo
** Fatto questo risulterà un residuo di fido di 30.000, i 30.000 verranno divisi per 2 (il numero di rapporti che non hanno raggiunto il limite (visto che sul secondo per ora ho attribuito 70.000 e quindi sono sotto limite).
** Il risultato di tale suddivisione è quindi 15.000
** Sul rapporto 1 non c'è nessun limite e quindi viene attribuito 15.000
** Sul rapporto 2 attribuendo 15.000 raggiungo il limite degli 80.000 per questo viene attribuito solo 10.000
** Ho quindi 5.000 di avanzo che vengono attribuiti interamente al 1° rapporto (essendo l'unico rapporto rimasto senza limite.
** In conclusione avrò quindi 20.000 di fido attribuiti al 1° rapporto (15.000+5.000) e
80.000 al 2° rapporto (70.000+10.000).

Dati di output : 
* Indicatore 35 acceso se non esiste il gruppo
* Campo di output del gruppo di affidamento (£C6EO_GA)
* Importo totale di fido (£C6EO_FT)
* N° di rapporti che compongono il gruppo (£C6EO_NR)
* Schiera rapporti del gruppo (£C6EO_RB)
* Schiera dei tipi rapporti del gruppo (corrispondenti alla precedente schiera) (£C6EO_TR)
* Schiera della quota di fido di ogni rapporto (£C6EO_FR)
* Schiera degli eventuali importi limite al fido (£C6EO_LI)


