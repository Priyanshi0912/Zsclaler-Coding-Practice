from os import *
from sys import *
from collections import *
from math import *

def help(ind,target,arr,dp):
    if target==0:
        return True
    if ind==0:
        dp[ind][target]=(arr[0]==target)
        return dp[ind][target]
    if dp[ind][target]!=-1:
        return dp[ind][target]
    nottake=help(ind-1,target,arr,dp)
    take=False
    if target>=arr[ind]:
        take=help(ind-1,target-arr[ind],arr,dp)
    dp[ind][target]=(take or nottake)
    return dp[ind][target]
def subsetSumToK(n, k, arr):
    
    dp=[[-1]*(k+1) for _ in range(n+1)]
    return help(n-1,k,arr,dp)


    pass
