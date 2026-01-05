# bigdata_traffic_project
Instituto Politecnico Nacional
Unidad Profesional Interdisciplinaria en Ingenieria Campus Tlaxcala
Licenciatura en Ciencia de Datos
Big Data

El presente proyecto fue realizado por:
Abraham Morales Sánchez, 2023710098
Ricardo Sebastian Garcia Lopez, 2023710120
Luis Eduardo Beristain Cuecuecha, 2022710277

Pasos Para reproducir el proceso Realizado:
1. cd Documentos/proyecto
2. nano generate_traffic_data.py
3. python3 generate_traffic_data.py
4. start-all.sh
5. hadoop-daemon.sh start datanode
6. jps (Verificar que este NameNode y DataNode)
7. hdfs dfsadmin -safemode leave
8. hdfs dfs -mkdir /traffic_data
9. hdfs dfs -put traffic_data.csv /traffic_data/
10. hdfs dfs -ls /traffic_data
11. hive
12. En hive: CREATE TABLE traffic (
          sensor_id INT,
          event_time STRING,
          location STRING,
          speed DOUBLE,
          vehicle_count INT
          )
          ROW FORMAT DELIMITED
          FIELDS TERMINATED BY ','
          STORED AS TEXTFILE;

12. En hive: LOAD DATA INPATH '/traffic_data/traffic_data.csv' INTO TABLE traffic;
13. En hive: SELECT location, AVG(speed), SUM(vehicle_count)
          FROM traffic
          GROUP BY location; 

14. nano traffic_analysis.pig
15. pig traffic_analysis.pig
16. hdfs dfs -ls /traffic_results
17. hdfs dfs -cat /traffic_results/part-r-00000
18. nano traffic_clustering.py
19. /opt/spark/bin/spark-submit traffic_clustering.py
20. hdfs dfs -get /traffic_predictions ./traffic_predictions
21. nano visualization.py
22. python3 visualization.py
