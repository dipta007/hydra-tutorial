import logging

log = logging.getLogger(__name__)

class BigDataset:
    def __init__(self, path, batch_size):
        log.info(f'Big Dataset -> {path}, {batch_size}')