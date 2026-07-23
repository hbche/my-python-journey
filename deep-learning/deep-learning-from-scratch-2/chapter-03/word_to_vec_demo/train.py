import sys

sys.path.append("../..")
from common.optimizer import Adam
from common.trainer import Trainer
from common.util import convert_one_hot, create_contexts_target, preprocess
from simple_skip_gram import SimpleSkipGram

window_size = 1
hidden_size = 5
barch_size = 3
max_epoch = 1000

# 数据预处理
text = "You say goodbye and i say hello."
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
# 创建上下文及目标向量
contexts, target = create_contexts_target(corpus, vocab_size, window_size=window_size)
# 转换为 ont-hot 形式
contexts = convert_one_hot(contexts, vocab_size)
target = convert_one_hot(target, vocab_size)
print("contexts shape: ", contexts.shape)
print("target shape: ", target.shape)

# 初始化模型
model = SimpleSkipGram(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

# 开始训练
trainer.fit(contexts, target, max_epoch, barch_size)
trainer.plot()

word_vecs = model.word_vecs
# 输出每个单词的分布式向量
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])
