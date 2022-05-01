import requests
import xml.etree.ElementTree as ET
from map_phoneme import map_phoneme 



test_xml ="""<?xml version="1.0"?>
<utterance input_string="beidh scr&#xFA;d&#xFA; agam am&#xE1;rach" name="20220501_183110_505437.xml">
<sentence input_string="beidh scr&#xFA;d&#xFA; agam am&#xE1;rach" audio_file="/tmp/01ed9233-9e99-493d-a29d-22547bc23077.wav" soundfilename="20220501_183110_505437_001">
<token input_string="SILENCE_TOKEN">
<word input_string="SILENCE_TOKEN" trans_source="Utterance.py" trans_output_format="final">
<syllable>
<phoneme symbol="sil"/>
</syllable>
</word>
</token>
<token input_string="beidh">
<word input_string="beidh" trans_source="res/dictionaries/ga_GD/lexicon_gaoth_dobhair.txt++">
<syllable stress="1">
<phoneme symbol="bj"/>
<phoneme symbol="ee"/>
<phoneme symbol="gfj"/>
</syllable>
</word>
</token>
<token input_string="scr&#xFA;d&#xFA;">
<word input_string="scr&#xFA;d&#xFA;" trans_source="res/dictionaries/ga_GD/lexicon_gaoth_dobhair.txt++">
<syllable stress="1">
<phoneme symbol="s"/>
<phoneme symbol="k"/>
<phoneme symbol="r"/>
<phoneme symbol="uu"/>
</syllable>
<syllable stress="0">
<phoneme symbol="d"/>
<phoneme symbol="uu"/>
</syllable>
</word>
</token>
<token input_string="agam">
<word input_string="agam" trans_source="res/dictionaries/ga_GD/lexicon_gaoth_dobhair.txt++">
<syllable stress="1">
<phoneme symbol="@"/>
</syllable>
<syllable stress="0">
<phoneme symbol="g"/>
<phoneme symbol="@"/>
<phoneme symbol="m"/>
</syllable>
</word>
</token>
<token input_string="am&#xE1;rach">
<word input_string="am&#xE1;rach" trans_source="res/dictionaries/ga_GD/lexicon_gaoth_dobhair.txt++">
<syllable stress="0">
<phoneme symbol="@"/>
</syllable>
<syllable stress="1">
<phoneme symbol="m"/>
<phoneme symbol="aa"/>
</syllable>
<syllable stress="0">
<phoneme symbol="r"/>
<phoneme symbol="a"/>
<phoneme symbol="h"/>
</syllable>
</word>
</token>
<token input_string="SILENCE_TOKEN">
<word input_string="SILENCE_TOKEN" trans_source="Utterance.py" trans_output_format="final">
<syllable>
<phoneme symbol="sil"/>
</syllable>
</word>
</token>
<selection>
<selection_item source_middle="None" source="nnmnkwii" segment="bj" synth_end="0.34"/>
<selection_item source_middle="None" source="nnmnkwii" segment="ee" synth_end="0.37"/>
<selection_item source_middle="None" source="nnmnkwii" segment="gfj" synth_end="0.43"/>
<selection_item source_middle="None" source="nnmnkwii" segment="s" synth_end="0.615"/>
<selection_item source_middle="None" source="nnmnkwii" segment="k" synth_end="0.71"/>
<selection_item source_middle="None" source="nnmnkwii" segment="r" synth_end="0.75"/>
<selection_item source_middle="None" source="nnmnkwii" segment="uu" synth_end="0.85"/>
<selection_item source_middle="None" source="nnmnkwii" segment="d" synth_end="0.98"/>
<selection_item source_middle="None" source="nnmnkwii" segment="uu" synth_end="1.075"/>
<selection_item source_middle="None" source="nnmnkwii" segment="@" synth_end="1.14"/>
<selection_item source_middle="None" source="nnmnkwii" segment="g" synth_end="1.245"/>
<selection_item source_middle="None" source="nnmnkwii" segment="@" synth_end="1.285"/>
<selection_item source_middle="None" source="nnmnkwii" segment="m" synth_end="1.385"/>
<selection_item source_middle="None" source="nnmnkwii" segment="@" synth_end="1.42"/>
<selection_item source_middle="None" source="nnmnkwii" segment="m" synth_end="1.54"/>
<selection_item source_middle="None" source="nnmnkwii" segment="aa" synth_end="1.665"/>
<selection_item source_middle="None" source="nnmnkwii" segment="r" synth_end="1.76"/>
<selection_item source_middle="None" source="nnmnkwii" segment="a" synth_end="1.825"/>
<selection_item source_middle="None" source="nnmnkwii" segment="h" synth_end="1.895"/>
</selection>
</sentence>
</utterance>
"""


def get_pronounciation(input_string):
	payload = {"dialect":(None,"ga_UL"), "inputText": (None,input_string), "synth-mode":(None,"dnn"), "speed":(None,"1.0"), "pitch":(None, "1.0"), "speaker":(None,"female")}

	request_cookies = {"privacy":"accepted","synthInput":input_string}
	response = requests.post("https://abair.ie/action/synthesize", cookies=request_cookies, files=payload) 


	xml = ET.fromstring(response.content)

	soundFileURI = xml.find('sentence').get('soundfilename')
	soundFileURL = "https://abair.ie/audio/" + soundFileURI + ".mp3"
	xpath = ".//word"
	words = xml.findall(xpath)

	result = ''
	for word in words:
			if word.get('input_string') == "SILENCE_TOKEN":
				continue
			for syllable in word:
				for phoneme in syllable:
					#result += PHONEME_MAP[phoneme.get('symbol')]
					result += map_phoneme(phoneme.get('symbol'))
			result += ' '
	
	soundFile = requests.get(soundFileURL, cookies=request_cookies)
	
	return (result, soundFile.content)
