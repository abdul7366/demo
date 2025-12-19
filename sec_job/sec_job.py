import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .load("s3://bucketdec162025abd/departments.csv")


df.write \
    .mode("overwrite") \
    .format("csv") \
    .option("header", "true") \
    .save("s3://bucketdec162025abd/dec18abd")

job.commit()