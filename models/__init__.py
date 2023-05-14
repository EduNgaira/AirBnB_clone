#!/usr/bin/python3
"""__init__ file fordirectory initialization"""
import models.engine.file_storage


storage = models.engine.file_storage.FileStorage()
storage.reload()
