from Src.Models.Node import Node

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # INSERE NO INÍCIO DA LISTA (inserePrimeiro)
    def insert_first(self, father, coord, level, level2=None):
        new_node = Node(father, coord, level, level2)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node

        self.head = new_node

    # INSERE NO FIM DA LISTA (insereUltimo)
    def insert_last(self, father, coord, level, level2=None):
        new_node = Node(father, coord, level, level2)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail

        self.tail = new_node

    # INSERE NA POSIÇÃO ORDENADA PELO LEVEL (inserePos_X)
    def insert_ordered_by_level(self, father, coord, level, level2=None):
        if self.head is None:
            self.insert_first(father, coord, level, level2)
        else:
            current = self.head
            while current.level < level:
                current = current.next
                if current is None:
                    break

            if current == self.head:
                self.insert_first(father, coord, level, level2)
            elif current is None:
                self.insert_last(father, coord, level, level2)
            else:
                new_node = Node(father, coord, level, level2)
                prev = current.previous
                prev.next = new_node
                new_node.previous = prev
                new_node.next = current
                current.previous = new_node

    # REMOVE NO INÍCIO DA LISTA (deletaPrimeiro)
    def remove_first(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None

        return node

    # REMOVE NO FIM DA LISTA (deletaUltimo)
    def remove_last(self):
        if self.tail is None:
            return None

        node = self.tail
        self.tail = self.tail.previous

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        return node

    # RETORNA O PRIMEIRO DA LISTA (primeiro)
    def first(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA (ultimo)
    def last(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA (vazio)
    def is_empty(self):
        return self.head is None

    # EXIBE O CONTEÚDO DA LISTA (exibeLista)
    def get_list(self):
        current = self.head
        
        result = []
        while current is not None:
            result.append([current.coord, current.level])
            current = current.next

        return result

    # EXIBE O CAMINHO ENCONTRADO (exibeCaminho)
    def get_path(self):
        current = self.tail

        path = []
        while current.father is not None:
            path.append(current.coord)
            current = current.father

        path.append(current.coord)
        return path[::-1]

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL) (exibeCaminho1)
    def get_path_from(self, coord):
        current = self.head

        while current.coord != coord:
            current = current.next

        path = []
        current = current.father
        while current.father is not None:
            path.append(current.coord)
            current = current.father

        path.append(current.coord)
        return path[::-1]

    # EXIBE O CAMINHO ENCONTRADO (COMPARA COORD E LEVEL) (exibeCaminho2)
    def get_path_from_coord_level(self, coord, level):
        current = self.tail

        while current.coord != coord or current.level != level:
            current = current.previous

        path = []
        while current.father is not None:
            path.append(current.coord)
            current = current.father

        path.append(current.coord)
        return path[::-1]
