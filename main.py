import hydra

@hydra.main(version_base=None, config_path="config")
def my_app(cfg):
    print(cfg)

if __name__ == "__main__":
    my_app()