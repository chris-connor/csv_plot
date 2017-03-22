__author__ = 'Chris Connor'
''' This script saves a timeseries plot for each .csv file in it's current working directory./
    Each .csv file should have only two columns of data: Column A: Time, Column B: Values'''
if __name__ == "__main__":
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    import glob
    import warnings
    warnings.filterwarnings("ignore")
    '''create a list of all .csv files in the current working directory'''
    path = os.getcwd()
    extension = 'csv'
    os.chdir(path)
    result = [i for i in glob.glob('*.{}'.format(extension))]

    '''create and save a separate timeseries plot of all .csv files in cwd as a .png'''
    for x in result:
        '''read in data and coerce it to a useable format in pandas'''
        filename, ext = os.path.splitext(x)
        df = pd.read_csv(x)
        names = df.columns.values
        xdata, xLabel = df[str(names[0])], str(names[0])
        ydata, yLabel = df[str(names[1])],str(names[1])
        xdata = pd.to_datetime(xdata, errors = 'coerce')

        '''plot data in maximized window'''
        plt.plot_date(x=xdata, y=ydata)
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()

        '''save plot to .png using input filename as name and column headers as axis labels'''
        ext = '.png'
        figname = str(filename + ext)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend()
        plt.savefig(figname,bbox_inches = 'tight')
        plt.clf()
