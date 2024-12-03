image bg winter_park = "winter_park.jpg"
image character Alex = "alex.png"
image character Maria = "maria.png"
image character Andrei = "andrei.png"
image character Elena = "elena.png"
define Maria = Character("Maria")
define Andrei = Character("Andrei")
define Alex = Character("Alex")
define Elena = Character("Elena")

# Test Change
label start:
    "Este o zi friguroasa de iarna. Zapada acopera totul, iar prietenii s-au adunat an parc pentru a petrece timp impreun"
    show maria 
    Maria "Uau, ce peisaj frumos! Abia asteptam sa facem o plimbare prin parc."
    show andrei
    Andrei "Aș fi putut să stau acasă la căldură, dar zăpada asta îmi dă o energie incredibilă!"
    
    Elena "Și mie îmi place. Este perfect pentru o bătălie cu bulgări de zăpadă!"
    
    Alex "De ce nu am face un concurs de oameni de zăpadă? Cine poate construi cel mai creativ om de zăpadă?"
    
    Maria "Aș putea să fac un om de zăpadă cu pălărie și fular roz! Ce ziceți?"

    Andrei "Haha, și eu m-aș gândi la un om de zăpadă cu o pelerină de supererou!"
    
    Elena "O, da! Cu siguranță, cel mai tare om de zăpadă va fi al nostru! Hai să vedem cine face cel mai bun!"

    # Primul concurs
    menu:
        "Începem să facem oamenii de zăpadă":
            jump snowman_competition
        "Ne încălzim cu ceai și ne povestim amintiri":
            jump warm_up

label snowman_competition:
    scene bg winter_park with dissolve
    "Toți prietenii încep să construiască oamenii lor de zăpadă, râzând și distrându-se în zăpadă."
    
    Alex "Ia uite! Am făcut un om de zăpadă cu o pălărie de viking!"
    
    Maria "Al meu are un nas de morcov imens! Este clar că am câștigat!"
    
    Elena "Nu știu... omul meu de zăpadă arată ca un personaj dintr-un film de groază!"
    
    Andrei "Ce părere aveți despre al meu? Super-erou de zăpadă, nu-i așa?"
    
    Alex "Ha-ha! Îmi place! Dar tot cred că omul meu de zăpadă e cel mai original!"
    
    Maria "Original? Poate, dar ce zici de îmbrăcămintea mea? E un om de zăpadă cu stil!"
    
    Elena "Bine, bine, hai să vedem cine are cel mai mare om de zăpadă!"
    
    Andrei "Asta e pentru cei care vor să impresioneze! Eu sunt mai concentrat pe detalii."
    
    Maria "Poate ar trebui să facem o alegere democratică și să votăm pentru cel mai creativ om de zăpadă!"
    
    Elena "Da, hai! Cine vrea să înceapă?"

    menu:
        "Votăm acum":
            jump voting
        "Continuăm să construim":
            jump snowman_competition_continue

label voting:
    "Fiecare prieten dă un vot pentru omul de zăpadă preferat."
    show alex
    Alex "Eu îl aleg pe Andrei! Omul lui de zăpadă este cu adevărat original!"
    
    Maria "Eu îl aleg pe Elena! Omul ei are o expresie atât de interesantă!"
    
    Elena "Mulțumesc, Maria! Dar eu îl aleg pe Alex! Omul tău are o pălărie super tare!"
    
    Andrei "Eu îl aleg pe Alex, fără îndoială! E un om de zăpadă de supererou!"
    
    "După voturi, toată lumea râde și este de acord că fiecare om de zăpadă este unic în felul său."
    
    Maria "Se pare că suntem cu toții câștigători!"
    
    Andrei "Da, chiar dacă nu am avut un învingător clar, ne-am distrat cu toții."
    
    Elena "Eu zic că ar trebui să facem o poză cu toți oamenii de zăpadă!"
    
    Alex "Asta este o idee grozavă! Hai să facem o poză!"

    "Toți se adună pentru o fotografie amuzantă cu oamenii lor de zăpadă, zâmbind și râzând."

    menu:
        "Mergem să bem ceai și să povestim amintiri":
            jump warm_up
        "Mai rămânem în parc și continuăm distracția":
            jump park_fun

label warm_up:
    scene bg winter_park with dissolve
    "După ce s-au jucat în zăpadă, prietenii se adună într-o cabană mică pentru a bea ceai fierbinte și a povesti amintiri."
    
    Maria "A fost atât de amuzant! Nu mă mai simt atât de frig acum."
    
    Andrei "Chiar! Ceaiul ăsta cald este exact ce îmi trebuia. Poate că ar trebui să facem asta mai des în iarnă."
    
    Elena "Mă bucur că suntem împreună. Iarna are ceva magic când suntem toți aici."
    
    Alex "Da, și nu contează cât de frig este afară, atâta timp cât avem prietenii aproape."
    
    Maria "Și amintirile de iarnă pe care le creăm împreună sunt cele mai frumoase!"
    
    Andrei "Într-adevăr! Vă mai aduceți aminte când eram mici și făceam oameni de zăpadă toată ziua?"
    
    Elena "Da, dar niciodată nu ne ieșeau oameni de zăpadă atât de frumoși ca acum!"
    
    Alex "Credeți că acum, când suntem mai mari, ar trebui să facem un om de zăpadă uriaș?"
    
    Maria "Hai să încercăm! Poate că anul ăsta, vom face cel mai mare om de zăpadă din parc!"
    
    Andrei "Aș vrea să văd cum ar arăta unul uriaș... dar avem nevoie de multă zăpadă!"
    
    Elena "Nu vă faceți griji! Dacă suntem împreună, putem face orice!"
    
    Alex "Și o să facem un om de zăpadă care va rămâne în istorie!"
    
    Maria "Dar, până atunci, hai să ne bucurăm de acest ceai și de ziua asta minunată!"
    
    Andrei "Sunt de acord! Deși iarna poate fi rece, prietenii și căldura unui ceai fac totul mai frumos."

    Elena "Exact! Așa că să profităm de fiecare moment!"

    return

label park_fun:
    scene bg winter_park with dissolve
    "Prietenii decid să rămână mai mult în parc, jucându-se și explorând zăpada."
    
    Andrei "Uite, eu am găsit un loc perfect pentru a face o bătălie cu bulgări de zăpadă!"
    
    Maria "Să vedem cine lovește primul!"
    
    Elena "Ha-ha! Pregătiți-vă, voi toți! Nu o să scap de mine!"
    
    Alex "Și eu mă pregătesc! Să vedem cine este cel mai rapid"
    
    Maria "A fost incredibil! Am pierdut un pic, dar mă simt bine!"
    
    Andrei "Nu am mai râs atât de mult de mult timp"



    return
