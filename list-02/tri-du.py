# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Tri-du

cards = map(int, raw_input().split())
print cards[0] if cards[0] == cards[1] else max(cards)