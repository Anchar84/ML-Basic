from abc import ABC, abstractmethod

# базовая метоинформация файла, общая для всех типов файлов
class Metadata:

    def __init__(self, name, size, create_dt, update_dt, owner):
        self._name = name
        self._size = size
        self._create_dt = create_dt
        self._update_dt = update_dt
        self._owner = owner

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def create_dt(self):
        return self._create_dt
    
    @property
    def update_dt(self):
        return self._update_dt
    
    @property
    def owner(self):
        return self._owner

# базовая абстракция для чтенья и записи файла
class BytesStream(ABC):

    @abstractmethod
    def get_bytes(self):
        # возвращает байты файла, наследники имплементируют конкретную реализацию
        pass

    @abstractmethod
    def save_bytes(self):
        # записывает байты файла, наследники имплементируют конкретную реализацию
        pass

class BaseFile:

    def __init__(self, bytes_stream):
        # для чтенье и записи байтов файлов используется bytes_stream
        pass

    def load_file(self):
        # загрузка файла с помощью bytes_stream
        pass

    def write_file(self):
        # запись файла с помощью bytes_stream
        pass

    @abstractmethod
    def get_metadata(self):
        pass

class AudioMetadata:
    
    def __init__(self, bitrate, duration):
        self._bitrate = bitrate
        self._duration = duration

    @property
    def bitrate(self):
        return self._bitrate
    
    @property
    def duration(self):
        return self._duration
    
class AudioFile(BaseFile):
    def get_audiodata(self):
        pass

    def set_bitrate(self, bitrate):
        pass

    def set_duration(self, duration):
        pass

class VideoMetadata:
    
    def __init__(self, resolution, fps):
        self._resolution = resolution
        self._fps = fps

    @property
    def resolution(self):
        return self._resolution
    
    @property
    def fps(self):
        return self._fps
    
class VideoFile(BaseFile):
    def get_videodata(self):
        pass

    def set_resolution(self, resolution):
        pass

    def set_fps(self, fps):
        pass

class PhotoMetadata:
    
    def __init__(self, format, resolution):
        self._format = format
        self._resolution = resolution

    @property
    def resolution(self):
        return self._resolution
    
    @property
    def format(self):
        return self._format
    
class PhotoFile(BaseFile):
    def get_photodata(self):
        pass

    def set_resolution(self, resolution):
        pass

    def set_format(self, format):
        pass
