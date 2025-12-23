with open('213AnywhereAve.txt', 'r') as file:
    print(file.readable())      # print 'True'
    print(file.writable())      # print 'False'
    print(file.seekable())      # print 'True'