from textgenrnn import textgenrnn

# If cintinue training, disable this
textgen = textgenrnn(name="quran")                   
textgen.reset()

'''
# If continue training, enable this
textgen = textgenrnn(
  name="quran",
  weights_path='./quran_weights.hdf5',
  config_path='./quran_config.json',
  vocab_path='./quran_vocab.json'
)
'''

# Begin Training
textgen.train_from_file(
    file_path = 'dataset/quran.txt',
    new_model = True, # If continue training, set to False
    num_epochs = 15,
    word_level = True,
    rnn_bidirectional = True, 
    max_length = 40,
    rnn_layers = 3,
)
