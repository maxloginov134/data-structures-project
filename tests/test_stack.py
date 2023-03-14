"""Здесь надо написать тесты с использованием pytest для модуля stack."""
from src.stack import Node, Stack


def test_node_init():
    assert Node(next_node="next_node", data="data1")


