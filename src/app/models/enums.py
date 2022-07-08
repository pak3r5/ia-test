from enum import Enum


class OrderType(str, Enum):
    PENDING = 'Pending'
    IN_PROCESS = 'In Process'
    COMPLETED = 'Completed'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'


def get_status_to_int(order: OrderType) -> int:
    if order == OrderType.PENDING:
        return 0
    elif order == OrderType.IN_PROCESS:
        return 1
    elif order == OrderType.COMPLETED:
        return 2
    elif order == OrderType.DELIVERED:
        return 3
    elif order == OrderType.CANCELED:
        return 4
    return -1


def get_status_to_order_type(order: int) -> OrderType:
    if order == 0:
        return OrderType.PENDING
    elif order == 1:
        return OrderType.IN_PROCESS
    elif order == 2:
        return OrderType.COMPLETED
    elif order == 3:
        return OrderType.DELIVERED
    elif order == 4:
        return OrderType.CANCELED
    return OrderType.PENDING


def get_status_str_to_order_type(order: str) -> OrderType:
    if order.upper() == 'PENDING':
        return OrderType.PENDING
    elif order.upper() == 'IN_PROCESS':
        return OrderType.IN_PROCESS
    elif order.upper() == 'COMPLETED':
        return OrderType.COMPLETED
    elif order.upper() == 'DELIVERED':
        return OrderType.DELIVERED
    elif order.upper() == 'CANCELED':
        return OrderType.CANCELED
    return OrderType.PENDING
