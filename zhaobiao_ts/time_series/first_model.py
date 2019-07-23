import matplotlib.pyplot as plt
import pandas

from zhaobiao_ts.util.util import file2ts, test_stationarity, show_p_q_graph, show_ts
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
"""
输入策略，输出抓到的数据，
输入抓到的数据，输出策略
"""

# 1.获取时间序列
ts = file2ts('ts_15min_201904train')  # 默认15分钟一次进行取样


def data2strategy(data):
    """
    输入本次抓取的数据，进行分析，输出下次抓取的策略
    :param data:
    :return:
    """
    predicted = []
    for i in range(96-2):
        if not data[i] and data[i+1] > sum(data) // 96 and data[i+1] > data[i+2]:
            data[i] = 1
    for i in range(96):
        predicted.append(1 if data[i] else 0)
    return predicted


def strategy2data(strategy, offset):
    """
    输入策略和数据，根据策略得到抓取的数据
    :param strategy:
    :param offset:
    :return:
    """
    origin_data = []
    crawl_data = []
    count = 0
    for i in range(offset, offset+96):
        origin_data.append(ts[i])
        count += ts[i]
        if strategy[i-offset]:
            crawl_data.append(count)
            count = 0
        else:
            crawl_data.append(0)

    return crawl_data


if __name__ == '__main__':
    # 初始化第1天的策略
    strategy = [1 for i in range(96)]

    # 初始化第1天的数据
    origin_data = []
    for i in range(96):
        origin_data.append(ts[i])

    # 抓取得到第1天的数据
    first_day_data = strategy2data(strategy, 0)

    print(strategy[:45])
    print(origin_data[:45])
    print(first_day_data[:45])
    print('-'*100)

    # 得到第2天的策略
    strategy = data2strategy(first_day_data)

    # 得到第2天的原始数据
    origin_data = []
    for i in range(96, 96+96):
        origin_data.append(ts[i])

    # 得到第2天的抓取数据
    sec_day_data = strategy2data(strategy, 96)

    print(strategy[:45])
    print(origin_data[:45])
    print(sec_day_data[:45])
    print('-' * 100)

    # 得到第3天的策略
    strategy = data2strategy(sec_day_data)

    # 得到第3天的原始数据
    origin_data = []
    for i in range(96*2, 96*3):
        origin_data.append(ts[i])

    # 得到第3天的抓取数据
    third_day_data = strategy2data(strategy, 96*2)
    print(strategy[:45])
    print(origin_data[:45])
    print(third_day_data[:45])
    print('-' * 100)

    plt.plot(origin_data)
    plt.plot(third_day_data)
    plt.show()




