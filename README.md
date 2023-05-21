# abair_discord_bot

This bot allows users to get the pronounciation of Irish words in the discord app. 

Uses APIs provided by abair.ie to provide the IPA trasncription as well as a synthisised recording of the word/sentence being pronounced.

Bot is triggered by the comment '!abair'. First 'word' is what dialet the user desires for a generalised choice of three
- gc = Gaeilge Chonnacht
- gm = Gaeilge na Mumhan
- gu = Gaeilge Uladh
followed by the sentence the user wants transcribed.

The bot will repeat the sentence back into the same channel where the command was invoked, repeating the sentence the user entered, followed by the IPA transcription.
A recording will be attached.
e.g.
`!abair gc Táim anseo go fóill`
will get the response
```
Táim anseo go fóill
tˠɑːmʲ əɴˠʃo gˠə fˠoːʟʲ
```
with the pronounciation recording attached.
