# Rifasatura quantità ordine/contenitori
Questa funzione può essere chiamata direttamente da voce di menù oppure può essere richiamata dalle azioni utente dell'oggetto ordine di produzione (funzioni "A-") e presenta la quadratura tra le quantità dell'ordine di produzione e quelle dei suoi contenitori.
### Formato video
![P5PMFP_05](http://localhost:3000/immagini/MBDOC_OGG-P_P5MFP10/P5PMFP_05.png)Dato un ordine il programma confronta la quantità ordinata da testata ordine, la quantità calcolata dai contenitori : 
 * totale pianificata
 * totale wip
 * in ordine (versata + totale pianificata + totale wip)

Se esistono delle differenze è possibile ottenere la quandratura : 
 * modificando la quantità dell'ordine di produzione, la quantità in ordine non può essere diminuita al di sotto della qtà già versata
 * modificando la quantità dei contenitori, si può agire solo sulla quantità pianificata

### Trattamento scarti
Esistono due diversi modi di gestione scarti : 
 * >Reintegro; la quantità versata corrisponde a quella prodotta (buoni); lo scarto produce un'uscita del materiale dal Wip (MFP); lo scarto è reintegrato nel pianificato : 
 ** se scarto alla 1° fase non consumo il pianificato;
 ** se scarto dalla 2° fase lo scarto genera un nuovo contenitore pianficato con quantità scarto
 * >Nettificazione; la quantità versata corrisponde alla somma di quella prodotta (buoni) e quella scartata; lo scarto produce una uscita del materiale dal Wip (MFP); Lo scarto è definitivo : 
 ** se scarto alla 1° fase consumo il pianficato;
 ** se scarto dalla 2° fase non eseguo alcuna funzione sul pianificato.
