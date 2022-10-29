from zlib import Z_NO_COMPRESSION
from django.shortcuts import render
import scipy.stats as stats

# Create your views here.
class ZScoreGen:
    def calculate_z_score(self,x):
        if len(x):
            zscores = stats.zscore(x)  
            return zscores
        return -1