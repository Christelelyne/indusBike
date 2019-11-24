## Testing the ability to industrialize a source code

## Context

The data is from the Static geographical information of CityBike‘s stations in Brisbane. 
Here are the different variables of our case:

  - address
  - coordinates
  - longitude
  - latitude
  - position
  - id
  
  The code will be launched on 10Go of data in a daily frequency.

## Description

  The program is generating the clusters from a dataset of bike stations. In input there is a JSON file with several parameters, the goal is to gather the relevant information, perform the clustering and industrialize the program.
  
  The clustering algorithm implemented will be based on the longitude and latitude variables.
  The clustering method used here is Kmeans from the ML PySpark library.
  
  
 ## LAUNCH THE JOB
 1.   Command to be executed on Spark cluster
 
      **spark-submit --master spark://<Spark_cluster>:7077 --executor-memory 4G CityBike.py Brisbane_CityBike.json**
      
      *<Spark_Cluster>: DNS or IP address  of used spark cluster*
      
      *executor-memory: Depending on the number of cores and the entire memory on the cluster(10Go of data scheduled)*
      
 2. Create a scheduler 
 
    - On Linux, depending on permissions, edit your crontab file and update it accordingly
    - On windows, task scheduler is helpful to achieve this task
    - On Azure platform, there is a scheduler which can be configured, in this use case your Spark should be in the cloud.
 
