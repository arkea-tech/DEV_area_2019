from elasticsearch import Elasticsearch
import urllib3
import json
import datetime
import ssl
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ElasticSearchInterface:

    def __init__(self, in_docker=True):
        """
        Initialisation of ElasticSearchInterface class
        :param in_docker: if server is running in a docker container
        """
        if in_docker is True:
            self.es = Elasticsearch(
                hosts=["db:9200"],
                verify_certs=False
            )
        else:
            self.es = Elasticsearch(
                hosts=["localhost:9200"],
                verify_certs=False
            )

    def create_index(self, index_name: str):
        """
        Create a new index supposing index name is unique
        :param index_name: name of the new index
        :return: OK / KO
        """
        if self.es.indices.exists(index=index_name) is True:
            return "KO"
        else:
            request_body = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                }
            }
            print('\nCreating index: {}'.format(index_name.upper()))
            self.es.indices.create(
                index=index_name,
                body=request_body
            )
            return "OK"

    def reset_index(self, index_name: str):
        """
        Reset an existing index or create it if does not exist
        :param index_name: name of the index to reset
        :return: OK/KO
        """
        self.delete_existing_index(index_name)
        request_body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        }
        print('\nResetting index: {}'.format(index_name.upper()))
        self.es.indices.create(index=index_name,
                               body=request_body)
        return "OK"

    def delete_existing_index(self, index_name: str):
        """
        Delete existing index
        :param index_name: name of the index to delete
        :return: OK/KO
        """
        if self.es.indices.exists(index=index_name) is True:
            print('\nDeleting index: {}'.format(index_name.upper()))
            self.es.indices.delete(index_name)
            return "OK"
        else:
            print('Index {} already exists'.format(index_name.upper()))
            return "KO"

    def index_data(self, index_name: str, data=None):
        """
        Index some data into a specific index
        :param index_name: name of the index where we index the data
        :param data: the data to index
        :return: OK/KO
        """
        key = '%030x' % random.randrange(16 ** 30)
        self.es.index(index=index_name, id=key, body=data)
        self.es.indices.refresh(index=index_name)
        return "OK"

    def account_already_exists(self, email: str):
        """
        Return bool describing if account already exists or not
        :param email: email of the account to check
        :return: True/False
        """
        query = {"query": {"bool": {"must": {"term": {"email": email}}}}}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) > 0:
            return True
        return False

    def account_uuid_exists(self, uuid: str):
        """
        Check if a user already exists based on uuid
        :param uuid: uuid of supposed user
        :return: True/False
        """
        query = {"query": {"bool": {"must": {"match": {"_id": uuid}}}}}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) > 0:
            return True
        return False

    def get_user_services(self, uuid):
        """
        Return all user's AREAs
        :param uuid: user uuid
        :return: list (or empty list) of area
        """
        query = {"query": {"bool": {"must": {"match": {"_id": uuid}}}}}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) < 1:
            return []
        services = res['hits']['hits'][0]['_source']['services']
        return services

    def get_user_from_uuid(self, uuid):
        """
        Get user document
        :param uuid: user uuid
        :return: document
        """
        query = {"query": {"bool": {"must": {"match": {"_id": uuid}}}}}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) < 1:
            return []
        return res['hits']['hits'][0]['_source']

    def get_user_notifs(self, uuid):
        """
        Get all notifications for a user
        :param uuid: user uuid
        :return: list of notifications
        """
        query = {"query": {"bool": {"must": {"match": {"_id": uuid}}}}}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) < 1:
            return []
        notifs = res['hits']['hits'][0]['_source']['notifications']
        return notifs

    def get_user_uuids(self):
        """
        Get all users' uuids
        :return: list of uuids
        """
        query = {"size": 25, "_source": ["_id"]}
        res = self.es.search(index='accounts', body=query)
        if len(res['hits']['hits']) < 1:
            return []
        ids = []
        for elem in res['hits']['hits']:
            ids.append(elem['_id'])
        return ids

    def update_user_services(self, uuid, services):
        """
        Force an update on user's AREA
        :param uuid: user uuid
        :param services: updated AREAs
        :return: nothing
        """
        self.es.update(index='accounts', id=uuid, body={"doc": {"services": services}})
        self.es.indices.refresh(index='accounts')

    def delete_user_services(self, uuid):
        """
        Delete user's AREAs
        :param uuid: user uuid
        :return: nothing
        """
        self.es.update(index='accounts', id=uuid, body={"doc": {"services": []}})
        self.es.indices.refresh(index='accounts')

    def update_user_tokens(self, uuid, tokens):
        """
        Update user's access tokens
        :param uuid: user uuid
        :param tokens: new user's access tokens
        :return: nothing
        """
        self.es.update(index='accounts', id=uuid, body={"doc": {"access_tokens": tokens}})
        self.es.indices.refresh(index='accounts')
