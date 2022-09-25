import hydra
import logging

# logger for this file
log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    log.debug("Debug")
    log.info("Info")
    log.warning("Warning")

if __name__ == "__main__":
    my_app()