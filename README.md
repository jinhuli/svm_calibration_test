# svm_calibration_test
`�汾�ţ�`0.0.1
`�������ڣ�`January 19, 2018

һ���������������ģ�ͣ�heston��1993�������ؿ���ģ�⣨MCS������50ETFУ׼�����۵ļ򵥿⡣

���⣬���ڲ���MCS����������Ȩ�Ķ��ۣ��ұ���ʲ�·��ģ����ÿһ��������Ϊ��λ�����Ե���Ȩ�����սϳ�ʱ������ڽ϶�ĵ������������������ٶȡ����⣬��ʵ��������ŷʽ������Ȩ���С�

����һ��������дһ�����ܣ����λ·���Ĵ���������~��

***
|Author|shallty_ht|
|---|---
|E-mail|hulinfeng.ht@foxmail.com
***
# ��������ע�⣡
�����а������г�����ץȡģ����õ���Wind��ѶAPI�����ԣ����Ҫʹ�ñ��⵱�е����ݵ��ú���������ذ�װ����������
����[Wind��ѶAPI˵����ַ](http://www.dajiangzhang.com/document "��ͣ��ʾ")
�����ܰ�װ��API���������������������ȡ��Ȩ�г�ʵ�����ݡ�
����������
numpy
pandas
scipy
***
## Ŀ¼
* [svm_calibration_test](#svm_calibration_test)
  * [StoVolaMoMsc](#StoVolaMoMsc)
      * [get_underlying](#get_underlying)
      * [get_option_price](#get_option_price)
  * [get_wind_optiondata](#get_wind_optiondata)
  * [get_underlying_vol](#get_underlying_vol)
  * [CalibrationIns](#CalibrationIns)
      * [add_***](#add_***)
      * [get_dif](#get_dif)
  * [Calibrate](#Calibrate)
      * [loc_fmin](#loc_fmin)
      * [opti_param](#opti_param)
***

 # svm_calibration_test
 `from svm_calibration_test import *`
 50ETF��Ȩ���ؿ���ģ�����У׼ʵ��
Ŀ�꣺������С�������������ؿ���ģ��Ĳ���������ģ����������Ȩ�۸�
����ÿ���³���һ�첻ͬ��������Ȩ���̼۸���Ϊ�г��۸�
����H93���������ģ�ͽ���У׼
����������Ȩ�ڵ�һ�첻ͬ��������Ȩ���̼���Ϊ��֤��׼

���˼·��
1. ���ȹ������ؿ���ģ�ⷽ������Ȩ�۸���㣬·����λ�նȵ�λ����ȵ�λΪ������252�졣
2. ����һ��У׼��������������������ֻ����Ȩ���ۺ�������Ȩ����ʱ�估��Ȩ�۸��������Ϊ�������Ż�����
3. ���Ż��������ã�Ŀ�꺯��Ϊ��С�����������ʾ�Ƿ��Ż��ɹ���
***
## StoVolaMoMsc
`StoVolaMoMsc(S0, r, V0, kappa_v, theta_v, sigma_v, rho, K, startdate, enddate)`
ŷʽ������Ȩ���ؿ��巽�����۶���
``` Python
  Parameters
  ==========
    S0 : float
        ����ʲ���ʼ�۸�
    r : float
        �޷�������
    V0 : float
        ��������ʳ�ʼ��ֵ
    kappa_v : float
        ��ֵ�ظ�����
    theta_v : float
        ���ھ�ֵ����
    sigma_v : float
        ��������ɢ��
    rho : float
        ��������ʺͱ���ʲ������ϵ��
    K : float
        ��Ȩ�۸�
    startdate : str
        ��ʼ��
    enddate : str
        ������
    
    Returns
    =======
    op : float
        ��Ȩ�۸�
```
### get_underlying
`StoVolaMoMsc().get_underlying(fixseed=False)`
���ر���ʲ��۸�䶯·��
``` Python
    Parameters
    ==========
    fixseed : bool
        �Ƿ��趨���������
```
### get_option_price
`StoVolaMoMsc().get_option_price(fixseed=False, mul=False)`
������Ȩ�۸�
mul������ó�True�����ж��MCS�����ҷ�������Ϊ���MCS�ľ�ֵ����������С��list��
``` Python
    Parameters
    ==========
    fixseed : bool
        �Ƿ��趨���������
    mul : bool
        �Ƿ���ж��ѭ��
           
    Returns
    =======
    option_price_describe_list : list
        ��Ȩ�۸�
```
***
## get_wind_optiondata
`get_wind_optiondata(startdate, enddate)`
����Wind���ݽӿڻ�ȡ��Ȩ�����г����ݡ�
``` Python
    Parameters
    ==========
    startdate : str
        �������ݿ�ʼ����
    enddate : str
        �������ݽ�������
    
    Returns
    =======
    option_data_set : DataFrame
        �������̼ۼ������յ���Ϣ����Ȩ���ݼ�
```
***
## get_underlying_vol
`get_underlying_vol(enddate)`
����Wind���ݽӿڻ�ȡ����ʲ��г������ʡ�
```Python
    Parameters
    ==========
    enddate : str
        �������ݽ�������
    
    Returns
    =======
    volatility : float
        ����ʲ������������Ϊֹ��һ������ʷ���������ʲ�����
```
***
## CalibrationIns
`CalibrationIns()`
 ����У׼���ߣ���ҪУ׼����Ϊkappa_v, theta_v, sigma_v, rho����get_dif()�����д���list[kappa_v, theta_v, sigma_v, rho]������MCSģ�������г�ʵ����Ȩ�۸�ľ�����
```Python
    Methods
    =======
    add_underlying : pandas.Series
        ����������ӱ���ʲ��г��۸�����
    add_volatility : pandas.Series
        ����������ӱ���ʲ���ʷ����������
    add_strike_price : pandas.Series
        �������������Ȩ��Ȩ�۸�����
    add_startdate : pandas.Series
        �������������Ȩ��Լ�г����ݻ�ȡ����
    add_enddate : pandas.Series
        �������������Ȩ��Լ������
    add_rate : pandas.Series
        ������������г�ʵ���޷���һ�������ʣ�shibor��
    add_mar_price : pandas.Series
        �������������Ȩ��Լ�г��۸�  
    get_dif :
        ȡ�ò�ͬ������ģ���������г�ʵ�ʼ۸�������
```
ע��������г�����Ҫ����˳���ϵ�һ�¡�
������У׼��Ȩ��ԼΪ3������ÿһ�����������е�����Ҫ��֤���е�Series[0]�н��ǵ�һ����Լ��ص����ݣ�Series[1]�н�Ϊ�ڶ�����Լ������ݣ��������ơ�
### get_dif
`CalibrationIns().get_dif(p)`
`p = [kappa_v, theta_v, sigma_v, rho]`
���ظ��ݴ�������������Ȩ�۸���ʵ���г���Ȩ�۸�֮��ľ�����
***
## Calibrate
`Calibrate(price_diff_class)`
����У׼���󡣲���scipy.optimize���������յĲ���У׼��
�˶��������һ����CalibrationIns().get_dif()������С������������Ӧ����С�������Ķ����������Ҫ������һ��Ŀ¼���Ѿ���ʼ����CalibrationIns()���󣬷����޷����С�
###  loc_fmin
`Calibrate(price_diff_class).loc_fmin()`
����ʹ��price_diff�ֲ���С�Ĳ���ֵ��
### opti_param
`Calibrate(price_diff_class).opti_param(initial_list)`
`initial_list=[kappa_v, theta_v, sigma_v, rho]`Ϊȫ�����Ż���ʵ�������û������ȸ��ݾֲ����ŵĽ������ȫ��������ʼ������
����ʹ��price_diffȫ����С�Ĳ���ֵ��