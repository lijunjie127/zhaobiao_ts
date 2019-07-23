import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf


def file2ts(file_path_and_name, resample_freq='15min'):
    """
    读取csv文件中的数据，转换成时间序列
    重新采样（自动处理缺失值，时间自动变为等间隔，自动按照时间顺序排序）
    Parameters
    ----------
    file_path_and_name : str
        文件的路径和名称
        例如：'../raw_data/ccgp_country_ctime_date_statistics.csv'
    resample_freq : str
        时间序列重新采样的周期
        'y': 年
        'm': 月
        'd': 日
        'h': 小时
        'min': 分钟
        '15min': 15分钟
        's': 秒
    """
    # 1.读取csv格式数据，默认DataFrame格式
    df = pd.read_csv(file_path_and_name)

    # 2.将数据索引改为日期形式
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index("Date", inplace=True)

    # 3.将DataFram数据格式转换为Series格式
    ts = pd.Series(df['Count'].values, index=df.index)

    # 4.按照一定频率重新采样
    ts = ts.resample(resample_freq, closed='left').sum()
    return ts


def test_stationarity(time_series):
    """
    使用ADF来检验时间序列的平稳性
    :param time_series:
    :return:
    """
    t = sm.tsa.stattools.adfuller(time_series)
    if float(t[1]) < 0.05:
        print('{}:通过平稳性检验'.format(t[1]))
        return True
    else:
        print('{}:未通过平稳性检验'.format(t[1]))
        return False


def show_p_q_graph(time_series):
    """
    展示数据的ACF和PACF图，模型定阶
    :param time_series:
    :return:
    """
    # (p, q) = (sm.tsa.arma_order_select_ic(ts, max_ar=7, max_ma=7, ic='aic')['aic_min_order'])
    plot_acf(time_series)
    plot_pacf(time_series)
    plt.show()


def show_ts(ts):
    if isinstance(ts, list):
        for time_series in ts:
            time_series.plot(label=str(time_series))
        plt.title('time_series_data')
        # plt.legend(loc='best')

    if isinstance(ts, pd.core.series.Series):
        ts.plot(label=str(ts))

    plt.show()
