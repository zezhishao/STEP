import sys
sys.path.append('../..')
from argparse import ArgumentParser

from easytorch import launch_training
import setproctitle
setproctitle.setproctitle("STEP")

def parse_args():
    parser = ArgumentParser(description='Welcome to EasyTorch!')
    # pre-training
    # parser.add_argument('-c', '--cfg', default='config/METR-LA/pretraining.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='config/PEMS-BAY/pretraining.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='config/PEMS04/pretraining.py', help='training config')

    # forecasting
    parser.add_argument('-c', '--cfg', default='config/METR-LA/forecasting.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='config/PEMS-BAY/forecasting.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='config/PEMS04/forecasting.py', help='training config')

    parser.add_argument('--gpus', default=None, help='visible gpus')
    parser.add_argument('--tf32', default=True, help='enable tf32 on Ampere device')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    launch_training(args.cfg, args.gpus, args.tf32)
