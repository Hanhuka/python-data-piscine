from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print(ft_tqdm.__doc__)
print(tqdm.__doc__)
for elem in ft_tqdm(range(333)):
    # print(elem)
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    # print(elem)
    sleep(0.005)
print()
