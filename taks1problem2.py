def Task1Problem2(stones):
    # target list banaya ithaca word ka
    target = {'i': 1, 't': 1, 'h': 1, 'a': 2, 'c': 1}
    
    # assume an empty bag jisme hum count store karenge
    bag = {'i': 0, 't': 0, 'h': 0, 'a': 0, 'c': 0}
    
    # step track karega ki konsa turn chal raha hai srt from 1
    
    for step, stone in enumerate(stones, 1):
        
        # case insensitive karne ke liye lower use kiya
        s = stone.lower()
        
        # agar stone target me hai toh bag me plus 1 kar do
        if s in bag:
            bag[s] += 1
            
        # ab check karte hain ki saare letters mile ya nahi
        sab_mil_gaya = True
        
        for letter, req in target.items():
            # agar bag me required amount se kam hai toh flag false kar do
            if bag[letter] < req:
                sab_mil_gaya = False
                break 
                
        # agar flag true hi raha mtlb jo chaiye tha mil gaya 
        if sab_mil_gaya:
            return step 
            
    # agar loop khatam ho gaya aur word nahi bana toh ofc wrong hai Q so -1
    return -1


# testing ke liye example input pass kar rahe hain
input_stones = ['T', 'X', 'I', 'A', 'H', 'C', 'B', 'A']
ans = Task1Problem2(input_stones)
print(ans)
