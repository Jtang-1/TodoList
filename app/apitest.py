import unittest
import requests
import sys #print(..., file=sys.stderr)



class ApiTest (unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"
    TODOURL = BASE + "todo"
    TODOLISTURL = BASE + "todolist"
    TODO_OBJ = {
        "id": 1,
        "content": "Drink Water"
    }
    NEW_TODO_OBJ = {
        'id': 1,
        'content': 'Eat Food'
    }

    def _get_each_task_url(self,id):
        return f'{ApiTest.TODOURL}/{id}'

    #POST request to /todo to create a new todo
    def test_1_add_new_task(self):
        response = requests.post(ApiTest.TODOURL, json = ApiTest.TODO_OBJ)
        self.assertEqual(response.status_code,201)

    #GET request to test new task is added
    def test_2_get_new_tastk(self):
        id = ApiTest.TODO_OBJ['id']
        response = requests.get(self._get_each_task_url(id))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), ApiTest.TODO_OBJ)

    #PUT reqest to test updating task
    def test_3_update_existing_task(self):
        id = ApiTest.TODO_OBJ['id']

        response = requests.put(self._get_each_task_url(id), json = ApiTest.NEW_TODO_OBJ)
        self.assertEqual(response.status_code, 201)

    # GET request to test task is updated
    def test_4_get_new_book_ater_update(self):
        id = ApiTest.TODO_OBJ['id']
        response = requests.get(self._get_each_task_url(id))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), ApiTest.NEW_TODO_OBJ)
    
    #DELETE request
    def test_5_delete_tast(self):
        id = ApiTest.TODO_OBJ['id']
        response = requests.delete(self._get_each_task_url(id))
        self.assertEqual(response.status_code, 204)

    #Check Deleted
    def test_6_get_new_book_ater_update(self):
        id = ApiTest.TODO_OBJ['id']
        response = requests.get(self._get_each_task_url(id))
        self.assertEqual(response.status_code, 404)




        

    



