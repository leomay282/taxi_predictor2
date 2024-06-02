import pandas as pd


def agregate_columns_to_input(
    dataset: pd.DataFrame,
):
    # Replace tpep_pickup_datetime and tpep_dropoff_datetime columns with new columns
    dataset["pickup_year"] = dataset["tpep_pickup_datetime"].dt.year # si
    dataset["pickup_day"] = dataset["tpep_pickup_datetime"].dt.day # si
    dataset["pickup_hour"] = dataset["tpep_pickup_datetime"].dt.hour # si
    dataset["pickup_minute"] = dataset["tpep_pickup_datetime"].dt.minute # si
    dataset["pickup_day_of_week"] = dataset["tpep_pickup_datetime"].dt.dayofweek # si

    dataset["average_speed_mph"] = 2 # si esta mal!

def drop_column_if_exists(dataset, column_name):
    if column_name in dataset.columns:
        dataset.drop(column_name, inplace=True, axis=1)

    # Luego puedes llamar a esta función para cada columna que quieras eliminar
    drop_column_if_exists(dataset, "tip_amount")
    drop_column_if_exists(dataset, "extra")
    drop_column_if_exists(dataset, "improvement_surcharge")
    drop_column_if_exists(dataset, "fare_amount")
    drop_column_if_exists(dataset, "VendorID")
    drop_column_if_exists(dataset, "store_and_fwd_flag")
    drop_column_if_exists(dataset, "trip_distance")
    drop_column_if_exists(dataset, "RatecodeID")
    drop_column_if_exists(dataset, "tolls_amount")
    drop_column_if_exists(dataset, "tpep_pickup_datetime")


    return dataset
