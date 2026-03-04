import asyncio
import edge_tts
#list_of_voices
#fil-PH-AngeloNeural
#fil-PH-BlessicaNeural
#en-PH-JamesNeural
#en-PH-RosaNeural
async def main():

    dialogues = [
        ("tagal tagal na non", "fil-PH-AngeloNeural"),
        ("pero yung matagal na yun nandito pa rin!", "fil-PH-BlessicaNeural"),
        ("that was just one mistake, isa lang", "fil-PH-AngeloNeural"),
        ("ni isa, dalawa, tatlo pareho lang yun! sumawsaw ka pa rin sa iba!", "fil-PH-BlessicaNeural"),
        ("lasing ako non", "fil-PH-AngeloNeural"),
        ("lintek na palusot yun kahit lasing ka alam mo ginagawa mo!", "fil-PH-BlessicaNeural"),
        ("kaya nga, nag sorry agad ako sayo non diba kasi kahit anong sabihin ko, i was wrong, nagkamali ako nasaktan kita", "fil-PH-AngeloNeural"),
        ("kayong mga lalaki akala niyo pag nangbabae kayo nasasaktan niyo lang kami makikipagchukchakan kayo tapos ini expect niyo iiyak lang kami itutulog lang saglit tapos pag gising okay na? yun ang pangarap namin sana nga ganon lang kadali yun am i not enough? may kulang ba sakin? may mali ba sakin? kapapalit palit bako?", "fil-PH-BlessicaNeural"),
        ("no", "fil-PH-AngeloNeural"),
        ("then why! bakit mo ko nagawang lokohin??!!", "fil-PH-BlessicaNeural"),
    ]

    with open("conversation.mp3", "wb") as audio_file:
        for text, voice in dialogues:
            communicate = edge_tts.Communicate(text, voice)
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_file.write(chunk["data"])

asyncio.run(main())