from collections.abc import Iterable


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
        except IndexError as e:
            raise IndexError('Invalid index : '+str(sourat_num)) from e

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

    def __init__(self, number):
        self.num = number
        self.ayats = []

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
        except IndexError as e:
            raise IndexError('Invalid index : '+str(ayat_num)) from e

    def __len__(self):
        return len(self.ayats)

    def __str__(self):
        return Sourat.sourats_titles[self.num-1]

    def __iter__(self):
        return iter(self.ayats)

    def __eq__(self, other):
        if not isinstance(other, Sourat):
            raise TypeError('Can not compare Sourat to another object with a different type')
        return self.get_location() == other.get_location()

    def __repr__(self):
        return "<Sourat ({}) name='{}' contains {} Ayat{}>".format(self.get_location(), str(self),
                                                                   len(self), 's' if len(self) > 1 else '')

    def get_location(self):
        return self.num


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
        except IndexError as e:
            raise IndexError('Invalid index : ' + str(word_num)) from e

    def __len__(self):
        return len(self.words)

    def __str__(self):
        return ' '.join([str(word) for word in self.words])

    def __iter__(self):
        return iter(self.words)

    def __eq__(self, other):
        if not isinstance(other, Ayat):
            raise TypeError('Can not compare Ayat to another object with a different type')
        return self.get_location() == other.get_location()

    def __repr__(self):
        return "<Ayat ({},{}) contains {} word{}>".format(*self.get_location(), len(self), 's' if len(self) > 1 else '')

    def get_location(self):
        return self.sourat.get_location(), self.num


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
        self.root = features.get('ROOT', None)
        self.lem = features.get('LEM', None)
        self.type = features['type']
        self.next = None
        self.previous = None
        self.ayat = ayat

    def __iadd__(self, other):
        if not isinstance(other, Word):
            raise TypeError('+= can be used in Word only with Word object')
        self.next = other
        other.previous = self
        return other

    def __add__(self, other):
        return self.__iadd__(other)

    def __isub__(self, other):
        if not isinstance(other, Word):
            raise TypeError('-= can be used in Ayat only with Word object')
        other.next = self
        self.previous = other
        return other

    def __sub__(self, other):
        return self.__isub__(other)

    def __int__(self):
        return self.num

    def __str__(self):
        return self.get_prefix() + self.text + self.get_suffix()

    def __iter__(self):
        next_part = self
        while next_part:
            yield next_part
            next_part = next_part.next

    def __eq__(self, other):
        if not isinstance(other, Word):
            raise TypeError('Can not compare Word to another object with a different type')
        return self.get_location() == other.get_location()

    def __repr__(self):
        return "<Word ({},{},{}) prefix='{}' stem='{}' suffix='{}' lemme='{}' root='{}'>".format(
            *self.get_location(), self.get_prefix(), self.get_stem(),
            self.get_suffix(), self.get_lemme(), self.get_root()
        )

    def get_location(self):
        sourat_num, ayat_num = self.ayat.get_location()
        return sourat_num, ayat_num, self.num

    def get_prefix(self):
        prefix = ''
        if self.type == 'STEM':
            previous_part = self.previous
            while previous_part:  # Find all prefixes/predecessor stems
                prefix = previous_part.text + prefix
                previous_part = previous_part.previous
        return prefix

    def get_suffix(self):
        suffix = ''
        if self.type == 'STEM':
            next_part = self.next
            while next_part:  # Find all suffixes/successor stems
                suffix += next_part.text
                next_part = next_part.next
        return suffix

    def get_stem(self):
        if self.type == 'STEM':
            return self.text
        else:
            return ''

    def get_lemme(self):
        return self.lem or ''

    def get_root(self):
        return self.root or ''


def parse_quranic_corpus(file_path):
    try:
        quran = Quran()
        with open(file_path, encoding='utf-8', errors='ignore') as corpus_file:
            # Invalid Sourat, Ayat and Word. Used just to initialize.
            current_sourat = Sourat(0)
            current_ayat = Ayat(0, current_sourat)
            current_word = Word(0, '', {'type': 'STEM'}, current_ayat)
            word_prefix = None
            for line in corpus_file:
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
                if current_sourat.get_location() != sourat_num:  # Found another Sourat
                    current_sourat = Sourat(sourat_num)
                    quran += current_sourat
                if current_ayat.get_location() != (sourat_num, ayat_num):  # Found another Ayat
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
        return quran
    except (IndexError, ValueError, TypeError) as e:
        raise SyntaxError('The syntax of the file is invalid') from e


def search_word(searched_word, quran):
    if not isinstance(searched_word, str):
        raise TypeError('searched_word must be str')
    matches = []
    for sourat in quran:
        for ayat in sourat:
            for word in ayat:
                score = 0
                word_prefix = word.get_prefix()
                word_stem = word.get_stem()
                word_suffix = word.get_suffix()
                word_lemme = word.get_lemme()
                word_root = word.get_root()
                if word_prefix and searched_word.startswith(word_prefix):  # Prefix matches
                    if searched_word.startswith(word_stem, len(word_prefix)):  # Stem matches
                        if searched_word.endswith(word_suffix):  # Suffix matches
                            score = 4
                        else:
                            score = 3
                elif searched_word.startswith(word_stem):
                    if word_suffix and searched_word.endswith(word_suffix):
                        score = 4
                    else:
                        score = 3
                elif (word_lemme and searched_word.startswith(word_lemme))\
                        or (word_root and searched_word.startswith(word_root)):
                    score = 2
                if score > 0:
                    matches.append((word, score))
    return sorted(matches, key=lambda m: m[1])

if __name__ == '__main__':
    from QuranTransliteration import *
    quran_last_14_sourats = parse_quranic_corpus('quranic-corpus-morphology-0.4-last-14-sourats.txt')
    for sourat in quran_last_14_sourats:
        print('-'*10)
        print('سورة', sourat)
        i = 1
        for ayat in sourat:
            for word in ayat:
                print(transliterate_to_arabic(str(word)), end=' ')
            print('(', i, ')', sep='')
            i += 1
        print()
    searched_word = transliterate_to_ascii(input('Search\n> '))
    found_words = search_word(searched_word, quran_last_14_sourats)
    print(found_words)
