import hydra

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    activation = hydra.utils.instantiate(cfg.train.activation)
    print(activation, type(activation))

if __name__ == "__main__":
    my_app()