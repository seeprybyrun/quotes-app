from quotes_app import *


def test_delete_all_addresses():
    Addresses.delete_all_records()
    addresses = Addresses.get_all_records()
    assert len(addresses) == 0
    print 'test_delete_all_addresses: passes'


def test_add_address():
    params = {
        'street_address': '615 Georgia Ave',
        'city': 'Hinesville',
        'us_state': 'GA',
        'zip_code': '30303'
    }
    Addresses.add_record(**params)
    assert Addresses.get_records_satisfying(**params)
    print 'test_add_address: passes'


def test_delete_all_customers():
    Customers.delete_all_records()
    customers = Customers.get_all_records()
    assert len(customers) == 0
    print 'test_delete_all_customers: passes'


def test_add_customer():
    params = {
        'first_name': 'Jane',
        'last_name': 'Roe',
        'email': 'jroe@example.com',
        'phone': '123-456-7890'
    }
    Customers.add_record(**params)
    assert Customers.get_records_satisfying(**params)
    print 'test_add_customer: passes'


if __name__ == '__main__':
    test_delete_all_addresses()
    test_add_address()
    test_delete_all_customers()
    test_add_customer()
    print 'Success! All tests pass!'
