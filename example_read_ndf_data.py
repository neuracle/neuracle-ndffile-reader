from matplotlib.pyplot import isinteractive
from NDFSysParser import FileNEF, FileNTP,FileNSF,FileNDF,FolderNHF, FolderNSF
from NDFSysUtility import FolderCatergory, NDFUtility
from NDFSysMNE import mneNDF
import mne
from ReadNDF import ReadNDFChannels,ReadOneChannel
import time


#ndfMneObj = mneNDF('./data/202205131116_N170/2/','./data/202205131116_N170/neuracle.nef')
#data = ndfMneObj.read2MneRaw(10,20)

# chs = ReadNDFChannels('./data/Lucy/')
# data = ReadOneChannel('./data/','Lucy','Fz',0,2)

t1 = time.time()
ndfMneObj = mneNDF(r'C:\\Users\\83660\\Desktop\\data\\20250509194331_25-5-9晚上闭眼\\潘玲')
# ndfMneObj = mneNDF('./data/20230818104251_10米运动/1/')
#ndfMneObj = mneNDF('./data/20230512161614_37min/1/') 
data = ndfMneObj.read2MneRaw()
infoTest = data.info
channels = data.ch_names
timeLen = data.n_times
eegdata=data.get_data()
ch1=eegdata[5,:]
for i in range(3000,3005):
    print(ch1[i])
# t2 = time.time()
# print(t2-t1)

#data.plot(start = 0, duration = 1)

# #dataEpoch = mne.epochs(raw=data)
# event_id = {'1': 1,
#             '2': 2,
#             '3': 3,
#             '4': 4
#             }
# events_, _ = mne.events_from_annotations(
# data,event_id=event_id)
# #fig = mne.viz.plot_events(events_,
# #                             sfreq=data.info['sfreq'])


# tmax = 30. - 1. / data.info['sfreq']  # tmax in included
# baseline = (None, 0)
# epochs = mne.Epochs(raw=data, events=events_,
#                               event_id=event_id, tmin=0., tmax=tmax, baseline=None)

# epochs.plot_psd(fmin=0., fmax=40.,spatial_colors=False)
