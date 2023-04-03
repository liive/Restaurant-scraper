import psycopg2
from sqlalchemy import create_engine
from config import host, dbname, user, password, port

# PostgreSQL database credentials


def load_data_to_database(df):

    # create a connection string to connect to the database
    conn_str = (
        f"host={host} dbname={dbname} user={user} password={password} port={port}"
    )

    # create a connection object by passing a connection string to the 'psycopg2.connect()' method to interact with the database
    conn = psycopg2.connect(conn_str)
    # create a cursor object by calling the 'cursor()' method on the connection object "conn" to execute SQL queries on the database
    cursor = conn.cursor()

    # drop the 'restaurants' table if it exists
    drop_table_query = "DROP TABLE IF EXISTS restaurants;"
    cursor.execute(drop_table_query)
    conn.commit()

    # Create the 'restaurants' table
    create_table_query = """
    CREATE TABLE restaurants (
        id SERIAL PRIMARY KEY,
        business_name VARCHAR,
        tripadvisor_rating DECIMAL,
        tripadvisor_number_reviews VARCHAR,
        phone_number VARCHAR,
        yp_number_ofratings INTEGER,
        yp_star_ratings DECIMAL,
        street_address VARCHAR,
        locality VARCHAR,
        region VARCHAR,
        postalcode VARCHAR
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Create a connection string for SQLAlchemy
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

    # Load data from the DataFrame into the "restaurants" table
    df.to_sql("restaurants", engine, if_exists="append", index=False)

    # Close the cursor and connecton to the PostgreSQL database
    cursor.close()
    conn.close()
