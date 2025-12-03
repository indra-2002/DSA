class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        def station(mid):
            needed=0
            for i in range(1,len(stations)):
                gap=int((stations[i]-stations[i-1])/mid)
                needed+=gap
            return needed<=k
        l=0
        h=stations[-1]-stations[0]
        while h-l > 1e-6:
            mid=(l+h)/2
            if station(mid):
                h=mid
            else:
                l=mid
        return h