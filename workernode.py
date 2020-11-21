from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import time
import xmlrpc.client
import sys
import xml.etree.ElementTree as ET

# Restrict to a particular path.
DStore_Dictionary = {}
port = int(sys.argv[1])
neighborPorts = []
neighborClients = []
hasNeighbors = True

try:
    # do something
    tree = ET.parse(f'{port}.xml')
    root = tree.getroot()

    for child in root:
        neighborPorts.append(child.attrib["port"])

    for p in neighborPorts:
        neighborClients.append(
            xmlrpc.client.ServerProxy(f'http://localhost:{p}'))

except FileNotFoundError:
    # handle ValueError exception
    hasNeighbors = False


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', int(sys.argv[1])),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    class DStoreAPI:

        def Set(self, name, val):
            DStore_Dictionary[name] = val
            if(hasNeighbors):
                for client in neighborClients:
                    client.Set(name, val)
            return 'Added Succesfully'

        def Get(self, name):
            try:
                # do something
                if(hasNeighbors):
                    for client in neighborClients:
                        client.Get(name)
                return DStore_Dictionary[name]

            except KeyError:
                # handle ValueError exception
                return 'Item not found in store!'

        def Inc(self, name):
            try:
                # do something
                if(hasNeighbors):
                    for client in neighborClients:
                        client.Inc(name)
                DStore_Dictionary[name] = DStore_Dictionary[name] + 1
                return DStore_Dictionary[name]

            except TypeError:
                # handle ValueError exception
                return 'Item value is not a number!'

            except KeyError:
                # handle ValueError exception
                return 'Item not found in store!'

        def Delete(self, name):
            try:
                # do something
                if(hasNeighbors):
                    for client in neighborClients:
                        client.Delete(name)
                DStore_Dictionary.pop(name)
                return 'Deleted Succesfully'

            except KeyError:
                # handle ValueError exception
                return 'Item not found in store!'

        def Expire(self, name, val):
            # Python 3.7+
            if(hasNeighbors):
                for client in neighborClients:
                    client.Expire(name, val)

            def delete():
                DStore_Dictionary.pop(name)
                return 'deleted succesfully'
            x = threading.Timer(val, delete)
            x.start()
            return 'timer set succesfully'

    server.register_instance(DStoreAPI())

    # Run the server's main loop
    server.serve_forever()
