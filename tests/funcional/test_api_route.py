import json
import pdb

from graph import graph

FILE_PATH = 'files/input-routes.csv'

class TestRouteResource():
    url_route_add = '/route/add'
    url_route_find = '/route/find'

    def test_add_route_endpoint(self, test_client):
        def should_add_new_line_to_routes_file(test_client):
            data = {
                'weight': 30,
                'initial_position': 'BPS',
                'final_position': 'GRU'
            }

            with open(FILE_PATH, 'r') as f:
                lines = f.readlines()

            total_lines = len(lines)

            response = test_client.post(self.url_route_add, data=json.dumps(data))

            res_data = json.loads(response.data)

            assert res_data == True

            f = open('files/input-routes.csv')
            lines = f.readlines()
            f.close()

            assert len(lines) == total_lines+1
            last_line = lines[-1]

            assert last_line == '{},{},{}'.format(data['initial_position'], data['final_position'], data['weight'])

        def should_return_400_if_initial_position_is_not_str(test_client):
            data = {
                'weight': 30,
                'initial_position': 44444,
                'final_position': 'GRU'
            }

            response = test_client.post(self.url_route_add, data=json.dumps(data))
            assert response.status_code == 400

        def should_return_400_if_final_position_is_not_str(test_client):
            data = {
                'weight': 30,
                'initial_position': 'GRU',
                'final_position': 333.0
            }

            response = test_client.post(self.url_route_add, data=json.dumps(data))
            assert response.status_code == 400

        def should_return_400_if_weight_is_not_int(test_client):
            data = {
                'weight': 'LLL',
                'initial_position': 'CDG',
                'final_position': 'GRU'
            }

            response = test_client.post(self.url_route_add, data=json.dumps(data))
            assert response.status_code == 400

        def should_return_400_if_weight_is_smaller_than_1(test_client):
            data = {
                'weight': 0,
                'initial_position': 'CDG',
                'final_position': 'GRU'
            }

            response = test_client.post(self.url_route_add, data=json.dumps(data))
            assert response.status_code == 400

        should_add_new_line_to_routes_file(test_client)
        should_return_400_if_initial_position_is_not_str(test_client)
        should_return_400_if_final_position_is_not_str(test_client)
        should_return_400_if_weight_is_not_int(test_client)
        should_return_400_if_weight_is_smaller_than_1(test_client)


    def test_find_route_endpoint(self, test_client):
        def should_return_expected_route_in_expected_format(test_client):
            data = {
                'initial_position': 'GRU',
                'final_position': 'CDG'
            }

            response = test_client.get(self.url_route_find, query_string=data)
            res_data = json.loads(response.data)

            g = graph.create_graph(FILE_PATH)
            best_route_price = graph.get_best_route_price(g, data['initial_position'], data['final_position'])

            assert best_route_price == res_data

        def should_return_400_if_initial_position_does_not_exist(test_client):
            data = {
                'initial_position': 'DDD',
                'final_position': 'LLL'
            }

            response = test_client.get(self.url_route_find, query_string=data)
            assert response.status_code == 400

        def should_return_400_if_final_position_does_not_exist(test_client):

            data = {
                'initial_position': 'GRU',
                'final_position': 'LLL'
            }

            response = test_client.get(self.url_route_find, query_string=data)
            assert response.status_code == 400

        def should_return_200_if_theres_no_path_available(test_client):
            data = {
                'initial_position': 'CDG',
                'final_position': 'GRU'
            }

            response = test_client.get(self.url_route_find, query_string=data)
            res_data = json.loads(response.data)
            assert response.status_code == 200
            assert res_data == 'It is not possible to go from {} to {}'.format(data['initial_position'], data['final_position'])

        should_return_expected_route_in_expected_format(test_client)
        should_return_400_if_initial_position_does_not_exist(test_client)
        should_return_400_if_final_position_does_not_exist(test_client)
        should_return_200_if_theres_no_path_available(test_client)
