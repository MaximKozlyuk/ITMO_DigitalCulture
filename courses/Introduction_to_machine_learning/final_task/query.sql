select * from pulsar_stars
        where (target = 0 and (mip >= 96.921875 and mip <= 97.4140625))
        or (target =1 and (mip >= 41.8828125 and mip <= 47.4140625));

-- выборочное среднее столбца MIP до номировки:
select sum(mip) / count(1) from pulsar_stars
        where (target = 0 and (mip >= 96.921875 and mip <= 97.4140625))
        or (target =1 and (mip >= 41.8828125 and mip <= 47.4140625));