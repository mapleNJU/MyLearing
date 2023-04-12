import time
import torch
import numpy as np
from train_eval import train, init_network, test
from model import Config, TextCNN
import argparse
parser = argparse.ArgumentParser(description='Chinese Text Classification')
parser.add_argument('--train', default='y',choices=['y','n'], type=str, help='y for Train, n for Test')
args = parser.parse_args()
if __name__ == '__main__':

    dataset = 'Mydata'  # 数据集
    embedding = 'embedding_SougouNews.npz'
    model_name = 'TextCNN'  
    from utils import build_dataset, build_iterator
    config = Config(dataset, embedding)
    np.random.seed(1)

    # 固定网络结构
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True

    start_time = time.time()
    vocab, train_data, dev_data, test_data = build_dataset(config)
    train_iter = build_iterator(train_data, config)
    dev_iter = build_iterator(dev_data, config)
    test_iter = build_iterator(test_data, config,test = True)
    
    config.n_vocab = len(vocab)
    model = TextCNN(config).to(config.device)
    
    # train
    if args.train == 'y':
        init_network(model)
        train(config, model, train_iter, dev_iter)
    # test
    else:
        print("This is Test")
        test(config, model, test_iter)
