# abair_discord_bot

## Eng
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

## GLE
Cuireann an bot seo foghraíocht na Gaeilge ar fáil d'úsáideoirí Discord

Úsáidtear APIs de chuid abair.ie le trascríbhinn IPA agus taifead sintéiseach an fhocail nó na habairte á rá a chur ar fáil 

Cuirtear an bot ar siúl nuair a scrítear '!abair'. Roghnaítear an chanúint leis an gcéad 'fhocal'. Tá trí rogha ann.
- gc = Gaeilge Chonnacht
- gm = Gaolainn na Mumhan
- gu = Gaeilig Uladh

Déanfaidh an bot aithris ar an abairt sa gcainéal a ndearnadh an t-ordú. Beidh aithris ar an abairt i bhfreagra an bhot, agus IPA transcription agus taifead lena gcois.

e.g.
`!abair gc Táim anseo go fóill`

Gheobhaidh an méid sin thuas an freagra thíos
```
Táim anseo go fóill
tˠɑːmʲ əɴˠʃo gˠə fˠoːʟʲ
```
agus taifead den fhoghraíocht lena gcois.
