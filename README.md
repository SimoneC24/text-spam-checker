# Text-Spam-Checker

Text-Spam-Checker è un progetto di controllo anti spam di testo. Come capita, a quasi tutti noi, spesso ci troviamo a ricevere mail, chiamate o messsaggi che consideriamo ”spam”.
In generale lo spam è l’invio di messaggi pubblicitari e/o truffaldini che l’utente non ha richiesto. E’ un fenomeno mondiale, complesso, che colpisce tanti utenti. Purtroppo non è facile difendersi o bloccarlo. I provider lo combattono ogni giorno lavorando, in sintesi, su tre filoni che operano insieme: i servizi internazionali antispam, i propri sistemi antispam, le segnalazioni degli utenti, che possono accelerare il lavoro.
L’obiettivo degli spammer è la pubblicità: comuni offerte commerciali, proposte di vendita di materiale pornografico o illegale, farmaci senza prescrizione medica. Il loro scopo è carpire dati personali, indirizzi email e password di utenti, numeri di carte di credito e di conto corrente ecc.
Gli spammer sono, a tutti gli effetti, dei criminali. Lo Spam è soprattutto strumento di truffa, che propone improbabili progetti finanziari, o vincite false fatte dall’utente in questione, chiede le credenziali di accesso al tuo conto corrente online. Altri messaggi truffa imitano quelli del tuo provider, di tuoi fornitori o della tua banca, avvisandoti della “scadenza” di un servizio o del “mancato pagamento” di una fattura e, con la scusa dell’urgenza, chiedono di fare versamenti o di inviare IBAN, carte di credito o dati personali.
Gli spammers inviano le mail pubblicitarie o truffaldine a migliaia di indirizzi, utilizzando server in localit`a remote o caselle mittenti create appositamente di volta in volta. Oppure servendosi di caselle reali di ignari utenti, che sono riusciti a violare grazie al fatto che il titolare utilizzava una password non sicura o che le credenziali sono finite in rete a causa dell’hackeraggio di qualche piccolo sito cui l’utente si era iscritto.

## SVOLGIMENTO

### Il processo di ottenimento

 Per raggiungere l’obiettivo ci serviremo di un dataset di messaggi.
Il dataset in questione consta di circa 5500 righe, in formato csv, e in ogni riga troviamo
una stringa di testo, la quale rappresenta il messaggio da valutare, e un’etichetta in formato
testuale autoesplicativa, con due valori ammessi (spam, ham). Facendo alcune ricerche, anche
se questo dataset non ha tutte le occorrenze di messaggi che servirebbero, è sembrato il più
adatto per lo sviluppo del machine learner. Abbiamo potuto scaricare il suddetto dataset da
Kaggle.
In futuro per questo progetto potremo trovare dei dati adatti al nostro modello, in questo modo potremo migliorare 
i risultati ottenuti.

### Processo di costruzione del modello

Per questo progetto è stato necessario usare una rete neurale artificiale, perchè, essendo un problema nella quale i dati, oltre a non essere strutturati, possono avere una forma particolarmente complessa

### Processo di valutazione del modello

Seppure il modello abbia totalizzato un’accuratezza molto alta, andando a visualizzare in dettaglio i risultati, 
si nota che il modello è più bravo a riconoscere casi di non-spam piuttosto che
casi di spam. Questo fattore potrebbe assolutamente essere riconducibile allo sbilanciamento delle
etichette. Il nostro modello ha quindi problemi di overfitting e data leakage.
In pratica avendo a disposizione molte più istanze di massaggi ham e quindi essendo molto
più allenato a riconoscere i messaggi ham che quelli spam, anche in fase di valutazione tende a
riconoscere molto bene questo tipo di messaggi che quelli spam.
Inotre il modello crede di fare anche predizioni molto accurate perch´e avendo molte istanze di
messaggi non-spam ne indovinerà tante e sbaglierà poche spam non rendendosi conto che dovrebbe
riconoscere proprio quelle.

### Possibili applicazioni in casi reali

Il modello in questione può essere usato per vari scopi. Oggi questo tipo di modelli è usato
tantissimo per il controllo delle mail spam. Questo però è solo il più comune tra gli usi. Possiamo
pensare al controllo delle chiamate spam o meno, oppure per tutelare le carte di credito che ormai
sono di uso quotidiano per tutti noi. Inoltre, il modello pu`o essere usato per filtrare qualsiasi
tipo di messaggio, in un ambiente in cui non ci interessa tenere conto di chi sia il mittente. Un
caso reale potrebbe essere l’applicazione in ambienti di blogging o social, in cui si vuole effettuare
una prima selezione di messaggi potenzialmente SPAM, i quali dovranno essere supervisionati da
amministratori del sistema prima di essere resi pubblici

### Conclusioni

Nonostante l’elevata accuratezza del modello nella classificazione di dati provenienti dal Dataset
utilizzato per l’apprendimento, il suo comportamento presenta molti dubbi nel caso in cui lo si
utilizzi per predirre l’etichetta di nuove stringe (magari scritte a mano). Questo comportamento
potrebbe essere una delle conseguenze della poca numerosità dei dati. Dopo aver reso visibili pregi
e difetti del nostro machine learning possiamo dire che i risultati sono soddisfacenti ma non del
tutto. Sicuramente, come abbiamo già detto, la causa principale sono i dati sbilanciati da noi
posseduti e visto che questo progetto è nato soprattutto per sconfiggere il problema dei messaggi
considerati spam possiamo dire che si può fare nettamente meglio.

## Link Utili

[Jupiter Notebook](https://github.com/SimoneC24/text-spam-checker/blob/main/REAMDE.ipynb)

[Modello](https://github.com/SimoneC24/text-spam-checker/tree/main/training_1)

[Programma-Principale](https://github.com/SimoneC24/text-spam-checker/blob/main/__main__.py)

[Documentazione](https://github.com/SimoneC24/text-spam-checker/blob/main/Documentazione_Text_Spam_Checker.pdf)