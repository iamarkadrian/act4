while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    word = word.lower()
    if word == "chupacabra":
        break
    elif word == "exit":
        print("Use the magic word to exit!")
    elif word == "leave":
        print("Use the magic word to exit!")
    elif word == "quit":
        print("Use the magic word to exit!")
        
print("You've successfully left the loop!")