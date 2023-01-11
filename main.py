from sklearn.model_selection import train_test_split
from scipy.interpolate import UnivariateSpline
from sklearn import linear_model
import xgboost as xgb
from ultis import *

df = pd.read_csv('new_gy_contest_traveltime_training_data_second.txt', delimiter=';', dtype={'link_ID': object})
print(df.head(10))

link_df = pd.read_csv('gy_contest_link_info.txt', delimiter=';', dtype={'link_ID': object})
print(link_df.head(10))

link_tops = pd.read_csv('gy_contest_link_top.txt', delimiter=',', dtype={'link_ID': object})
print(link_tops.head(10))

df['time_interval_begin'] = pd.to_datetime(df['time_interval'].map(lambda x: x[1:20]))
print(df.head(10))