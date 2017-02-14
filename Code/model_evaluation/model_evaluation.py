

def test_stationarity(timeseries):
	'''判断序列是不是稳定的 传入pd的Series的对象'''
	#Determing rolling statistics
	rolmean = pd.rolling_mean(timeseries, window=7)
	rolstd = pd.rolling_std(timeseries, window=7)

	#Plot rolling statistics:
	orig = plt.plot(timeseries, color='blue',label='Original')
	mean = plt.plot(rolmean, color='red', label='Rolling Mean')
	std = plt.plot(rolstd, color='black', label = 'Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show()
	
	#Perform Dickey-Fuller test:
	print 'Results of Dickey-Fuller Test:'
	dftest = adfuller(timeseries, autolag='AIC')
	dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
	for key,value in dftest[4].items():
		dfoutput['Critical Value (%s)'%key] = value
	print dfoutput