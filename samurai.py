# Samurai (based on RPS)
#  Matt Kaczmarek, created Nov 9 2016
#
#  Update: Feb 2 2017
#    -Spacing redone
#    -Rewrote some text for clarity

import random
import math

def main():
  names = ['Motohito','Mihito','Hikohito','Fusahito','Katsuhito','Tomohito','Michihito','Kazuhito','Kotohito','Okiko','Tsuguhito','Nagahito','Satohito','Asahito','Toshiko','Yasuhito','Teruhito','Hidehito','Morohito','Ayahito','Takauji','Yoshiakira','Yoshimitsu','Yoshimochi','Yoshikazu','Yoshinori','Yoshikatsu','Yoshimasa','Yoshihisa','Yoshitane','Yoshizumi','Yoshiharu','Yoshiteru','Yoshihide','Yoshiaki','Nobutada','Hidenobu','Hideyoshi','Hideyori','Ieyasu','Hidetada','Iemitsu','Ietsuna','Tsunayoshi','Ienobu','Ietsugu','Yoshimune','Ieshige','Ieharu','Ienari','Ieyoshi','Iesada','Iemochi','Yoshinobu']
  clans = ['Amago','Arisugawa','Asaka','Asakura','Chosokabe','Date','Fushimi','Hojo','Hosokawa','Hatekayama','Ikeda','Imagawa','Katsura','Kaya','Kitashirakawa','Kuni','Maeda','Mori','Nanbu','Nashimoto','Oda','Otomo','Ouchi','Shiba','Shimazu','Takeda','Tokugawa','Uesugi','Yamana','Yamashina','Yamato']

  while True:
    # Player stats
    level = 1
    hp = 3
    maxHP = 3
    kills = 0

    # Instructions
    print()
    print('=========== Way Of The Samurai ===========')
    print()
    print('>The goal of the game is to defeat an army of Ronin, rogue Samurai')
    print('>You can attack, counter, or wait')
    print('>Attack beats wait, wait beats counter, counter beats attack')
    print('>Waiting makes your opponent mad, while countering makes them wary')
    input('Press "Enter": ')

    # Game
    while hp > 0:
      # Generate enemy
      eName = clans[random.randint(0,len(clans)-1)] + " " + names[random.randint(0,len(names)-1)]
      eAggro = 25 + random.randint(-15,15)
      eHP = 3

      # Start of fight
      print()
      print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      print()
      print('Your opponent is ',eName,'.',sep='')

      # Battle
      while hp > 0 and eHP > 0:
        # Enemy move
        will = random.randint(0,100) + eAggro
        if will > 125:
          eMove = 1 # attack
        elif will < 75:
          eMove = 2 # counter
        else:
          eMove = 3 # wait

        # Player move
        print()
        print(kills,'kills')
        print('HP =',hp)
        print('Enemy HP =',eHP)
        try:
          move = int(input('1) Attack, 2) Counter, 3) Wait: '))
        except:
          move = 1
        if move!=1 and move!=2 and move!=3:
          move = 1

        # Execution of moves
        print()
        if move==1 and eMove==1:
          print('>You and your opponent cross swords')
        elif move==1 and eMove==2:
          print('>Your opponent counters your attack')
          hp -= 1
        elif move==1 and eMove==3:
          print('>You catch your opponent off guard')
          eHP -= 1
        elif move==2 and eMove==1:
          print(">You counter your opponent's attack")
          eHP -= 1
        elif move==2 and eMove==2:
          print('>You both stand ready, but nothing happens')
        elif move==2 and eMove==3:
          print('>You stand ready, but your opponent waits')
        elif move==3 and eMove==1:
          print('>Your opponent catches you off guard')
          hp -= 1
        elif move==3 and eMove==2:
          print('>Your opponent stands ready, but you wait')
        elif move==3 and eMove==3:
          print('>You and your opponent stare at each other menacingly')

        # Update aggro
        if move==2:
          eAggro -= 25
        elif move==3:
          eAggro += 25
                                
        # Keep aggro in reasonable bounds
        if eAggro > 75:
          eAggro = 75
        elif eAggro < -75:
          eAggro = -75

      print()
      # Victory
      if hp > 0:
        print('You won:')
        kills += 1
        print('>You now have',kills,'kill(s)')
        hp = maxHP

      # Defeat
      else:
        print('Rest in peace:')
        print('>You killed',kills,'ronin')

      # Wait for player
      input('Press "Enter": ')

main()

# End
