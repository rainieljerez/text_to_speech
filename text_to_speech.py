import asyncio
import edge_tts
#fil-PH-AngeloNeural
#fil-PH-BlessicaNeural
#en-PH-JamesNeural
#en-PH-RosaNeural
async def main():
    tts = edge_tts.Communicate("isa dalawa tatlo you will never be celine", "fil-PH-AngeloNeural")
    tts = edge_tts.Communicate("isa dalawa tatlo you will never be celine", "fil-PH-AngeloNeural")
    await tts.save ("test.mp3")

asyncio.run(main())
