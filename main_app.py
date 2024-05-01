import cherrypy
import os


class ServerConfigurator:
    @staticmethod
    def get_cherrypy_config():
        return {
            '/': {
                'tools.sessions.on': True,
                'tools.response_headers.on': True,
                'tools.response_headers.headers': [('Content-Type', 'application/json')],
            }
        }

    @staticmethod
    def configure_server(port):
        cherrypy.config.update({'server.socket_port': port})

    @staticmethod
    def start_service():
        config = ServerConfigurator.get_cherrypy_config()
        # Placeholder for service start
        cherrypy.quickstart(None, '/', config)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    ServerConfigurator.configure_server(port)
    ServerConfigurator.start_service()
