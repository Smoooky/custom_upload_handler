from django.core.files.uploadhandler import TemporaryFileUploadHandler


class ProgressBarUploadHandler(TemporaryFileUploadHandler):
    """
    Custom upload handler that displays progress bar when uploading
    """
    def __init__(self, request=None):
        self.current_size = 0
        self.name = request.POST.get('name')
        super(ProgressBarUploadHandler, self).__init__(request)

    def receive_data_chunk(self, raw_data, start):
        self.current_size += len(raw_data)
        print(self.current_size)
        super(ProgressBarUploadHandler, self).receive_data_chunk(raw_data, start)