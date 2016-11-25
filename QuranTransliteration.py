import re

redundant_alef_ascii_pattern = re.compile('\{|Y`(?!\W)|YA|`')
redundant_alef_arabic_pattern = re.compile('\u0671|\u0649\u0670(?!\W)|\u0649\u0627|\u0670')
false_maqsoura_ascii_pattern = re.compile('Y(?=\W)')
false_maqsoura_arabic_pattern = re.compile('\u0649(?=\W)')
false_alef_ascii_pattern = re.compile('YA(?=\W)')
false_alef_arabic_pattern = re.compile('\u0649\u0627(?=\W)')

quran_buckwalter_scheme = {
    "'": "\u0621",
    ">": "\u0623",
    "&": "\u0624",
    "<": "\u0625",
    "}": "\u0626",
    "A": "\u0627",
    "b": "\u0628",
    "p": "\u0629",
    "t": "\u062A",
    "v": "\u062B",
    "j": "\u062C",
    "H": "\u062D",
    "x": "\u062E",
    "d": "\u062F",
    "*": "\u0630",
    "r": "\u0631",
    "z": "\u0632",
    "s": "\u0633",
    "$": "\u0634",
    "S": "\u0635",
    "D": "\u0636",
    "T": "\u0637",
    "Z": "\u0638",
    "E": "\u0639",
    "g": "\u063A",
    "_": "\u0640",
    "f": "\u0641",
    "q": "\u0642",
    "k": "\u0643",
    "l": "\u0644",
    "m": "\u0645",
    "n": "\u0646",
    "h": "\u0647",
    "w": "\u0648",
    "Y": "\u0649",
    "y": "\u064A",
    "F": "\u064B",
    "N": "\u064C",
    "K": "\u064D",
    "a": "\u064E",
    "u": "\u064F",
    "i": "\u0650",
    "~": "\u0651",
    "o": "\u0652",
    "^": "\u0653",
    "#": "\u0654",
    "`": "\u0670",
    "{": "\u0671",
    ":": "\u06DC",
    "@": "\u06DF",
    "\"": "\u06E0",
    "[": "\u06E2",
    ";": "\u06E3",
    ",": "\u06E5",
    ".": "\u06E6",
    "!": "\u06E8",
    "-": "\u06EA",
    "+": "\u06EB",
    "%": "\u06EC",
    "]": "\u06ED",
    ' ': ' '
}
quran_buckwalter_reversed_scheme = dict((v, k) for (k, v) in quran_buckwalter_scheme.items())

diacritics_arabic = {"\u0640", "\u064B", "\u064C", "\u064D", "\u064E", "\u064F", "\u0650", "\u0651", "\u0652", "\u0653",
                     "\u0654", "\u06DC", "\u06DF", "\u06E0", "\u06E2", "\u06E3", "\u06E5", "\u06E6", "\u06E8", "\u06EA",
                     "\u06EB", "\u06EC", "\u06ED"}

diacritics_ascii = {quran_buckwalter_reversed_scheme[key] for key in diacritics_arabic}


def transliterate_to_arabic(quran_text):
    if not isinstance(quran_text, str):
        raise TypeError('quran_text must be an str')
    try:
        return ''.join(quran_buckwalter_scheme[l] for l in quran_text)
    except KeyError as e:
        raise ValueError('quran_text can only contains buckwalter characters and spaces') from e


def transliterate_to_ascii(quran_text):
    if not isinstance(quran_text, str):
        raise TypeError('quran_text must be an str')
    try:
        return ''.join(quran_buckwalter_reversed_scheme[l] for l in quran_text)
    except KeyError as e:
        raise ValueError('quran_text can only contains Quran arabic characters and spaces') from e


def clear_diacritics_arabic(arabic_text):
    diacritics_stripped = ''.join(l for l in arabic_text if l not in diacritics_arabic)
    alefs_normalised = re.sub(redundant_alef_arabic_pattern, "\u0627", diacritics_stripped)  # Normalize alefs
    end_ya_corrected = re.sub(false_maqsoura_arabic_pattern, '\u064A', alefs_normalised)
    return re.sub(false_alef_arabic_pattern, '\u0649', end_ya_corrected)


def clear_diacritics_ascii(ascii_text):
    diacritics_stripped = ''.join(l for l in ascii_text if l not in diacritics_ascii)
    alefs_normalised = re.sub(redundant_alef_ascii_pattern, 'A', diacritics_stripped)  # Normalize alefs
    end_ya_corrected = re.sub(false_maqsoura_ascii_pattern, 'y', alefs_normalised)
    return re.sub(false_alef_ascii_pattern, 'Y', end_ya_corrected)
