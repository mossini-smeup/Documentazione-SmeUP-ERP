Passi di installazione
Tabelle necessarie : 
   :  : DEC T(ST) K(P52)

 - _2_Definizione fonti e gruppi fonte per PDC. Dovrà essere costruita una fonte futura con fabbisogno giornaliero, di conseguenza deve essere definito un gruppo fonti da utilizzare nel calcolo del fabbisogno giornaliero, questo gruppo fonti deve essere costituito di una fonte esistente di movimenti post MRP (fonte utente) e di una fonte futura degli ordini pianificati per PDC.
 - Utilizzando il gruppo fonti che raggruppa le due fonti prima definite (nell'esempio il gruppo fonti si chiama ADC) si costruisce la fonte di domanda PDC.
 - Deve inoltre essere definita anche la fonte esistente di disponibilità dei componenti montati nei contenitori nel WIP PDC.
 - _2_Definizione politica di riordino per PDC. Deve essere definita la politica di riordino PDC nella tabella M5A, questa politica sarà associata nei parametri di pianificazione agli articoli che si vogliono gestire a PDC
 - Deve essere notata la fonte di pianificazione che è quella che viene usata dai programmi di schedulazione PDC che, leggendo i suggerimenti MRP, predispongono i contenitori pianificati da lanciare.
 - _2_Definizione parametri risorsa. Deve essere definita una categoria parametri di risorsa (se già esiste si possono aggiungere nuovi parametri) in cui un parametro rappresenta l'ubicazione pre-macchina ed un secondo parametro rappresenta l'ubicazione post-macchina.
 -- i nomi dei parametri generati per descrivere le ubicazioni pre e post macchina devono essere riportati nelle impostazioni generali della PDC (quindi una volta generati e battezzati questi 2 parametri non possono più cambiare nome salvo riallineamento dell'intera parametrizzazione PDC).
 - _2_Attribuzione parametri risorsa. Devono essere definiti dei gruppi risorsa a cui associare i parametri risorsa
 - Tutte le risorse presenti nel ciclo di lavorazione che sono candidate a diventare anche punti di controllo della definizione del ciclo logistico dovranno essere associate ad uno di questi gruppi risorse
 - _2_Impostazioni generali. Per completare le informazioni legate alle impostazioni generali si definiscono i parametri guida  della gestione PDC che sono compresi nella tabella di personalizzazione P52
 - _2_Definizione parametri di pianificazione per articolo. Nei parametri di pianificazione degli articoli che si vogliono gestire a PDC deve essere inserita come politica di riordino la politica PDC definita in precedenza, inoltre deve essere assegnata una quantità di lotto multiplo  : 
 - _2_Costruzione ciclo logistico. Per attivare la gestione del ciclo logistico si parte dal formato di sintesi produzione a disponibilità chiamata selezionando in sequenza FUNZIONI SU RISORSE (3) e STRUTTURA LOGISTICA (3).

