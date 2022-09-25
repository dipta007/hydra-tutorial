import hydra

@hydra.main(version_base=None, config_path="config", config_name="root")
def my_app(cfg):
    print(cfg.train.enc_hid_size)
    print(cfg['train']['enc_hid_size'])
    print(cfg.train.dec_hid_size)

    cfg.train.vocab_size = 40000
    print(cfg.train.vocab_size)

if __name__ == "__main__":
    my_app()