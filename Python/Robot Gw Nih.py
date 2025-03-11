import random

class Robot:
    def __init__(self, name, hp, att, acc, crit, armor):
        self.name = name
        self.hp = hp
        self.att = att
        self.acc = acc
        self.crit = crit
        self.armor = armor
        self.armor_durability = 100  # Durability of the armor
        self.stun = False
        self.special_cd = 0  # Cooldown buat special attack
    
    def att_enemy(self, target):
        if self.stun:
            print(f"{self.name} is stunned and can't attack!")
            self.stun = False
            return
        
        if random.randint(1, 100) <= self.acc:
            if random.randint(1, 100) <= self.crit:
                dmg = self.att * 2
                print(f"{self.name} crits {target.name} for {dmg} damage!")
            else:
                dmg = self.att
                print(f"{self.name} hits {target.name} for {dmg} damage!")
            
            damage_reduction = target.armor / 100
            final_dmg = int(dmg * (1 - damage_reduction))
            target.hp -= final_dmg
            target.armor_durability -= 10  # Reduce armor durability on hit
            if target.armor_durability <= 0:
                target.armor = 0  # Armor is broken
                print(f"{target.name}'s armor is broken!")
            print(f"{target.name} takes {final_dmg} damage after armor reduction!")
        else:
            print(f"{self.name} misses {target.name}!")
    
    def repair_armor(self):
        if self.armor_durability < 100:
            self.armor_durability += 20
            self.armor = 20  # Restore some armor
            print(f"{self.name} repairs armor! Durability restored to {self.armor_durability}.")
        else:
            print(f"{self.name}'s armor is already at max durability!")
    
    def special_attack(self, target):
        if self.special_cd == 0:
            dmg = self.att * 3
            print(f"{self.name} uses SPECIAL ATTACK on {target.name} for {dmg} damage!")
            damage_reduction = target.armor / 100
            final_dmg = int(dmg * (1 - damage_reduction))
            target.hp -= final_dmg
            print(f"{target.name} takes {final_dmg} damage after armor reduction!")
            self.special_cd = 3  # Cooldown 3 ronde
        else:
            print(f"{self.name}'s special attack is on cooldown ({self.special_cd} rounds left).")
    
    def regen(self):
        heal = random.randint(10, 50)
        self.hp += heal
        print(f"{self.name} regenerates {heal} health!")

    def stunned(self, target):
        if random.randint(1, 100) <= 35:
            target.stun = True
            print(f"{self.name} stuns {target.name}!")
        else:
            print(f"{self.name} fails to stun {target.name}!")
    
    def alive(self):
        return self.hp > 0
    
    def update_cooldowns(self):
        if self.special_cd > 0:
            self.special_cd -= 1

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round_num = 1
    
    def display(self):
        print(f"Round {self.round_num}")
        print(f"{self.player1.name}: {self.player1.hp} HP, {self.player1.armor} Armor, {self.player1.armor_durability} Durability")
        print(f"{self.player2.name}: {self.player2.hp} HP, {self.player2.armor} Armor, {self.player2.armor_durability} Durability")
    
    def battle_round(self):
        self.display()

        for robot, target in [(self.player1, self.player2), (self.player2, self.player1)]:
            if not robot.alive() or not target.alive():
                return False

            print(f"\n{robot.name}'s turn!")
            print(f"1. Attack")
            print(f"2. Special Attack (Cooldown: {robot.special_cd} rounds)")
            print(f"3. Regenerate")
            print(f"4. Stun")
            print(f"5. Repair Armor")
            print(f"6. Do nothing")
            print(f"7. Give up")
            choice = input(f"Choose an action: ") 
            
            if choice == "1":
                robot.att_enemy(target)
            elif choice == "2":
                robot.special_attack(target)
            elif choice == "3":
                robot.regen()
            elif choice == "4":
                robot.stunned(target)
            elif choice == "5":
                robot.repair_armor()
            elif choice == "6":
                print(f"{robot.name} does nothing!")
            elif choice == "7":
                print(f"{robot.name} gives up! {target.name} wins!")
                return False
            else:
                print("Invalid choice!")
                continue

            robot.update_cooldowns()
        
        self.round_num += 1
        return True
    
    def play(self):
        print("\nBattle Start!")
        while self.player1.alive() and self.player2.alive():
            if not self.battle_round():
                return
        
        if self.player1.alive():
            print(f"{self.player1.name} wins!")
        elif self.player2.alive():
            print(f"{self.player2.name} wins!")
        else:
            print("It's a draw!")

player1_name = input("Enter name for Player 1's robot: ")
player2_name = input("Enter name for Player 2's robot: ")

player1 = Robot(player1_name, 100, 10, 80, 10, 20)
player2 = Robot(player2_name, 100, 10, 80, 10, 20)

battle = Battle(player1, player2)
battle.play()
