# File: autojob/src/preprocessing/custom stopwords.py

custom_stop_word_list = [
    "a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act",
    "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ah",
    "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among",
    "amongst", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything",
    "anyway", "anyways", "anywhere", "apparently", "approximately", "are", "aren", "arent", "arise", "around",
    "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "b", "back", "be",
    "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings",
    "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond", "biol", "both",
    "brief", "briefly", "but", "by", "c", "ca", "came", "can", "cannot", "cause", "causes", "certain",
    "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "could", "d", "date", "did",
    "different", "do", "does", "doing", "done", "down", "downwards", "due", "during", "e", "each", "ed", "edu",
    "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et",
    "et-al", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f",
    "far", "few", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "for", "former",
    "formerly", "forth", "found", "four", "from", "further", "furthermore", "g", "gave", "get", "gets", "getting",
    "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "h", "had", "happens",
    "hardly", "has", "have", "haven't", "having", "he", "hed", "hence", "her", "here", "hereafter", "hereby",
    "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his", "hither", "home",
    "how", "howbeit", "however", "hundred", "i", "id", "ie", "if", "immediate", "immediately", "importance", "important",
    "in", "inc", "indeed", "instead", "into", "inward", "is", "it", "itd", "itll", "hope", "alcohol", "self", "clearly", "bilingual",
    "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "l",
    "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked",
    "likely", "line", "little", "ll", "look", "looking", "looks", "ltd", "m", "made", "mainly", "make", "makes",
    "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million",
    "miss", "ml", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "n",
    "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never",
    "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "normally",
    "nos", "not", "noted", "nothing", "now", "nowhere", "o", "obtain", "obtained", "obviously", "of", "off", "often",
    "oh", "ok", "okay", "old", "omitted", "on", "once", "one", "ones", "only", "onto", "or", "ord", "other",
    "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "owing", "own", "p",
    "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly",
    "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly",
    "proud", "provides", "put", "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "re", "readily",
    "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively",
    "respectively", "resulted", "resulting", "results", "right", "run", "s", "said", "same", "saw", "say", "saying", "says",
    "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven",
    "several", "shall", "she", "shed", "shes", "should", "show", "showed", "shown", "showns", "shows", "significant",
    "significantly", "similar", "similarly", "since", "six", "slightly", "so", "some", "somebody", "somehow", "someone",
    "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified",
    "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently",
    "suggest", "sup", "sure", "t", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx",
    "that", "thatll", "thats", "thatve", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter",
    "thereby", "thered", "therefore", "therein", "theres", "thereto", "thereupon", "thereve", "these", "they", "theyd", "theyre",
    "theyve", "think", "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through", "throughout", "thru",
    "thus", "til", "tip", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "Working Hours"
    "ts", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "apply for this job", 
    "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "posting date", 
    "very", "via", "viz", "vol", "vols", "vs", "w", "want", "wants", "was", "way", "we", "wed", "welcome", "went", "full time", 
    "were", "werent", "weve", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "closing date", 
    "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "telephone",
    "whoever", "whole", "wholl", "whom", "whomever", "whos", "whose", "why", "widely", "willing", "wish", "with", "within", "eastern time", "experience", "work",
    "without", "wont", "words", "world", "would", "wouldnt", "www", "x", "y", "yes", "yet", "you", "youd", "youll", "day", 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 
    "your", "youre", "yours", "yourself", "canada", "company culture", "ontario", "ottawa", "quebec", "de", "opportunity", "time", "year", "related", "member", "candidate", "disability", "commited", "ability", "job", "company culture", "la", "en", "le", "ou", "qui"
]

