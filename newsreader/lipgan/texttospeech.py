""""
Convert the text to speech mp3 
"""

from gtts import gTTS
from django.conf import settings


class TextToSpeech:
    """
    Text to speech class
    """

    def __init__(self) -> None:
        self.language = 'en'

    def save(self, string="hello", filename="welcome.mp3"):
        """
        save the audio
        """
        myobj = gTTS(text=string, lang=self.language, slow=False)
        myobj.save(settings.MP3_PATH+"/" + filename)
