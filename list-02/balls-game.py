# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Balls Game


def explode_balls(balls, index):
    balls_exploded = 1
    i = index
    j = i + 1

    while len(balls) > 2 and i < j:
        if j < len(balls) and balls[i] == balls[j]:
            balls_exploded += 1
            j += 1
        else:
            if balls_exploded >= 2:
                if j < len(balls) and i >= 0 and balls[i - 1] == balls[j]:
                    balls = balls[:i] + balls[j:]

                    if len(balls) > 2:
                        i -= 1
                        j = i + 1

                        while i >= 0 and balls[i] == balls[j]:
                            i -= 1

                        if abs(j - (i+1)) >= 2:
                            return balls_exploded + explode_balls(balls, i + 1)
                        else:
                            i += 1
                            j = i + 1

                            while j < len(balls) and balls[i] == balls[j]:
                                j += 1

                            if abs(i - (j - 1)) >= 2:
                                return balls_exploded + explode_balls(balls, i)
                            else:
                                return balls_exploded
                    else:
                        return balls_exploded
                else:
                    return balls_exploded
            else:
                return 0

    return balls_exploded


amount_balls, amount_color, ball = map(int, raw_input().split())
balls = map(int, raw_input().split())
balls_exploded = [0]

try:
    if len(balls) > 1:
        index = balls.index(ball)

        while True:
            if index == 0 and balls[index] == balls[index + 1]:
                balls_exploded.append(2)
            elif index < len(balls) - 1 and balls[index] == balls[index + 1]:
                balls_add = balls[:index] + [ball] + balls[index:]
                balls_exploded.append(explode_balls(balls_add, index) - 1)

            index = balls.index(ball, index + 1)

    print max(balls_exploded)
except ValueError:
    print max(balls_exploded)