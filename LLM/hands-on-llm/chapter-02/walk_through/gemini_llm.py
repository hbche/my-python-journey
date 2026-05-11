from dotenv import find_dotenv, load_dotenv
from google import genai

_ = load_dotenv(find_dotenv())

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How to learn AI works? Answer in Chinese please",
)

print(response.text)

# 学习人工智能（AI）的工作原理是一个既兴奋又充满挑战的过程。为了让你能够系统地掌握，我建议按照以下**五个阶段**循序渐进地学习：

# ### 第一阶段：理解基本概念（科普与直觉）
# 在深入数学和代码之前，先搞清楚 AI 是什么、能做什么。
# *   **区分三个概念：**
#     *   **人工智能 (AI)：** 让机器展示出智能的广泛领域。
#     *   **机器学习 (Machine Learning)：** AI 的一个子集，通过数据来训练算法，而不是手动编写规则。
#     *   **深度学习 (Deep Learning)：** 机器学习的一种，模仿人脑神经网络，是目前 ChatGPT 等技术的核心。
# *   **学习资源：** 观看 YouTube 或 B站上的科普视频（如“3Blue1Brown”的神经网络系列）。

# ### 第二阶段：数学基础（AI 的底层逻辑）
# AI 的本质是数学。你不需要成为数学家，但必须理解以下核心概念：
# *   **线性代数：** 矩阵和向量运算（数据在 AI 中是以矩阵形式存在的）。
# *   **微积分：** 导数和梯度下降（AI 如何通过“找坡度”来纠正错误、不断进步）。
# *   **概率论与统计学：** 贝叶斯定理、分布、均值与方差（AI 实际上是在处理概率问题）。

# ### 第三阶段：编程技能（实现 AI 的工具）
# **Python** 是 AI 领域的通用语言，必须掌握。
# *   **Python 基础：** 语法、列表、字典、函数。
# *   **数据处理库：**
#     *   **NumPy：** 处理数值矩阵。
#     *   **Pandas：** 处理表格数据。
#     *   **Matplotlib/Seaborn：** 数据可视化。
# *   **AI 框架：** 当你准备动手做实验时，学习 **PyTorch** 或 **TensorFlow**（目前学术界和工业界 PyTorch 更流行）。

# ### 第四阶段：机器学习与深度学习算法
# 这是最核心的部分。
# *   **传统机器学习：** 线性回归、逻辑回归、决策树、随机森林、支持向量机 (SVM)。
# *   **深度学习基础：**
#     *   多层感知机 (MLP)。
#     *   **反向传播 (Backpropagation)：** 理解模型是如何学习的。
#     *   **损失函数 (Loss Function)：** 衡量模型表现好坏。
# *   **现代模型架构：**
#     *   **CNN (卷积神经网络)：** 用于图像识别。
#     *   **RNN/LSTM：** 用于序列数据（如语音）。
#     *   **Transformer：** **最重要的架构**，它是 ChatGPT 等大语言模型的基础。

# ### 第五阶段：实践与前沿（动手做项目）
# 理论看十遍，不如代码写一遍。
# *   **经典项目：**
#     *   MNIST 手写数字识别（AI 界的“Hello World”）。
#     *   泰坦尼克号生存预测（经典 Kaggle 入门赛）。
#     *   使用预训练模型（如 Hugging Face 上的模型）进行文本分类或图片生成。
# *   **关注 LLM (大语言模型)：** 了解 Prompt Engineering (提示工程) 和 Fine-tuning (微调)。

# ---

# ### 推荐学习资源（黄金清单）：
# 1.  **入门首选：** 吴恩达 (Andrew Ng) 的 **《机器学习》 (Machine Learning Specialization)** —— Coursera 或 B站上有免费搬运。他能把复杂的数学讲得非常简单。
# 2.  **进阶必看：** 吴恩达的 **《深度学习》 (Deep Learning Specialization)**。
# 3.  **书籍：** 《Python 机器学习》(作者 Sebastian Raschka) 或 《动手学深度学习》(李沐 D2L.ai，有配套视频和开源代码，非常硬核)。
# 4.  **实战平台：** **Kaggle**。参加上面的竞赛，看别人的代码（Notebooks）。

# ### 学习建议：
# *   **不要被数学卡死：** 如果遇到太难的公式，先跳过去看它在代码里是怎么用的，以后再回头啃数学。
# *   **“以练促学”：** 找一个你感兴趣的问题（比如预测股价、识别猫狗、生成小说），带着问题去学技术，动力会更强。

# 你想从哪个部分开始深入了解？我可以为你推荐更具体的资料。
