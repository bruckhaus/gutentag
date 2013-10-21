import nltk


class Tagger:
    def __init__(self):
        pass

    @staticmethod
    def leaves(tree):
        """Finds NP (nounphrase) leaf nodes of a chunk tree."""
        for subtree in tree.subtrees(filter=lambda t: t.node == 'NP'):
            yield subtree.leaves()

    @staticmethod
    def normalise(word):
        """Normalises words to lowercase and stems and lemmatizes it."""
        lemmatizer = nltk.WordNetLemmatizer()
        stemmer = nltk.stem.porter.PorterStemmer()
        word = word.lower()
        word = stemmer.stem_word(word)
        word = lemmatizer.lemmatize(word)
        return word

    @staticmethod
    def acceptable_word(word):
        """Checks conditions for acceptable word: length, stopword."""
        from nltk.corpus import stopwords

        stopwords = stopwords.words('english')
        accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
        return accepted

    @staticmethod
    def get_terms(tree):
        for leaf in Tagger.leaves(tree):
            term = [Tagger.normalise(w) for w, t in leaf if Tagger.acceptable_word(w)]
            yield term

    @staticmethod
    def tag(text):
        """
        Tag a text.
        """

        sentence_re = r'''(?x)      # set flag to allow verbose regexps
              ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
            | \w+(-\w+)*            # words with optional internal hyphens
            | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
            | \.\.\.                # ellipsis
            | [][.,;"'?():-_`]      # these are separate tokens
        '''

        #Taken from Su Nam Kim Paper...
        grammar = r"""
            NBAR:
                {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

            NP:
                {<NBAR>}
                {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
        """
        chunker = nltk.RegexpParser(grammar)

        # Used when tokenizing words
        tokens = nltk.regexp_tokenize(text, sentence_re)
        pos_tokens = nltk.tag.pos_tag(tokens)
        tree = chunker.parse(pos_tokens)
        terms = Tagger.get_terms(tree)

        result = ''

        for term in terms:
            for word in term:
                result += ', ' + word

        return result[2:]