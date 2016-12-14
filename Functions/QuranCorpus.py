from collections.abc import Iterable
from os import stat
from Functions.QuranTransliteration import transliterate_to_arabic, clear_diacritics_ascii, transliterate_to_ascii


class Quran(Iterable):
    """
    Represent the Quran.
    """

    def __init__(self):
        self.sourats = []

    def __iadd__(self, other):
        if not isinstance(other, Sourat):
            raise TypeError('+= in Quran can only be used with Sourat object')
        if other not in self.sourats:
            self.sourats.append(other)
        return self

    def __getitem__(self, sourat_num):
        if not (isinstance(sourat_num, int) or isinstance(sourat_num, slice)):
            raise TypeError('Indexing Quran can be done only using ints or slices')
        if isinstance(sourat_num, int):
            sourat_num -= 1
        else:
            sourat_num = slice(sourat_num.start - 1, sourat_num.stop)
        try:
            return self.sourats[sourat_num]
        except IndexError:
            return None

    def __len__(self):
        return len(self.sourats)

    def __iter__(self):
        return iter(self.sourats)

    def __repr__(self):
        return "<Quran contains {} Sourat{}>".format(len(self), 's' if len(self) > 1 else '')


class Sourat(Iterable):
    """
    Represent a Sourat of Quran.
    """

    sourats_titles = [
        "الفاتحة",
        "البقرة",
        "آل عمران",
        "النساء",
        "المائدة",
        "الأنعام",
        "الأعراف",
        "الأنفال",
        "التوبة",
        "يونس",
        "هود",
        "يوسف",
        "الرعد",
        "ابراهيم",
        "الحجر",
        "النحل",
        "الإسراء",
        "الكهف",
        "مريم",
        "طه",
        "الأنبياء",
        "الحج",
        "المؤمنون",
        "النور",
        "الفرقان",
        "الشعراء",
        "النمل",
        "القصص",
        "العنكبوت",
        "الروم",
        "لقمان",
        "السجدة",
        "الأحزاب",
        "سبإ",
        "فاطر",
        "يس",
        "الصافات",
        "ص",
        "الزمر",
        "غافر",
        "فصلت",
        "الشورى",
        "الزخرف",
        "الدخان",
        "الجاثية",
        "الأحقاف",
        "محمد",
        "الفتح",
        "الحجرات",
        "ق",
        "الذاريات",
        "الطور",
        "النجم",
        "القمر",
        "الرحمن",
        "الواقعة",
        "الحديد",
        "المجادلة",
        "الحشر",
        "الممتحنة",
        "الصف",
        "الجمعة",
        "المنافقون",
        "التغابن",
        "الطلاق",
        "التحريم",
        "الملك",
        "القلم",
        "الحاقة",
        "المعارج",
        "نوح",
        "الجن",
        "المزمل",
        "المدثر",
        "القيامة",
        "الانسان",
        "المرسلات",
        "النبإ",
        "النازعات",
        "عبس",
        "التكوير",
        "الإنفطار",
        "المطففين",
        "الإنشقاق",
        "البروج",
        "الطارق",
        "الأعلى",
        "الغاشية",
        "الفجر",
        "البلد",
        "الشمس",
        "الليل",
        "الضحى",
        "الشرح",
        "التين",
        "العلق",
        "القدر",
        "البينة",
        "الزلزلة",
        "العاديات",
        "القارعة",
        "التكاثر",
        "العصر",
        "الهمزة",
        "الفيل",
        "قريش",
        "الماعون",
        "الكوثر",
        "الكافرون",
        "النصر",
        "المسد",
        "الإخلاص",
        "الفلق",
        "الناس"
    ]

    def __init__(self, number, quran):
        if not isinstance(number, int):
            raise TypeError('number must be int')
        if not isinstance(quran, Quran):
            raise TypeError('quran must be Quran')
        self.num = number
        self.ayats = []
        self.quran = quran

    def __int__(self):
        return self.num

    def __iadd__(self, other):
        if not isinstance(other, Ayat):
            raise TypeError('+= can be used in Sourat only with Ayat object')
        if other not in self.ayats:
            self.ayats.append(other)
        return self

    def __getitem__(self, ayat_num):
        if not (isinstance(ayat_num, int) or isinstance(ayat_num, slice)):
            raise TypeError('Indexing Sourat can be done only using ints or slices')
        if isinstance(ayat_num, int):
            ayat_num -= 1
        else:
            ayat_num = slice(ayat_num.start-1, ayat_num.stop)
        try:
            return self.ayats[ayat_num]
        except IndexError:
            return None

    def __len__(self):
        return len(self.ayats)

    def __str__(self):
        return Sourat.sourats_titles[self.num-1]

    def __iter__(self):
        return iter(self.ayats)

    def __eq__(self, other):
        if not isinstance(other, Sourat):
            raise TypeError('Can not compare Sourat to another object with a different type')
        return self.location() == other.location()

    def __repr__(self):
        return "<Sourat ({}) name='{}' contains {} Ayat{}>".format(self.location(), str(self),
                                                                   len(self), 's' if len(self) > 1 else '')

    def location(self):
        return self.num

    def previous(self):
        p_num = self.num-1
        if p_num < 1:
            return None
        return self.quran[p_num]

    def next(self):
        n_num = self.num+1
        if n_num > len(self.quran):
            return None
        return self.quran[n_num]


class Ayat(Iterable):
    """
    Represent an Ayat in Sourat of Quran.
    """

    def __init__(self, number, sourat):
        if not isinstance(number, int):
            raise TypeError('number must be int')
        if not isinstance(sourat, Sourat):
            raise TypeError('sourat must be Sourat')
        self.num = number
        self.words = []
        self.sourat = sourat

    def __int__(self):
        return self.num

    def __iadd__(self, other):
        if not isinstance(other, Word):
            raise TypeError('+= can be used in Ayat only with Word object')
        if other not in self.words:
            self.words.append(other)
        return self

    def __getitem__(self, word_num):
        if not (isinstance(word_num, int) or isinstance(word_num, slice)):
            raise TypeError('Indexing Ayat can be done only using ints or slices')
        if isinstance(word_num, int):
            word_num -= 1
        else:
            word_num = slice(word_num.start - 1, word_num.stop)
        try:
            return self.words[word_num]
        except IndexError:
            return None

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return ' '.join([str(word) for word in self.words])

    def __iter__(self):
        return iter(self.words)

    def __eq__(self, other):
        if not isinstance(other, Ayat):
            raise TypeError('Can not compare Ayat to another object with a different type')
        return self.location() == other.location()

    def __repr__(self):
        return "<Ayat ({},{}) contains {} word{}>".format(*self.location(), len(self), 's' if len(self) > 1 else '')

    def location(self):
        return self.sourat.location(), self.num

    def previous(self):
        p_num = self.num-1
        if p_num < 1:
            s = self.sourat.previous()
            if s:
                return s[0]
            else:
                return None
        return self.sourat[p_num]

    def next(self):
        n_num = self.num+1
        if n_num > len(self.sourat):
            s = self.sourat.next()
            if s:
                return s[1]
            else:
                return None
        return self.sourat[n_num]

    def arabic_text(self):
        return transliterate_to_arabic(str(self))


class Word(Iterable):
    """
    Represent a word in an Ayat in a Sourat of Quran.
    """

    def __init__(self, number, text, features, ayat):
        if not isinstance(number, int):
            raise TypeError('number must be int')
        if not isinstance(text, str):
            raise TypeError('text must be str')
        if not (isinstance(features, dict) and features['type'] in ('PREFIX', 'STEM', 'SUFFIX')):
            raise TypeError('features[type] must be one of PREFIX, STEM, SUFFIX')
        if not isinstance(ayat, Ayat):
            raise TypeError('ayat must be Ayat')
        self.num = number
        self.text = text
        self.rt = features.get('ROOT', None)
        self.lem = features.get('LEM', None)
        self.type = features['type']
        self.next_part = None
        self.previous_part = None
        self.ayat = ayat

    def __iadd__(self, other):
        if not isinstance(other, Word):
            raise TypeError('+= can be used in Word only with Word object')
        self.next_part = other
        other.previous_part = self
        return other

    def __add__(self, other):
        return self.__iadd__(other)

    def __isub__(self, other):
        if not isinstance(other, Word):
            raise TypeError('-= can be used in Ayat only with Word object')
        other.next_part = self
        self.previous_part = other
        return other

    def __sub__(self, other):
        return self.__isub__(other)

    def __int__(self):
        return self.num

    def __str__(self):
        return self.prefix() + self.text + self.suffix()

    def __iter__(self):
        next_part = self
        while next_part:
            yield next_part
            next_part = next_part.next_part

    def __eq__(self, other):
        if not isinstance(other, Word):
            raise TypeError('Can not compare Word to another object with a different type')
        return self.location() == other.location()

    def __repr__(self):
        return "<Word ({},{},{}) prefix='{}' stem='{}' suffix='{}' lemme='{}' root='{}'>".format(
            *self.location(), self.prefix(), self.stem(),
            self.suffix(), self.lemme(), self.root()
        )

    def __hash__(self):
        sourat_num, ayat_num = self.ayat.location()
        return sourat_num * 100000 + ayat_num * 100 + self.num

    def location(self):
        sourat_num, ayat_num = self.ayat.location()
        return sourat_num, ayat_num, self.num

    def prefix(self):
        prefix = ''
        if self.type == 'STEM':
            previous_part = self.previous_part
            while previous_part:  # Find all prefixes/predecessor stems
                prefix = previous_part.text + prefix
                previous_part = previous_part.previous_part
        return prefix

    def suffix(self):
        suffix = ''
        if self.type == 'STEM':
            next_part = self.next_part
            while next_part:  # Find all suffixes/successor stems
                suffix += next_part.text
                next_part = next_part.next_part
        return suffix

    def stem(self):
        if self.type == 'STEM':
            return self.text
        else:
            return ''

    def lemme(self):
        return self.lem or ''

    def root(self):
        return self.rt or ''

    def previous(self):
        p_num = self.num-1
        if p_num < 1:
            previous_ayat = self.ayat.previous()
            if previous_ayat:
                return previous_ayat[0]
            else:
                return None
        return self.ayat[p_num]

    def next(self):
        n_num = self.num+1
        if n_num > len(self.ayat):
            next_ayat = self.ayat.next()
            if next_ayat:
                return next_ayat[1]
            else:
                return None
        return self.ayat[n_num]

    def arabic_text(self):
        return transliterate_to_arabic(str(self))


def parse_quranic_corpus(file_path, progress_function=lambda progress: None):
    try:
        quran = Quran()
        with open(file_path, encoding='utf-8', errors='ignore') as corpus_file:
            bytes_read = 0
            file_size = stat(file_path).st_size
            # Invalid Sourat, Ayat and Word. Used just to initialize.
            current_sourat = Sourat(0, quran)
            current_ayat = Ayat(0, current_sourat)
            current_word = Word(0, '', {'type': 'STEM'}, current_ayat)
            word_prefix = None
            for line in corpus_file:
                line_size = len(line.encode())  # Number of bytes in this line
                line = line.strip()
                if not line.startswith('('):
                    continue  # Ignore any lines without data
                line_parts = line.split('\t')
                sourat_num, ayat_num, word_num, word_part_num = (
                    int(number.strip('()')) for number in line_parts[0].split(':')
                )
                text = line_parts[1]
                # tag = line_parts[2]  # Useless for now.
                features = line_parts[3].split('|')
                features_dict = {'type': features[0]}
                for feature in features[1:]:
                    if feature.startswith('POS:'):  # Part of speech
                        features_dict['POS'] = feature[4:]
                    if feature.startswith('LEM:'):  # Lemme
                        features_dict['LEM'] = feature[4:]
                    elif feature.startswith('ROOT:'):  # Root
                        features_dict['ROOT'] = feature[5:]
                if current_sourat.location() != sourat_num:  # Found another Sourat
                    current_sourat = Sourat(sourat_num, quran)
                    quran += current_sourat
                if current_ayat.location() != (sourat_num, ayat_num):  # Found another Ayat
                    current_ayat = Ayat(ayat_num, current_sourat)
                    current_sourat += current_ayat
                word_part = Word(word_num, text, features_dict, current_ayat)
                if features_dict['type'] == 'PREFIX':
                    if word_prefix is None:
                        word_prefix = word_part
                    else:
                        word_prefix += word_part
                elif features_dict['type'] == 'STEM':
                    if word_prefix is None:
                        current_word = word_part
                    else:
                        current_word = word_prefix + word_part
                        word_prefix = None
                    current_ayat += current_word
                else:  # Found a suffix
                    current_word += word_part
                bytes_read += line_size
                progress_function(round(bytes_read/file_size*100))
        return quran
    except (IndexError, ValueError, TypeError) as e:
        raise SyntaxError('The syntax of the file is invalid') from e


def search_word(searched_word, quran, strict_search=False, basic_search=True, lemme_search=True, root_search=True):
    if not isinstance(searched_word, str):
        raise TypeError('searched_word must be str')
    if not isinstance(quran, Quran):
        raise TypeError('quran must be Quran')
    matches = []
    searched_word_nd = clear_diacritics_ascii(searched_word)
    for sourat in quran:
        for ayat in sourat:
            for word in ayat:
                score = 0
                word_prefix = word.prefix()
                word_stem = word.stem()
                word_suffix = word.suffix()
                word_lemme = word.lemme()
                word_root = word.root()
                word_prefix_nd = clear_diacritics_ascii(word_prefix)
                word_stem_nd = clear_diacritics_ascii(word_stem)
                word_suffix_nd = clear_diacritics_ascii(word_suffix)
                word_lemme_nd = clear_diacritics_ascii(word_lemme)
                if word_prefix and searched_word.startswith(word_prefix) and word_stem and searched_word[len(word_prefix):].startswith(word_stem) and word_suffix and searched_word[len(word_prefix)+len(word_stem):] == word_suffix and basic_search:
                    score = 4  # Found a prefix+stem+suffix
                elif word_prefix and searched_word.startswith(word_prefix) and word_stem and searched_word[len(word_prefix):] == word_stem and basic_search:
                    score = 4  # Found a prefix+stem
                elif word_stem and searched_word.startswith(word_stem) and word_suffix and searched_word[len(word_stem):] == word_suffix and basic_search:
                    score = 4  # Found a stem+suffix
                elif word_stem and searched_word == word_stem and basic_search:
                    score = 3  # Found a stem
                elif word_lemme and searched_word == word_lemme and lemme_search:
                    score = 2  # Found a lemme_search
                elif word_root and searched_word == word_root and root_search:
                    score = 1  # Found a root_search
                elif not strict_search:  # No diacritics, apply the same rules again except for the root_search because it is already without diacritics
                    if word_prefix_nd and searched_word_nd.startswith(word_prefix_nd) and word_stem_nd and searched_word_nd[len(word_prefix_nd):].startswith(word_stem_nd) and word_suffix_nd and searched_word_nd[len(word_prefix_nd) + len(word_stem_nd):] == word_suffix_nd and basic_search:
                        score = 4  # Found a prefix+stem+suffix
                    elif word_prefix_nd and searched_word_nd.startswith(word_prefix_nd) and word_stem_nd and searched_word_nd[len(word_prefix_nd):] == word_stem_nd and basic_search:
                        score = 4  # Found a prefix+stem
                    elif word_stem_nd and searched_word_nd.startswith(word_stem_nd) and word_suffix_nd and searched_word_nd[len(word_stem_nd):] == word_suffix_nd and basic_search:
                        score = 4  # Found a stem+suffix
                    elif word_stem_nd and searched_word_nd == word_stem_nd and basic_search:
                        score = 3  # Found a stem
                    elif word_lemme_nd and searched_word_nd == word_lemme_nd and lemme_search:
                        score = 2  # Found a lemme_search
                if score > 0:
                    matches.append((word, score))
    return sorted(matches, key=lambda m: m[1], reverse=True)


def concordance(searched_word, quran, words_before_count=5, words_after_count=5, strict=False, basic=True, lemme=True, root=True):
    contexts = []
    indexes = []
    scores = []
    found_words = search_word(searched_word, quran, strict, basic, lemme, root)
    for word, score in found_words:
        context = [word]
        i = words_before_count
        previous_word = word.previous()
        while previous_word and i > 0:
            context.append(previous_word)
            previous_word = previous_word.previous()
            i -= 1
        context.reverse()
        indexes.append(len(context) - 1)
        i = 0
        next_word = word.next()
        while next_word and i < words_after_count:
            context.append(next_word)
            next_word = next_word.next()
            i += 1
        contexts.append(tuple(context))
        scores.append(score)
    return contexts, indexes, scores

if __name__ == '__main__':
    quran = parse_quranic_corpus('../quranic-corpus-morphology-0.4.txt')
    # for sourat in quran:
    #     for ayat in sourat:
    #         print(ayat.arabic_text())
    #     print()

    word_to_be_searched = True
    while word_to_be_searched:
        word_to_be_searched = transliterate_to_ascii(input('Search : '))
        if word_to_be_searched:
            print(word_to_be_searched)
            contexts, indexes, scores = concordance(word_to_be_searched, quran, words_before_count=4, words_after_count=2)
            for context, index, score in zip(contexts, indexes, scores):
                for i in range(len(context)):
                    if i == index:
                        print('{', context[i].arabic_text(), '}', sep='', end=' ')
                    else:
                        print(context[i].arabic_text(), end=' ')
                print(score)
