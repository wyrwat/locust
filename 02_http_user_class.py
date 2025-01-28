from locust import HttpUser,constant, task


class MyReqRes(HttpUser):

    host = 'https://regres.in'
    wait_time = constant(1)

    @task
    def get_user(self):
        request =  self.client.get('/api/users?page=2')
        print(request.text)
        print(request.status_code)
        print(request.headers)


    @task
    def create_user(self):
        request = self.client.post('/api/users', data='''{'name': 'morpheus', 'job': 'leader'}''')
        print(request.text)
        print(request.status_code)
        print(request.headers)