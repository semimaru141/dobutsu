from src.applications.compress_train_data import compress_train_data

read_filename = 'multi1_20_merged'
new_filename = 'multi1_compressed'

if __name__ == "__main__":
    compress_train_data(read_filename, new_filename, key='score')
