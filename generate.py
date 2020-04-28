from textgenrnn import textgenrnn

textgen = textgenrnn(
  name="quran",
  weights_path='./quran_weights.hdf5',
  config_path='./quran_config.json',
  vocab_path='./quran_vocab.json'
)
textgen.generate(20,temperature=1.0)
