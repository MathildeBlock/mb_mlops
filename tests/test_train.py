import pytest
from my_project.train import train

def test_train():
    assert train() == 'Training is successful'
