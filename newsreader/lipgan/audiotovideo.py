
"""
 module to handle the audio to video conversion

"""
import os
from django.conf import settings
from lipgan.batch_inference import main


class ParserArgs:
    """
     Class to handle the input params for liptosync
    """
    def __init__(self, checkpoint_path, model, face_det_checkpoint, face, 
                audio, results_dir, 
                results_filename, 
                results_voice_filename,static, 
                fps,max_sec, pads,face_det_batch_size,
                lipgan_batch_size, n_gpu ) -> None:

        self.checkpoint_path = checkpoint_path
        self.model = model
        self.face_det_checkpoint = face_det_checkpoint
        self.face = face
        self.audio = audio
        self.results_dir = results_dir
        self.results_filename = results_filename
        self.results_voice_filename = results_voice_filename
        self.static = static
        self.fps = fps
        self.max_sec = max_sec
        self.pads = pads
        self.face_det_batch_size = face_det_batch_size
        self.lipgan_batch_size = lipgan_batch_size
        self.n_gpu = n_gpu
        self.img_size = 96


class AudioVideo:
    """ convert the audio to video"""
 
    def save_video(self, filename):
        """ Save the video to a file"""
        try:
            path_1 = os.path.join(settings.BASE_DIR,'lipgan/')
            
            checkpoint_path = path_1+"logs/lipgan_residual_mel.h5"
            model = "residual"
            face_det_checkpoint= path_1+'logs/mmod_human_face_detector.dat'
            face=path_1+"logs/image.jpeg" 
            audio = path_1+"logs/"+filename+".mp3"
            results_dir = path_1+"logs/result/" 
            results_filename = path_1+"logs/result/"+filename+".mp4" 
            results_voice_filename = path_1+"logs/result/" +filename +"_voice.mp4"
            static = True
            fps = 25
            max_sec = 240
            pads = [0, 0, 0, 0]
            face_det_batch_size = 64
            lipgan_batch_size =256
            n_gpu = 1

            args = ParserArgs(checkpoint_path=checkpoint_path, 
                               model= model, 
                               face_det_checkpoint=face_det_checkpoint,
                               face=face,
                               audio=audio,
                               results_dir=results_dir,
                               results_filename=results_filename,
                               results_voice_filename=results_voice_filename,
                               static=static,
                               fps=fps,
                               max_sec=max_sec,
                               pads=pads,
                               face_det_batch_size=face_det_batch_size,
                               lipgan_batch_size=lipgan_batch_size,
                               n_gpu=n_gpu

                               )
            main(args)
        except Exception as ex:
            print({"status": "failed", "output":str(ex)})
        
        print("success")
        


