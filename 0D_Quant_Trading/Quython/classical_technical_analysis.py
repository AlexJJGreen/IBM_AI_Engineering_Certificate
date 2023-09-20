def moving_average(series, window):
    series_moving_average = []
    for i,x in enumerate(series):
        if i - window < 0:
            pass
        else:
            
