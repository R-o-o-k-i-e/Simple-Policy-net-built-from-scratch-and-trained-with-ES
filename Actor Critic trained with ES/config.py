import torch
args={'hidden_dim':64,
      'hidden_layer':2,
      'device':torch.device('cuda:0'),
      'generation_size':100,
      'parents_size':20,
      'tournament_size':5,
      'mutation_rate':1.0,
      'sigma':0.2,
      'generations':100,
      'champion_save':1,
      }