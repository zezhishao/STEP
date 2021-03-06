import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from easydict import EasyDict
from Runner_TSFormer import TSFormerRunner

DATASET_NAME = "PEMS04"

CFG = EasyDict()
BATCH_SIZE  = 8
PATCH_SIZE  = 12
WINDOW_SIZE = 288 * 7 * 2
HIDDEN_DIM  = 96
L           = 4
EPOCHES     = 200
NUM_WORKERS = 2
PIN_MEMORY  = True
PREFETCH    = True
GPU_NUM     = 2
SEED        = 0
MASK_RATIO  = 0.75

# General
CFG.Description = "TSFormer@EZ torch"
CFG.RUNNER = TSFormerRunner
CFG.DATASET_NAME = DATASET_NAME
CFG.INDEX = 12
CFG.FIND_UNUSED_PARAMETERS = False 
CFG.USE_GPU = True if GPU_NUM >0 else False
CFG.GPU_NUM = GPU_NUM
CFG.SEED = SEED
CFG.CUDNN_ENABLED = True
# Model
CFG.MODEL = EasyDict()
CFG.MODEL.NAME = "TSFormer"
CFG.MODEL.PARAM = {
    "patch_size":PATCH_SIZE,
    "in_channel":1,
    "out_channel":HIDDEN_DIM,
    "dropout":0.1,
    "mask_size":WINDOW_SIZE/PATCH_SIZE,
    "mask_ratio":MASK_RATIO,
    "L":L,
    "spectral":False
}

# Train
CFG.TRAIN = EasyDict()
CFG.TRAIN.CKPT_SAVE_STRATEGY = "SaveEveryEpoch"
CFG.TRAIN.NUM_EPOCHS = EPOCHES
CFG.TRAIN.CKPT_SAVE_DIR = os.path.join(
    'checkpoints',
    '_'.join([CFG.MODEL.NAME, str(CFG.TRAIN.NUM_EPOCHS)])
)
## DATA
CFG.TRAIN.DATA = EasyDict()
CFG.TRAIN.DATA.SEQ_LEN = WINDOW_SIZE
CFG.TRAIN.DATA.DIR = "datasets/"+CFG.DATASET_NAME
CFG.TRAIN.DATA.PREFETCH = PREFETCH
CFG.TRAIN.DATA.BATCH_SIZE = BATCH_SIZE
CFG.TRAIN.DATA.SHUFFLE = True
CFG.TRAIN.DATA.NUM_WORKERS = NUM_WORKERS
CFG.TRAIN.DATA.PIN_MEMORY = PIN_MEMORY
## OPTIM
CFG.TRAIN.OPTIM = EasyDict()
CFG.TRAIN.OPTIM.TYPE = "AdamW"
CFG.TRAIN.OPTIM.PARAM= {
    "lr":0.001,
    "weight_decay":0,
    "eps":1.0e-8,
    "betas":(0.9, 0.95)
}
CFG.TRAIN.LR_SCHEDULER = EasyDict()
CFG.TRAIN.LR_SCHEDULER.TYPE = "MultiStepLR"
CFG.TRAIN.LR_SCHEDULER.PARAM= {
    "milestones":[50],
    "gamma":0.5
}
# Validate
CFG.VAL = EasyDict()
CFG.VAL.INTERVAL = 1
CFG.VAL.DATA = EasyDict()
CFG.VAL.DATA.SEQ_LEN = WINDOW_SIZE
CFG.VAL.DATA.DIR = CFG.TRAIN.DATA.DIR
CFG.VAL.DATA.PREFETCH = CFG.TRAIN.DATA.PREFETCH
CFG.VAL.DATA.BATCH_SIZE = CFG.TRAIN.DATA.BATCH_SIZE
CFG.VAL.DATA.SHUFFLE = False
CFG.VAL.DATA.NUM_WORKERS = CFG.TRAIN.DATA.NUM_WORKERS
CFG.VAL.DATA.PIN_MEMORY = PIN_MEMORY
# Validate
CFG.TEST = EasyDict()
CFG.TEST.INTERVAL = 1
CFG.TEST.DATA = EasyDict()
CFG.TEST.DATA.SEQ_LEN = WINDOW_SIZE
CFG.TEST.DATA.DIR = CFG.TRAIN.DATA.DIR
CFG.TEST.DATA.PREFETCH = CFG.TRAIN.DATA.PREFETCH
CFG.TEST.DATA.BATCH_SIZE = CFG.TRAIN.DATA.BATCH_SIZE
CFG.TEST.DATA.SHUFFLE = False
CFG.TEST.DATA.NUM_WORKERS = CFG.TRAIN.DATA.NUM_WORKERS
CFG.TEST.DATA.PIN_MEMORY = PIN_MEMORY
