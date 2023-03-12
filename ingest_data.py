#!/usr/bin/env python
# coding: utf-8

import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    """Main function to receive user params and use them to create and 
    populate an Postgresql database
       Create 6 tables, one from each csv file.

    Args:
        params:
            user - user name for postgres
            password - password for postgres
            host - host for postgres
            port - port for postgres
            db - database name for postgres
            path - path for the csv files'

    """
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    path = params.path
    name_files = [
                  'Person.Person', 'Production.Product', 'Sales.Customer', 
                  'Sales.SalesOrderDetail', 'Sales.SalesOrderHeader', 
                  'Sales.SpecialOfferProduct'
                 ]

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    for item in name_files:
        path = rf"{path}\{item}.csv"
        t_start = time()
        df = pd.read_csv(path, sep=';')
        df.ModifiedDate = pd.to_datetime(df.ModifiedDate)
        df.head(n=0).to_sql(name=item, con=engine, if_exists='replace')
        df.to_sql(name=item, con=engine, if_exists='append')
        t_end = time()
        print('Inserted another File, took %.3f second' % (t_end - t_start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--path', required=True, help='path for the csv files')

    args = parser.parse_args()

    main(args)