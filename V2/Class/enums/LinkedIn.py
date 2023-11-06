from enum import Enum

class PageProfileButtons(Enum):
    CONNECT = "Conectar"
    PENDING = "Pendiente"
    FOLLOW = "Seguir"
    MAS = "Más acciones"

class Action(Enum):
    CONNECT = "Conectar"
    PENDING = "Pendiente"
    FOLLOW = "Seguir"
    MAS = "Más acciones"

class ConectionStatus(Enum):
    PENDING = "Esperando apruebe la conexion"
    FOLLOW = "Siguiendo"
    CONNECT = "Solicitud de conexion enviada"
    IMPOSSIBLE = "No es posible conectar"