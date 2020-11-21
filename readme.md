Proyecto #2 SO2 - DStore. Hecho por: Angel Rojas 2016-5474

Funcionamiento del Proyecto:

El DStore funciona mediante la combinacion de los siguientes modulos: workernode y clientprogram.

Workernode: El modulo workernode representa todos los nodos de la red estatica que trabajan para manejar el DStore. Cada workernode se inicializa con el puerto en el que va a correr mediante la linea de comando. Los nodos utilizan una API con 5 funciones especificas para poder cumplir los requisitios al comunicarse con el client application. Cada nodo tiene una memoria individual representada mediante un Diccionario. Cada nodo inicializa un servidor XMLRPC mediante un websocket en un puerto especifico. Al inicializarse, los nodos utilizan los archivos auxiliares titulados '[puerto].xml' los cuales tienen las especificaciones xml de los puertos vecinos a los cuales el nodo debe comunicar. Cuando el cliente se comunica con el nodo principal, este ubica le reenvia el mensaje a sus nodos vecinos, y se repite el proceso recursivamente en los otros nodos.

Clientprogram: El modulo clientprogram inicializa un cliente XMLRPC que se conecta al puerto del workernode principal y inicializa el menu del DStore. Cada vez que el usuario digita una accion concerniente a la tienda, el client le envia el mensaje al workernode inicial mediante la API, para alterar la memoria.

Como correr el Demo del Proyecto de manera satisfactoria:

1. Inicializar los 4 nodos de la red utilizando el comando 'py workernode.py [puerto]'. Los 4 puertos preescritos en los archivos son los puertos 8000, 8001, 8002, y 8003.
2. Inicializar el modulo clientprogram utilizando el comando 'py clientprogram.py'
3. Seguir las instrucciones del menu que surge al ejecutar el paso 2 para realizar las pruebas del DStore.
