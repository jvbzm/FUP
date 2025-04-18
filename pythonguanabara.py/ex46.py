import time
print('Contem que os fogos estão sendo lançados!')
for fogo in range(10, 0, -1):
    print(fogo)
    print('...')
    time.sleep(1)
print('KABOM!')