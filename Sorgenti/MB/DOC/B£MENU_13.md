# Ottenere un menù a partire dalle sezioni di una scheda

Il richiamo del B£MENU_13 consente di ottenere un albero di menù a partire dalle sezioni di una scheda.
Solo le subsezioni scheda  ( :  : G.SUB.SCH) possono essere visualizzate come menù.
Per indicare che una subsezione scheda deve essere visualizzata come voce di menù, è necessario compilare la proprietà Menu del tag  :  : G.SUB.SCH specificando se la sezione deve visualizzata come voce foglia (Menu="Vis") oppure se il B£MENU_13 deve analizzare la sottoscheda alla ricerca di ulteriori sezioni da aggiungere al menù (Menu="Exp").
Nella generazione del menù vengono verificate le autorizzazioni e lo usrlvl dell'utente.
