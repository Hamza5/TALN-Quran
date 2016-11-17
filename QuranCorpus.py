from collections.abc import Iterable


class Quran(Iterable):
    """
    Represent the Quran.
    """

    def __init__(self):
        self.sourats = []

    def __iadd__(self, other):
        assert isinstance(other, Sourat)
        if other not in self.sourats:
            self.sourats.append(other)
        return self

    def __getitem__(self, sourat_num):
        assert isinstance(sourat_num, int) or isinstance(sourat_num, slice)
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
        assert isinstance(other, Ayat)
        if isinstance(other, Ayat):
            if other not in self.ayats:
                self.ayats.append(other)
        return self

    def __getitem__(self, ayat_num):
        assert isinstance(ayat_num, int) or isinstance(ayat_num, slice)
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


class Ayat(Iterable):
    """
    Represent an Ayat in Sourat of Quran.
    """

    def __init__(self, number):
        assert isinstance(number, int)
        self.num = number
        self.words = []

    def __int__(self):
        return self.num

    def __iadd__(self, other):
        assert isinstance(other, Word)
        if isinstance(other, Word):
            if other not in self.words:
                self.words.append(other)
        return self

    def __getitem__(self, word_num):
        assert isinstance(word_num, int) or isinstance(word_num, slice)
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


class Word(Iterable):
    """
    Represent a word in an Ayat in a Sourat of Quran.
    """

    def __init__(self, number, text, features):
        assert isinstance(number, int)
        assert isinstance(text, str)
        assert isinstance(features, dict) and features['type'] in ('PREFIX', 'STEM', 'SUFFIX')
        self.num = number
        self.text = text
        self.root = features.get('ROOT', None)
        self.lem = features.get('LEM', None)
        self.type = features['type']
        self.next = None

    def __iadd__(self, other):
        assert isinstance(other, Word)
        self.next = other
        return other

    def __isub__(self, other):
        assert isinstance(other, Word)
        other.next = self
        return other

    def __int__(self):
        return self.num

    def __str__(self):
        whole_word = self.text
        next_part = self.next
        while next_part:
            whole_word += next_part.text
            next_part = next_part.next
        return whole_word

    def __iter__(self):
        next_part = self
        while next_part:
            yield next_part
            next_part = next_part.next


def parse_quranic_corpus(file_path):
    quran = Quran()
    with open(file_path, encoding='utf-8', errors='ignore') as corpus_file:
        # Invalid Sourat, Ayat and Word. Used just to initialize.
        current_sourat = Sourat(0)
        current_ayat = Ayat(0)
        current_word = Word(0, '', {'type': 'STEM'})
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
            if sourat_num != int(current_sourat):  # Found another Sourat
                current_sourat = Sourat(sourat_num)
                quran += current_sourat
            if ayat_num != int(current_ayat):  # Found another Ayat
                current_ayat = Ayat(ayat_num)
                current_sourat += current_ayat
            if word_num != int(current_word):  # Found another word
                current_word = Word(word_num, text, features_dict)
                current_ayat += current_word
            else:  # Found a suffix or an attached stem after a stem, or a stem after prefix
                current_word += Word(word_num, text, features_dict)
    return quran

if __name__ == '__main__':
    from QuranTransliteration import transliterate_to_arabic
    quran = parse_quranic_corpus('quranic-corpus-morphology-0.4.txt')
    for sourat in quran:
        print(sourat)
        for ayat in sourat:
            print(transliterate_to_arabic(str(ayat)))
        break
