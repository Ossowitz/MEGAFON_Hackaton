import json
import psycopg2
import requests

from common.customer import Customer

with open('body.json', 'r') as file1, open('new_body.json', 'r') as file2:
    body = json.load(file1)
    new_body = json.load(file2)

customer = Customer(body)
dumps = customer.__dict__()
print(dumps)

url = "http://dbss-sso.external.rm-dhekoli.cloud.billing.ru:47226/openapi/v1/customerManagement/customers"
auth = ('Admin', '1111')

response = requests.post(url, json=dumps, auth=auth)

client_id = response.json()["customerId"]
get_url = url + '/' + str(client_id)

get_response = requests.get(get_url, auth=auth)

print(client_id)
print(get_response)

first_name = new_body['party']['nameInfo']['firstName']
patronymic = new_body['party']['nameInfo']['patronymic']
surname = new_body['party']['nameInfo']['surname']

connection_params = {
    "database": "CHM",
    "user": "chm",
    "password": "chm",
    "host": "dbss-postgres.rm-root.cloud.billing.ru",
    "port": "5432"
}

with psycopg2.connect(**connection_params) as conn:
    with conn.cursor() as cur:
        update_query = """
            UPDATE public.cam_int_customers
            SET prt_joined_name = %s,
                prt_first_name = %s,
                prt_surname = %s,
                prt_patronymic = %s
            WHERE cust_id = %s
        """
        client_data = (surname + " " + first_name + " " + patronymic, first_name, surname, patronymic, client_id)

        cur.execute(update_query, client_data)
        conn.commit()
