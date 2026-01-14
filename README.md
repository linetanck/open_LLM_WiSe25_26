# Open LLMs in der Praxis: Liebeslieder
Projekt für das Seminar Open LLMs in der Praxis. Karoline Tanck 7449219 
![Taylor_Swift_The_Eras_Tour_Lover_Set_(53108816372)](https://github.com/user-attachments/assets/3cf8eaa4-dac0-4498-8f6f-2b7730ca2cc6)  
_Bild von Paolo Villanueva - Taylor Swift The Eras Tour: Lover Set, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=135971014._


## Aufgabenstellung
In diesem Projekt sollen open LLMs auf ihre Fähigkeit Texte zu interpretieren und klassifizieren, getestet werden. Dabei wird sich fokussiert auf Songtexte von Taylor Swift und auf die Art des Liebesliedes.  
Grundsätzlich lassen sich Ergebnisse dieses Projektes auch auf andere Formen von Lyrik übertragen, zum Beispiel Gedichte. Sollten das genutzte offene LLM gut performen in diesem Projekt, dann ermöglichen LLMs das schnelle Analysieren solcher kurzen künstlerischen Texte.  
Die Klassen, in welche das LLM die Liebeslieder klassifizieren soll sind: 
* "happily in love",
* "broken up",
* "yearning",
* "revenge empowerment",
* "forbidden love",
* "unrelated to love"

Beim Prompting wurden sowohl Zero-Shot-Prompting als auch Few-Shot-Prompting ausprobiert. Dabei performt llama 3.2 in diesem Experiment am besten mit Zero-Shot-Prompting.

Dabei performt das Modell in diesem Experiment am Besten mit folgendem Prompt:
```
You are a strict song lyrics classifier.

            Choose EXACTLY ONE label from this list:
            happily in love
            broken up
            yearning
            revenge empowerment
            forbidden love
            unrelated to love

            Decision rules (follow in order):
            1. If the lyrics are NOT mainly about romantic love → unrelated to love
            2. If they express anger or moving on after being hurt → revenge empowerment
            3. If a relationship has ended or is ending → broken up
            4. If the singer wants someone they are NOT with (distance, unrequited, waiting, missing) → yearning
            5. If the love must be hidden or is socially forbidden → forbidden love
            6. If the relationship is mutual, happy, and ongoing or the lyrics express being happily in love → happily in love

            First, silently analyze the lyrics.
            Then output ONLY the label.
            No explanation. No punctuation.

            Lyrics: {lyrics}
```

## Daten:
Bei der Erstellung eines Datensatzes wurde darauf geachtet, dass genug Lieder eines Artist im Datensatz sind. Taylor Swift als Musikerin hat eine sehr große Diskografie und singt oft über Liebe, weswegen sich das Experiment auf ihre Lieder fokussiert.  
Aufgrund der Notwendigkeit einer manuellen Einteilung der Songs in die Kategorien ist es auch wichtig, dass alle Lieder tatsächlich gerne einmal gehört werden. 

Es wurden alle Songs vom Album Red (2012) und Lover (2019) genutzt. Die Wahl fiel auf diese zwei Alben, da dass Album Red eine Trennung und das Album Lover eine glückliche Beziehung behandelt. Somit sollte die Klassenverteilung gleichmäßiger sein. Die Songlyrics stammen aus einem Kaggle Datensatz von Ishika Johari  
https://www.kaggle.com/datasets/ishikajohari/taylor-swift-all-lyrics-30-albums  
Die Zielkategorien wurden manuell hinzugefügt. Im manuellen Annotationsprozess wurden, wie auch im Experiement, die gesamten Songtexte gelesen und eine Klasse vergeben. Es wurde immer die Klasse vergeben, welche am besten auf den Liedtext zugetroffen hat.  
Für die Datenverarbeitung im Code wurden Pandas DataFrames genutzt.

## Modell
Das Projekt wurde mit dem Modell [llama3.2:3b](https://ollama.com/library/llama3.2:3b) via Ollama gemacht.  
In der Entscheidungsfindung welches Modell genutzt wird, wurde neben der Offenheit hauptsächlich auf die Größe des Modells in Relation zur Leistungsfähigkeit geachtet. Das Projekt soll auf einem Laptop mit geringem Arbeitsspeicher durchführbar sein, da dies auch ein zukünftiges Anwendungsszenario sein könnte. Laut Ollama übertrifft llama3.2:3b viele der anderen offenen Modelle und ist besonders gut darin, Zusammenfassungen zu erstellen.

## Ergebnisse  
Das beste Ergebnis des Experiments sind 43,2% Trefferquote der Zielklasse mit dem oben genannten prompt. In 16 von 37 Fällen hat das Modell das selbe Label vergeben wie die manuelle Klassifizierung.  
Verteilt man die Klassen beliebig ergibt dies eine Trefferquote von 16-18%.  
Die Confusion Matrix zeigt, dass die Klasse "happily in love" am besten performt, wobei "revenge empowerment" over-predicted wird und "forbidden love" nie richtig vergeben wurde.  
### Mögliche Gründe / Verbesserungen  
* Trotz mehrfacher Überarbeitung der Klassen: Klassen nicht eindeutig genug
* kleines Modell (nur 3B)
* immer noch wenige Daten


