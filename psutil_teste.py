import psutil
from time import sleep

# tipo = input("Diga o que você quer monitorar:")

# if tipo == 0:
#     tipo = input("1 - CPU \n 2 - Disco \n 3 - Memória")

part_disk = psutil.disk_partitions()

print("Quantidade de nucleos virtuais: " + str(psutil.cpu_count()))
print("Quantidade de nucleos físicos :" + str(psutil.cpu_count(logical=False)))
print(part_disk[0].mountpoint)


