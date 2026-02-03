# 🌟 Starr Drop Simulator: The Psychology of the Reveal

This Python project replicates the **Starr Drop** mechanic from the mobile game *Brawl Stars* by Supercell. It is designed to demonstrate how simple probability and feedback loops can create an engaging and "wanting-more" player experience.

> **Note:** This code was developed as a conceptual student project to explore game design logic.

---

## 🕹️ How It Works

1. **The Starting Point:** Every drop begins at the **Rare** tier.
2. **The Tap Sequence:** The simulation goes through 4 "taps." In this code, `time.sleep(.05)` simulates the brief pause between a player tapping the screen and the rarity updating.
3. **The Upgrade Logic:** On each tap, there is a mathematical chance for the rarity to increase:
   - It uses the formula: `random.randint(1, (rarity+1)*3) == 1`.
   - **The Math:** As the `rarity` increases, the number it multiplies by gets larger, making the "win" condition harder to hit. This makes **Legendary** drops feel significantly more valuable than **Rare** ones.

## 📈 Player Psychology Analysis

Why does this code represent a mechanic that makes people want to play more?

### 1. Variable Ratio Reinforcement
The "Starr Drop" is essentially a digital reward container. Because the player doesn't know *if* it will upgrade, but knows it *could*, the brain releases dopamine in anticipation. This is the same principle behind "blind boxes" or "loot boxes."

### 2. The Power of "The Reveal"
By printing the rarity at every stage of the `for` loop, the code builds tension. 
* Seeing **Rare → Rare → Rare** creates a desire for better luck next time.
* Seeing **Rare → Super Rare → Epic** creates a "winning streak" feeling that encourages the player to keep opening more drops.

### 3. Visual Scarcity
At the end of the script, the `Counter` tool provides a summary. Seeing a result like:
* `Rare x 15`
* `Legendary x 1`

Directly visualizes the **scarcity** of the top-tier rewards. This confirms to the player that they have found something "special," which triggers a sense of achievement.

---

## 🚀 Instructions for Use

### Prerequisites
* Python 3.x installed on your machine.

### Running the Script
1. Copy the code into a file named `starr_drop.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder where the file is saved.
4. Run the command:
   ```bash
   python starr_drop.py
