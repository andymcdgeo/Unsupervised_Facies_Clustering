import pandas as pd
import matplotlib.pyplot as plt

def create_plot(wellname, dataframe, curves_to_plot, depth_curve, facies_curves=[]):
    num_tracks = len(curves_to_plot)
    
    fig, ax = plt.subplots(nrows=1, ncols=num_tracks, figsize=(num_tracks*2, 10))
    fig.suptitle(wellname, fontsize=20, y=1.05)
    
    for i, curve in enumerate(curves_to_plot):
        ax[i].plot(dataframe[curve], depth_curve)

        ax[i].set_title(curve, fontsize=14, fontweight='bold')
        ax[i].grid(which='major', color='lightgrey', linestyle='-')
        
        ax[i].set_ylim(depth_curve.max(), depth_curve.min())

        if i == 0:
            ax[i].set_ylabel('DEPTH (m)', fontsize=18, fontweight='bold')
        else:
            plt.setp(ax[i].get_yticklabels(), visible = False)
        
        if curve in facies_curves:
            for key in lithology_setup.keys():
                color = lithology_setup[key]['color']
                ax[i].fill_betweenx(depth_curve, 0, 4, 
                                  where=(dataframe[curve]==key),
                                  facecolor=color)
    plt.tight_layout()
    plt.show()

workingdf = pd.DataFrame({'WELL':['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'], 
                    'DEPTH':[4300, 4310, 4320, 4330, 4340, 4350, 4360, 4370, 4380, 4390], 
                     'GR':[45, 40, 30, 12, 6, 12, 8, 10, 20, 18], 
                     'FACIES':[1, 1, 1, 1, 2, 1, 2, 2, 3, 3]})

lithology_setup = {1: {'lith':'Sandstone', 'color':'#ffff00'},
                 2: {'lith':'Sandstone/Shale', 'color':'#ffe119'},
                 3: {'lith':'Shale', 'color':'#bebebe'},}


curves_to_plot = ['GR', 'FACIES']
facies_curve=['FACIES']
grouped = workingdf.groupby('WELL')

# Create empty lists
dfs_wells = []
wellnames = []

#Split up the data by well
for well, data in grouped:
    dfs_wells.append(data)
    wellnames.append(well)

well = 0

create_plot(wellnames[well], 
            dfs_wells[well], 
            curves_to_plot, 
            dfs_wells[well]['DEPTH'], 
            facies_curve)


