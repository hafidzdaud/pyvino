from .object_detector import ObjectDetector


class FaceDetector(ObjectDetector):
    def __init__(self, device=None,
                 model_fp=None, model_dir=None,
                 cpu_extension=None, path_config=None):
        self.task = 'detect_face'
        super().__init__(self.task, device,
                         model_fp, model_dir,
                         cpu_extension, path_config)
