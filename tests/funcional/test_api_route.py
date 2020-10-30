import json
import pdb

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

            f = open('files/input-routes.csv')
            lines = f.readlines()
            f.close()

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

        should_add_new_line_to_routes_file(test_client)