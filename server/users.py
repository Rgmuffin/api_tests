import cherrypy

users = {
    '1': {
        'username': 'Artem R',
        'email': 'artem_r@gmail.com',
        'department': 'Alpha',
        'date_joined': '2020-02-11'
    },
    '2': {
        'username': 'Oleg T',
        'email': 'oleg_t@gmail.com',
        'department': 'Alpha',
        'date_joined': '2020-02-11'
    },
    '3': {
        'username': 'Ivan S',
        'email': 'ivan_s@gmail.com',
        'department': 'Delta',
        'date_joined': '2020-02-11'
    },
    '4': {
        'username': 'Vladimir P',
        'email': 'vladimir_p@gmail.com',
        'department': 'Delta',
        'date_joined': '2020-02-11'
    },
    '5': {
        'username': 'Tatyana V',
        'email': 'tatyana_v@gmail.com',
        'department': 'Omega',
        'date_joined': '2020-02-11'
    },
    '6': {
        'username': 'Arthur K',
        'email': 'arthur_k@gmail.com',
        'department': 'Omega',
        'date_joined': '2020-02-11'
    },
}

class Users:
    def GET(self, username=None, department=None):
        data1 = []
        data2 = []
        if username == None:
            for user in users:
                data1.append(users[user])
        else:
            for user in users:
                if username in users[user]['username']:
                    data1.append(users[user])
        if department == None:
            for user in users:
                data2.append(users[user])
        else:
            for user in users:
                if department == users[user]['department']:
                    data2.append(users[user])
        data3 = []
        for item in data1:
            if item in data2:
                data3.append(item)
        return ('data: %s' % data3)

    exposed = True


class Departments:
    def GET(self, department=None):
        data1 = []
        if department == None:
            for dept in users:
                data1.append(users[dept]["department"])
            return ('List of Departments: %s' % list(sorted(set(data1))))
        else:
            for dept in users:
                if department in users[dept]['department']:
                    data1.append(users[dept])
        return (f'Users in department {department}: {data1}')

    exposed = True

if __name__ == '__main__':
    cherrypy.tree.mount(
        Users(), '/api/users', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Departments(), '/api/department',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.engine.start()
cherrypy.engine.block()


