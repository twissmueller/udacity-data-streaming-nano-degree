from pyspark.sql import SparkSession


def create_spark_session():
    spark = SparkSession.builder \
        .master("local") \
        .config("spark.ui.port", 3000) \
        .appName("Spark UI") \
        .getOrCreate()

if __name__ == "__main__":
    create_spark_session()
