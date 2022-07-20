
from stackapi import StackAPI

SITE = StackAPI("stackoverflow")
comments = SITE.fetch('comments')

# print(comments[0])