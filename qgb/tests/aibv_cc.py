

wsapp.send('{"symbol":"ETHUSDT","period":"1min","type_opentime":"hk0","debug":2}')
'''
or send '{"sign": "xujtuYfS+VUQG4rFqUiz3/ELYGxFim/F5zs6yWh1+sX2/p/1w1bokrPVgWAZibjICSrQQzBCsiYAIxTpRWFltzMODQlONMy+AwZM4MfReVmgDslrxh7t/U74oj7F+WO+ek/c/Fhv5tJMp+rSR5K/a4iQePGnIqjt+J/cox1UXdo="}'  # 转成bytes也 不清楚具体格式。有有效期，发送一次后再用也不行
'''
##########################
'''
(Pdb) exit
{"code":1000,"data":{"type":"quotevew","symbol":"ethusdt","bids":[["1224.91000000","1.35670000"],["1224.81000000","3.34970000"],["1224.80000000","5.17310000"],["1224.76000000","14.00720000"],["1224.55000000","15.61570000"],["1224.32000000","28.30200000"],["1224.31000000","28.53740000"],["1224.12000000","28.94720000"],["1224.11000000","29.35680000"],["1224.04000000","63.15780000"],["1224.02000000","79.41390000"],["1223.94000000","131.84930000"],["1223.89000000","134.84060000"],["1223.81000000","137.98050000"],["1223.79000000","142.13200000"],["1223.78000000","166.20380000"],["1223.75000000","169.72610000"],["1223.73000000","184.72610000"],["1223.71000000","196.22610000"],["1223.70000000","208.62610000"]],"asks":[["1224.92000000","1.19230000"],["1224.93000000","1.99560000"],["1224.98000000","6.08710000"],["1225.00000000","6.89040000"],["1225.07000000","7.69370000"],["1225.13000000","7.71000000"],["1225.14000000","11.53730000"],["1225.27000000","15.62780000"],["1225.29000000","16.44400000"],["1225.49000000","16.63350000"],["1225.51000000","17.49380000"],["1225.57000000","18.17190000"],["1225.58000000","42.98290000"],["1225.74000000","65.61680000"],["1225.80000000","65.89110000"],["1225.81000000","69.89110000"],["1225.83000000","70.21340000"],["1225.84000000","72.35260000"],["1225.86000000","72.55970000"],["1225.88000000","73.27430000"]],"bids_y":[["1224.91000000","1.35670000"],["1224.81000000","1.99300000"],["1224.80000000","1.82340000"],["1224.76000000","8.83410000"],["1224.55000000","1.60850000"],["1224.32000000","12.68630000"],["1224.31000000","0.23540000"],["1224.12000000","0.40980000"],["1224.11000000","0.40960000"],["1224.04000000","33.80100000"],["1224.02000000","16.25610000"],["1223.94000000","52.43540000"],["1223.89000000","2.99130000"],["1223.81000000","3.13990000"],["1223.79000000","4.15150000"],["1223.78000000","24.07180000"],["1223.75000000","3.52230000"],["1223.73000000","15.00000000"],["1223.71000000","11.50000000"],["1223.70000000","12.40000000"]],"asks_y":[["1224.92000000","1.19230000"],["1224.93000000","0.80330000"],["1224.98000000","4.09150000"],["1225.00000000","0.80330000"],["1225.07000000","0.80330000"],["1225.13000000","0.01630000"],["1225.14000000","3.82730000"],["1225.27000000","4.09050000"],["1225.29000000","0.81620000"],["1225.49000000","0.18950000"],["1225.51000000","0.86030000"],["1225.57000000","0.67810000"],["1225.58000000","24.81100000"],["1225.74000000","22.63390000"],["1225.80000000","0.27430000"],["1225.81000000","4.00000000"],["1225.83000000","0.32230000"],["1225.84000000","2.13920000"],["1225.86000000","0.20710000"],["1225.88000000","0.71460000"]],"bids_same_price":[["1224.02",79],["1223.7",129]],"asks_same_price":[["1225.88",67],["1224.98",6]]},"message":"","other":""}
--Return--
'''