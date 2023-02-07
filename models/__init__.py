import models.engine.file_storage
import importlib


storage = models.engine.file_storage.FileStorage()
importlib.reload(models.engine.file_storage)
