import hydra

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    dummy = hydra.utils.instantiate(cfg.train.dummy)

if __name__ == "__main__":
    my_app()