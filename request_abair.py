import requests
import xml.etree.ElementTree as ET
from constants import map_phoneme
from constants import DIALECTS_VOICE
import json
import base64
import aiohttp



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

synthesise_request_text = """{"synthinput":{
"text":"cén chaoi a bhfuil tú\n","ssml":"string"},"voiceparams":{"languageCode":"ga-IE","name":"ga_CO_snc_nemo","ssmlGen
der":"UNSPECIFIED"},"audioconfig":{"audioEncoding":"LINEAR16","speakingRate":1,"pitch":1,"volumeGainDb":1,"htsParams":"s
tring","sampleRateHertz":0,"effectsProfileId":[]},"outputType":"JSON"}"""


async def get_pronounciation_text(input_string, dialect):
	text_request_payload = {"dialect":dialect, "inputText": input_string, "synth-mode":"dnn", "speed":"1.0", "pitch": "1.0", "speaker":"female"}
	text_request_payload_form = aiohttp.FormData()
	
	for key, value in text_request_payload.items():
		text_request_payload_form.add_field(key, value)
	request_cookies = {"privacy":"accepted","synthInput":input_string}
	
	async with aiohttp.ClientSession() as session:
		async with session.post("https://abair.ie/action/synthesize", cookies=request_cookies, data=text_request_payload_form) as resp:
			
			if resp.status != 200:
				return None
			
			response_text = await resp.text()
			
			xml = ET.fromstring(response_text)
			
			xpath = ".//word"
			words = xml.findall(xpath)
			
			result = ''
			for word in words:
					if word.get('input_string') == "SILENCE_TOKEN":
						continue
					for syllable in word:
						for phoneme in syllable:
							#result += PHONEME_MAP[phoneme.get('symbol')]
							if phoneme.get('symbol') == 'sil':
								continue
							result += map_phoneme(phoneme.get('symbol'), dialect)
					result += ' '
			return result
	
	
async def get_pronounciation_voice(input_string, dialect):
	request_cookies = {"privacy":"accepted","synthInput":input_string}
	
	voice_request_payload = json.loads(synthesise_request_text, strict=False)
	voice_request_payload["synthinput"]["text"] = input_string + "\n"
	voice_request_payload["voiceparams"]["name"] = DIALECTS_VOICE[dialect]
	
	async with aiohttp.ClientSession() as session:
		async with session.post("https://abair.ie/api2/synthesise", headers={"Content-Type":"application/json"}, data=json.dumps(voice_request_payload)) as resp:
			if resp.status != 200:
				return None
			
			responce_voice_json = await resp.json()
			
			audio = base64.standard_b64decode(responce_voice_json["audioContent"])
			
			return audio
	
	

	
async def get_pronounciation(input_string, dialect):
	pronounciation_voice_promise = get_pronounciation_voice(input_string, dialect)
	pronounciation_text_promise = get_pronounciation_text(input_string, dialect)
	
	return (await pronounciation_text_promise, await pronounciation_voice_promise)
