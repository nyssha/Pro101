import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb') 
        dbx.files_upload(f.read(), file_to)

    with open(local_path, 'rb' ) as f:
        dbx.file_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))   

def main():
    access_token =  'sl.BDOSqFweTR3nkamLKgEEbxd7KkFLTbuJ8dYOVNxTNGErAJjDAGBaU5Dwg59NGX2X171akPfCM-xPG5e95j6k4zINuxW22TihHmIiF2OgEVyLABbwH91k3iNNpEmqJ71G2ZGRERQ' 
    transferData = TransferData(access_token)

    file_from = 'test.txt' 
    file_to = '/test_dropbox/test.txt'

    transferData.upload_file(file_from,file_to)

if __name__ == '__main__':
    main()           