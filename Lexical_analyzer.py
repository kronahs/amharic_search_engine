import re

common_amh_abbreveations = {
  "ት/ቤት": "ትምህርት ቤት",
  "ት/ርት": "ትምህርት",
  "ት/ክፍል": "ትምህርት ክፍል",
  "ሃ/አለቃ": "ሃምሳ አለቃ",
  "ሃ/ስላሴ": "ሃይለ ስላሴ",
  "ደ/ዘይት": "ደብረ ዘይት",
  "ደ/ታቦር": "ደብረ ታቦር",
  "መ/ር": "መምህር",
  "መ/ቤት": "መስሪያ ቤት",
  "መ/አለቃ": "መቶ አለቃ",
  "ክ/ከተማ": "ክፍለ ከተማ",
  "ክ/ሀገር": "ክፍለ ሀገር",
  "ወ/ር": "",
  "ወ/ሮ": "ወይዘሮ",
  "ወ/ሪት": "ወይዘሪት",
  "ወ/ስላሴ": "ወልደ ስላሴ",
  "ፍ/ስላሴ": "ፍቅረ ስላሴ",
  "ፍ/ቤት": "ፍርድ ቤት",
  "ጽ/ቤት": "ጽህፈት ቤት",
  "ሲ/ር": "",
  "ፕ/ር": "ፕሮፌሰር",
  "ጠ/ሚንስትር": "ጠቅላይ ሚኒስተር",
  "ዶ/ር": "ዶክተር",
  "ገ/ገዮርጊስ": "",
  "ቤ/ክርስትያን": "ቤተ ክርስትያን",
  "ም/ስራ": "",
  "ም/ቤት": "ምክር ቤተ",
  "ተ/ሃይማኖት": "ተክለ ሃይማኖት",
  "ሚ/ር": "ሚኒስትር",
  "ኮ/ል": "ኮሎኔል",
  "ሜ/ጀነራል": "ሜጀር ጀነራል"
}
def lexAnalyze(corpus):
    # Remove abbreviations
    for key in common_amh_abbreveations:
        regex = re.compile(re.escape(key))
        corpus = regex.sub(common_amh_abbreveations[key], corpus)
        # Remove punctuation, numbers, and hyphens
    corpus = re.sub(r'[.\?"\',/#!$%^&*;:፣፤።{}=\-_`~()0-9፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻]+', ' ', corpus)
    # Remove extra spaces
    corpus = re.sub(r'\s{2,}', ' ', corpus)
    return corpus