def build_path_to_data(folder = ''):
    yourEnv =[]
    while True:
        yourEnv = input('Send 1 if you work in your OS,\n insert 2 if you work in GoogleDrive: ')
        if yourEnv == '1' :
            path_hw= "./data/" + folder + "/"
            return path_hw
            break
        elif yourEnv == '2' :
            # from google.colab import drive
            drive.mount("/content/drive")
            path_hw = "/content/drive/My Drive/DataScience/" + folder + "/"
            return path_hw
            break
        elif yourEnv == '3' :
            path_hw = "./"
            break
        else:
            print('There is no such variant.Please try again')
    return path_hw

"""
  @staticmethod
  def build_folder_path(folder = ''):
    yourEnv =[]
    while True:
        yourEnv = input('Send 1 if you work in your OS,\n insert 2 if you work in GoogleDrive: ')
        if yourEnv == '1' :
            path_hw= "./data/" + folder + "/"
            return path_hw
            break
        elif yourEnv == '2' :
            from google.colab import drive
            drive.mount("/content/drive")
            path_hw = "/content/drive/My Drive/DataScience/" + folder + "/"
            return path_hw
            break
        elif yourEnv == '3' :
            path_hw = "./"
            break
        else:
            print('There is no such variant.Please try again')
"""
