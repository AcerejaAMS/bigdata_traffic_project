raw = LOAD '/traffic_data/traffic_data.csv' USING PigStorage(',');

-- quitar encabezado
noheader = FILTER raw BY $0 != 'sensor_id';

-- castear después
clean = FOREACH noheader GENERATE
          (int)$0 as sensor_id,
          (chararray)$1 as event_time,
          (chararray)$2 as location,
          (double)$3 as speed,
          (int)$4 as vehicle_count;

filtered = FILTER clean BY speed > 0;

grouped = GROUP filtered BY location;

stats = FOREACH grouped GENERATE
         group AS location,
         AVG(filtered.speed) AS avg_speed,
         SUM(filtered.vehicle_count) AS total_vehicles;

STORE stats INTO '/traffic_results' USING PigStorage(',');

