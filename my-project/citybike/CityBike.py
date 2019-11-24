#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from matplotlib import pyplot as plot

import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

class Clust:

    def __init__(self, fileData):
    
        self.file = fileData
        self.spark = SparkSession.builder.appName('CityBiKe').master('spark://192.168.0.15:7077').getOrCreate()
        
    def dataPreprocessing(self):
        print ("dataPreprocessing")
        bikes = self.spark.read.json(self.file, multiLine=True)
        bikes.show()
        bikesPandas = bikes.toPandas()
        #To be improved
        coordinatesToBeClustered = bikesPandas.drop(columns=['id', 'address','coordinates','position','name'])

        #Cleaning data: remove NA values and inconsistant values
        coordinatesToBeClustered= coordinatesToBeClustered.dropna()

        # Remove the label 'not relevant' on the longitude and latitude 
        coordinatesToBeClustered = coordinatesToBeClustered.set_index("longitude")
        coordinatesToBeClustered = coordinatesToBeClustered.drop("not relevant", axis = 0)
        coordinatesToBeClustered = coordinatesToBeClustered.reset_index()
        coordinatesToBeClustered = coordinatesToBeClustered.set_index("latitude")
        coordinatesToBeClustered = coordinatesToBeClustered.drop("not relevant", axis = 0)
        coordinatesToBeClustered = coordinatesToBeClustered.reset_index()


        #Convert all data from String to float
        coordinatesToBeClustered = coordinatesToBeClustered.astype(float)
        df = self.spark.createDataFrame(coordinatesToBeClustered)
        return df

    def dataplotting(self):
        colormap=np.array(['Red','green','blue','yellow','pink','black'])
        plot.scatter(self.coordinatesToBeClustered.iloc[:,0],self.coordinatesToBeClustered.iloc[:,1], c='b')
        plot.show()


    def Kmeans(self, dataframe):
        # We are going to use the Elbow method to determine the best number of cluster
        #Kmeans clustering model
        
        #In ML Pyspark, Kmeans need features
        assembler = VectorAssembler(inputCols=['latitude','longitude'],outputCol="features")
        dataframe = assembler.transform(dataframe)

        cost = np.zeros(20)
        for k in range (2,20):
            kmeans = KMeans().setK(k).setSeed(1)
            model = kmeans.fit(dataframe)
            cost[k] = model.computeCost(dataframe)

        fig, ax = plot.subplots(1,1, figsize =(8,6))
        ax.plot(range(2,20),cost[2:20])
        ax.set_xlabel('Number of Clusters')
        ax.set_ylabel('Score')
        ax.set_title("Elbow curve")

        centers = model.clusterCenters()
        print("Cluster Centers: ")
        for center in centers:
            print(center)
        return centers
    
def main():
        mycluster = Clust("Brisbane_CityBike.json")
        mycluster.Kmeans(mycluster.dataPreprocessing())
        
if __name__ == '__main__':
    
    main()

