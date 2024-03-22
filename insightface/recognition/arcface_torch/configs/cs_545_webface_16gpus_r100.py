from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.margin_list = (1.0, 0.0, 0.4)
config.network = "r100"
config.resume = False
config.output = None
config.embedding_size = 512
config.sample_rate = 0.2
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 5e-4
config.batch_size = 256
config.lr = 0.3
config.verbose = 2000
config.dali = False

config.rec = "/train/faces_webface_112x112"
config.num_classes = 10572
config.num_image = 490623
config.num_epoch = 20
config.warmup_epoch = 1
config.val_targets = ["lfw", "cfp_fp", "agedb_30"]
