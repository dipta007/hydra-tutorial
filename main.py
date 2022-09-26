import hydra
import json
import omegaconf

import logging
log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="config", config_name='root')
def my_app(cfg):
    config = omegaconf.OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)
    config = dict(config)
    log.info(json.dumps(config, indent=2))
    dataset = hydra.utils.instantiate(cfg.data.train)

if __name__ == "__main__":
    my_app()