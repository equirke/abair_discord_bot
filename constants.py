
PHONEME_MAP = {
  "a":"a",
  "e":"e",
  "i":"i",
  "o":"o",
  "o_o":"ɔ",
  "u":"u",
  "aa":"ɑː",
  "ee":"eː",
  "ii":"iː",
  "oo":"oː",
  "uu":"uː",
  "@":"ə",
  ## diphthongs
  "i@":"iə",
  "u@":"uə",
  # broad / velarized
  "b":"bˠ",
  "d":"dˠ",
  "f":"fˠ",
  "g":"gˠ",
  "gf":"ɣ",
  "k":"kˠ",
  "l":"lˠ",
  "ll":"ʟˠ",
  "m":"mˠ",
  "n":"nˠ",
  "ng":"ŋ",
  "nn":"ɴˠ",
  "p":"pˠ",
  "r":"ɾˠ",
  "s":"sˠ",
  "t":"tˠ",
  "v":"w",
  "x":"x",
  # slender / palatalized
  "bj":"bʲ",
  "dj":"dʲ",
  "fj":"fʲ",
  "gj":"ɟ",
  "gfj":"j",
  "kj":"c",
  "lj":"lʲ",
  "llj":"ʟʲ",
  "mj":"mʲ",
  "nj":"nʲ",
  "ngj":"ɲ",
  "nnj":"ɴʲ",
  "pj":"pʲ",
  "rj":"ɾʲ",
  "sj":"ʃ",
  "tj":"tʲ",
  "vj":"vʲ",
  "xj":"ç",
  # voiceless velarized
  "l_d":"l̪ˠ",
  "ll_d":"l̪ˠ",
  "n_d":"n̪ˠ",
  "nn_d":"n̪ˠ",
  "r_d":"r̪ˠ",
  # voiceless palatalized
  "lj_d":"l̪ʲ",
  "llj_d":"l̪ʲ",
  "nj_d":"n̪ʲ",
  "nnj_d":"n̪ʲ",
  "rj_d":"r̪ʲ"
}

GD_PHOMEME_MAP = {
  "aa":"aː"
}

CD_PHOMEME_MAP = {
  "v":"vˠ"
}

def map_phoneme(c, dialect):
	if dialect == "ga_MU" and c in CD_PHOMEME_MAP:
		return CD_PHOMEME_MAP[c]
	if dialect == "ga_UL" and c in GD_PHOMEME_MAP:
		return GD_PHOMEME_MAP[c]
	if c not in PHONEME_MAP:
		return c
	return PHONEME_MAP[c]

DIALECTS = {
  "CD":"ga_MU",
  "GD":"ga_UL",
  "CO":"ga_CO"
}

def map_dialect(d):
	if d not in DIALECTS:
		return None
	return DIALECTS[d]