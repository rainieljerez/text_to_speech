import asyncio
import edge_tts
#fil-PH-AngeloNeural
#fil-PH-BlessicaNeural
#en-PH-JamesNeural
#en-PH-RosaNeural
async def main():
    tts = edge_tts.Communicate("mabuhay ako si angelo", "fil-PH-AngeloNeural")
    tts = edge_tts.Communicate("mabuhay ako si blessica", "fil-PH-BlessicaNeural")
    await tts.save ("mabuhay introduction.mp3")

asyncio.run(main())
