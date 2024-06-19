#Loadbalancer distributes incoming requests among a pool of servers
class Server:
    def __init__(self,name):
        self.name=name
        self.load=0

    def handle_request(self):
        self.load+=1
        print(f"Server {self.name} is handling the request. Current load {self.load}")

    def finish_request(self):
        self.load-=1
        print(f"Server {self.name} has finished a request. Current load: {self.load}")
    
class LoadBalancer:
    def __init__(self,servers):
        self.servers=servers
        self.index=0
    def get_next_server(self):
        server=self.servers[self.index]
        self.index=(self.index+1)%len(self.servers)
        return server
    
    def handle_request(self):
        server=self.get_next_server()
        server.handle_request()

#creating a list of servers
servers=[Server("A"),Server("B"),Server("C")]
#init the load balancers with the servers
load_balancer=LoadBalancer(servers)

#simulating of handling of servers
for _ in range(10):
    load_balancer.handle_request()