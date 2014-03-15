import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from datetime import datetime

plt.close()
names = ['clark', 'gordon', 'bruce', 'peter', 'jean','aurora']
appnames = ['PCCS', 'RTC Recon', 'RMS', 'Debit Match', 'Insight']
sdev = np.random.randint(low=100, high=150, size=100)
mdev = np.random.randint(low=100, high=500, size=100)
ldev = np.random.randint(low=0, high=1000, size=100)

print "head sdev = " + str(sdev[1:10]) + "| SD sdev = " + str(np.std(sdev))
print "head mdev = " + str(mdev[1:10]) + "| SD mdev = " + str(np.std(mdev))
print "head ldev = " + str(ldev[1:10]) + "| SD lodev = " + str(np.std(ldev))

md = {}

md["clark"] = np.random.randint(low=100, high=150, size=100)
md["gordon"] = np.random.randint(low=100, high=500, size=100)
md["bruce"] = np.random.randint(low=0, high=1000, size=100)
md["peter"] = np.random.randint(low=100, high=150, size=100)
md["jean"] = np.random.randint(low=100, high=500, size=100)
md["aurora"] = np.random.randint(low=0, high=1000, size=100)

# making clark believable and adding weekends
md["clark"][54:80] = md["clark"][54:80] + 100 #holiday season for clark
md["clark"][1:100:7] = md["clark"][1:100:7] * 0.0
md["clark"][2:100:7] = md["clark"][2:100:7] * 0.0
md["clark"][35] = 750  # clark steals 750 credit cards
nonzero_clark_index = np.where(md["clark"] != 0)
clark_counts = [md["clark"][x] for x in nonzero_clark_index]
mean_clark = np.repeat(np.mean(clark_counts), len(md["clark"]))
max1d_clark = mean_clark + np.repeat(np.std(clark_counts), len(md["clark"]))
max3d_clark = mean_clark + np.repeat(np.std(clark_counts), len(md["clark"]))*3

md["gordon"][54:80] = md["gordon"][54:80] + 100 #holiday season for clark
md["gordon"][1:100:7] = md["gordon"][1:100:7] * 0.0
md["gordon"][2:100:7] = md["gordon"][2:100:7] * 0.0
nonzero_gordon_index = np.where(md["gordon"] != 0)
gordon_counts = [md["gordon"][x] for x in nonzero_gordon_index]
mean_gordon = np.repeat(np.mean(gordon_counts), len(md["gordon"]))
max1d_gordon = mean_gordon + np.repeat(np.std(gordon_counts), len(md["gordon"]))
max3d_gordon = mean_gordon + np.repeat(np.std(gordon_counts), len(md["gordon"]))*3

md["bruce"][54:80] = md["bruce"][54:80] + 150 #holiday season for clark
md["bruce"][1:100:7] = md["bruce"][1:100:7] * 0.0
md["bruce"][2:100:7] = md["bruce"][2:100:7] * 0.0
nonzero_bruce_index = np.where(md["bruce"] != 0)
bruce_counts = [md["bruce"][x] for x in nonzero_bruce_index]
mean_bruce = np.repeat(np.mean(bruce_counts), len(md["bruce"]))
max1d_bruce = mean_bruce + np.repeat(np.std(bruce_counts), len(md["bruce"]))
max3d_bruce = mean_bruce + np.repeat(np.std(bruce_counts), len(md["bruce"]))*3

md["peter"][54:80] = md["peter"][54:80] + 300 #holiday season for clark
md["peter"][1:100:7] = md["peter"][1:100:7] * 0.0
md["peter"][2:100:7] = md["peter"][2:100:7] * 0.0

md["jean"][54:80] = md["jean"][54:80] + 100 #holiday season for clark
md["jean"][1:100:7] = md["jean"][1:100:7] * 0.0
md["jean"][2:100:7] = md["jean"][2:100:7] * 0.0
md["jean"][1] = 800 # jean steals 800 credit cards

md["aurora"][54:80] = md["aurora"][54:80] + 100 #holiday season for clark
md["aurora"][3:100:7] = md["aurora"][3:100:7] * 0.0
md["aurora"][4:100:7] = md["aurora"][4:100:7] * 0.0

startdate = datetime.strptime("2014,jan,1 08:00", "%Y,%b,%d %H:%M")
stopdate = datetime.strptime("2014,mar,31 08:00", "%Y,%b,%d %H:%M")
dategap = stopdate - startdate
#x_ticks = np.arange(0,dategap.days, 10)
datetime.strptime("2014-jan-1 08:00", "%Y-%b-%d %H:%M")
week = ["Sa", "Su","M", "T", "W", "R", "F"]
x_ticklabels = 14*week
x_ticks = np.arange(3,100)

# plot stuff:
fig0 = plt.figure()
ax0 = fig0.add_subplot(211)
ax1 = fig0.add_subplot(212)

fig1 = plt.figure()
ax2 = fig1.add_subplot(211)
ax3 = fig1.add_subplot(212)

fig2 = plt.figure()
ax4 = fig2.add_subplot(211)
ax5 = fig2.add_subplot(212)

ax0.plot(md["clark"], 'o-', markersize=3, label="Clark (low variance)")
ax0.plot(mean_clark, '--', label="average")
ax0.plot(max1d_clark, '--', color="pink", label="1SD")
ax0.plot(max3d_clark, '--', color="red", label="3SD (threshold)")

ax1.plot(md["gordon"], 'o-', markersize=3, label="Gordon (high variance)")
ax1.plot(mean_gordon, '--', label="average")
ax1.plot(max1d_gordon, '--', color="pink", label="1SD")
ax1.plot(max3d_gordon, '--', color="red", label="3SD (threshold)")

ax2.plot(md["bruce"], 'o-', markersize=3, label="Bruce")
ax2.plot(mean_bruce, '--', label="average")
ax2.plot(max1d_bruce, '--', color="pink", label="1SD")
ax2.plot(max3d_bruce, '--', color="red", label="3SD (threshold)")

ax3.plot(md["peter"], 'o-', markersize=3, label="Peter")
ax4.plot(md["jean"], 'o-', markersize=3, label="Jean")
ax5.plot(md["aurora"], 'o-', markersize=3, color='green', label="Aurora")
# plot some STDev stuff

# Constantinos ##################
xlabel_fontsize = 10.0
ylabel_fontsize = 10.0
title_fontsize = 12.0
legend_fontsize = 10.00
ANNOTATE_FONTSIZE = 8.0
#################################
ax0.set_xlabel("days", fontsize=xlabel_fontsize)
ax0.set_xticks(np.arange(1,101))
ax0.set_xticklabels(x_ticklabels, fontsize=6)
ax0.set_ylabel("count of PANs accessed", fontsize=ylabel_fontsize)
ax0.annotate("Clark doesn't work on weekends", xy=(1,0), xytext=(1,700), fontsize=ANNOTATE_FONTSIZE, arrowprops=dict(arrowstyle="->", connectionstyle="arc, angleA=0, armA=30, rad=10"))
ax0.annotate('On average, Clark accesses about 158 PANs / day', xy=(15,158), xytext=(12,650), fontsize=ANNOTATE_FONTSIZE, arrowprops=dict(arrowstyle="->", connectionstyle="arc, angleA=0, armA=30, rad=10"))
ax0.annotate('Within 1 SD, we see false positive threshold violations', xy=(63,241), xytext=(55,525), fontsize=ANNOTATE_FONTSIZE, arrowprops=dict(arrowstyle="->", connectionstyle="arc, angleA=0, armA=30, rad=10"))
ax0.annotate('Within 3 SD, we see only one threshold violation', xy=(35,403), xytext=(36,600), fontsize=ANNOTATE_FONTSIZE, arrowprops=dict(arrowstyle="->", connectionstyle="arc, angleA=0, armA=30, rad=10"))
ax0.annotate('Clark steals 750 credit cards numbers!', xy=(35,700), xytext=(65,700), fontsize=ANNOTATE_FONTSIZE, arrowprops=dict(arrowstyle="->", connectionstyle="arc, angleA=0, armA=30, rad=10"))
ax0.legend(fontsize=legend_fontsize)
ax0.set_title("User = Clark")

ax1.legend(fontsize=legend_fontsize)
ax1.set_title("User = Gordon")
ax1.set_xlabel("days", fontsize=xlabel_fontsize)
ax1.set_xticks(np.arange(1,101))
ax1.set_xticklabels(x_ticklabels, fontsize=6)
ax1.set_ylabel("count of PANs accessed", fontsize=ylabel_fontsize)


ax2.legend(fontsize=legend_fontsize)
ax2.set_title("User = Bruce")
ax2.set_xlabel("days", fontsize=xlabel_fontsize)
ax2.set_xticks(np.arange(1,101))
ax2.set_xticklabels(x_ticklabels, fontsize=6)
ax2.set_ylabel("count of PANs accessed", fontsize=ylabel_fontsize)

ax3.legend(fontsize=legend_fontsize)
ax3.set_title("User = Peter")
ax3.set_xlabel("days", fontsize=xlabel_fontsize)
ax3.set_xticks(np.arange(1,101))
ax3.set_xticklabels(x_ticklabels, fontsize=6)
ax3.set_ylabel("count of PANs accessed", fontsize=ylabel_fontsize)
ax4.legend(fontsize=legend_fontsize)
ax5.legend(fontsize=legend_fontsize)


#plt.tight_layout()
#ax1 = fig0.axes()
fig0.show()
#fig1.show()
#fig2.show()

#
#def getnums(inputlist,maxnum):
#    """
#    __author__ = "dave dyer"
#    input the list name and the number of random numbers you'd like from the list and it'll return that # in a list.
#    """
#    rand_sample = [inputlist[i] for i in sorted(random.sample(xrange(len(inputlist)), maxnum)) ]   
#    return(outputlist)
#
#clark = sdev
#gordon = sample

#clark <- sample(smalldev, size=100)
#gordon <- sample(meddev, size=100)
#bruce <- sample(largedev, size=100)
#peter <- sample(smalldev, size=100)
#jean <- sample(meddev, size=100)
#aurora <- sample(largedev, size=100)
#aurora[71] <- 1500
#gordon[23] <- 2000
