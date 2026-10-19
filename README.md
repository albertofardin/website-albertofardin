# Alberto Fardin | Senior Software Engineer & Creative Director

> URL: https://www.albertofardin.it

Sito portfolio di Alberto Fardin: una sola pagina HTML con tutte le immagini incorporate, senza dipendenze né build tool. Contiene i casi studio Arcana Nexus e SeeCommerce PXM, le esperienze, le competenze e i contatti.

## Struttura

```
nuovo-sito/
├── template.html    ← sorgente da modificare (testi, stile, struttura)
├── img/             ← immagini WebP, richiamate nel template come {{nome}}
├── build.py         ← incorpora le immagini nel template
└── site/
    ├── albertofardin.html   ← versione da mettere online (rinominala index.html)
    └── index.html           ← versione per l'anteprima su claude.ai
```

## Aggiornare il sito

1. Modifica `template.html`, oppure aggiungi o sostituisci le immagini in `img/`.
2. Dalla cartella del progetto lancia:

   ```bash
   python3 build.py .
   ```

3. Le due pagine in `site/` vengono rigenerate.

Per aggiungere un'immagine, salvala in `img/nome.webp` e richiamala nel template con `src="{{nome}}"`. Se un'immagine richiamata manca, la build si ferma.

Per convertire nuove immagini in WebP usa `cwebp`, per esempio `cwebp -q 72 -resize 1100 0 originale.png -o img/nome.webp`.

## Pubblicazione

Carica `site/albertofardin.html` sul server di albertofardin.it con il nome `index.html`. È un unico file di circa 1,2 MB. I font arrivano da Google Fonts, il CV dal PDF già presente sul sito attuale (`/AlbertoFardin CV.pdf`).

Anteprima privata su claude.ai: https://claude.ai/artifact/GYDXmCP1vYSFQQoJRmdVmr

## Provenienza delle immagini

- **Arcana Nexus**: screenshot estratti dalle guide PDF per giocatori e master (`arcanadomine/public/guide/`). Loghi delle campagne e foto dell'evento dalla cartella `public/` dello stesso repo.
- **SeeCommerce**: immagini e loghi dei brand presi da seecommerce.it, © WARDA Srl. Prima di pubblicare conviene chiedere l'autorizzazione a WARDA.
- **Ritratto**: ritagliato dal CV in PDF.
- **Numeri di Arcana Nexus** (commit, modelli, endpoint, test): ricavati dal repository a ottobre 2026. Vanno aggiornati a mano nel template.
