from tree_sitter import Language, Parser
import multiprocessing
import os
from multiprocessing.pool import Pool

Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    # 'vendor/tree-sitter-go',
    # 'vendor/tree-sitter-javascript',
    'vendor/tree-sitter-python'
  ]
)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)


class MccabeFactory(object):
    """go through every node of AST to record each node"""
    def __init__(self):
        # last processed verticle
        self.end_verticle = None

    def add_to_path(self, verticle):
        # todo: add commit
        if not self.end_verticle:
            return
        self.edge.link_verticles(self.end_verticle, verticle)
        self.end_verticle = verticle

    def visit_statement(self,node):
        node_name = node.type
        visit_func = getattr(self, node_name+'_visitor',self.linear_statement_visitor)
        return visit_func(node)

    def do_visit(self,tree,file_name):
        self.edge = Edge(file_name)
        self.visit_statement(tree.root_node)

    def module_visitor(self, node):
        for inode in node.children:
            self.visit_statement(inode)

    children_visitor = module_visitor

    def with_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'with:{}'.format(line_start)
        with_verticle = Verticle(name)
        self.add_to_path(with_verticle)
        self.block_visitor(node)

    def block_visitor(self, node):
        for inode in node.children:
            if inode.type == 'block':
                self.children_visitor(inode)
    def if_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'if:{}'.format(line_start)
        if_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = if_verticle
        else:
            self.add_to_path(if_verticle)
        self.if_block_visitor(if_verticle, node)

    def if_block_visitor(self, begin_verticle, node):
        final_verticle = Verticle('')
        possible_end = [begin_verticle]
        for inode in node.children:
            if inode.type == 'block':
                self.children_visitor(inode)
                possible_end.append(self.end_verticle)
            if inode.type == 'elif_clause':
                self.end_verticle = begin_verticle
                self.block_visitor(inode)
                possible_end.append(self.end_verticle)
            if inode.type == 'else_clause':
                self.end_verticle = begin_verticle
                self.block_visitor(inode)
                possible_end.append(self.end_verticle)
                # if the 'if' statement has 'else' statement, the 'if' statement no longer need to be linked to the final verticel
                possible_end = possible_end[1:]
        for iend in possible_end:
            self.edge.link_verticles(iend, final_verticle)
        self.end_verticle = final_verticle

    def try_block_visitor(self, begin_verticle, node):
        final_verticle = Verticle('')
        possible_end = []
        for inode in node.children:
            if inode.type == 'block':
                self.children_visitor(inode)
                possible_end.append(self.end_verticle)
            if inode.type == 'except_clause':
                self.end_verticle = begin_verticle
                self.block_visitor(inode)
                possible_end.append(self.end_verticle)
        for iend in possible_end:
            self.edge.link_verticles(iend, final_verticle)
        self.end_verticle = final_verticle



    def try_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'try:{}'.format(line_start)
        try_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = try_verticle
        else:
            self.add_to_path(try_verticle)
        self.try_block_visitor(try_verticle, node)

    def function_definition_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'fun:{}'.format(line_start)
        fun_verticle = Verticle(name)
        self.end_verticle = fun_verticle
        self.block_visitor(node)
        final_verticle = Verticle('')
        self.edge.link_verticles(self.end_verticle, final_verticle)
        self.edge.link_verticles(fun_verticle, final_verticle)
        self.end_verticle = final_verticle

    def linear_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'simple:{}'.format(line_start)
        sim_verticle = Verticle(name)
        self.add_to_path(sim_verticle)

    def while_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'while:{}'.format(line_start)
        while_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = while_verticle
        else:
            self.add_to_path(while_verticle)
        self.block_visitor(node)
        final_verticle = Verticle('')
        self.edge.link_verticles(self.end_verticle, final_verticle)
        self.edge.link_verticles(while_verticle, final_verticle)

    def for_statement_visitor(self, node):
        line_start = node.start_point[0] + 1
        name = 'for:{}'.format(line_start)
        for_verticle = Verticle(name)
        if not self.end_verticle:
            self.end_verticle = for_verticle
        else:
            self.add_to_path(for_verticle)
        self.block_visitor(node)
        final_verticle = Verticle('')
        self.edge.link_verticles(self.end_verticle, final_verticle)
        self.edge.link_verticles(for_verticle, final_verticle)
        self.end_verticle = final_verticle


class Verticle(object):
    def __init__(self,name):
      self.name = name


class Edge(object):
    def __init__(self,name):
        self.name = name
        self.edge_verticle = {}

    def link_verticles(self,v1,v2):
        self.edge_verticle.setdefault(v1,[]).append(v2)
        self.edge_verticle[v2] = []

    def compute_complex(self):
        # print('nnnnnnnnnnnnnnnnnnnnnnnn')
        # for key,value in self.edge_verticle.items():
        #     print('key--{}, value--{}'.format(key.name,[i.name for i in value]))
        nodes = len(self.edge_verticle)
        edges = sum([len(i) for i in self.edge_verticle.values()])
        return edges-nodes+2

def split_list(file_list, n):
    for i in range(0, len(file_list), n):
        yield file_list[i:i + n]

def do_calculate(file_name):
    code = read_file(file_name)
    tree = parser.parse(bytes(code, "utf8"))
    visitor = MccabeFactory()
    visitor.do_visit(tree,file_name)
    print(visitor.edge.name + '----------' + str(visitor.edge.compute_complex())+'\n')

def main(file_path):
    file_list = []
    for _,_,files in os.walk(file_path):
        for ifile in files:
            if ifile.endswith('.py'):
                file_list.append(os.path.join(file_path,ifile))
    worker_nums = multiprocessing.cpu_count()
    p = Pool(worker_nums)
    for ifile in file_list:
        p.apply_async(do_calculate, args=(ifile,))
    p.close()
    p.join()
    print('finished')



    # root_node = tree.root_node
    # assert root_node.type == 'module'
    # assert root_node.start_point == (1, 0)
    # assert root_node.end_point == (3, 13)
    #
    # function_node = root_node.children[0]
    # assert function_node.type == 'function_definition'
    # assert function_node.child_by_field_name('name').type == 'identifier'
    #
    # function_name_node = function_node.children[1]
    # assert function_name_node.type == 'identifier'
    # assert function_name_node.start_point == (1, 4)
    # assert function_name_node.end_point == (1, 7)


if __name__ == '__main__':
    file_path = '/Users/liwang/Documents/myself/merico/test_files/'
    main(file_path)