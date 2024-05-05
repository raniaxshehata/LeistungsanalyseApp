import json
from my_classes import Person, Subject
from datetime import datetime

test_subject = Subject("Eda", "Gür", "female", datetime(2002,08,16), "ge7045@mci4me.at")

#test
test_subject.put()
test_subject.update_email()

#habe ich die zuvor definierte klassen person und subject verwendet und eine instanz des subjects für testzwecke erstellt.
#put() und update_email() rufe ich auf um den workflow zu testn
