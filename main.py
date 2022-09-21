import hydra

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    trainer = hydra.utils.instantiate(cfg.train.activation)
    trainer.run()

if __name__ == "__main__":
    my_app()