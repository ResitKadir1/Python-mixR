import pyarrow.parquet as pq

table = pq.read_table("taxi.parquet")

#apache arrow
df = table.to_pandas()

print(df.types)


