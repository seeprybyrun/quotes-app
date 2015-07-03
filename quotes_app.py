#!/usr/bin/env python

import psycopg2


class Table(object):
    table_name = ''
    field_names = []

    @classmethod
    def get_records_satisfying(cls, **kwargs):
        fields_to_fill = set(cls.field_names) & set(kwargs.keys())

        if not fields_to_fill:
            raise Exception('No valid parameters given')

        query = 'SELECT * FROM {} WHERE '.format(cls.table_name)
        query += ' AND '.join(['{} = %s'.format(field) for field in fields_to_fill])
        params = [kwargs[field] for field in fields_to_fill]

        result = _query_db(query, params)
        return [record for record in result]


    @classmethod
    def get_all_records(cls):
        query = 'SELECT * FROM {}'.format(cls.table_name)
        result = _query_db(query)
        return [record for record in result]


    @classmethod
    def add_record(cls, **kwargs):
        fields_to_fill = set(cls.field_names) & set(kwargs.keys())

        if not fields_to_fill:
            raise Exception('No valid parameters given')

        braces_separated_by_commas = ', '.join(['{}'] * len(fields_to_fill))
        fields_to_fill_as_string = braces_separated_by_commas.format(*fields_to_fill)

        values_to_insert = [kwargs[field] for field in fields_to_fill]
        percent_esses = ', '.join(['(%s)'] * len(fields_to_fill))

        query = 'INSERT INTO {} ({}) VALUES ({});'.format(cls.table_name, fields_to_fill_as_string, percent_esses)

        _query_db_and_commit(query, values_to_insert)


    @classmethod
    def delete_record_by_id(cls, id_number):
        query = 'DELETE FROM {} WHERE id = %s'.format(cls.table_name)
        params = [id_number]
        _query_db_and_commit(query, params)


    @classmethod
    def delete_all_records(cls):
        query = 'DELETE FROM {}'.format(cls.table_name)
        _query_db_and_commit(query)


class Addresses(Table):
    field_names = ['street_address', 'city', 'us_state', 'zip_code', 'id']
    table_name = 'addresses'


class Customers(Table):
    field_names = ['first_name', 'last_name', 'email', 'phone', 'mailing_address']
    table_name = 'customers'


def _query_db(query, *query_arguments):
    db_connection = _connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute(query, *query_arguments)
    result = cursor.fetchall()
    db_connection.close()
    return result


def _query_db_and_commit(query, *query_arguments):
    db_connection = _connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute(query, *query_arguments)
    db_connection.commit()
    db_connection.close()


def _connect_to_db():
    return psycopg2.connect("dbname=quotes_app")


def _pair_consecutive_elements(iterable):
    return zip(iterable[::2], iterable[1::2])
