import aiohttp

async def get_pronunciation_text_and_voice(word):

    text_request_payload_form = aiohttp.FormData()
    text_request_payload_form.add_field("abairt", word)
    text_request_payload_form.add_field("slang", "gd")
    text_request_payload_form.add_field("wholeword", "true")


    async with aiohttp.ClientSession() as session:
        async with session.post("https://learngaelic.scot/dictionary/search",
                                data=text_request_payload_form) as resp:

            if resp.status != 200:
                return None

            response_json = await resp.json()

            if len(response_json) == 0:
                return None

            recording_id = response_json[0]['id']

            async with session.get(f"https://s3-eu-west-1.amazonaws.com/lg-dic/{recording_id}.webm",
                                    data=text_request_payload_form) as resp:

                if resp.status != 200:
                    return response_json[0]['ipa'], None

                audio = await resp.read()

                return response_json[0]['ipa'], audio

async def get_recommendations(word):

    text_request_payload_form = aiohttp.FormData()
    text_request_payload_form.add_field("q", word)
    async with aiohttp.ClientSession() as session:
        async with session.post("https://learngaelic.scot/dictionary/suggest",
                                data=text_request_payload_form) as resp:
            if resp.status != 200:
                return None

            response_json = await resp.json()

            if len(response_json) == 0:
                return None

            return response_json
