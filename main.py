import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1. / (1 + np.exp(-x+10))


def plot_sigmoid():
    x = np.linspace(0, 20, 1000)  # 这个表示在-10到10之间生成1000个x值
    y = sigmoid(x)  # 对上述生成的1000个数循环用sigmoid公式求对应的y
    plt.xlim((0, 20))
    plt.ylim((0.00, 1.00))
    plt.yticks([0.5, 1.0], [0.5, 1.0])  # 设置y轴显示的刻度
    plt.plot(x, y, color="black")  # 用上述生成的1000个xy值对生成1000个点
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # 删除右边框设为无
    ax.spines['top'].set_color('none')  # 删除上边框设为无
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))  # 调整x轴位置
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))  # 调整y轴位置
    plt.savefig("sigmoid.png")
    plt.legend(['Sigmoid'])
    plt.show()


if __name__ == "__main__":
    plot_sigmoid()
