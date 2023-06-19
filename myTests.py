from ex11_utils import  find_length_n_paths,find_length_n_words

# s=find_length_n_paths(3,[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'G', 'K', 'L'], ['M', 'N', 'O', 'P']],('ABC', 'CDE', 'ABCD'))
# print(s)

s=find_length_n_words(3,[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'G', 'K', 'L'], ['M', 'N', 'O', 'P']],('ABC', 'CDE', 'ABCD'))
print(s)