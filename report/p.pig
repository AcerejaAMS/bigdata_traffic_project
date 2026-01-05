raw = LOAD '/traffic_data/traffic_data.csv' USING PigStorage(',');
DUMP raw;
