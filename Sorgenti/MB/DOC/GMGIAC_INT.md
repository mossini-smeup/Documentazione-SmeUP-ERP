# Definizione della giacenza
 Per creare una giacenza,e permetterne le attività successive, è necessario : 
 * _2_Definire l'AREA o le AREEdi magazzino di cui si vuole avere la giacenza.
 :  : DEC T(ST) K(GMR)

 * _2_Definire i TIPI GIACENZA, ovvero il  grado  di dettaglio con cui voglio interrogare le giacenze di un articolo in una particolare area.
_R_Il tipo giacenza è l'elemento che deve essere  definito sulle causali di movimentazione, affinchè le giacenze vengano movimentate correttamente.
 :  : DEC T(ST) K(GMQ)
 :  : DEC T(ST) K(GMC)
Le chiavi di giacenza tipiche sono : 
 ** _9_CONFIGURAZIONE
 ** _9_UBICAZIONE
 ** _9_LOTTO
 ** _9_ENTE(Cliente / Fornitore)
 ** _9_FASE DI LAVORAZIONE
 ** _9_COMMESSA
 ** _9_COLLO
E' possibile definire>4chiavi di giacenza libere, più una fissa che è il collo.

 * _2_Definire la FORMA DI INTERROGAZIONEdella giacenza (cioè il logico di interrogazione dell'archivio giacenza GMQUAN0F).
 :  : DEC T(ST) K(GMF)

# Interrogazione giacenza
E' sufficente accedere alla voce di menu>INTERROGAZIONE GIACENZEe definire la>FORMA DI RAPPRESENTAZIONE.
Quando si usa per la prima volta una FORMA di interrogazione è possibile che il Sistema informatico chieda di generare il logico.

# Gestione giacenza
Sul  dettaglio  ottenuto con l'>INTERROGAZIONE GIACENZEsono attive alcune azioni dalla_9_visualizzazionedel dettaglio alla_9_rettifica. Tali azioni sono legate ad una classe di autorizzazione (vd documento specifico).

# Suggerimenti di conversione
Se  si  deve  procedere  con la conversione delle giacenze, è consigliabile non creare direttamente l'archivio delle giacenze (GMQUAN0F), ma far ricorstruire la giacenza attraverso l'elaborazione dei movimenti di magazzino che alimentano naturalmente lo stesso.

La giacenza  è  infatti  un  archivio dinamico che viene aggiornato ad ogni movimento. Attraverso i movimenti  di  inizializzazione  abbiamo  quindi un utile archivio di riferimento, per eventuali verifiche future.
