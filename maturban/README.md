
### To download the timemaps of all of the six domains

```sh
% python getTimeMap.py https://www.whitehouse.gov ./results/wh/timemap.txt
% python getTimeMap.py https://www.energy.gov ./results/energy/timemap.txt
% python getTimeMap.py http://www.va.gov ./results/va/timemap.txt
% python getTimeMap.py http://www.hhs.gov ./results/hhs/timemap.txt
% python getTimeMap.py https://www.epa.gov ./results/epa/timemap.txt
% python getTimeMap.py https://www.dhs.gov ./results/dhs/timemap.txt
```

### To generate the final results in different file format 
```sh
% python generateSimhashAndTFIDF.py ./results/wh/timemap.txt ./results/wh/res.txt ./results/wh/res.csv ./results/wh/res.json  
% python generateSimhashAndTFIDF.py ./results/energy/timemap.txt ./results/energy/res.txt ./results/energy/res.csv ./results/energy/res.json  
% python generateSimhashAndTFIDF.py ./results/va/timemap.txt ./results/va/res.txt ./results/va/res.csv ./results/va/res.json  
% python generateSimhashAndTFIDF.py ./results/hhs/timemap.txt ./results/hhs/res.txt ./results/hhs/res.csv ./results/hhs/res.json  
% python generateSimhashAndTFIDF.py ./results/epa/timemap.txt ./results/epa/res.txt ./results/epa/res.csv ./results/epa/res.json  
% python generateSimhashAndTFIDF.py ./results/dhs/timemap.txt ./results/dhs/res.txt ./results/dhs/res.csv ./results/dhs/res.json  
```
