import subprocess

if __name__ == '__main__':
    for seq_id in ['016', '030', '061', '078', '086', '096', '206', '223', '255']:
        process = subprocess.Popen(
                ['./playback', 
                 '/data/data/scenenn/103.24.77.34/scenenn/main/oni/' + seq_id + '.oni', 
                 '/data/data/scenenn/103.24.77.34/scenenn/main/oni_unpacked/' + seq_id], 
                stdout=subprocess.PIPE, universal_newlines=True
            )
        process.communicate()