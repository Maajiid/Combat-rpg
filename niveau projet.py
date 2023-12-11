if Héros.EXP == 100:
        Héros.lvl += 1
        Héros.HP *= 1.1
        Héros.DEF *= 1.1
        Héros.DMG *= 1.1
        Héros.EXP = 0
        print(f"Vous avez atteint le niveau {Héros.lvl}! Vos statistique ont augmenter")