from flask import Blueprint, render_template, request
from Src.Algorithms.Profundidade import Profundidade

def get_environment():
    return "Ola!!! eu sou um return!!!"


Router = Blueprint('router', __name__)

# @Router.route("/amplitude")
# def profundidade(): return Profundidade(get_environment())

@Router.route("/profundidade")
def profundidade(): return Profundidade(get_environment())

# @Router.route("/aprofundamento")
# def profundidade(): return Profundidade(get_environment())

# @Router.route("/bidirecional")
# def profundidade(): return Profundidade(get_environment())

# @Router.route("/custo_uniforme")
# def profundidade(): return Profundidade(get_environment())

# @Router.route("/greedy")
# def profundidade(): return Profundidade(get_environment())

# @Router.route("/aestrela")
# def profundidade(): return Profundidade(get_environment())

# @Router.route("/aiaestrela")
# def profundidade(): return Profundidade(get_environment())

