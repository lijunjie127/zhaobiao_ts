import matplotlib.pyplot as plt
import pandas

from zhaobiao_ts.util.util import file2ts, test_stationarity, show_p_q_graph, show_ts
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1.获取时间序列
fpan = '../raw_data/ccgp_country_ptime_date_statistics.csv'
ts = file2ts(fpan, 'd')  # 两个参数分别是：文件位置和采样周期

# 2.检验数据的平稳性并平稳化数据集
# test_stationarity(ts)
ts_diff1 = ts.diff(1)
ts_diff1.dropna(inplace=True)
# test_stationarity(ts_diff1)

# 通过图表展示原数据
# show_ts([ts, ts_diff1])
# show_ts(ts)
ts.to_csv('ts_d')

# 通过图表观察pq信息
# show_p_q_graph(ts)
# show_p_q_graph(ts_diff1)

# print(ts.count())
# print(ts)


# 3.划分训练集和测试集(7:3的比例)
# start = int(ts.count() * 0.4)
# seg = int(ts.count() * 0.9)  # 4212 4681
# train = ts[:seg]  # 六月之前为训练集
# test = ts[seg:-1]   # 七月开始为测试集
# print(train.tail(12))
# print(test.tail(12))

# 6.1 可视化输出训练数据和测试数据
# plt.plot(train, color='black', label='data_train')
# plt.plot(test, color='orange', label='data_test')
# plt.plot(train, label='data_train')
# plt.plot(test, label='data_test')
# plt.title('Original')
# plt.legend(loc='best')
# plt.show()

# 7.通过ARIMA差分自回归移动平均模型对数据进行训练
# fit1 = sm.tsa.statespace.SARIMAX(train, order=(2, 1, 4), seasonal_order=(2, 1, 4, 7)).fit()
# predict_series = fit1.predict(start="2019-6-26", end="2019-7-14", dynamic=True)
# plt.figure(figsize=(16, 8))
# # plt.plot(train, label='Train')
# plt.plot(test, label='True')
# plt.plot(predict_series, label='Predict')
# plt.title('2019_ccgp_country_publish_time')
# plt.legend(loc='best')
# plt.show()
#
# # print(test.count(), predict_series.count())
# rms = sqrt(mean_squared_error(test, predict_series))
# print(rms)
