import logging

log = logging.getLogger(__name__)

class SmallDataset:
    def __init__(self, path, batch_size):
        log.info(f'Small Dataset -> {path}, {batch_size}')