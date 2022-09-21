import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    print(cfg)

if __name__ == "__main__":
    my_app()