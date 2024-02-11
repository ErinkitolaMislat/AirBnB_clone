#!/usr/bin/python3
"""__init__ dunder method for models directory"""
from AirBnB_clone.models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
