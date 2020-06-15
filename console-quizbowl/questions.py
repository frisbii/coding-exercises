def resetQuestions():
    questionBank = []

    # All questions come from the PACE 2019 National Scholastic Tournament packet
    # Retrieved from https://quizbowlpackets.com/2316/ on March 13, 2020

    # // is the separator used to split questions into clues.
    # (*) is the marker for the end of power. After read, power is not given.

    question0 = {
        'prompt' : 
            '''This city's rulers were charged with providing 'care for all souls' in a proclamation by Zosimus the Bearded.// Those rulers of this city adopted the double-headed eagle as a symbol after one of them married Sophia Palaiologina, and crowned themselves with a golden cap supposedly awarded to their ancestors by Constantine Monomakh.// (*) The monk Philotheus began the tradition of calling this city the 'Third Rome.'// By winning the Great Stand on the Ugra River, this city asserted its independence from the 'Tatar Yoke' imposed by the Golden Horde.// Under its Rurikid rulers, this city replaced Constantinople as the focal point of Orthodox culture and housed such icon painters as Andrei Rublev.// For 10 points, name this city which contains the Kremlin.''',
        'answer' : ['Moscow', 'Moskva', 'Muscovy'],
        'full answer' : '''Moscow [accept Moskva or Muscovy]''',
        'subject' : '''history'''
        }
    questionBank.append(question0)

    question1 = {
        'prompt' : 
            '''One book by this philosopher divides science into the categories of 'practical,' 'theoretical,' and 'productive.'// That book by this thinker includes 'logical,' 'ontological,' and 'psychological' ways of stating the law of non-contradiction.// In 'Book Theta’ of that work by this philosopher, he distinguishes between a substance's possible modes of existence, or 'potentiality,' from its definite existence, or 'actuality.'// (*) This philosopher proposed 'material,' 'efficient,' 'final,' and 'formal' as the four types of causes in a book which studies 'being qua being.'// This author of Metaphysics discussed logic in Prior Analytics, which appears in his collection Organon.// For 10 points, name this ancient Greek philosopher who founded the Lyceum.''',
        'answer' : ['Aristotle', 'Aristoteles'],
        'full answer' : '''Aristotle of Stagira [accept Aristoteles]''',
        'subject' : '''rmp'''
    }
    questionBank.append(question1)

    question2 = {
        'prompt' : 
            '''Due to its low atomic mass, beryllium is nearly transparent to this phenomenon, which allows it to serve as a 'window'.// Spectroscopic techniques using this radiation cannot effectively detect the presence of hydrogen or helium.// Manne Siegbahn introduced the notation used in spectroscopy based on this radiation, which includes the k alpha transition.// (*) ESCA uses this phenomenon to induce the photoelectric effect.// Because this radiation has wavelengths on the same scale as interatomic spacing, crystal lattices serve as effective diffraction gratings for it.// Experiments with Crookes tubes resulted in Wilhelm Roentgen's discovery of this form of radiation.// For 10 points, name this ionizing radiation with energy higher than UV light and lower than gamma rays.''',
        'answer' : ['x-rays', 'x-ray', 'xray', 'xrays', 'x ray', 'x rays'],
        'full answer' : '''x-rays''',
        'subject' : '''science'''
    }
    questionBank.append(question2)

    question3 = {
        'prompt' : 
            '''Ashley Montagu called these concepts a 'fallacy' in the book Man's Most Dangerous Myth, and he helped UNESCO issue a 1950 statement that treated these concepts scientifically.// Johann Blumenbach proposed five of these concepts, and subscribed to the 'degenerist' view that these concepts can be traced back to Adam and Eve.// (*) Samuel Morton used craniometric skull measurements to create these constructs, to support his polygenist account of the origin of these groups.// Historical examples of these groupings include Caucasoid, Mongoloid, and Negroid; in the modern era police officers often create 'profiles' based on these constructs.// For 10 points, name these sociological groupings of humans into categories, such as 'black' or 'white' people.''',
        'answer' : ['race', 'races'],
        'full answer' : '''races''',
        'subject' : '''social science'''
    }
    questionBank.append(question3)

    question4 = {
        'prompt' : 
            '''This city's goldsmiths once lived in the small cottages along Golden Lane that were built in the 16th century to house the men guarding its castle.// Cultural attractions in this city include the Estates Theatre, where Don Giovanni premiered, and a national art museum that houses the Slav Epic.// In 2010, this city celebrated the 600th anniversary of an astronomical clock in the tower of its Old Town Hall.// (*) This city's Pinkasova memorial documents the 77,000 murdered Jews who once lived in its prominent Jewish Quarter.// Until the middle of the 19th century, the iconic Charles Bridge in this city was the only way to cross the Vltava River.// For 10 points, name this chief city of Bohemia and capital of the Czech Republic.''',
        'answer' : ['Prague', 'Praha'],
        'full answer' : '''Prague [accept Praha]''',
        'subject' : '''geography'''
    }
    questionBank.append(question4)

    question5 = {
        'prompt' : 
            '''This work concludes with the speaker telling readers that they are 'grossly mistaken' if they think she can recollect any of the 'hodge-podge medley of speech' she has just spoken.// This essay praises bees and their 'inimitable combs' for their 'industry' despite being 'Nature's dumb creatures.'// Much of this essay attacks 'long-robed philosophers,' 'artisans,' and priests, and describes how the title character is served by Laziness, Forgetfulness, and Self-Love.// (*) This  encomium is often published with the illustrations of Hans Holbein, and is named for a goddess who is the daughter of Youth and Plutus laughing at the stupidity of the world.// Thomas More is the dedicatee of, for 10 points, what essay by Desiderius Erasmus that venerates foolishness?''',
        'answer' : ['Praise of Folly', 'In Praise of Folly', 'The Praise of Folly', 'Stultitiae Laus', 'Moriae Encomium'],
        'full answer' : '''In Praise of Folly [accept The Praise of Folly or Stultitiae Laus or Moriae Encomium]''',
        'subject' : '''geography'''
    }
    questionBank.append(question5)

    question6 = {
        'prompt' : 
            '''In 1905, a jury in this state refused to convict a man who admitted to shooting Guy Bradley, a game warden tasked with single-handedly protecting this state's birds from poachers.// Dixie Highway booster Carl G. Fisher put up a billboard in Times Square boasting that it was 'June' in this state during a 1920s land bubble ended by the sinking of the Prinz Valdemar.// In that same decade, a white mob destroyed Rosewood, which, like Eatonville, was an all-black community in this state.// (*) In 1992, this state was the first in the contiguous US where the Category 5 Hurricane Andrew made landfall.// Henry Flagler built a railroad to an island off this state's coast sometimes called the Conch Republic.// For 10 points, name this state home to Key West.''',
        'answer' : ['Florida'],
        'full answer' : '''Florida''',
        'subject' : '''history'''
    }
    questionBank.append(question6)

    question7 = {
        'prompt' : 
            '''A more politically neutral version of this painting, which adds a woman in a blue-and-white striped dress to its right, was painted by Paul Baudry.// An arm in this painting is often compared to one in Caravaggio's Entombment of Christ and is found next to an object whose handle was changed from white to black.// Having seen the actual scene of this painting, the artist added such details as a green rug and a vinegar-soaked cloth wrapped around its subject's head.// (*) The artist's signature is found on a block of wood in this painting next to the title figure's slumped arm, which holds a fountain pen.// A bloody letter from Charlotte Corday is shown in, for 10 points, what Jacques-Louis David painting of an assassinated French Revolutionary?''',
        'answer' : ['Death of Marat', 'Last Breath of Marat', 'Assassination of Marat', 'La Mort de Marat', 'Marat Assassine', 'The Death of Marat', 'The Last Breath of Marat', 'The Assassination of Marat'],
        'full answer' : '''The Death of Marat [accept The Last Breath of Marat or The Assassination of Marat or La Mort de Marat or Marat Assassiné]''',
        'subject' : '''fine arts'''
    }
    questionBank.append(question7)

    question8 = {
        'prompt' : 
            '''The formula for the grand potential reduces to this equation if the log Z term equals particle number.// This equation is true if, at constant temperature, entropy scales linearly with the log of volume.// If this equation is true, then all the departure and residual functions are zero, and the enthalpy depends only on temperature.// This equation is generally a decent approximation if the specific volume is greater than 5 liters per mole.// (*) This equation is equivalent to setting the compressibility factor to one or when the a and b parameters are zero in the van der Waals equation.// A constant found in this equation is approximately 8.314 joules per mole kelvin.// For 10 points, name this equation of state used for gases at low pressures and high temperatures that equates PV to nRT.''',
        'answer' : ['ideal gas', 'ideal gas law'],
        'full answer' : '''Ideal gas law''',
        'subject' : '''science'''
    }
    questionBank.append(question8)

    question9 = {
        'prompt' : 
            '''Most numbers with this property take the form of '1 plus 9 times a triangular number,' and are themselves also triangular.// These numbers are the period-1 analogues of sociable and amicable numbers.// These values take the form '2 to the quantity 'p minus 1', times the quantity ‘2 to the p, minus 1,’' whenever the latter is prime.// These numbers are neither 'deficient' nor 'abundant.'// (*) By the Euclid-Euler Theorem, even numbers of this kind are in one-to-one correspondence with Mersenne primes.// 28 and 496 are small examples of these numbers. Since 1, 2, and 3 both add and multiply to 6, it's the smallest one of these numbers.// For 10 points, what numbers are the sum of their own proper divisors?''',
        'answer' : ['perfect', 'perfect numbers', 'even perfect', 'even perfect numbers'],
        'full answer' : '''perfect numbers [accept even perfect numbers]''',
        'subject' : '''science'''
    }
    questionBank.append(question9)

    question10 = {
        'prompt' : 
            '''Benjamin Halevy denounced the Kafr Qasim massacre during this event as 'illegality that pierces the eye and revolts the heart', and other killings occurred during this event at Khan Yunis.// Hugh Stockwell agreed to move Operation Telescope ahead of schedule based on Andre Beaufre's suggestion during this event.// Robert Menzies failed to end this event peacefully, leading to the bombing of troops under Abdel Hakim Amer in this event's Operation Musketeer.// (*) President Eisenhower was credited with ending this event, which began with a coordinated attack by British, French and Israeli forces.// For 10 points, name this event, which led to the resignation of Anthony Eden and occurred after Gamal Abdel Nasser nationalized the namesake canal.''',
        'answer' : ['Suez Crisis', 'second arab israeli war', 'tripartite aggression', 'sinai war'],
        'full answer' : '''Suez Crisis [accept Second Arab-Israeli War or Tripartite Aggression or Sinai War]''',
        'subject' : '''history'''
    }
    questionBank.append(question10)

    question11 = {
        'prompt' : 
            '''A building in this city contains fifteen rocks in a rectangular pool of raked gravel arranged such that visitors cannot view all the rocks simultaneously.// The uppermost floor of another building in this city is called the Cupola of the Ultimate and is topped by a bronze statue of a phoenix.// So-called 'nightingale floors' were built to ward off assassins at Nijo Castle in this city, which is the largest in its country to have a grid-like plan modeled on China's Xi'an.// (*) The Saihōji temple in this city houses a celebrated example of a waterless, rock-filled Zen garden.// In 1950, an acolyte burned down a religious building in this city whose top two floors had gilding.// For 10 points, name this Japanese city home to the Temple of the Golden Pavilion.''',
        'answer' : ['kyoto', 'kyoto shi'],
        'full answer' : '''Kyoto''',
        'subject' : '''fine arts'''
    }
    questionBank.append(question11)

    question12 = {
        'prompt' : 
            '''Since none of the third-person pronouns in Hungarian or Turkish possess this grammatical property, there is often ambiguity in reference.// In Arabic, different varieties of this property are distinguished by the presence of a word-final ta marbutah, which inflects to have a 't' sound in the construct case.// Languages like Basque use an 'animate-inanimate' distinction with respect to this property.// (*) Proto-Indo-European had three categories for this concept, which its descendant language Latin inherited.// In Spanish, nouns and adjectives must agree in terms of number and this other property, which is typically distinguished by -a and -o endings.// 'Neuter' is often the third category of, for 10 points, what linguistic property that can be masculine or feminine?''',
        'answer' : ['grammatical gender', 'gender'],
        'full answer' : '''grammatical gender''',
        'subject' : '''social science'''
    }
    questionBank.append(question12)

    question13 = {
        'prompt' : 
            '''In a preface, the author explains the fate of this character by likening her speed to 60 and a man's speed to 100, noting 'women's rights' will not allow her to catch up.// This character is given a lilac sprig to waft as she listens to another character tell a story about entering a rich 'Turkish pavilion.'// The work in which she appears begins with a character noting she is 'crazy again tonight! absolutely crazy!' shortly after she orders her servant to kiss her shoe.// (*) This character and the male lead plan to run away to Lake Como to set up a hotel, which is why he kills this woman's pet canary before they plan to leave.// This noblewoman is given a razor by the valet Jean to kill herself at the play's end.// For 10 points, give this title character of an August Strindberg play.''',
        'answer' : ['julie', 'miss julie', 'countess julie', 'froken julie'],
        'full answer' : '''Miss Julie [accept Countess Julie or Fröken Julie]''',
        'subject' : '''literature'''
    }
    questionBank.append(question13)

    question14 = {
        'prompt' : 
            '''Antimicrobial nanoparticles of this element turn bacteria into 'zombies' that kill other bacteria.// This element catalyzes the oxidative syntheses of formaldehyde and ethylene oxide.// An electrode containing this element's chloride has largely replaced the calomel electrode in pH meters.// This element's nitrate precipitates out halides as cream-colored solids and stains skin and nervous tissue in Golgi's black reaction.// (*) This element is the lighter constituent of electrum.// This element has the highest thermal and electrical conductivity and is generally in a +1 oxidation state, with a 5s1 4d10 electron configuration, similar to copper, which lies right above it on the periodic table.// For 10 points, name this noble metal with symbol Ag.''',
        'answer' : ['silver'],
        'full answer' : '''Silver''',
        'subject' : '''science'''
    }
    questionBank.append(question14)

    question15 = {
        'prompt' : 
            '''This member of the Alice B. Toklas Memorial Democratic Club found a winning political issue by highlighting the dog poop problem in city parks.// This one-time camera-shop owner led a boycott against Coors for not hiring union teamsters and staged one of the earliest anti-apartheid campaigns by trying to force the South African consulate out of his city.// He opposed the Briggs Initiative, which would have prevented people like himself from teaching in schools.// (*) A campaign to 'avenge' this Mayor of Castro Street sparked the White Night riots of 1979.// Along with Mayor George Moscone, this member of the San Francisco Board of Supervisors was assassinated by Dan White in 1978.// For 10 points, name this first openly gay elected official in the US.''',
        'answer' : ['milk', 'harvey milk', 'harvey bernard milk'],
        'full answer' : '''Harvey Milk [or Harvey Bernard Milk]''',
        'subject' : '''history'''
    }
    questionBank.append(question15)

    question16 = {
        'prompt' : 
            '''This goddess convinces Calais and Zetes to break off their pursuit of the Harpies.// In a Roman myth, she turns Romulus's wife Hersilia into one of the Horae; in the Aeneid, she steals a lock of hair from Dido.// In a Homeric hymn, several Olympians bribe this goddess with a golden thread to summon Eileithyia to Delos to help Leto give birth.// This goddess obtains the water from Styx used by the other deities to swear oaths.// (*) This goddess, who is often depicted with golden wings, is the wife of the wind god Zephyrus.// Some stories depict her as always standing by the side of Hera, only leaving to communicate with mortals on her behalf.// For 10 points, what Greek goddess, the messenger of the gods, was the personification of the rainbow?''',
        'answer' : ['iris'],
        'full answer' : '''Iris''',
        'subject' : '''rmp'''
    }
    questionBank.append(question16)

    question17 = {
        'prompt' : 
            '''The melancholy motto that opens this composer's Symphony No. 5, which begins 'long G, then two short Gs, then long A,' is restated triumphantly in major to open the finale, marked Andante maestoso.// In this composer's Symphony No. 4, a high A played by the oboe begins the trio of a scherzo in which the strings play pizzicato throughout.// That fourth symphony by this composer opens with a brass fanfare introducing a Beethoven-inspired 'fate' motif.// (*) This man used the odd time signature of 5/4 for a dance in his last symphony, called the 'limping waltz.'// That sixth symphony by this composer of the Manfred Symphony premiered nine days before his death.// For 10 points, name this Russian composer of the 'Pathetique' symphony and 1812 Overture.''',
        'answer' : ['pyotr ilyich tchaikovsky', 'pyotr tchaikovsky', 'tchaikovsky'],
        'full answer' : '''Pyotr Ilyich Tchaikovsky''',
        'subject' : '''fine arts'''
    }
    questionBank.append(question17)

    question18 = {
        'prompt' : 
            '''The viral protein SV40 is expressed in a cell derived from this organism in the workhorse strain 293T.// Adherent cells derived from this organism are dissociated using Versene, a dilute stock of EDTA.// At least a fifth of all cell banks worldwide were once contaminated by a strain from this species that has an approximately triploid chromosome count.// Calcium phosphate transfects DNA into cells sourced from this organism like HEK 293.// (*) At Johns Hopkins in 1951, George Gey isolated an immortalized cell line from this species, which was infected with papillomavirus, and therefore, could surpass this species' Hayflick limit of 60 doublings.// For 10 points, HeLa cells are used for in vitro studies of what species which normally has 46 chromosomes?''',
        'answer' : ['human', 'homo sapien', 'humans', 'homo sapiens'],
        'full answer' : '''human [accept Homo sapiens]''',
        'subject' : '''science'''
    }
    questionBank.append(question18)

    question19 = {
        'prompt' : 
            ''''Crazy-headed' irregular troops of this polity carried out the Batak massacre.// To get around the absolute silence mandated at its court, courtesans practiced a form of sign language called ixarette.// Flower arrangement became popular in England following Lady Mary Wortley Montagu's writings about this empire's customs.// Conquered people were brought to the capital of this empire via the surgun system.// (*) The valide was the mother of its emperor.// Following the Alhambra Decree, most Spanish Jews emigrated to this empire.// This empire's court was held in Topkapi Palace, and its Chief Black Eunuch presided over the emperor's harem.// For 10 points, name this empire that conquered the Byzantine capital of Constantinople.''',
        'answer' : ['ottoman', 'ottoman empire', 'turkish empire', 'turkey', 'the exalted ottoman state'],
        'full answer' : '''Ottoman Empire [accept The Exalted Ottoman State or Turkish Empire or Turkey]''',
        'subject' : '''history'''
    }
    questionBank.append(question19)

    question20 = {
        'prompt' : 
            '''Particles with behavior between that of bosons and fermions called anyons can only exist in systems with limited values for this quantity.// Systems with differing values for this quantity may be treated equivalently through compactification.// Hermann Weyl's treatment of the anthropic principle notes that Maxwell's treatment of electromagnetism would not hold if the universe had a different value for this quantity.// Attempts to solve the hierarchy problem often increase this value to account for the graviton.// (*) This quantity equals 11 in M-theory. This value for a brane is one larger than that of a string.// In Minkowski space, this quantity is 4 due to treating space and time as a continuum.// For 10 points, name this quantity, which is typically treated as 3 for space.''',
        'answer' : ['dimension', 'number of dimensions', 'dimensions'],
        'full answer' : '''dimension [accept number of dimensions]''',
        'subject' : '''science'''
    }
    questionBank.append(question20)

    return questionBank