import pygame
import json

from csv import reader

from arcade.func.read_json import read_json

config = read_json(file="./arcade/data/config.json")