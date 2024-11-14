"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

import random

def main() -> None:
    # set variables for cost to play and base prize
    cost_to_play: int = 1
    base_prize: int = 10
    mega_number: int = 6
    mega_multiplier: int = 10
    # roll three dice
    roll1: int = random.randint(1,6)
    roll2: int = random.randint(1,6)
    roll3: int = random.randint(1,6)
    # check if they are equal   
    payout: int = 0
    if roll1 == roll2 and roll1 == roll3:
    # if they are, calculate the prize
        if roll1 == mega_number:
            payout = mega_multiplier*base_prize
        else:
            payout = base_prize*roll1
        
    # output results
    print(f"Casino collects: ${cost_to_play}")
    print(f"Player rolls: {roll1}-{roll2}-{roll3}")
    print(f"Casino pays out: ${payout}")
    print(f"Profit: ${cost_to_play-payout}")
if __name__ == "__main__":
    main()