#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Intialization
import os
import sys

os.environ["SPARK_HOME"] = "/home/talentum/spark"
os.environ["PYLIB"] = os.environ["SPARK_HOME"] + "/python/lib"
# In below two lines, use /usr/bin/python2.7 if you want to use Python 2
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3.6" 
os.environ["PYSPARK_DRIVER_PYTHON"] = "/usr/bin/python3"
sys.path.insert(0, os.environ["PYLIB"] +"/py4j-0.10.7-src.zip")
sys.path.insert(0, os.environ["PYLIB"] +"/pyspark.zip")

# NOTE: Whichever package you want mention here.
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-xml_2.11:0.6.0 pyspark-shell' 
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.11:2.4.0 pyspark-shell'
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-xml_2.11:0.6.0,org.apache.spark:spark-avro_2.11:2.4.3 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-xml_2.11:0.6.0,org.apache.spark:spark-avro_2.11:2.4.0 pyspark-shell'


# In[2]:


#Entrypoint 2.x
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()

# On yarn:
# spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().master("yarn").getOrCreate()
# specify .master("yarn")

sc = spark.sparkContext


# In[3]:


get_ipython().system('pwd')


# In[8]:


# Reading the file
tips_df = spark.read.csv('file:///home/talentum/test-jupyter/exam/tips.csv', header=True, inferSchema=True)


# In[9]:


tips_df.show(4)


# In[14]:


# Print the schema
tips_df.printSchema()


# In[15]:


# calculating new df with precentage
tips_df_precentage = tips_df.withColumn('tip_percentage', (tips_df.tip/tips_df.total_bill)*100)
tips_df_precentage.show(2)


# In[18]:


tips_above_threshold_df = tips_df_precentage.filter(tips_df_precentage.tip_percentage >= 5)
tips_above_threshold_df.show(5)


# In[29]:


# Pringting the total tips which re greate than 5$
print(f"Number of tips (Dataframe): {tips_above_threshold_df.count()}")


# In[27]:


# Using sql to to the same thing
tips_df.createOrReplaceTempView("tips")


# Writing the quey 
tips_above_threshold_sql = spark.sql("""
    SELECT * 
    FROM tips
    WHERE (tip/ total_bill)*100 >= 5
""")

# Show the result
tips_above_threshold_sql.show(5)


# In[28]:


# Sohwing total sql results
print(f"Number of tips (SQL): {tips_above_threshold_sql.count()}")

