"""
    View module to redirect the api and get the lipsync video
"""
import uuid
import logging
from django.conf import settings
from django.shortcuts import render
from lipgan.form import TextForm
from lipgan.audiotovideo import AudioVideo
from lipgan.texttospeech import TextToSpeech
# Create your views here.


logger = logging.getLogger(__name__)


def index(request):
    """
    Get and POST calls
    Get reurn the index
    POST process the data and return the video
    """
    render_return = None
    if request.method == "GET":
        logger.info("index call")
        render_return = render(request, "lipgan/index.html")
    elif request.method == "POST":
        render_return = process_post(request=request)
    return render_return


def process_post(request) -> render:
    """
     Process the post request
    """
    form = TextForm(request.POST)
    render_return = None
    txtspeech = TextToSpeech()
    render_return = render(request, "lipgan/index.html", {
                "url": ""
            })
    if(form.is_valid()):
        audo = AudioVideo()
        uid = str(uuid.uuid1())
        filename = str(uid)+".mp3"
        txtspeech.save(request.POST.get('txtArea'), filename)
        audo.save_video(uid)
        render_return = render(request, "lipgan/index.html", {
                "url": settings.MEDIA_URL+uid+"_voice"+".mp4"
            })

    return render_return
