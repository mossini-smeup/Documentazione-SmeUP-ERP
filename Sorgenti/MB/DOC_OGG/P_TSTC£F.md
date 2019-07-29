# £C£F FUNZIONI ARCHIVIO ESTENSIONE OGGETTO
# OBIETTIVO
Gestire le operazioni base del record nel tracciato C£ESO00F Estensioni oggetto.

# FUNZIONI E METODI
## SCANSIONI
Attraverso l'api è possibile effettuare scansioni, posizionamento e lettura, con chiave o senza, in avanti e indietro.
Le chiavi devono essere impostate mediante i campi del formato record, che viene utilizzato in questo caso anche come input, oltre che come output per comunicare il risultato della lettura.
Il numero di chiavi utilizzate, se non passato, viene calcolato automaticamente dall'API, ma è consigliato specificare in modo specifico il numero di chiavi da utilizzare, relativamente al metodo di scansione richiesto, in modo da poter utilizzare anche delle chiavi blank, che il metodo automatico non considererebbe.
### Particolarità chiavi tipo oggetto in scansione
Per i metodi di scansione che prevedono chiavi con tipo oggetto (esempio 6L che prevede P£TP01/2/3), è possibile evitare di impostare tali chiavi, utilizzando la funzionalità implicita che le valorizza automaticamente in base al contenuto del campo P£TPRC ricevuto.
Tale funzionalità permette di evitare che il programma chiamante effettui la lettura della griglia per valorizzarli dinamicamente, o effettui un impostazione cablata dei tipi oggetto.
L'automatismo si innesca se : 
* è stata passata la categoria parametri nel campo P£TPRC
* il campo P£TPxx è blank
* è stato passato il numero di campi chiave da utilizzare in modo specifico

# Particolarità :  £C£F e parametri non estesi.
Per facilitare l'utilizzo da parte dei programmatori, la £C£F è in grado di leggere e scrivere sia sull'archivio C£ESOx0F che sul C£CONx0F, deviandosi in modo automatico e trasparente a seconda che il parametro (elemento di B£N) sia definito come esteso (C£ESOx0F) o meno (C£CONx0F).
Si è quindi ritenuto di adottare gli stessi metodi di scansione della £C£E (da 0F a 5L) .
I campi da valorizzare sono quelli del tracciato del C£ESOx0F e vengono poi deviati sui campi corrispondenti del C£CONx0F.

_3_ N.B. :  Utilizzo di metodi che includano il campo CDVA ed effetti sulle performance 
L'utilizzo di metodi che includano il campo CDVA causa un degrado di performance quando applicato ai parametri estesi, data la dimensione del campo (30000 caratteri).
Questo si verifica non solo quando il campo CDVA è utilizzato come chiave, in quanto i record vengono comunque ordinati per il campo.
Si consiglia quindi di evitare l'utilizzo dei metodi che includono il campo CDVA quando non sia necessario filtrare e/o ordinare in base a tale campo.
Ad esempio si consiglia di valutare l'utilizzo del metodo 9L (implementato anche sulle £C£E) anziché dei metodi 0L e 5L e del metodo 6L invece del metodo 5L_3K.
