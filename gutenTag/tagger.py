import sys
import nltk

# Taken from Su Nam Kim Paper:
GRAMMAR = r'''
            NBAR:
                {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

            NP:
                {<NBAR>}
                {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
        '''

# Used when tokenizing words
SENTENCE_REGEX = r'''(?x)      # set flag to allow verbose regexps
              ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
            | \w+(-\w+)*            # words with optional internal hyphens
            | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
            | \.\.\.                # ellipsis
            | [][.,;"'?():-_`]      # these are separate tokens
        '''


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
        """Normalises words to lowercase and lemmatizes it."""
        word = word.lower()
        lemmatizer = nltk.WordNetLemmatizer()
        word = lemmatizer.lemmatize(word)
        return word

    @staticmethod
    def acceptable_word(word):
        """Checks conditions for acceptable word: length, stopword."""
        stopwords = nltk.corpus.stopwords.words('english')
        accepted = bool(2 <= len(word) <= 40 and
                        word.lower() not in stopwords)
        return accepted

    @staticmethod
    def get_terms(tree):
        for leaf in Tagger.leaves(tree):
            term = [Tagger.normalise(w) for w, t in leaf if Tagger.acceptable_word(w)]
            yield term

    @staticmethod
    def word_list(terms):
        result = ''
        for term in terms:
            for word in term:
                result += ', ' + word
        return result[2:]

    @staticmethod
    def tag(text):
        tokens = nltk.regexp_tokenize(text, SENTENCE_REGEX)
        pos_tokens = nltk.tag.pos_tag(tokens)
        chunker = nltk.RegexpParser(GRAMMAR)
        tree = chunker.parse(pos_tokens)
        terms = Tagger.get_terms(tree)
        return Tagger.word_list(terms)

    @staticmethod
    def tag_file(file_name):
        with open(file_name) as input_file:
            content = input_file.read()
            return Tagger.tag(content)


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("Usage: python %s <filename>\n" % (argv[0]))
        exit(1)

    tags = Tagger.tag_file(argv[1])
    print tags

if __name__ == "__main__":
    sys.exit(main(sys.argv))