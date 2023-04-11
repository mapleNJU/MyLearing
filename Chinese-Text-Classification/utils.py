import os
import torch
import numpy as np
import pickle as pkl
import re


MAX_VOCAB_SIZE = 10000  # 字表长度限制
UNK, PAD = '<UNK>', '<PAD>'  # 未知字，padding符号

# 构建字表
def build_vocab(file_path, tokenizer):
    vocab_dic = {}
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            lin = line.strip()
            if not lin:
                continue
            content = lin[2:].replace(" ","")
            content = re.sub(r'[0-9]+', '', content)
            for word in tokenizer(content):
                vocab_dic[word] = vocab_dic.get(word, 0) + 1
        vocab_list = sorted([_ for _ in vocab_dic.items()], key=lambda x: x[1], reverse=True)
        vocab_dic = {word_count[0]: idx for idx, word_count in enumerate(vocab_list)}
        vocab_dic.update({UNK: len(vocab_dic), PAD: len(vocab_dic) + 1})
    return vocab_dic


def build_dataset(config):
    tokenizer = lambda x: [y for y in x]  # char-level
    if os.path.exists(config.vocab_path):
        vocab = pkl.load(open(config.vocab_path, 'rb'))
    else:
        vocab = build_vocab(config.train_path, tokenizer=tokenizer)
        pkl.dump(vocab, open(config.vocab_path, 'wb'))

    def load_dataset(path, pad_size=64,test = False):
        contents = []
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f:
                lin = line.strip()
                if not lin:
                    continue
                if test == False:
                    label = lin[0]
                    content = lin[2:].strip()
                else:
                    content = lin
                content = lin[2:].replace(" ","")
                content = re.sub(r'[0-9]+', '', content)
                words_line = []
                token = tokenizer(content)
                seq_len = len(token)
                if pad_size:
                    if len(token) < pad_size:
                        token.extend([PAD] * (pad_size - len(token)))
                    else:
                        token = token[:pad_size]
                        seq_len = pad_size
                # word to id
                for word in token:
                    words_line.append(vocab.get(word, vocab.get(UNK)))
                if test == False:
                    contents.append((words_line, int(label), seq_len))
                else:
                    contents.append((words_line, seq_len))
            return contents  # [([...], 0), ([...], 1), ...]
    train = load_dataset(config.train_path, config.pad_size)
    dev = load_dataset(config.dev_path, config.pad_size)
    test = load_dataset(config.test_path, config.pad_size,test = True)
    return vocab, train, dev, test


class DatasetIterater(object):
    def __init__(self, batches, batch_size, device,test = False):
        self.batch_size = batch_size
        self.batches = batches
        self.test = test
        self.n_batches = len(batches) // batch_size
        self.residue = False  # 记录batch数量是否为整数
        if len(batches) % self.n_batches != 0:
            self.residue = True
        self.index = 0
        self.device = device
    def _to_tensor(self, datas):
        if self.test != True:
            x = torch.LongTensor([_[0] for _ in datas]).to(self.device)
            y = torch.LongTensor([_[1] for _ in datas]).to(self.device)

        # pad前的长度(超过pad_size的设为pad_size)
            seq_len = torch.LongTensor([_[2] for _ in datas]).to(self.device)
            return (x, seq_len), y
        else:
            x = torch.LongTensor([_[0] for _ in datas]).to(self.device)
            seq_len = torch.LongTensor([_[1] for _ in datas]).to(self.device)
            return (x, seq_len)
    def __next__(self):
        if self.residue and self.index == self.n_batches:
            batches = self.batches[self.index * self.batch_size: len(self.batches)]
            self.index += 1
            batches = self._to_tensor(batches)
            return batches

        elif self.index >= self.n_batches:
            self.index = 0
            raise StopIteration
        else:
            batches = self.batches[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            self.index += 1
            batches = self._to_tensor(batches)
            return batches

    def __iter__(self):
        return self

    def __len__(self):
        if self.residue:
            return self.n_batches + 1
        else:
            return self.n_batches


def build_iterator(dataset, config,test = False):
    iter = DatasetIterater(dataset, config.batch_size, config.device,test)
    return iter


if __name__ == "__main__":
    '''提取预训练字向量'''
    train_dir = "./Mydata/data/train.txt"
    vocab_dir = "./Mydata/data/vocab.pkl"
    pretrain_dir = "./Mydata/data/sgns.sogou.char"
    emb_dim = 300
    filename_trimmed_dir = "./Mydata/data/embedding_SougouNews"
    if os.path.exists(vocab_dir):
        word_to_id = pkl.load(open(vocab_dir, 'rb'))
    else:
        tokenizer = lambda x: [y for y in x]
        word_to_id = build_vocab(train_dir, tokenizer=tokenizer)
        pkl.dump(word_to_id, open(vocab_dir, 'wb'))

    embeddings = np.random.rand(len(word_to_id), emb_dim)
    f = open(pretrain_dir, "r", encoding='UTF-8')
    for i, line in enumerate(f.readlines()):
        lin = line.strip().split(" ")
        if lin[0] in word_to_id:
            idx = word_to_id[lin[0]]
            emb = [float(x) for x in lin[1:301]]
            embeddings[idx] = np.asarray(emb, dtype='float32')
    f.close()
    np.savez_compressed(filename_trimmed_dir, embeddings=embeddings)
