from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict


class HebrewCharTypes(Enum):
    """
    The types of chars used in Hebrew.
    """

    LETTER: str = "letter"
    YIDDISH_LETTER: str = "yiddish_letter"
    PUNCTUATION: str = "punctuation"
    NIKUD: str = "nikud"

    def __str__(self) -> str:
        return self.value


# TODO: Future properties:
#  - Number/order of the char in aleph bes if the letter is HebrewCharTypes.Letter.
#  - Maybe a reference to a minor/final letter when applicable.
#  - Gematria value of the letter for future use in `Hebrew` methods such as
#    `Hebrew.get_gematria_value(type=Gematria.MisparGadol)`.
#     - This is a bit tricky because the gematria value of a letter is not a single value, there are different values
#       used by different systems.
@dataclass
class HebrewChar:
    """
    A class to hold the metadata for a Hebrew glyph.

    This class is used internally by HebrewGlyph only.
    """

    char: str
    name: str
    hebrew_name: str
    name_alts: Optional[List[str]] = None
    hebrew_name_alts: Optional[List[str]] = None
    final_letter: bool = False
    type: HebrewCharTypes = HebrewCharTypes.LETTER

    @property
    def hebrew_names(self) -> List[str]:
        return [self.hebrew_name] + (self.hebrew_name_alts or [])

    @property
    def names(self) -> List[str]:
        return [self.name] + (self.name_alts or [])

    # TODO: if a string like "HebrewGlyph" is the better way to Type this than the way I did HebrewStringT, update that
    #  Typing, or Type it here.
    @classmethod
    def search(cls, char_name: str) -> Optional["HebrewChar"]:
        """
        Search for a HebrewChar by one of its names.
        :param char_name:
        :return:
        """
        # TODO : Add search by hebrew_name, which will need to support hebrew text with or without nikud.
        for char in _ALL_CHARS:
            if char_name.lower() in [n.lower() for n in char.names]:
                return CHARS[char.char]
        return None


# TODO:
#  - Populate the alt hebrew and english names with additional spellings, this is helpful for the
#    `HebrewGlyph.search()` method.
#  - Add the rest of the hebrew unicode characters as `HebrewChar` instances instead of plain strings`


ALEPH = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
BET = HebrewChar(char="בּ", name="Bet", hebrew_name="בֵּית")
VET = HebrewChar(char="ב", name="Vet", hebrew_name="בֵית")
GIMEL = HebrewChar(char="ג", name="Gimel", hebrew_name="גִימֵל")
DALET = DALED = HebrewChar(
    char="ד", name="Dalet", hebrew_name="דָלֶת", name_alts=["Daled"]
)
HE = HEI = HEY = HebrewChar(
    char="ה", name="He", hebrew_name="הֵא", name_alts=["Hei", "Hey"]
)
VAV = VUV = HebrewChar(char="ו", name="Vav", hebrew_name="וָו", name_alts=["Vuv"])
ZAYIN = HebrewChar(char="ז", name="Zayin", hebrew_name="זַיִן")
CHET = HET = CHES = HebrewChar(
    char="ח", name="Chet", hebrew_name="חֵית", name_alts=["Het", "Ches"]
)
TET = TES = HebrewChar(char="ט", name="Tet", hebrew_name="טֵית", name_alts=["Tes"])
YOD = YUD = HebrewChar(char="י", name="Yod", hebrew_name="יוֹד", name_alts=["Yud"])
CAF = HebrewChar(char="כּ", name="Kaf", hebrew_name="כַּף")
KAF_SOFIT = FINAL_KAF = HebrewChar(
    char="ךּ",
    name="Kaf Sofit",
    final_letter=True,
    hebrew_name="כַּף סוֹפִית",
    name_alts=["Final Kaf"],
)
CHAF = HebrewChar(char="כ", name="Chaf", hebrew_name="כַף")
CHAF_SOFIT = FINAL_CHAF = HebrewChar(
    char="ך",
    name="Chaf Sofit",
    final_letter=True,
    hebrew_name="כַף סוֹפִית",
    name_alts=["Final Chaf"],
)
LAMED = LAMID = HebrewChar(
    char="ל", name="Lamed", hebrew_name="לָמֶד", name_alts=["Lamid"]
)
MEM = HebrewChar(char="מ", name="Mem", hebrew_name="מֵם")
MEM_SOFIT = FINAL_MEM = HebrewChar(
    char="ם",
    name="Mem Sofit",
    final_letter=True,
    hebrew_name="מֵם סוֹפִית",
    name_alts=["Final Mem"],
)
NUN = HebrewChar(char="נ", name="Nun", hebrew_name="נוּן")
NUN_SOFIT = FINAL_NUN = HebrewChar(
    char="ן",
    name="Nun Sofit",
    final_letter=True,
    hebrew_name="נוּן סוֹפִית",
    name_alts=["Final Nun"],
)
SAMEKH = SAMACH = HebrewChar(
    char="ס", name="Samekh", hebrew_name="סָמֶך", name_alts=["Samach"]
)
AYIN = HebrewChar(char="ע", name="Ayin", hebrew_name="עַיִן")
PE = HebrewChar(char="פּ", name="Pe", hebrew_name="")
FE = HebrewChar(char="פ", name="Fe", hebrew_name="פֵא")
PE_SOFIT = FINAL_PE = HebrewChar(
    char="ףּ",
    name="Fe Sofit",
    final_letter=True,
    hebrew_name="פֵּא סוֹפִית",
    name_alts=["Final Pe"],
)
FE_SOFIT = FINAL_FE = HebrewChar(
    char="ף",
    name="Fe Sofit",
    final_letter=True,
    hebrew_name="פֵא סוֹפִית",
    name_alts=["Final Fe"],
)
TSADI = TZADIK = HebrewChar(
    char="צ",
    name="Tsadi",
    hebrew_name="צַדִי",
    hebrew_name_alts=["צדיק"],
    name_alts=["Tzadik"],
)
TSADI_SOFIT = FINAL_TSADI = TZADIK_SOFIT = FINAL_TZADIK = HebrewChar(
    char="ץ",
    name="Tsadi Sofit",
    final_letter=True,
    hebrew_name="צַדִי סוֹפִית",
    hebrew_name_alts=["צדיק סופית"],
)
QOF = KUF = HebrewChar(char="ק", name="Qof", hebrew_name="קוֹף", name_alts=["Kuf"])
RESH = HebrewChar(char="ר", name="Resh", hebrew_name="רֵישׁ")
# TODO: The naming here might need help. We should definitely support all 3 versions as this is likely to be found
#  in text, but the naming might be unexpected.
SHIN = HebrewChar(char="שׁ", name="Shin", hebrew_name="שִׁין")
SIN = HebrewChar(char="שׂ", name="Sin", hebrew_name="שִׂין")
PLAIN_SIN = HebrewChar(
    char="ש", name="Plain Sin", hebrew_name="שִׁין", hebrew_name_alts=["שִׂין"]
)
TAV = TAF = HebrewChar(char="תּ", name="Tav", hebrew_name="תּו", name_alts=["Taf"])
SAV = SAF = HebrewChar(char="ת", name="Sav", hebrew_name="תָו", name_alts=["Saf"])
DOUBLE_YOD = DOUBLE_YUD = HebrewChar(
    char="ײ",
    name="Double Yod",
    hebrew_name="",
    name_alts=["Saf"],
    type=HebrewCharTypes.YIDDISH_LETTER,
)
DOUBLE_VAV = DOUBLE_VUV = HebrewChar(
    char="װ",
    name="Double Vav",
    hebrew_name="",
    name_alts=["Double Vuv"],
    type=HebrewCharTypes.YIDDISH_LETTER,
)
VAV_YOD = VAV_YUD = VUV_YOD = VUV_YUD = HebrewChar(
    char="ױ", name="Vav Yod", hebrew_name="", type=HebrewCharTypes.YIDDISH_LETTER
)

# Niqqudot or Vowel characters
SIN_DOT = "ׂ"
SHIN_DOT = "ׁ"
DAGESH = "ּ"
QUBUTS = KUBUTZ = "ֻ"
SHURUK = "וּ"
HOLAM = "ֹ"
QAMATS = KUMATZ = "ָ"
PATAH = PATACH = "ַ"
SEGOL = "ֶ"
TSERE = "ֵ"
HIRIQ = CHIRIK = "ִ"
HATAF_QAMATS = "ֳ"
HATAF_PATAH = "ֲ"
HATAF_SEGOL = "ֱ"
SHEVA = SHIVAH = "ְ"
UPPER_DOT = "ׄ"
NIQQUD = [
    SIN_DOT,
    SHIN_DOT,
    DAGESH,
    QUBUTS,
    HOLAM,
    QAMATS,
    PATAH,
    SEGOL,
    TSERE,
    HIRIQ,
    HATAF_QAMATS,
    HATAF_PATAH,
    HATAF_SEGOL,
    SHEVA,
    UPPER_DOT,
]

# Punctuation characters
MAQAF = "־"
PASEQ = "׀"
SOF_PASSUK = "׃"
ETNAHTA = "֑"
SEGOL_TOP = "֒"
SHALSHELET = "֓"
ZAQEF_QATAN = "֔"
ZAQEF_GADOL = "֕"
TIFCHA = "֖"
REVIA = "֗"
ZINOR = "֮"
PASHTA = "֙"
PASHTA_2 = QADMA = "֨"
YETIV = "֚"
TEVIR = "֛"
PAZER = "֡"
TELISHA_GEDOLA = "֠"
TELISHA_KETANNAH = "֩"
PAZER_GADOL = "֟"
GERESH = "׳"
AZLA_GERESH = "֜"
GERSHAYIM = "״"
GERSHAYIM_2 = "֞"
MERCHA = "֥"
MUNACH = "֣"
MAHPACH = "֤"
DARGA = "֧"
MERCHA_KEFULA = "֦"
YERACH_BEN_YOMO = "֪"
MASORA = "֯"
DEHI = "֭"
ZARQA = "֘"
GERESH_MUQDAM = "֝"
QARNEY_PARA = "֟"
OLA = "֫"
ILUY = "֬"
RAFE = "ֿ"
METEG = "ֽ"
PUNCTUATION = [
    MAQAF,
    PASEQ,
    SOF_PASSUK,
    GERESH,
    GERSHAYIM,
    GERSHAYIM_2,
    RAFE,
    METEG,
    ETNAHTA,
    SEGOL_TOP,
    SHALSHELET,
    ZAQEF_QATAN,
    ZAQEF_GADOL,
    TIFCHA,
    REVIA,
    ZINOR,
    PASHTA,
    PASHTA_2,
    YETIV,
    TEVIR,
    PAZER,
    PAZER_GADOL,
    TELISHA_GEDOLA,
    TELISHA_KETANNAH,
    AZLA_GERESH,
    MERCHA,
    MUNACH,
    MAHPACH,
    DARGA,
    MERCHA_KEFULA,
    YERACH_BEN_YOMO,
    MASORA,
    DEHI,
    ZARQA,
    GERESH_MUQDAM,
    QARNEY_PARA,
    OLA,
    ILUY,
]

# Every instance of _CharMetadata in this file.
# This is used for defining collections with list comprehensions based on the Chars metadata
_ALL_CHARS: List[HebrewChar] = [
    ALEPH,
    BET,
    VET,
    GIMEL,
    DALET,
    HE,
    VAV,
    ZAYIN,
    CHET,
    TET,
    YOD,
    CAF,
    KAF_SOFIT,
    CHAF,
    CHAF_SOFIT,
    LAMED,
    MEM,
    MEM_SOFIT,
    NUN,
    NUN_SOFIT,
    SAMEKH,
    AYIN,
    PE,
    FE,
    PE_SOFIT,
    FE_SOFIT,
    TSADI,
    TSADI_SOFIT,
    QOF,
    RESH,
    SHIN,
    SIN,
    PLAIN_SIN,
    TAV,
    SAV,
    DOUBLE_YOD,
    DOUBLE_VAV,
    VAV_YOD,
]

# A dict of all instances of _CharMetadata supported where the key is the char and the value is its _CharMetadata.
# This is useful for when you have a hebrew char and want to get its _CharMetadata.
CHARS: Dict[str, HebrewChar] = {c.char: c for c in _ALL_CHARS}

# Final letters in the Hebrew Alphabet
FINAL_LETTERS: List[HebrewChar] = [
    c for c in _ALL_CHARS if c.final_letter and len(c.char) == 1
]

YIDDISH_LETTERS: List[HebrewChar] = [
    c for c in _ALL_CHARS if c.type == HebrewCharTypes.YIDDISH_LETTER
]
