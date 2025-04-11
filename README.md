# Patrones-Estructurales
Decorator and Proxy Activity

¿Cuál es la principal diferencia entre el patrón Decorator y el patrón Proxy?
La principal diferencia entre estos patrones es que tienen diferentes intenciones al momento de envolver un objeto para agregar funcionalidad.
El decorator agrega funcionalidades adicionales mientras que el Proxy controla el acceso al objeto. El enfoque del decorator es extender el comportamiento del objeto mientras que el proxy controla el acceso al objeto o sustituye su instancia.


¿En qué tipo de escenarios usarías cada uno?
Usaría el Decorator para agregar responsabilidades adicionales sin modificar la clase original, como un sistema de pedidos de bebidas donde puedes agregar multiples cosas a la bebida de manera opcional. Sin embargo, usaria Proxy para realizar tareas como cargar bajo demanda, logs o control de acceso; como lo puede ser acceder a una imagen que solo se carga cuando se necesite.
