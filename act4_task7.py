block_symbol = input("Enter the block symbol: ")
total_blocks = int(input("Enter the total number of blocks: "))

height = 0
blocks_used = 0
level = 1

while blocks_used + level <= total_blocks:
    blocks_used += level
    height += 1
    level += 2

leftover_blocks = total_blocks - blocks_used

for i in range(1, height + 1):
    print(" " * (height - i) + block_symbol * (2 * i - 1))

print(f"The height of the pyramid: {height}")
print(f"Blocks left unused: {leftover_blocks}")