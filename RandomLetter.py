#Random Letter Generator

#  Created by Tiago Ferreira on 02/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import random

Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

RandomNumber = random.randint(0,25)

print(Letters[RandomNumber])
