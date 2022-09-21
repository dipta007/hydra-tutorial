import hydra
import torch

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    model = torch.nn.Linear(10, 2)
    optimizer = hydra.utils.instantiate(cfg.train.optimizer)(model.parameters())
    print(type(optimizer))

if __name__ == "__main__":
    my_app()