from src.applications.compress_train_data import compress_train_data

read_filename = '1hour2'
new_filename = '1hour2_compressed'

if __name__ == "__main__":
    compress_train_data(read_filename, new_filename)
