#!/usr/bin/env python3.8
import random
import numpy as np
from tqdm import tqdm



class Node:
  def __init__(self, coords=None):
    self.coords = coords
    self.pheromon_level = 0
    self.available_nodes = []
    self.probs = []   
    self.is_end = False
    self.is_start = False

  def update_probs(self):
    total_pheromons = sum([node.pheromon_level for node in self.available_nodes])
    
    for i, node in enumerate(self.available_nodes):
      self.probs[i] =  node.pheromon_level/total_pheromons

  def init_probs(self):
    prob_val = 1/len(self.available_nodes)
    self.probs = [prob_val] * len(self.available_nodes) 
 
  def select_node(self):
    #probs = [x.pheromon_level for x in self.available_nodes]
    idx, node =random.choices(list(enumerate(self.available_nodes)), weights=self.probs)[0]
    return node, idx 

class Graph:
  def __init__(self, con_matrix, nodes=None, start_idx=0, end_idx=1):
    self.con_matrix = con_matrix
    self.shape = self.con_matrix.shape
 
 
    if self.shape[0] != self.shape[1]: raise RuntimeError("Wrong dims for connection matrix")

    self.nodes = [Node(coords=i) for i in range(self.shape[0])]

    self.start_node = self.nodes[start_idx]
    self.end_node = self.nodes[end_idx] 

    self.start_node.is_start = True
    self.end_node.is_end = True

  def initialize_graph(self):
    for i, node in enumerate(self.nodes):
      for j in range(len(self.con_matrix[:, i])):
        if self.con_matrix[i, j]:
          node.available_nodes.append(self.nodes[j])
      node.init_probs()

  def update(self):
    for node in self.nodes:
      node.update_probs()

  def evaporate(self, v=0.3):
    for node in self.nodes:
      node.pheromon_level *= (1-v)
      


class Ant:
    def __init__(self, graph):
      self.memory = []
      self.graph = graph
      self.position = graph.start_node
      self.traversed_path = [graph.start_node]
      self.backwards = False
   

    def add_memory(self):
      for node in self.traversed_path:
        self.memory.append(node.coords)
 
    def step(self):
      if self.backwards:
        self.position = self.traversed_path.pop()
        self.position.pheromon_level += 1

        if self.position.is_start:
          self.backwards = False
          self.traversed_path = [graph.start_node]
    
      else: 
        self.position, _ = self.position.select_node()
        self.traversed_path.append(self.position) 
 
        if self.position.is_end:
          self.backwards = True
          self.memory  = []
          self.add_memory()
          self.traversed_path.pop()
          self.position.pheromon_level += 1

if __name__ == "__main__":

  graph = Graph(np.array([[0, 1, 1], [1,0, 1], [1,1, 0]]))
  graph.initialize_graph()
  colony = [Ant(graph)] * 100
  
  for t in tqdm(range(200)):
    for i, ant in enumerate(colony):
      ant.step()

    graph.update()
    graph.evaporate()
