# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "P"
    print(opponent_history)
#    if len(opponent_history) > 2:
#        guess = opponent_history[-2]

  
    player = "player"
    try:
      if (opponent_history[3001] == "P"):
        try:
          if (opponent_history[3002] == "P"):
            player = "abbey"
            cat = 3000
          else:
            player = "kris"
        except:
          fill = 0
      else:
        try:
          if (opponent_history[3002] == "P"):
            player = "quincy"
          else:
            player = "mrugesh"
        except:
          fill = 0
    except:
      try:
        if (opponent_history[2001] == "P"):
          try:
            if (opponent_history[2002] == "P"):
              player = "abbey"
            else:
              player = "kris"
          except:
            fill = 0
        else:
          try:
            if (opponent_history[2002] == "P"):
              player = "quincy"
            else:
              player = "mrugesh"
          except:
            fill = 0
      except:
        try:
          if (opponent_history[1001] == "P"):
            try:
              if (opponent_history[1002] == "P"):
                player = "abbey"
              else:
                player = "kris"
            except:
              fill = 0
          else:
            try:
              if (opponent_history[1002] == "P"):
                player = "quincy"
              else:
                player = "mrugesh"
            except:
              fill = 0
        except:
          try:
            if (opponent_history[1] == "P"):
              try:
                if (opponent_history[2] == "P"):
                  player = "abbey"
                else:
                  player = "kris"
              except:
                fill = 0
            else:
              try:
                if (opponent_history[2] == "P"):
                  player = "quincy"
                else:
                  player = "mrugesh"
              except:
                fill = 0
          except:
            fill=0
  
    
  
# Kris Strat
    if (player == "kris"):
      if (prev_play == "R"):
        guess = "S"
        return guess
      elif (prev_play == "P"):
        guess = "R"
        return guess
      elif (prev_play == "S"):
        guess = "P"
        return guess
      else:
        return guess

  # Abbey Strat
    if (player == "abbey"):
      if (opponent_history[-2]==prev_play):
        if (prev_play == "R"):
          guess = "R"
          return guess
        elif (prev_play == "P"):
          guess = "P"
          return guess
        elif (prev_play == "S"):
          guess = "S"
          return guess
        else:
          return guess
      else:
        if (prev_play == "R"):
          guess = "P"
          return guess
        elif (prev_play == "P"):
          guess = "S"
          return guess
        elif (prev_play == "S"):
          guess = "R"
          return guess
        else:
          return guess

  # Mrugesh Strat
    if (player == "mrugesh"):
      if (prev_play == "R"):
        guess = "P"
        return guess
      elif (prev_play == "P"):
        guess = "S"
        return guess
      elif (prev_play == "S"):
        guess = "R"
        return guess
      else:
        return guess

  



# Quincy Strat and Default Strat
    if (prev_play == "R"):
      guess = "P"
      return guess
    elif (prev_play == "P"):
      guess = "S"
      return guess
    elif (prev_play == "S"):
      guess = "R"
      return guess
    else:
      return guess
